SRC_DIR="./protos"
DST_DIR="./grpc"

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
    echo Done!
    echo
fi
