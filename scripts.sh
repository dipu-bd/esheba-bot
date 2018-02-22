if [ $1 = "build" ]
then
  echo Building proto...
  python -m grpc_tools.protoc --proto_path="protos" --python_out="EshebaBot" "protos/service.proto"
  echo Done.
  echo
fi

