## Implementation

Need to define proto file, gRPC client and gRPC server.

## gRPC Types

### Unary

Sends a single request declared in the .proto file to the server, and gets back a single response.

```py
rpc HelloServer(RequestMessage) returns (ResponseMessage)
```

### Server Streaming

Client gets back a stream of messsage and reads until there are no messages.

```py
rpc HelloServer(RequestMessage) returns (stream ResponseMessage)
```

### Client Streaming

Client writes a message sequence and waits for the server to read all messages. Server returns a response.

```py
rpc HelloServer(stream RequestMessage) returns (ResponseMessage)
```

### Bidirectional Streaming

Both client and server use a read-write stream to send a message sequence and operate independently.

```py
rpc HelloServer(stream RequestMessage) returns (stream ResponseMessage)
```
