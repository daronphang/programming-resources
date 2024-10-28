## Anycast DNS

CDN service providers use Anycast to route traffic to the nearest data center with the capacity to process the request efficiently. An anycast-enabled CDN assigns the same IP address to multiple edge servers, relying on IP routing to deliver requests to the servers that are nearby in the network to the clients originating the requests.

Using Anycast means the network can be extremely resilient. Because traffic will find the best path, an entire data center can be taken offline and traffic will automatically flow to a proximal data center.

The Anycast approach does not use the resolver IP, but rather uses the **client IP** for Anycast routing. In contrast, DNS load balancing uses the address of the resolver. This provides a better picture as to where users are located, enabling performance metrics to be run to the user's IP, not the resolver IP.

Another CDN anycast methodology used is where anycast-based CDN load balancing provides access to replicated media content. In conjunction with routing protocols, Anycast can optimally route content requests to any one of the replicated content server nodes to maintain service scalability.

### Key features

- Shared IP: Multiple endpoints share a common IP address or range
- Localization: Traffic is routed to the topologically nearest endpoint server
- Redundancy: Automatically switches to alternate servers if one goes down
- Scalability: Seamlessly scales capacity by adding more Anycast nodes
- Load Distribution: Spreading requests across endpoints balances load efficiently

### How it works

- The CDN provider assigns the same IP address to multiple edge servers located in different geographic regions
- When a user’s device sends a DNS query to resolve the domain name to an IP address, the query is routed to a DNS server using standard DNS routing protocol
- The DNS server responds with the shared IP address of the CDN’s edge servers
- The user's device sends the content request to the shared IP address
- The request is automatically routed to the nearest edge server based on the network topology and routing protocols

### DNS mitigation

A properly Anycasted CDN increases the surface area of the receiving network so that the unfiltered denial-of-service traffic from a distributed botnet will be absorbed by each of the CDN’s data centers. As a result, as a network continues to grow in size and capacity it becomes harder and harder to launch an effective DDoS against anyone using the CDN.
