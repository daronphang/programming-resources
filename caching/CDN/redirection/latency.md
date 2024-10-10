## Latency redirection

Replicating content across a geographically distributed set of servers and redirecting clients to the closest server in terms of **latency** has emerged as a common paradigm for improving client performance.

For this, all clients in the **same routable prefix** (expressed in CIDR e.g. 10.10.1.0/24) are grouped together. Grouping of clients into prefixes is naturally performed as part of Internet routing, and the current set of routable prefixes are discovered from BGP updates.

Common knowledge to optimize client latencies in such a setting is to establish **more CDN nodes** so as to have a CDN node in the proximity of every client and reduce the RTT. However, this does not suffice:

- Though most clients are served by a geographically nearby CDN node, a sizeable fraction of clients experience latencies several tens of milliseconds (e.g. 50ms) higher than other clients in the same region due to clients having circuitous routes i.e. **worst-case RTTs remain unchanged**
- Connections to most clients are impacted by significant **queueing delays**; they often override the benefits of a client interacting with a nearby server

## RTTs

RTT measured at TCP layer have three components:

- Transmission delay: Time to put a packet on the wire
- Propagation delay: Time spent from one end of the wire to the other end
- Queuing delay: Time spent by a packet waiting to be forwarded

### Client redirection

Clients can be redirected to nodes distant from them if:

- The lowest RTT node is under higher load
- DNS Nameserver used by the client is not co-located with it
- Network conditions change between when the RTT to the client's prefix was measured and when that information is used to make redirection decisions

### Propagation delay

Inflation in propagation delay could be the outcome of two factors:

- Node is far away from the client
- Routing inefficiencies

### Latency inflation

Two factors result in significant latency inflation:

1. Prefixes having **inefficient routes** to their nearby nodes, often caused by **asymmetric reverse path** i.e. forward and reverse paths are different; this becomes more pronounced when considering prefixes served by nodes active for less than a year
2. Clients in most prefixes incur significant latency overheads due to **queuing of packets**

## WhyHigh

Google built a system called WhyHigh to aid administrators in quantifying the performance gains from the significant expense and effort that goes into deploying nodes in a CDN.

WhyHigh first identifies clients with poor latencies as ones which experience latencies much higher than that along the best path to the same region. WhyHigh attempts to group together all prefixes likely affected by the same underlying cause. For example, we find that when a prefix suffers from inflated latencies, other prefixes served by the same AS path are also likely affected.

WhyHigh then attempts to pinpoint the causes for the instances of latency inflation seen at each node. To infer these causes, WhyHigh combines several different data sources including BGP tables from routers, mapping of routers to geographic locations, RTT logs for connections from clients, and traffic volume information.

### Root causes of latency inflation

- **Lack of peering**: This leads to long AS paths if shorter paths from peers are not advertised
- **Limited bandwidth capacity**: Limited bandwidth between prefix's AS and peering links can cause circuitous routing
- **Routing misconfiguration**: This can lead to circuitous routing
- **Traffic engineering**: Traffic engineering policies put in place by network administrators may result in longer paths even though alternate shorter paths exist

## Overlay

Overlay routing systems have attempted to circumvent inflated paths by routing through end-hosts that serve as relays.
