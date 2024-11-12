## Transport layer load balancing (layer 4)

Operate at the transport layer (OSI Layer 4) and make forwarding decisions based on IP address and TCP/UDP ports. L4 LB is stream-based i.e. can distribute packets stream by stream.

One key characteristic of Layer 4 load balancers is that they **do not inspect the content of the data packets**. They focus on the network-level information and do not have visibility into the actual message or payload carried by the packets.

### Implementation

- **NAT**: Performs virtual IP (public) and destination IP (private/public) address translation. LB rewrites the target address of the request message to destination IP, and source address of the response message to the virtual IP
- **DR (Direct Routing)**: Only the request packets sent by client go through the LB, while the response packets are sent directly to the client to reduce load pressure. Replaces the MAC address of the packet object with the MAC address of the server, instead of changing the IP address of the request object

The principles of DR are as follows:

- Virtual IP addresses for both load balancers and servers are configured, but requires that the **virtual IP addresses of servers to not respond to ARP requests**
- An actual IP address needs to be configured for the server in order to communicate with the load balancer
- Clients send requests to the virtual IP addresses of servers; as they cannot respond to ARP requests, the LB will receive the packets and distribute them to the corresponding server by rewriting the MAC addresses
- The load balancer and the servers need to be in the **same layer 2 network**, since MAC addresses are used to forward the requests directly instead of using the traditional forwarding method of looking up the routing table to distribute packets

### Advantages

- **Simplicity**: Simpler to run and maintain as compared to higher-layer LB, and require less configuration and management overhead
- **Better performance and higher throughput**: Do not need to perform data lookups or deep packet inspection, resulting in faster routing decisions and reduced latency
- **Enhanced security**: Do not need to decrypt TLS which enhances security by maintaining confidentiality of encrypted traffic
- **Efficient connection handling**: Typically establish only one TCP connection between client and selected server

### Disadvantages

- **Lack of smart/flexible load balancing**: Cannot make intelligent routing decisions based on the content of data packets
- **No caching**: Cannot perform caching as they cannot see the content of data packets

## Application layer load balancing (layer 7)

Operate at the application layer (OSI Layer 7). L7 LB controls application layer service distribution through content analysis, and brings many possibilities for more refined balancing. However, it also puts forward **very high requirements for system performance**. Usually, specialized chips are implemented in the form of hardware circuits.

### Advantages

- **Smarter load balancing**: Can make intelligent routing decisions based on the content of data packets by inspecting headers, URLs, cookies, etc.
- **Caching capabilities**: Can cache frequently requested content, reducing load and latency
- **Reverse proxy functionality**: Can act as reverse proxies, providing additional features including SSL termination, request/response modification, URL rewriting

### Disadvantages

-**Higher cost**: More complex and resource-intensive than layer 4 LB

- **Data decryption**: Additional processing of decrypting TLS content
- **Multiple TCP connections**: Typically maintain two TCP connections; one between the client and load balancer, and another between load balancer and backend server

## Layer 4-7 hybrid

In practical applications, L4 and L7 LBs are often used together. A L7 LB is typically used as the backend of a L4 LB to load balance requests sent by external clients i.e. client -> L4 LB -> L7 LB. Although L7 LBs offer more functionality than L4 LBs, they have a **lower throughput**, which makes L4 LBs better suited to protect against DDoS.

## Network Load Balancer (NLB)

An NLB operates at layer 4 for network-level traffic management based on ports and IP addresses. Network load balancers can handle both TCP and UDP, as well as TCP connections encrypted with TLS.

### Implementation

NLB is implemented through core routing and switching equipment using:

1. HSRP (Hot Standby Router Protocol) or VRRP (Virtual Router Redundancy Protocol)
2. MSTP (Multiple Spanning Tree Protocol)

Port Channels can increase network bandwidth and improve the high availability of network connections.

## Link Load Balancer (LLB)

LLB is used to load balance in multiple network links through dynamic algorithms. It refers to the management of traffic that is initiated within a LAN that is destined to go out over various WAN links i.e. **sits at LAN-WAN boundary**.

In order to avoid network usability risks caused by network outbound failures of operators and solve problems such as network access failure caused by insufficient network bandwidth, enterprise users usually rent networks from two or more operators at the same time.

To reasonably use the network outbound of multiple operators, traditional policy-based routing can be used. Although it solves the problem to some extent, but is inconvenient to configure and **difficult to dynamically adapt to network architecture changes**. Most importantly, it cannot adjust message distribution dynamically according to actual bandwidth usage, resulting in waste of idle link throughput capacity. Hence, LLB is proposed to solve this problem.

LLB can be divided into two cases according to business traffic: outbound and inbound.

### Outbound

Outbound LLB solves the problem of how to dynamically allocate and load balance among multiple different links when accessing external interconnection services (extranet) within the enterprise's internal business system. It can achieve the function of sharing the traffic of intranet users accessing the extranet server on multiple physical links.

### Inbound

Inbound LLB solves the problem of how users located outside the interconnection (external network users) can dynamically balance and allocate on multiple links when accessing internal enterprise websites and business systems, and intelligently switch to another available link when one link is interrupted.

The principle of inbound LLB is to use the LB device as an **authoritative DNS nameserver** to record the mapping relationship between domain name and IP addresses of internal network servers. When an external user accesses the internal server through the domain name method, the local DNS server will request a domain name resolution from the load balancing device according to the recursion principle.

### LLB vs server load balancing

In terms of load balancing equipment, their key technologies, deployment methods, and other contents are similar.

In terms of scheduling algorithms, LLB has unique algorithms such as **nearest link selection algorithm**. This algorithm can detect the status of the link in real time during the link load balancing process, and select the optimal link based on the detection results to ensure that traffic is forwarded through the optimal link. This is achieved through link health checks (DNS, ICMP packets), establishing TCP half-open connections, etc. The heuristics of choosing the nearest link include the link physical bandwidth, link cost, link relay, time, routing hop count, etc.
