## HTTP1.1

## Features

### Text-based protocol

HTTP/1.1 uses plain text for its headers, making it easy to read and debug.

### Persistent connections

In versions before HTTP1.1, **each HTTP request will create and close a TCP connection**. For HTTP1.1 and above, it allows for multiple HTTP requests to pass over a **persistent TCP connection** (HTTP Keep-Alive), improving resource consumption.

### Chunked transfer encoding

Allows the server to start sending a response before knowing its total size.

### Caching and compression

Supports caching mechanisms and compression (e.g., gzip) to reduce load times.

Servers should compress data (HTML, CSS, Javascript, XML) as much as possible, and should use content encoding where appropriate. Compressing already compressed media types (.zip, .jpeg, .png) is usually **not appropriate** as it can increase file size and consume compression time. If the original media is already encoded, this information is **not included** in the Content-Encoding header.

## Challenges

### Head-of-line blocking (limited concurrency)

Each HTTP/1.x connection can handle only one request at a time; a delay in one request can block the processing of subsequent requests over the same connection e.g. processing time, network latency, packet loss, etc. This happens because each request/response is processed sequentially on a single connection.

This limitation often led to inefficient use of network resources.

### Lack of prioritization

HTTP/1.x did not offer a way to prioritize requests, which could lead to less critical resources blocking more important ones.

### Header inefficiency

Headers are sent with each request and response, resulting in substantial overhead, especially for large data transfers.
