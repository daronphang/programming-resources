## Upstream resiliency

We explore patterns that can protect against upstream pressure.

### Load shedding

A server has very little control over how many requests it receives at any given time, which can deeply impact its performance.

The operating system has a connection queue per port with a limited capacity that, when reached, causes new connection attempts to be rejected immediately. But typically, under extreme load, the server crawls to a halt before that limit is reached as it **starves out of resources** like memory, threads, sockets, or files. This causes the response time to increase to the point the server becomes unavailable to the outside world.

When a server operates at capacity, it should start **rejecting excess requests** so that it can focus on the ones it is already processing, and preventing from degrading further. This can be done by failing fast and returning 503, and this technique is known as load shedding. In addition, the server can implement priorities, and reject only the lower-priority ones.

Unfortunately, rejecting a request doesn’t completely offload from the server the cost of handling it. Depending on how the rejection is implemented, the server might still have to **pay the price of opening a TLS connection** and read the request just to finally reject it. Hence, load shedding can only help so much, and if the load keeps increasing, eventually, the cost of rejecting requests takes over, and the service starts to degrade.

### Load leveling

Load leveling is an alternative to load shedding, which can be used when clients don’t expect a response within a short time frame.

The idea is to introduce a **messaging channel** between the clients and the service. The channel decouples the load directed to the service from its capacity, allowing the service to process requests at its own pace. Rather than requests being pushed to the service by the clients, they are pulled by the service from the channel.

### Rate limiting

Rate-limiting, or throttling, is a mechanism that rejects a request when a specific quota is exceeded. A service can have multiple quotas, like for the number of requests seen, or the number of bytes received within a time interval. Quotas are typically applied to specific users, API keys, or IP addresses.

When a service rate-limits a request, it needs to return a response with a particular error code so that the sender knows that it failed because a quota has been breached. For HTTP APIs, the most common way is to return 429. The response should also include Retry-After header indicating how long to wait before making a new request.

Rate-limiting is also used to enforce pricing tiers; if a user wants to use more resources, they also need to be prepared to pay more.

Rate-limiting only partially protects a service against DDoS. This is because the service still has to pay the price of opening a TLS connection, and downloading the request to read the API key. **Economies of scale** are the only true protection against DDoS attacks.

### Bulkhead

The goal of the bulkhead pattern is to isolate a fault in one part of a service from taking the entire service down with it. The pattern is named after the partitions of a ship’s hull. If one partition is damaged and fills up with water, the leak is isolated to that partition and doesn’t spread to the rest of the ship.

Some clients can create much more load on a service than others. Without any protections, a single greedy client can hammer the system and degrade every other client. Though rate-limiting can help to prevent a single client from using more resources than it should, it is **not bulletproof**. For example, a client may send very heavy or poisonous requests that causes the servers to degrade i.e. issue is intrinsic with the requests.

When everything else fails, the bulkhead pattern provides guaranteed fault isolation by design. The idea is to **partition a shared resource**, like a pool of service instances behind a load balancer, and assign each user of the service to a specific partition so that its requests can only utilize resources belonging to the partition it’s assigned to.

We can also introduce **virtual partitions** that are composed of a random subset of instances. This can make it much more unlikely for another user to be allocated to the exact same virtual partition.

However, you need to be careful when applying the bulkhead pattern; if you create too many partitions, you lose all the economy-of-scale benefits of sharing costly resources across a set of users.

### Health checks

Health checks can be used as a way to control the incoming traffic so that it doesn't reach a degraded server in the first place. Health checks are critical to achieving high availability.

If the server is behind a load balancer and can communicate that it’s overloaded, the balancer can stop sending requests to it. The health endpoint is periodically queried by the load balancer. If the endpoint returns an error, the load balancer considers the process unhealthy and takes it out of the pool.

Different types of health checks include:

- **Liveness health test**: Performs a HTTP heartbeat request
- **Local health test**: Checks whether the process is degraded or in some faulty state by comparing local metrics e.g. memory, disk space, CPU
- **Dependency health check**: Detects a degradation caused by a remote dependency e.g. database

For dependency health checks, if the health-check has a bug or the dependency is temporarily unreachable, it can cause all the processes behind a load balancer to fail the health check, and may bring the entire service down.

Instead, a smart load balancer first detects that a **large fraction** of the service instances is being reported as unhealthy, then considers the health-check to no longer be reliable. Rather than continuing to remove processes from the pool, it starts to **ignore the health-checks** altogether so that new requests can be sent to any process in the pool.

### Watchdog

Watchdog is a separate process that wakes up periodically and monitors the health of processes through metrics. When any monitored metric breaches a configured threshold, the watchdog considers the process degraded and deliberately restarts it.
