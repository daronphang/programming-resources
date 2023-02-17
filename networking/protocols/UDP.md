## UDP (User Datagram Protocol)

UDP is a message-oriented communication protocol that allows computing devices and applications to send data via a network without verifying its delivery, which is best suited to real-time communication and broadcast systems i.e. videoconferencing, live streaming.

UDP is a good choice in situations where delayed data is worthless. For RTC, there is no point retransmitting lost packets; instead, the application must fill the missing packet's time slot with silence.

UDP enables continuous data transmission without acknowledging or confirming the connection. It is 'connectionless' as no connection is established before communication occurs. Commonly referred to as the 'fire-and-forget' protocol.
