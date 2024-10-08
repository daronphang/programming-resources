## TCP (Transmission Control Protocol)

TCP is defined as a connection-oriented communication protocol that allows computing devices and applications to send data via a network and verify its delivery.

Before sending data, client and server must establish a connection. The server must actively listen for client requests whenever a connection is established. Task of TCP is to carry packets across the internet and ensure the **successful delivery** of messages and data across networks.

However, while TCP is an instinctively reliable protocol, the feedback mechanisms also result in a more significant overhead size i.e. consumes more bandwidth.

TCP dynamically adapts the rate of data transfer to the available network capacity. When it is idling, it does not consume any bandwidth.

### Handshake

TCP uses a **three-way handshake** to setup a TCP/IP connection over an IP based network:

1. The client (browser) sends a TCP SYNchronize packet to the server
2. The server receives the SYN and sends back a SYNchronize-ACKnowledgement
3. The client receives SYN-ACK and sends an ACKnowledge
4. The server receives ACK and TCP socket connection is established

TCP requires a total of **1 RTT** to complete the handshake.

<img src="../../assets/TCP.png">

### Segmentation

TCP partitions a byte stream into discrete packets called segments. The segments are sequentially numbered, which allows the receiver to detect holes and duplicates. Every segment sent needs to be acknowledged by the receiver. When that doesn’t happen, a timer fires on the sending side, and the segment is retransmitted. To ensure that the data hasn’t been corrupted in transit, the receiver uses a checksum to verify the integrity of a delivered segment.

### Flow control

Flow control is a backoff mechanism implemented to prevent the sender from overwhelming the receiver. The receiver stores incoming TCP segments waiting to be processed by the process into a receive buffer.

The receiver also communicates back to the sender the size of the buffer whenever it acknowledges a segment. The sender avoids sending more data that can fit in the receiver’s buffer. TCP is **rate-limiting** on a connection level.

### Congestion control

TCP not only guards against overwhelming the receiver, but also against flooding the underlying network.

The sender estimates the available bandwidth of the underlying network empirically through measurements. The sender maintains a **congestion window**, which represents the total number of outstanding segments that can be sent without an acknowledgement from the receiver.

When a new connection is established, the size of the congestion window is set to a system default. Then, for every segment acknowledged, the window increases its size exponentially until reaching an upper limit. This means that we can’t use the network’s full capacity right after a connection is established. **The lower the round trip time (RTT) is, the quicker the sender can start utilizing the underlying network’s bandwidth**.

### Pipelining

In traditional TCP operation, the sender waits for an acknowledgment for one segment before sending the next. With pipelining, the sender can continue to send data as long as it stays within the **allowed window size**.

Pipelining refers to the ability to **send multiple packets of data without waiting for an acknowledgment for each individual packet**. This technique reduces the idle time between sending packets, improves the efficiency of data transmission, reduces latency and improves overall throughput.
