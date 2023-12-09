import logging
from concurrent import futures
from grpc_reflection.v1alpha import reflection

import os
import grpc
import grpc_echo_pb2
import grpc_echo_pb2_grpc

LOGGER_DATEFMT = "%Y-%m-%d %H:%M:%S"
LOGGER_FORMAT = "[%(asctime)s.%(msecs)03d] %(message)s"
logging.basicConfig(
    level=logging.INFO, datefmt=LOGGER_DATEFMT, format=LOGGER_FORMAT
)


class Echo(grpc_echo_pb2_grpc.EchoServicer):
    def Ping(self, request, context):
        payload = str(request.payload)
        invocation_metadata = str(dict(context.invocation_metadata()))
        logging.info(f"Request payload: {request} | metadatum: {invocation_metadata}")
        pong = grpc_echo_pb2.Pong(
            payload=payload, invocation_metadata=invocation_metadata
        )
        return pong


def run_server_insecure():
    port = os.getenv('GRPC_PORT', "50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    SERVICE_NAMES = (
        grpc_echo_pb2.DESCRIPTOR.services_by_name['Echo'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(f"0.0.0.0:{port}")
    logging.info(f"GRPC echo server startingon port {port}")
    return server


def run_server_secure():
    port = os.getenv('GRPCS_PORT', "50052")
    server_key = open("certs/server.key", mode="rb").read()
    server_cert = open("certs/server.crt", mode="rb").read()
    server_credentials = grpc.ssl_server_credentials(
        [(server_key, server_cert)]
    )
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_echo_pb2_grpc.add_EchoServicer_to_server(Echo(), server)
    SERVICE_NAMES = (
        grpc_echo_pb2.DESCRIPTOR.services_by_name['Echo'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_secure_port(f"0.0.0.0:{port}", server_credentials)
    logging.info(f"GRPCS echo server startingon port {port}")
    return server


if __name__ == "__main__":
    server1 = run_server_insecure()
    server2 = run_server_secure()

    server1.start()
    server2.start()

    server1.wait_for_termination()
    server2.wait_for_termination()
