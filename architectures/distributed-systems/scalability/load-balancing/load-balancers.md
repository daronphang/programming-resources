## Load balancers

Load balancers helps to spread the traffic across a cluster of servers to improve responsiveness and availability of applications, websites or databases. Load balancers also keeps track of the status of all the resources while distributing requests; if a server is not available, it will redirect to another healthy server.

### Benefits

- **Performance**: Users experience faster, uninterrupted service
- **Scalability**: Service providers experience less downtime and higher throughput
- **Workload distribution**: Workload is distributed/balanced across nodes, instead of a single node performing a lot of work
- **Redundancy**: A failure in one node will route the request to another healthy node

## Scaling

While load balancers help scale the application, it’s important to ensure that they don’t become bottlenecks to the scalability.

- DNS round robin: Multiple load balancers are configured with different IP addresses but share the same domain name
- Clustered LB configuration
- GSLB
- Active-passive load balancing
- Anycast load balancing
- Elastic load balancing: Auto-scaling of load balancers based on incoming traffic

## Redundancy

The load balancer can be a single point of failure; to overcome this, a second load balancer can be connected to the first to form a cluster i.e. HA Proxy with keep-alived.
