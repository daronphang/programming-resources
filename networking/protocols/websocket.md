## Websocket

Websocket is a bidirectional, full-duplex protocol that is used in client-server communication. It is a stateful protocol i.e. connection between client and server will be kept alive (persistent) until it is terminated by either party. Operates over HTTP through a single TCP/IP socket connection. WebSocket URIs uses a new scheme ws: or wss: while the remainder of URI is the same as HTTP including host, port, path and any query parameters.

### Security

The biggest disadvantage of Websocket as a protocol is security. It is not restricted by same-origin policy, which may make CSRF-like attacks a lot easier.

## Applications

### Real-Time

Websocket is used to display data at client end, which is continuously being sent by the backend server. Examples include stock trading and autonomous driving.

### Gaming

Data is continuously received by the server without refreshing the UI.

### Chat

Websocket can be used to establish connection once for exchange, publishing and broadcasting the message among subscribers. Reuses the same websocket connection for sending and receiving the message.
