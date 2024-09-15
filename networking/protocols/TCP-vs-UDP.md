## TCP (Transmission Control Protocol)

TCP is defined as a connection-oriented communication protocol that allows computing devices and applications to send data via a network and verify its delivery. Relies on a three-way handshake (synchronization, synchronization acknowledgement and final acknowledgement).

Task of TCP is to carry packets across the internet and ensure the successful delivery of messages and data across networks.

Before sending data, client and server must establish a connection. The server must actively listen for client requests whenever a connection is established.

However, while TCP is an instinctively reliable protocol, the feedback mechanisms also result in a more significant overhead size i.e. consumes more bandwidth.

TCP dynamically adapts the rate of data transfer to the available network capacity. When it is idling, it does not consume any bandwidth.

<img src="../assets/TCP.png">

## UDP (User Datagram Protocol)

UDP is a message-oriented communication protocol that allows computing devices and applications to send data via a network without verifying its delivery, which is best suited to real-time communication and broadcast systems i.e. videoconferencing, live streaming.

UDP is a good choice in situations where delayed data is worthless. For RTC, there is no point retransmitting lost packets; instead, the application must fill the missing packet's time slot with silence.

UDP enables continuous data transmission without acknowledging or confirming the connection. It is **connection-less** as no connection is established before communication occurs. Commonly referred to as the 'fire-and-forget' protocol.

However, UDP has a drawback: it doesn’t guarantee the delivery of packets. If a packet is lost during transmission, UDP doesn’t have a built-in mechanism to retransmit it.

## Differences

<table>
<tr>
<th>Factor</th>
<th>TCP</th>
<th>UDP</th>
</tr>
<tr>
<td>Connection type</td>
<td>Requires an established connection before transmitting data</td>
<td>No connection is needed to start and stop a data transfer</td>
</tr>
<tr>
<td>Data sequence</td>
<td>Can sequence data i.e. in a specific order</td>
<td>Cannot sequence or arrange data</td>
</tr>
<tr>
<td>Data retransmission</td>
<td>Can retransmit data if packets fail to arrive</td>
<td>No data retransmitting</td>
</tr>
<tr>
<td>Delivery</td>
<td>Guaranteed</td>
<td>Not guaranteed</td>
</tr>
<tr>
<td>Error checking</td>
<td>Thorough error-checking guarantees data arrives in its intended state</td>
<td>Minimal error-checking</td>
</tr>
<tr>
<td>Broadcasting</td>
<td>Not supported</td>
<td>Supported</td>
</tr>
<tr>
<td>Speed</td>
<td>Slow</td>
<td>Fast</td>
</tr>
</table>
