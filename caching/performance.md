## Reducing latency

### Parallel requests and batching

Parallel requests and batching can help to minimize the number of network round trips necessary to respond to page requests.

A **directed acyclic graph (DAG)** that represents the dependencies between data can be constructed. This will help to maximize the number of items that can be fetched concurrently. By analyzing the DAG, the web server can determine the optimal order and grouping of data fetches. It identifies data items that can be retrieved in parallel, without any dependencies, and groups them in a single batch request.

### Client-server communication

Clients can use UDP and TCP to communicate with cache servers.

UDP is used for GET requests to reduce latency and overhead. Since UDP is connection-less, each thread in the origin/web server is allowed to directly communicate with cache servers directly. UDP packet losses are treated as cache-miss on the client-side.

For reliability, clients perform SET and DELETE operations over TCP. TCP alleviates the need to add a retry mechanism to the UDP implementation.

### Incast congestion

Clients can implement flow-control mechanisms to limit incast congestion. When a client requests a large number of keys, the responses can overwhelm components if those responses arrive all at once. Clients can use a **sliding window mechanism** to control the number of outstanding requests. When the client receives a response, the next request can be sent. Similar to TCP’s congestion control, the size of this sliding window grows slowly upon a successful request and shrinks when a request goes unanswered.

### Pre-established connections

The cache client can maintain a pool of open connections to the cache servers.

When the application needs to make a cache request, it borrows a connection from the pool instead of establishing a new TCP one. This is because a TCP handshake could nearly double the cache response times. Borrowing the connection avoids the overhead of the TCP handshake on each request.

However, keeping connections open consumes memory and other resources on both the client and server. Therefore, it’s important to carefully tune the number of connections to balance resource usage with the ability to handle traffic spikes.

### Fail-fast approach

If a cache server becomes unresponsive, the client immediately marks it as down for a few seconds and fails the request, treating it as a cache miss. The client will not retry the request or attempt to establish new connections to the problematic server.

The key insight is that even brief retry delays of 100ms can cause cascading failures under heavy load. The tradeoff is a slight increase in cache misses, but is better than risking a system-wide outage.

## Cache warming

A cold cache (empty) can retrieve data from a warm cache with normal hit rate caches instead of hitting the persistent storage. This will reduce the turnup time.

However, there can be race conditions here with cache consistency, which can be solved by adding a two second hold-off to deletes in the cold cache. This is turned off once the cold cache server's cache hit rate diminishes.
