## Round-trip time (RTT)

RTT is the duration in milliseconds it takes for a network request to go from a starting point to a destination and back again to the starting point. RTT is an important metric in determining the health of a connection on a local network or the larger Internet. The **ping** utility is a method of estimating RTT.

**Reducing RTT is a primary goal of a CDN**. Improvements in latency can be measured in the reduction of RTT and by eliminating instances where roundtrips are required, such as by modifying the standard TLS/SSL handshake.

### Factors affecting RTT

- **Nature of transmission medium**: Connections made over optical fiber behaves differently from connections made over copper
- **LAN traffic**: Traffic on LAN can bottleneck a connection before it ever reaches the larger Internet
- **Server response time**: Time taken for a server to process and respond to a request
- **Node count and congestion**: Path a connection takes across the Internet; more hops through intermediate nodes will result in slower connection
- **Physical distance**: Distance is a limiting factor in network connectivity that can only be reduced by moving content closer to users

### Optimization

By maintaining servers inside internet exchange points and by having preferred relationships with ISPs and other network carriers, a CDN is able to optimize network pathways between locations, resulting in reduced RTT and improved latency for visitors accessing content cached inside the CDN.

## HTTPS round trips

1. **DNS lookup**: Converting hostname to an IP address. As DNS resolvers usually cache popular domains, and latency to ISP is fairly low, this step often takes a negligible amount of time
2. **TCP handshake (1 RTT)**: Establish a TCP connection to the server
3. **TLS handshake (1-2 RTTs)**: Client and server exchange cryptographic key material and set up an encrypted connection
4. **HTTP (1 RTT)**: Browser sends an encrypted HTTP request to the server and receives a response

Assuming DNS is instantaneous, the number of round trips vary depending on whether the connection is new or resumed, and on the TLS version.

<table>
<tr>
<th></th>
<th>TLS1.2</th>
<th>TLS1.3</th>
</tr>

<tr>
<td>New Connection</td>
<td>4 RTT + DNS</td>
<td>3 RTT + DNS</td>
</tr>

<tr>
<td>Resumed Connection</td>
<td>3 RTT + DNS</td>
<td>2 RTT + DNS</td>
</tr>
</table>
