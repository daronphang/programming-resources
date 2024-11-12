## RTP (Real-time Transport Protocol)

As data packets inevitably encounter problems such as packet loss and delay jitter, the sender of streaming media adds a first field before sending the data packet to the transport layer. RTP is a protocol that defines a **standard packet structure** that includes audio and video data, sequence number, timestamp, and other useful information i.e. provides time information and achieves stream synchronization. RTP usually runs on top of **UDP**.
