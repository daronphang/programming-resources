## DNS redirection

DNS redirection is a transparent mechanism by which the client can be kept completely unaware of where documents are located. DNS redirection directs user requests for content to the nearest or most appropriate CDN edge server.

With DNS redirection, a client’s DNS request is redirected to an **authoritative DNS name server that is controlled by the CDN**, which then resolves the CDN server name to the IP address of one or more content servers.

For close proximity, a minimum of two edge servers can be returned for redundancy. For clients that are further away, more servers can be returned.

DNS redirection can be used to deliver full or partial site content:

- Full: All DNS requests for the origin server are redirected to the CDN
- Partial: The origin site modifies certain embedded URLs so that requests for only those URLs are redirected to the CDN

### Advantages

The main advantage of DNS-based selection is **full control over where to place users**. It's not an organic placement method, and users are explicitly directed, leaving nothing to chance. If a data centre is overloaded you simply don't send users there.

### Disadvantages

The DNS server responds to the client based on the **IP of the DNS resolver**, not the actual client IP address. This may result in a huge additional communication cost, as the local DNS server is often not that local. This problem can be mitigated if the local DNS resolver allows the client to also specify its own IP address.

There are also dragging issues with failover and performance issues with low DNS TTLs. Failing over with DNS is much slower than with, for example, pure BGP. BGP is designed to failover quickly.

## Global Server Load Balancing (GSLB)

GSLB is a technique used by CDN providers to distribute incoming traffic across multiple geographically dispersed servers or data centers.

The primary goal of GSLB is to ensure that user requests are routed to the server that can provide the best performance and availability. It typically considers the following factors:

- Geographic proximity
- Server load
- Network conditions

### DNS integration

For a CDN, the GSLB system is usually integrated into the CDN’s overall DNS infrastructure, which works alongside the standard DNS hierarchy. In a CDN setup, the GSLB operates at the **authoritative DNS level**:

- In a CDN setup, the authoritative DNS servers are managed by the CDN provider and integrate the GSLB system
- The GSLB receives the DNS query and analyzes it based on factors e.g. user's location, server load, network conditions, etc.
- Based on the analysis, it selects the optimal CDN edge server to handle the request and returns its IP address to the local DNS resolver/recursor
