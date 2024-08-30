## Global load balancers

Distribute incoming traffic across multiple CDNs and cloud providers.

## DNS-based load balancing

Use DNS responses to direct users to different CDN nodes based on various factors.

### Advantages

The main advantage of DNS-based selection is **full control over where to place users**. It's not an organic placement method, and users are explicitly directed, leaving nothing to chance. If a data centre is overloaded you simply don't send users there.

There are also dragging issues with failover and performance issues with low DNS TTLs. Failing over with DNS is much slower than with, for example, pure BGP. BGP is designed to failover quickly.

### Disadvantages

The DNS server responds to the client based on the **IP of the DNS resolver**, not the actual client IP address. A client based in Europe could be configured to use a resolver in the USA. As a result, the data centre IP returned to the client will be based in the USA and not Europe.

## Anycast routing

Anycast is a network addressing and routing method in which incoming requests can be routed to a variety of different locations or nodes. In the context of a CDN, Anycast typically routes incoming traffic to the nearest data center with the capacity to process the request efficiently.

## IP302

Client IP addresses and content addresses can be directly obtained, enabling precise scheduling.
