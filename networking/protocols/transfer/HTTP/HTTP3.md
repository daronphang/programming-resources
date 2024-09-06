## HTTP3

HTTP/3 does away with TCP, and instead utilizes a flavor of **UDP** called Quick UDP Internet Connections (QUIC).

## Benefits

### UDP-based transport

HTTP/3 utilizes UDP for faster, lower-latency data transmission. QUIC ensures reliability of delivery.

### QUIC handshake

UDP doesn't require a handshake to start sending data; however, QUIC has introduced its own handshake mechanism for security.

QUIC combines both transport and cryptographic handshakes in its connection establishment process i.e. integrated handshake. It reduces the number of round trips required to establish a secure connection.

QUIC enables 0-RTT (round trip time) connection establishment in certain situations, which can significantly reduce latency when connecting to a previously visited server.

<img src="../../assets/QUIC-handshake.png">

### Built-in encryption

QUIC incorporates TLS1.3 by default, ensuring a secure connection without the need for a separate TLS handshake. This reduces latency and improves connection establishment time.

### Reduced head-of-line blocking

Unlike TCP, QUIC handles packet loss at the individual stream level. This means that the loss of a single packet does not block the entire connection, further reducing head-of-line blocking issues.

### Connection migration

QUIC is designed to better support connection migration, allowing clients to change IP addresses without losing connectivity or incurring additional latency.

### Improved congestion control

QUIC offers more advanced congestion control mechanisms, allowing it to better adapt to varying network conditions and improve overall performance.

### Stream Multiplexing

Both HTTP/2 and HTTP/3 support multiplexing, allowing multiple requests and responses to be sent simultaneously over a single connection. But TCP, employed by HTTP/2, considers every request (including multiplexed ones) as a single byte stream. This approach employed by TCP is usually the cause of **head-of-line blocking issues** during multiplexed streaming in HTTP/2.

In HTTP/3, the issue is addressed via implementation of UDP’s **out-of-order delivery**, where each byte stream is transported independently over the network. If a packet is lost, only the affected stream waits for retransmission, while others continue unaffected.

<img src="../../assets/QUIC-streaming.png">
