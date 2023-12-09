FROM python:3.10.12-alpine3.18
ARG DIR="/grpc"
WORKDIR $DIR
ADD . $DIR
RUN pip3 install -r requirements.txt

CMD ["python3", "./server.py"]
