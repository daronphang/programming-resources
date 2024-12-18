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
