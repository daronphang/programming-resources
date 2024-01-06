## Protobuf

```proto
// both client and server 'stub' have SayHello() RPC method
service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}
```

## Generate Python Code from Protobufs

Generates \_pb2.py and \_pb2_grpc.py files. Latter module imports the former.

The former module is synthesized by protoc, which defines non-gRPC-specific code elements i.e. classes corresponding to protocol buffers messages and descriptors used by reflection.

https://grpc.io/docs/languages/python/generated-code/

### Command

1. Runs the protobuf compiler
2. Import path of protobuf code (not needed, but -I flag is required)
3. Output paths of created files (client and server code)
4. Path to the protobuf file

```console
$ python -m grpc_tools.protoc -I ../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld.proto
```

For each service defined in the .proto file, three primary elements are generated.

### Stub

Stub is used by the client to connect to a gRPC service. Has a constructor that takes a gRPC.Channel object and initializes the stub.

For each method in the service, the initializer adds a corresponding attribute to the stub object with the same name, that depends on the RPC type.

```
UnaryUnaryMultiCallable
UnaryStreamMultiCallable
StreamUnaryMultiCallable
StreamStreamMultiCallable
```

### Servicer

For each service, a Servicer class is generated, which serves as a the superclass of a service implementation. Used by the server to implement a gRPC service.

For each method in the service, a corresponding function in the Servicer class is generated. The functions are overridden with the service implementation.

### Registration Function

Function is used to register a servicer with a grpc.Server object, so that the server can route queries to the respective servicer.

Function takes an object that implements the Servicer i.e. subclass instance, and a grpc.Server object.

## Client

Stubs are used by clients to invoke server RPCs.

```py
from __future__ import print_function

import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you')) # serialize response
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
```

## Server

Servicer (GreeterServicer) defines the interface for implementations of the specific service.

```py
from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


# helloworld_pb2_grpc.GreeterServicer is the superclass
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name) # serialize response


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
```
