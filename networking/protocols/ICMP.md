## Internet Control Message Protocol (ICMP)

The ICMP is a network layer protocol used by network devices to diagnose network communication issues. ICMP is mainly used to determine whether or not data is reaching its intended destination in a timely manner. Commonly, the ICMP protocol is used on network devices, such as routers. ICMP is crucial for error reporting and testing, but it can also be used in distributed denial-of-service (DDoS) attacks. ICMP is used by **ping**.

## ping

Ping uses ICP Echo Request/Reply, and anything blocking ICMP will break it, even if the network works fine (TCP works but ping times out). Common issues include:

1. Firewalls, security groups, WAFs blocking ICMP
2. Many production servers intentionally drop ping
3. MTU/fragmentation issues, ICMP packets get dropped due to size

```sh
$ ping -M do -s 1400 host
```

4. Rate limiting/throttling
5. DNS issues
