## Multiplexing

Multiplexing relies on a concept called a **socket**, which consists of three things:

- An IP address
- Transport protocol
- Port number

## TCP vs UDP

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
<td>Thorough error-checking guarantees data arrives in its intended state, but consumes more bandwidth and processing cycles</td>
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
<tr>
<td>Multiplexing using ports</td>
<td>Not supported</td>
<td>Allows receiving hosts to choose the correct application for which the data is destined, based on port number</td>
</tr>
<tr>
<td>Flow control using windowing (sliding window)</td>
<td>Window concept lets the receiving host tell the sender how much data it can receive, to slow down or speed up</td>
<td>Not supported</td>
</tr>
</table>
