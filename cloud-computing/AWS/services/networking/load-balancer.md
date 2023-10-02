## Elastic Load Balancing

Distributes network traffic across its components including EC2, Lambda and containers.

### Benefits

- Highly available and distributes website traffic across multiple targets
- Provides high security through user authentication and TLS
- Handles drastic changes in website traffic without human intervention
- Helps improve the visibility of your applications through continuous monitoring and auditing
- Supports hybrid load balancing

## Algorithms

### Round Robin Method

Simple algorithm that is used to distribute client's request across a group of servers. Once a server has received a request, it will be moved to the bottom of the queue. Client request is sent to each server one by one, based on availability.

### Least Connection Method

Directs network traffic to the server, and is specifically used when there is a large number of client requests unevenly distributed between the servers.

### Least Response Time Method

Directs client requests to the server with the lowest average response time, and ensures that the load is balanced adequately among servers.

### IP Hash

Uses client's IP address to route network traffic to the available backend server.
