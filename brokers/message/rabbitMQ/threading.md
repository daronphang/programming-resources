## Connection and Channel

A connection (TCP) is a link between the client and the broker, that performs underlying networking tasks including initial authentication, IP resolution, and networking.

Many applications needs to have multiple connections to the broker, and instead of having many connections an application can reuse the connection, by instead, create and delete channels. Keeping many TCP connections open at the same time is not desired, as they consume system resources. The handshake process for a connection is also quite complex and requires at least 7 TCP packets or more if TLS is used.

A channel is the primary communication method for interacting with RabbitMQ, and acts as a virtual connection inside a TCP connection. A channel reuses a connection, forgoing the need to reauthorize and open a new TCP stream. Channels allow you to use resources more efficiently (more about this later in this article).

For applications that use multiple threads/processes for processing, it is very common to open a new channel per thread/process and not share channels between them.
