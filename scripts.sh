if [ $1 = 'build' ]
then
  echo 'Building proto...'

  python -m grpc_tools.protoc -I protos --python_out=./protos --grpc_python_out=. ./protos/service.proto

fi

