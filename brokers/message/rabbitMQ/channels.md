## Channels

A Connection represents a real TCP connection to the message broker. However, some applications need multiple logical connections to the broker, and it is undesirable to keep many TCP connections open at the same time because doing so consumes system resources and makes it more difficult to configure firewalls. AMQP 0-9-1 connections are multiplexed with channels that can be thought of as **lightweight connections that share a single TCP connection**.

A channel only exists in the context of a connection and never on its own. When a connection is closed, so are all channels on it.

Every protocol operation performed by a client happens on a channel. Communication on a particular channel is completely separate from communication on another channel.

For applications that use multiple threads/processes for processing, it is very common to open a **new channel per thread/process** and not share channels between them.

### Closing

When a channel is no longer needed, it should be closed. Closing a channel will render it unusable and schedule its resources to be reclaimed.

### Maximum number of channels per connection

The maximum number of channels that can be open on a connection simultaneously is negotiated by client and server at connection time. The value is configurable for both RabbitMQ and client libraries.

On the server side, the limit is controlled using the channel_max.

### Channel leaks

A channel leak is a condition under which an application repeatedly opens channels without closing them, or at least closing only some of them.

Channel leaks eventually exhaust the node (or multiple target nodes) of RAM and CPU resources.
