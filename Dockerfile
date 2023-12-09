FROM  --platform=$BUILDPLATFORM python:3.10.12-alpine3.18 AS builder

WORKDIR /grpc
ADD . .
RUN pip3 install -r requirements.txt

FROM python:3.10.12-alpine3.18 AS runner
COPY --from=builder /grpc /grpc
WORKDIR /grpc
CMD ["python3", "./server.py"]