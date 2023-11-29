## Border Gateway Protocol (BGP)

BGP is a set of rules that determine the best network routes for data transmission on the internet. The internet consists of thousands of private, public, corporate, and government networks linked together through standardized protocols, devices, and communication technologies. Whne you browse the internet, data travels across multiple networks before reaching its destination. **BGP's responsibility is to look at all the available paths that data could travel and select the best route**, which means hopping between autonomous systems.

BGP is the protocol that makes the internet work by enabling data routing. When a user in Singapore loads a website with origin servers in Argentina, BGP is the protocol that enables that communication to happen quickly and efficiently.

BGP creates network stability by guaranteeing that routers can adapt to route failures. When one path goes down, BGP quickly finds a new path. BGP makes routing decisions based on paths, defined by rules or network policies set by network administrators.

### Autonomous systems

The internet is a network of networks, and broken up into hundreds of thousands of smaller networks known as **autonomous systems (AS)**. Each of these networks is essentially a large pool of routers run by a single organization.

The structure of the internet is constantly changing, and every AS must be kept up to date with information regarding new routes as well as obsolete routes. This is done through **peering sessions** where each AS connects to neighboring ASes with a TCP/IP connection for the purpose of sharing routing information.

### Who operates BGP autonomous systems?

ASes typically belong to Internet Service Providers (ISPs) or other large organizations such as tech companies, universities, and government agencies i.e. Singtel, M1. Each AS wishing to exchange routing information must have a registered autnomous system number (ASN).

Internet Assigned Numbers Authority (IANA) assigns ASNs to Regional Internet Registries (RIRs), which then assigns them to ISPs and networks.

## How does BGP work?

BGP works using a mechanism called **peering**. Administrators assign certain routers as BGP peer or BGP speaker routers. You can think peers as devices on the edge or boundary of an autonomous system. BGP performs three main functions. BGP enables peering to send packets between ASes.

### Route discovery

BGP peers exchange routing information with neighboring BGP peers through network-layer reachability information (NLRI) and path attributes:

- NLRI includes connectivity information about neighbors
- Path attributes include information like latency, hop count, and cost of tranmission

After they have exchanged information, each BGP peer can then construct a graph of network connections around it.

### Route storage

During the discovery process, every BGP router collects route advertisement information and stores it in the form of routing tables. It uses the routing table for path selection and also updates it frequently.

### Path selection

BGP routers used the stored information to route traffic optimally. The primary factor in path selection is the shortest path, as determined by the stored route graphs.

When a destination is reachable from multiple paths, BGP selects the best one by sequentially evaluating other path attributes. BGP makes best-path decisions based on attributes that include the following:

- Highest weight
- Current reachability
- Hop counts
- Local preference
- Oldest path

## External vs internal BGP

Internal BGP refers to a mechanism that gives information about the internal routers in a system. This is done using a mesh topology, which involves routes being received from internal BGP neighbors without them being advertised to other internal BGP neighbors. In this way, an internal BGP system avoids loops. Routing loops are more common in external BGP systems because they do not use a similar mesh topology.

## BGP flaws and hijacking

In 2004, a Turkish ISP called TTNet accidentally advertised incorrect BGP routes to its neighbors. These routes claimed that TTNet itself was the best destination for all traffic on the Internet. As these routes spread further and further to more autonomous systems, a massive disruption occurred, creating a one-day crisis where many people across the world were not able to access some or all of the Internet.

Similarly, in 2008, a Pakistani ISP attempted to use a BGP route to block Pakistani users from visiting YouTube. The ISP then accidentally advertised these routes with its neighboring ASes and the route quickly spread across the Internet’s BGP network. This route sent users trying to access YouTube to a dead end, which resulted in YouTube’s being inaccessible for several hours.

These are examples of a practice called **BGP hijacking**, which does not always happen accidentally. In April 2018, attackers deliberately created bad BGP routes to redirect traffic that was meant for Amazon’s DNS service. The attackers were able to steal over $100,000 worth of cryptocurrency by redirecting the traffic to themselves.

BGP hijacking can be used for several kinds of attacks:

- Phishing and social engineering through re-routing users to fake websites
- DoS through traffic blackholing or redirection
- On-path attacks to modify exchanged data, and subvert reputation-based filtering systems
- Impersonation attacks to eavesdrop on communications

Incidents like these can happen because the **route-sharing function of BGP relies on trust**, and autonomous systems **implicitly trust** the routes that are shared with them. When peers announce incorrect route information (intentionally or not), traffic goes where it is not supposed to, potentially with malicious results.
