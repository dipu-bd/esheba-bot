#!/bin/bash

SRC_DIR="./protos"
DST_DIR="./service"
DOCKER_NAME="esheba-bot"

if [ ! $1 ]
then

    echo Creating destination folder... [$DST_DIR]
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

    echo =========== Remove unused docker files ===========
    sudo docker images -q | sudo xargs docker rmi

    echo =========== Building Docker ===========
    sudo docker build -t $DOCKER_NAME .

    echo =========== Stopping previous service ===========
    sudo docker stop $DOCKER_NAME
    sudo docker rm $DOCKER_NAME

    echo =========== Running docker ===========
    sudo docker run -d -p 5000:5000 --name $DOCKER_NAME $DOCKER_NAME

elif [ $1 = '~docker' ]
then

    echo =========== Remove unused docker files ===========
    sudo docker images -q | sudo xargs docker rmi

    echo =========== Stopping previous service ===========
    sudo docker stop $DOCKER_NAME

fi
