## dig

Used for performing DNS lookup, i.e. querying DNS servers.

```sh
$ dig whoami.byte008.com # get IP of DNS resolver

$ dig whoami.byte008.com @8.8.8.8 # force to use Google DNS
```

### Subnet

Subnet is a range of IP addresses inside a network. CDNs often return different IP addresses depending on where the user is located. Passing the subnet enables ECS from the recursive DNS, so that the authoritative Server can see the real user IP, and enables CDN to return the closest edge server.

```
Network: 192.168.0.0/16
Subnets: 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24

User -> Recursive DNS (ECS enabled) -> Authoritative DNS
```

DNS often does not send the full IP, but prefix to protect user privacy. You can pass subnet to simulate a DNS query from a specific client network so CDNs return the correct regional IP.

```sh
$ dig +subnet=1.2.3.4 example.com  # uses ECS, pretend client belongs to the subnet 1.2.3.4
```

### Caveat

When a client network utilizes perimeter security like proxies or firewalls, diagnostic tools such as `dig` and `traceroute` may show a completely different network path than the one used by actual application traffic. Consequently, their output is not representative of the real user traffic flow.

## traceroute

Traceroute is a tool used to diagnose problems in a network path. Traceroute is used to understand the path IP packets are taking from one computer (source IP address) to another (destination IP address). With traceroute, it makes it possible to understand:

- The path your packets are taking (including the IP addresses of each router)
- The RTT between the source and each hop, or router the packets pass through, in the network path

A traceroute tool sends packets to a destination IP and with a time-to-live (TTL) set to 1, so that the first router the packets reach will send back an error (“time exceeded”). When the error returns, the traceroute tool records the first router’s identity and round-trip time, increments the TTL, and sends new packets, repeating this process until either:

1. The last packet reaches the destination IP or
2. Two sets of packets are dropped

```sh
$ traceroute google.com

# each line is a hop (router) along the route
# 1  192.168.1.1
# 2  10.1.0.1
# 3  isp-router
# 4  backbone-router
# 5  google-edge

$ traceroute -I 128.75.237.56 # use ICMP echo for path probing
```

## mtr (my traceroute)

MTR is a tool that combines traceroute and ping, which is another common method for testing network connectivity and speed. In addition to the hops along the network path, MTR shows constantly updating information about the latency and packet loss along the route to the destination, by **continuously sending packets**. This helps in troubleshooting network issues by allowing you to see what’s happening along the path in real-time.

```sh
$ mtr -nz 71.18.1.84
```

### Packet loss, control plane policing

MTR works by sending out (as a default) ICMP Echo packets, with an incrementing TTL per packet. When the TTL expires, a router will send back an ICMP Type 11 (Time Exceeded), indicating how many hops there are from point A to point B.

Many network operators (including Cloudflare) set arbitrary limits on the amount of ICMP packets that are allowed to reach the control plane of a router. (The control plane is the router's brain.) A packet that exceeds a router's TTL has to be processed by the control plane. To prevent the control plane from being overwhelmed by too many of these packets, a rate limit (or policer) is put in place, which is why we see all that loss on the intermediary hops, but not the final hop.

## tcpdump

tcpdump is used to capture and inspect network packets on a system, i.e. lets you see the raw network traffic going in and out of a machine. Results can be viewed using Wireshark.

```sh
$ tcpdump -i eth0

$ tcpdump port 53 # capture DNS traffic

$ tcpdump tcp # capture TCP packets

$ tcpdump udp # capture UDP packets
```

## Ports

1. Using nc (netcat)

```sh
$ nc -zv HOST PORT
$ nc -zv google.com 80
```

2. Using telnet

```sh
$ telnet HOST PORT
$ telnet example.com 80
```

3. Checking locally using lsof

```sh
$ lsof -i :PORT
```

## HAR file

1. Given the remote IP, test the edge server the client is connected to

```sh
$ curl --resolve example.com:443:23.xx.xx.xx https://example.com/image.jpg
```

## Others

1. `https://ipinfo.io`: Get IP information for an IP address
2. Get public IP address

```sh
$ curl https://api.ipify.org
```
