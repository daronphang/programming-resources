## mtr (my traceroute)

Traceroute is a tool used to diagnose problems in a network path. Traceroute is used to understand the path IP packets are taking from one computer (source IP address) to another (destination IP address). With traceroute, it makes it possible to understand:

- The path your packets are taking (including the IP addresses of each router)
- The RTT between the source and each hop, or router the packets pass through, in the network path

A traceroute tool sends packets to a destination IP and with a time-to-live (TTL) set to 1, so that the first router the packets reach will send back an error (“time exceeded”). When the error returns, the traceroute tool records the first router’s identity and round-trip time, increments the TTL, and sends new packets, repeating this process until either:

1. The last packet reaches the destination IP or
2. Two sets of packets are dropped

My Traceroute (MTR) is a tool that combines traceroute and ping, which is another common method for testing network connectivity and speed. In addition to the hops along the network path, MTR shows constantly updating information about the latency and packet loss along the route to the destination. This helps in troubleshooting network issues by allowing you to see what’s happening along the path in real-time.

### Packet loss, control plane policing

MTR works by sending out (as a default) ICMP Echo packets, with an incrementing TTL per packet. When the TTL expires, a router will send back an ICMP Type 11 (Time Exceeded), indicating how many hops there are from point A to point B.

Many network operators (including Cloudflare) set arbitrary limits on the amount of ICMP packets that are allowed to reach the control plane of a router. (The control plane is the router's brain.) A packet that exceeds a router's TTL has to be processed by the control plane. To prevent the control plane from being overwhelmed by too many of these packets, a rate limit (or policer) is put in place, which is why we see all that loss on the intermediary hops, but not the final hop.
