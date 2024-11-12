## DNS redirection

DNS redirection is a transparent mechanism by which the client can be kept completely unaware of where documents are located. DNS redirection directs user requests for content to the nearest or most appropriate CDN edge server. Scheduling by DNS resolution is most commonly applied in **GSLB**.

With DNS redirection, a client’s DNS request is redirected to an **authoritative DNS name server that is controlled by the CDN**, which then resolves the CDN server name to the IP address of one or more content servers. DNS redirection can be used to deliver full or partial site content:

- Full: All DNS requests for the origin server are redirected to the CDN
- Partial: The origin site modifies certain embedded URLs so that requests for only those URLs are redirected to the CDN

For close proximity, a minimum of two edge servers can be returned for redundancy. For clients that are further away, more servers can be returned.

## Advantages

### Full control over placement

The main advantage of DNS-based selection is **full control over where to place users**. It's not an organic placement method, and users are explicitly directed, leaving nothing to chance. If a data centre is overloaded you simply don't send users there.

## Drawbacks

### DNS misconfiguration

The DNS server responds to the client based on the **IP of the local DNS resolver**, not the actual client IP address. In some cases, the user and local DNS server may not be in the same region. This may result in a huge additional communication cost. This problem can be mitigated if the local DNS resolver allows the client to also specify its own IP address i.e. user manually configures their own local DNS server.

There are also dragging issues with failover and performance issues with low DNS TTLs. Failing over with DNS is much slower than with, for example, pure BGP. BGP is designed to failover quickly.

### Invalidation issues

If the DNS caching mechanism of the local DNS server ignores TTL value, it will indefinitely cache the results. Moreover, DNS cache cannot cope with sudden server failures.
