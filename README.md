## Test scenario


```bash
  grpcurl  -H 'hdr: header' -d '{"payload": "Hello"}'  --plaintext 127.0.0.1:50051 grpc_echo.Echo/Ping
  grpcurl  -H 'hdr: header' -d '{"payload": "Hello"}'  --insecure  127.0.0.1:50052 grpc_echo.Echo/Ping
```

