## RTSP (Real-time Streaming Protocol)

RTSP is used to implement **playback control** e.g. pause, continue, fast forward, etc. RTSP is an application layer protocol belonging to the TCP/IP system, located above RTP and RTCP. It is **not a compression or transmission protocol**.

The interaction method of RTSP is similar to HTTP1.1, but the difference is that HTTP is an asymmetric protocol while RTSP is a symmetric protocol (both client and server can make requests).

RTSP can use either TCP or UDP transmission, which depends on the server's judgement of client's network conditions. If network conditions are good, it can use RTP over TCP.

### RTP session

RTSP control messages and data streams may be transmitted using different protocols e.g. RTSP control uses TCP, data streams use UDP. Essentially, when the server transmits data to the client, it does not know how the request-response interaction is between the two parties. During the session lifetime, the same media stream can be controlled by RTSP requests on different TCP connections. Therefore, the server needs to maintain "session state" to make RTSP requests and streams interrelated.

RTSP establishes a session for each resource access, starting from the client's first request to the object:

<table>
<tr>
<th>Method</th>
<th>Direction</th>
<th>Required</th>
<th>Meaning</th>
</tr>

<tr>
<td>DESCRIBE</td>
<td>Client-server</td>
<td>Recommended</td>
<td>Contains the RTSP URL and response type</td>
</tr>

<tr>
<td>OPTIONS</td>
<td>Client-server</td>
<td>Required</td>
<td>Access to available methods. Server-client is optional</td>
</tr>

<tr>
<td>SETUP</td>
<td>Client-server</td>
<td>Required</td>
<td>Server allocates resources for streaming media and starts an RTSP session. SETUP request includes an RTSP URL, an RTP data receiving port number, an RTCP data receiving port number, etc</td>
</tr>

<tr>
<td>PLAY</td>
<td>Client-server</td>
<td>Required</td>
<td>Server starts using the resources allocated by SETUP to transmit data. PLAY requests can be used for a single URL or multiple URLs. Supports range parameters i.e. data can be transmitted from anywhere of the media stream such as dragging</td>
</tr>

<tr>
<td>PAUSE</td>
<td>Client-server</td>
<td>Required</td>
<td>Pauses transmission. PLAY request is initiated to resume transmission</td>
</tr>

<tr>
<td>TEARDOWN</td>
<td>Client-server</td>
<td>Required</td>
<td>Stops transmitting and releases allocated resources</td>
</tr>
</table>
