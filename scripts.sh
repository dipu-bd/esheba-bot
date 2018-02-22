SRC_DIR="./protos"
DST_DIR="./service"

if [ $1 = "build" ]
then
    echo Building proto...
    mkdir -p "$DST_DIR"
    touch "$DST_DIR/__init__.py"
    python -m grpc_tools.protoc \
         --proto_path="$SRC_DIR" \
         --python_out="$DST_DIR" \
         --grpc_python_out="$DST_DIR" \
        "$SRC_DIR/service.proto"
    sed -i 's/import service_pb2/from . import service_pb2/gi' "$DST_DIR/service_pb2_grpc.py"
    echo Done!
    echo
fi
