## Proto

```proto
syntax = "proto3";

package unary;

service Unary{
  // Obtains the MessageResponse at a given position
 rpc GetServerResponse(Message) returns (MessageResponse) {}

}

message Message{
 string message = 1;
}

message MessageResponse{
 string message = 1;
 bool received = 2;
}
```

## Stubs

Generates two files named example_pb2.py and example_pb2_grpc.py.

```console
$ python -m grpc_tools.protoc --proto_path=. ./unary.proto --python_out=. --grpc_python_out=.

```

## Server

```py
import grpc
from concurrent import futures
import time
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2


class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'Hello I am up and running received "{message}" message from you'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
```

## Client

```py
import grpc
import unary.unary_pb2_grpc as pb2_grpc
import unary.unary_pb2 as pb2


class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)


if __name__ == '__main__':
    client = UnaryClient()
    result = client.get_url(message="Hello Server you there?")
    print(f'{result}')
```
