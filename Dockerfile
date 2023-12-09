FROM  --platform=$BUILDPLATFORM python:3.10.12-alpine3.18 AS runner
WORKDIR /grpc
ADD . .
RUN pip3 install -r requirements.txt
CMD ["python3", "./server.py"]
# FROM python:3.10.12-alpine3.18 AS runner
# COPY --from=builder /grpc /grpc
# WORKDIR /grpc
