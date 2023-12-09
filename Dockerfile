FROM  --platform=linux/amd64 python:3.10.12-alpine3.18

WORKDIR /grpc
ADD . .
RUN pip3 install -r requirements.txt

CMD ["python3", "./server.py"]