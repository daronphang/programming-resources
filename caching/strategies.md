## Hierarchical caching

Hierarchical caching is a strategy used in computer systems to improve performance by organizing cache memory in a multi-layered structure. Instead of relying on a single cache, hierarchical caching employs multiple levels of caches, each with varying sizes and speeds.

## Cooperative caching (distributed caching)

An alternative to building hierarchical caches is using cooperative caching, where **multiple nodes work together to share cached data**. Whenever a cache miss occurs at a web proxy, the proxy first checks a number of neighboring proxies to see if one of them contains the requested document. If such a check fails, the proxy forwards the request to the Web server responsible for the document. In a highly decentralized system, cooperative caching is highly effective.

<img src="./assets/cooperative-caching.png">

### Benefits

- **Reduced latency**: By allowing nodes to cooperate, cooperative caching can reduce the time it takes to retrieve data, especially when the requested data is already cached elsewhere
- **Load balancing**: Distributing cache hits across multiple nodes can help balance the load, preventing any single node from becoming a bottleneck while also alleviating pressure on the main data source
- **Dynamic adaptation**: Systems using cooperative caching can adapt to changing access patterns and node availability, dynamically adjusting which data to cache and how to share it among nodes
