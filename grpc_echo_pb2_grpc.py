# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_echo_pb2 as grpc__echo__pb2


class EchoStub(object):
    """The echo service replies with the message it received."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
            "/grpc_echo.Echo/Ping",
            request_serializer=grpc__echo__pb2.Content.SerializeToString,
            response_deserializer=grpc__echo__pb2.Pong.FromString,
        )


class EchoServicer(object):
    """The echo service replies with the message it received."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_EchoServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ping": grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=grpc__echo__pb2.Content.FromString,
            response_serializer=grpc__echo__pb2.Pong.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "grpc_echo.Echo", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Echo(object):
    """The echo service replies with the message it received."""

    @staticmethod
    def Ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/grpc_echo.Echo/Ping",
            grpc__echo__pb2.Content.SerializeToString,
            grpc__echo__pb2.Pong.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
