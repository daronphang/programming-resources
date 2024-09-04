## Addressing schemes

The IP uses three types of addressing schemes: Unicast, Multicast, and Anycast.

## Unicast

A Unicast address is used to identify a single unique host. It is used to send data to a single destination. In computer networking, unicast communication is a one-to-one transmission from one point in the network to another.

## Multicast

A Multicast address is used to deliver data to a group of destinations (a one-to-many transmission). IP multicast group addresses are represented by class-D IP addresses reserved specifically for multicast communications, ranging from 224.0.0.0 through 239.255.255.255.

Any IP packet sent to a multicast address is delivered to only those hosts that have joined that particular IP Multicast group, resulting in less network traffic, thereby reducing bandwidth and network overhead. If the host hasn’t joined the group, the receiver ignores the packets at the hardware level, eliminating platform software resource consumption in that network element. IPv6 multicast replaces broadcast addresses that were supported in IPv4.

## Anycast

Anycast is an IP network addressing scheme that allows multiple servers to share the same IP address, allowing for multiple physical destination servers to be logically identified by a single IP address i.e. Anycast network routing is able to route incoming connection requests across multiple data centers.

When requests come into a single IP address associated with the Anycast network, the network distributes the data based on some prioritization methodology i.e. location, number of hops, etc. The selection process behind choosing a particular data center will typically be optimized to reduce latency by selecting the data center with the shortest distance from the requester.

Anycast IP addresses are distributed across various geographic locations. Network routers direct user requests to the nearest edge server using the same IP address.

Anycast is characterized by a 1-to-1 of many association, and is one of the 5 main network protocol methods used in the Internet protocol.

### IPv4 and IPv6

Anycast is not officially supported in IPv4. However, this can be worked around through using BGP. Essentially, multiple hosts are given the same unicast IP and routes are announced through BGP. Therefore, routers interpret this as multiple routes to the same destination whereas in fact, they are routed to different destinations with the same address.

The drawback to this approach, however, is that the network may perform what is called a **"POP switch"** (point of presence) which changes the routing packets in the event that there is congestion or changes in the network.

IPv6 on the other hand explicitly supports anycast. IPv6 routers typically won't distinguish an anycast packet from a unicast packet through the network although special handling from the routers near the destination is required.

### DNS

Anycast makes DNS resolving much faster. With Anycast DNS, a DNS query will go to a network of DNS resolvers rather than to one specific resolver, and will be routed to whichever resolver is closest and available. DNS queries and responses will follow optimized paths in order to answer queries as quickly as possible.

Anycast also helps keep DNS resolving services highly available. If one DNS resolver goes offline, queries can still be answered by other resolvers in the network.

### BGP

Anycast and BGP work together to optimize the delivery of network services by using BGP to route traffic efficiently to the nearest or best-performing Anycast node, thereby enhancing performance, reliability, and scalability.

Each Anycast node advertises its presence using BGP. This involves sending BGP route announcements that include the shared IP address. These advertisements are propagated across the Internet to other BGP routers (autonomous systems).

When a router receives a packet destined for the Anycast IP address, it uses BGP's routing information to determine the best path to reach one of the advertised Anycast nodes. BGP routers use metrics such as network distance, AS path length, and other attributes to select the optimal route.

If the server fails, the anycast route is withdrawn from the routing table, and a router forwards the client’s request through an alternate path to another server that is listening on the same anycast IP address.

BGP continuously updates routing tables based on network changes. If one Anycast node becomes unreachable or less optimal, BGP will automatically reroute traffic to the next best Anycast node.
