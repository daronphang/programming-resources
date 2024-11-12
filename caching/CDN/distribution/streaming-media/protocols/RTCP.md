## RTCP (Real-time Transmission Control Protocol)

RTP is only responsible for delivering streaming media data packets. To ensure quality delivery in order, RTP is complemented with RTCP, which assists RTP in completing transmission quality control i.e. similar to TCP/IP.

RTCP is responsible for exchanging control information between session participants:

- **Sender Report**: Used to synchronize different streams in an RTP session. Includes synchronization information between media, timestamp, number of bytes sent, etc.
- **Receiver Report**: Provides feedback of data transmission including received data packets, number of lost data packets, round-trip delay, etc.

For the use of RTCP, it is recommended to keep BTCR (Byte Flow Control) within 5% of the session's bandwidth e.g. if sending rate for media streams is 4Mb/s, BTCR should be within 200kb/s.
