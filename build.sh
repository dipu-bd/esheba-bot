#!/bin/bash

SRC_DIR="./protos"
DST_DIR="./service"
DOCKER_NAME="esheba-bot"

if [ ! $1 ]
then
    echo Creating $DST_DIR...
    mkdir -p "$DST_DIR"
    touch "$DST_DIR/__init__.py"

    echo Building proto...
    python -m grpc_tools.protoc \
         --proto_path="$SRC_DIR" \
         --python_out="$DST_DIR" \
         --grpc_python_out="$DST_DIR" \
        "$SRC_DIR/service.proto"
    
    echo Replacing imports...
    sed -i 's/import service_pb2/from . import service_pb2/gi' "$DST_DIR/service_pb2_grpc.py"
    echo Done!

elif [ $1 = 'docker' ]
then

    echo =========== Grant access to root ===========
    sudo su

    echo =========== Remove unused docker files ===========
    echo docker images -q | xargs docker rmi

    echo =========== Building Docker ===========
    docker build -t $DOCKER_NAME .

    echo =========== Stopping previous service ===========
    docker stop $DOCKER_NAME
    docker rm $DOCKER_NAME

    echo =========== Running docker ===========
    docker run -d -p 5000:5000 --name $DOCKER_NAME $DOCKER_NAME
fi
