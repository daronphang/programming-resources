## Load balancers

Load balancers helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. Load balancers also keeps track of the status of all the resources while distributing requests; if a server is not available, it will redirect to another healthy server.

### Benefits

- Performance: Users experience faster, uninterrupted service
- Scalability: Service providers experience less downtime and higher throughput
- Workload distribution: Workload is distributed/balanced across nodes, instead of a single node performing a lot of work
- Redundancy: A failure in one node will route the request to another healthy node

## Types

### Layer 4

Operate at the transport layer (OSI Layer 4) and make forwarding decisions based on IP address and TCP/UDP ports.

One key characteristic of Layer 4 load balancers is that they **do not inspect the content of the data packets**. They focus on the network-level information and do not have visibility into the actual message or payload carried by the packets.

#### Advantages

- Simplicity: Simpler to run and maintain as compared to higher-layer LB, and require less configuration and management overhead
- Better performance: Do not need to perform data lookups or deep packet inspection, resulting in faster routing decisions and reduced latency
- Enhanced security: Do not need to decrypt TLS which enhances security by maintaining confidentiality of encrypted traffic
- Efficient connection handling: Typically establish only one TCP connection between client and selected server

#### Disadvantages

- Lack of smart/flexible load balancing: Cannot make intelligent routing decisions based on the content of data packets
- No caching: Cannot perform caching as they cannot see the content of data packets

### Layer 7

Operate at the application layer (OSI Layer 7).

#### Advantages

- Smarter load balancing: Can make intelligent routing decisions based on the content of data packets by inspecting headers, URLs, cookies, etc.
- Caching capabilities: Can cache frequently requested content, reducing load and latency
- Reverse proxy functionality: Can act as reverse proxies, providing additional features including SSL termination, request/response modification, URL rewriting

#### Disadvantages

- Higher cost: More complex and resource-intensive than layer 4 LB
- Data decryption: Additional processing of decrypting TLS content
- Multiple TCP connections: Typically maintain two TCP connections; one between the client and load balancer, and another between load balancer and backend server

### Global Server Load Balancing (GSLB)

Distributes traffic across multiple geographical locations to improve redundancy and performance on a global scale.

## Scaling

While load balancers help scale the application, it’s important to ensure that they don’t become bottlenecks to the scalability.

- DNS round robin: Multiple load balancers are configured with different IP addresses but share the same domain name
- Clustered LB configuration
- GSLB
- Active-passive load balancing
- Anycast load balancing
- Elastic load balancing: Auto-scaling of load balancers based on incoming traffic

## Algorithms

Load balancers consider two factors before forwarding a request to a backend server:

1. Ensure that the server they choose is actually responding appropriately to requests (health checks)
2. Use a pre-configured algorithm to select one from the set of healthy servers

### Least Connection Method

Directs traffic to the server with the fewest active connections. This approach is quite useful when there are a large number of persistent client connections which are unevenly distributed between the servers.

### Least Response Time Method

This algorithm directs traffic to the server with the fewest active connections and the lowest average response time.

### Least Bandwidth Method

This method selects the server that is currently serving the least amount of traffic measured in megabits per second (Mbps).

### Round Robin Method

This method cycles through a list of servers and sends each new request to the next server. When it reaches the end of the list, it starts over at the beginning. It is most useful when the servers are of equal specification and there are not many persistent connections.

### Weighted Round Robin Method

The weighted round-robin scheduling is designed to better handle servers with different processing capacities. Each server is assigned a weight (an integer value that indicates the processing capacity). Servers with higher weights receive new connections before those with less weights and servers with higher weights get more connections than those with less weights.

### IP Hash

Under this method, a hash of the IP address of the client is calculated to redirect the request to a server.

## Redundant load balancers

The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster i.e. HA Proxy with keep-alived.
