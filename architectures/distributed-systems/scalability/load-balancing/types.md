## Transport layer load balancing (layer 4)

Operate at the transport layer (OSI Layer 4) and make forwarding decisions based on IP address and TCP/UDP ports.

One key characteristic of Layer 4 load balancers is that they **do not inspect the content of the data packets**. They focus on the network-level information and do not have visibility into the actual message or payload carried by the packets.

### Advantages

- Simplicity: Simpler to run and maintain as compared to higher-layer LB, and require less configuration and management overhead
- Better performance and higher throughput: Do not need to perform data lookups or deep packet inspection, resulting in faster routing decisions and reduced latency
- Enhanced security: Do not need to decrypt TLS which enhances security by maintaining confidentiality of encrypted traffic
- Efficient connection handling: Typically establish only one TCP connection between client and selected server

### Disadvantages

- Lack of smart/flexible load balancing: Cannot make intelligent routing decisions based on the content of data packets
- No caching: Cannot perform caching as they cannot see the content of data packets

## Application layer load balancing (layer 7)

Operate at the application layer (OSI Layer 7).

### Advantages

- Smarter load balancing: Can make intelligent routing decisions based on the content of data packets by inspecting headers, URLs, cookies, etc.
- Caching capabilities: Can cache frequently requested content, reducing load and latency
- Reverse proxy functionality: Can act as reverse proxies, providing additional features including SSL termination, request/response modification, URL rewriting

### Disadvantages

- Higher cost: More complex and resource-intensive than layer 4 LB
- Data decryption: Additional processing of decrypting TLS content
- Multiple TCP connections: Typically maintain two TCP connections; one between the client and load balancer, and another between load balancer and backend server

### Hybrid

A L7 LB is typically used as the backend of a L4 LB to load balance requests sent by external clients i.e. client -> L4 LB -> L7 LB. Although L7 LBs offer more functionality than L4 LBs, they have a **lower throughput**, which makes L4 LBs better suited to protect against DDoS.

## Global Server Load Balancing (GSLB)

Distributes traffic across multiple geographical locations to improve redundancy and performance on a global scale.
