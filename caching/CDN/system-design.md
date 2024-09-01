## System design

## Functional requirements

- Content distribution: Define how the system will correctly distribute different web content material globally (static, dynamic) by implementing techniques for replication, material synchronization, etc.
- Caching: Specify the caching approach for each static and dynamic content material
- Load balancing: Define the load balancing algorithm to evenly distribute incoming requests across CDN nodes
- Content purge mechanism: Describe the mechanism to invalidate or update cached content material

## Non-functional requirements

- Scalability: Specify how the system will scale to deal with increased visitors i.e. horizontal scaling based on demand
- Reliability: Define the redundancy mechanisms at diverse levels to ensure high availability i.e. data replication, failover strategies, backup structures
- Performance: Achieving minimal latency for a superior user experience; over-provision memory to accommodate for increased usage and prevent performance issues
- Security: Providing robust protection against failures and securing hosted content

## Microservices

### Edge service

- Creating caching
- Retrieval of content
- Delivery of content

### Load balancing service

- Load balancing

### Security service

- DDoS safety
- Validating requests
- Authorizing requests

### Analytics service

- Real-time tracking of CDN performance
- Upgrade in content material delivery
