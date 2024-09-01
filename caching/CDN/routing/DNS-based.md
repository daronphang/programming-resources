## DNS-based load balancing

With DNS-based routing, when a user requests content, the CDN’s DNS server responds with the IP address of the most suitable edge server. This approach can take into account factors such as geographical proximity and server load to select the best edge server for handling the request.

### Advantages

The main advantage of DNS-based selection is **full control over where to place users**. It's not an organic placement method, and users are explicitly directed, leaving nothing to chance. If a data centre is overloaded you simply don't send users there.

### Disadvantages

The DNS server responds to the client based on the **IP of the DNS resolver**, not the actual client IP address. A client based in Europe could be configured to use a resolver in the USA. As a result, the data centre IP returned to the client will be based in the USA and not Europe.

There are also dragging issues with failover and performance issues with low DNS TTLs. Failing over with DNS is much slower than with, for example, pure BGP. BGP is designed to failover quickly.
