## Duplication

### Load balancing

The easiest way to add more capacity to a service is to create more instances of it and have some way of routing or load-balancing requests to them. This can be a fast and cheap way to scale out a stateless service.

### Replication

If the servers behind a load balancer are stateless, scaling out is as simple as adding more servers. But when there is state involved, some form of coordination is required.

Replication is the process of storing a copy of the same data in multiple nodes. Replication and sharding are techniques that are often combined, but are orthogonal to each other.

### Caching

Caching is a specific type of replication that only offers best-effort guarantees. A cache is a high-speed storage layer that temporarily buffers responses from downstream dependencies so that future requests can be served directly from it.
