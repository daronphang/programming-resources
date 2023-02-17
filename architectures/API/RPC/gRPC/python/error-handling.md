## Error Handling

```py
class MyService(proto_pb2.SomethingServicer):

    def Do(self, request, context):
        if not is_valid_field(request.field):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Consarnit!')
            return proto_pb2.Response()
        return proto_pb2.Response(response='Yeah!')
```
