## UDP (User Datagram Protocol)

UDP is a message-oriented communication protocol that allows computing devices and applications to send data via a network without verifying its delivery, which is best suited to real-time communication and broadcast systems i.e. videoconferencing, live streaming.

Unlike TCP, UDP does not expose the abstraction of a byte stream to its clients. Clients can only send discrete packets (**datagrams**) with a limited size.

UDP is a good choice in situations where delayed data is worthless. For RTC, there is no point retransmitting lost packets; instead, the application must fill the missing packet's time slot with silence.

UDP enables continuous data transmission without acknowledging or confirming the connection. It is **connection-less** as no connection is established before communication occurs. Commonly referred to as the 'fire-and-forget' protocol.

UDP does not guarantee delivery of packets (reliability) as datagrams don't have sequence numbers are not acknowledged. Also, UDP doesn’t implement flow and congestion control.

### UDP restriction

Some company networks block UDP intentionally for the following:

- Harder to control: Firewalls cannot easily track sessions
- Harder to inspect: Security devices are optimized for TCP (deep packet inspection), and UDP is harder to verify legitimacy, spoofed packets are easier to send
- Easier to abuse
- Often used in DDoS attacks

UDP can be used for:

- Global users
- High packet loss
- Long TLS handshake distances
