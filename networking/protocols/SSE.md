## Server Sent Events (SSE)

SSE is a technology that allows a web server to send updates to a webpage. It is a part of HTML 5 specification and similarly to WebSockets utilizes a single long live HTTP connection to send data in “real-time”. SSE is supported by most of the modern day browsers.

## Building blocks

### EventSource

Interface based on WHATWG specification and implemented by the browser. It allows the client to subscribe to events.

### EventStream

Protocol that describes the standard plain-text format of events sent by the server that must follow for the EventSource client to understand and propagate them.

Unfortunately, the Server Sent Events as a technology is designed to support only **text-based messages** and although we can send events with custom format in the end the message must be a UTF-8 encoded string.

```
MIME type: text/event-stream.
```

## Features

- Automatic reconnection
- Automatic stream resume

## SSE vs Websocket

- SSE provides one-way communication (server to client) while Websocket provides two-way communication
- SSE fully relies on HTTP and has support for both HTTP/1.1 (limits the number of parallel connections) and HTTP/2 (multiplexing)
- Websocket uses its custom protocol
- SSE is a pure text protocol (no complex format) while Websocket can handle both text and binary messages e.g. images, audio, files
- SSE can be polyfilled into older browsers that do not support it natively using Javascript
- SSE has built-in support for reconnection
