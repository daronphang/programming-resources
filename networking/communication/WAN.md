## WAN (Wide Area Network)

A WAN is the technology that connects offices, data centers, cloud applications, and cloud storage together. It spans beyond a single building to include multiple locations spread across geographic regions.

The main indicators for measuring the transmission performance and quality of a WAN are bandwidth and latency. Many applications were originally designed for LAN e.g.
Windows CIFS file sharing, enterprise resource planning (ERP) systems, databases, etc.

## Challenges and solutions

### Bandwidth issues

The bandwidth cost of a WAN is much higher than that of a LAN, and the resources are not as sufficient as those of a LAN. When the bandwidth is insufficient, the transmission of large files or data will be affected, such as sending emails with large attachments, uploading and downloading FTP files, and some file sharing operations.

Insufficient network bandwidth can be addressed as follows:

- Increase IT investment and expand bandwidth
- Reduce the amount of data transmission across the network e.g. compression, caching

### Transmission delay

In a network working environment, delay has a greater impact on data throughput than on bandwidth. Delays are caused by multiple reasons:

- **Physical distance** with data passing through multiple routing and switching devices
- **Working mechanism of TCP protocol** where data transmitted is limited by the congestion window (occurrence of this bottleneck is low) and the slow start of TCP congestion behavior. If network has high bandwidth and high latency, this behavior will lead to bandwidth wastage

To address the latency issue of the network, the most commonly used method is to **deploy devices in pairs at both ends of the network**, optimize TCP protocol, and achieve optimization of the entire transmission process.

### Low efficiency of application protocol

If an application is limited by the application's message size and message response confirmation mechanism, no matter how abundant the bandwidth is, the data transmission efficiency will not be high.

If the application protocol was originally designed for WAN, this problem would be minimized. For instance, HTTP adopts a persistent connection mechanism where webpage can use a single TCP connection to complete HTTP requests and responses.

However, if the application protocol was originally designed for LAN, it usually faces serious problems in WAN. For instance, TCP protocol is relatively **verbose** i.e. three-way handshake, high RTT, etc. CIFS protocol also involves many mechanisms including handshakes and confirmation.

To address the issue of inefficient application protocols, it is usually done by optimizing the application layer itself i.e. predicting customer behavior to send data packets in advance, caching, etc.
