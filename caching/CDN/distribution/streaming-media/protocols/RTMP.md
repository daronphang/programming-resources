## RTMP (Real-time Messaging Protocol)

**Flash** is a mainstream technology for current web applications, and many video websites use Flash players as their video playback clients. Communication between Flash clients and Flash streaming media servers can only be achieved using RTMP protocol.

RTMP is a proprietary protocol developed by Adobe Systems for transmitting audio, video and data between Flash players and streaming media servers. It is an application layer protocol built on top of TCP. However, RTMP messages are not encapsulated in TCP but are transmitted through **message blocks**.

### Drawbacks

RTMP relied on highly specialized servers and clients, which is expensive to build and maintain. Hence, the web has mostly been replaced by the standard **HTML5 video**.

## Messages

Clients and servers complete various control and management functions through interactive messages. RTMP messages can be divided into protocol control messages, command messages, video messages, audio messages, user data messages, and shared object messages.

### Command

RTMP server and client transmit command information through command messages, using the AMF encoding method.
