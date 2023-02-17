## Docs

https://protobuf.dev/

https://developers.google.com/protocol-buffers/docs/reference/python-generated

## Returning Response

```py
# client
from google.protobuf.json_format import MessageToDict

resp = stub.Hello(request='hello')
print(MessageToDict(resp, preserving_proto_field_name=True))
```

## Custom Validation

Can either convert to dict and parse it through Pydantic, or perform validation in code.

## Dynamic Fields

To read fields with composite types, need to perform recursion with value.items().

```proto
message Request {
    string name = 1;
    google.protobuf.Struct payload = 2;
}
```

```py
import pb2

p = pb2.Request()
p.name = 'john'
p.payload.update({'hello': 'world'})

# server
request.payload.items()
```

## Any

Need to pack (client) and unpack (server). Alternatively, can utilize MessageToDict() and Pydantic class for schema validation on server.

```proto
syntax = "proto3";
import "google/protobuf/any.proto";

message Random {
    string name = 1;
    int32 uid = 2;
}

message Request {
    google.protobuf.Any unknown = 1;
}
```

```py
# initialize protobuf class
random = pb2.Random()
random.name = 'john'
random.uid = 1234

# pack into Any
some_any = pb2.google_dot_protobuf_dot_any__pb2.Any()
some_any.Pack(random)

# attach to request
request = Request()
request.unknown.CopyFrom(some_any)

# unpack
some_any = pb2.google_dot_protobuf_dot_any__pb2.Any()
some_any.CopyFrom(request.unknown)
random = pb2.Random()
some_any.Unpack(random)
print(random)
```

```py
from google.protobuf.json_format import MessageToDict
from pydantic import BaseModel, StrictStr


class Testing(BaseModel):
    name: StrictStr


def hello(self, request, context):
    payload = MessageToDict()
    payload = Testing(**payload)
    print(payload)
```

## Repeated Fields

Repeated fields are represented as an object that acts like a Python sequence. As with embedded messages, you cannot assign the field directly, but you can manipulate it.

```py
foo = Foo()
foo.nums.append(15)        # Appends one value
foo.nums.extend([32, 47])  # Appends an entire list
```

### Nested Composite Fields

```proto
message Foo {
  repeated Bar bars = 1;
}

message Bar {
  optional int32 i = 1;
  optional int32 j = 2;
}

message FooBar {
    repeated google.protobuf.Struct results = 1;
}
```

```py
foo = Foo()
bar = foo.bars.add()        # Adds a Bar then modify
bar.i = 15
foo.bars.add().i = 32       # Adds and modify at the same time
new_bar = Bar()
new_bar.i = 40
another_bar = Bar()
another_bar.i = 57
foo.bars.append(new_bar)        # Uses append() to copy
foo.bars.extend([another_bar])  # Uses extend() to copy
```

```py
dummy = [
    {'name': 'john', 'address': '123'},
    {'name': 'john', 'address': '123'}
]

foo = Foo()
for x in dummy:
    bar = foo.bars.add()
    bar.update(x)   # for struct fields
```
