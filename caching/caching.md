## Challenges with low latency database reads

- Data retrieval speed from a disk has a threshold; beyond that, you cannot squeeze out more performance regardless of optimization on data model or queries
- Vertical scaling can take you far but assigning more resources by upgrading to better hosts has limitations
- Horizontal scaling by splitting your database into multiple partitions is a promising approach; however, it gets more operationally complex and doesn't eliminate issues such as **hot partitions**
- Both horizontal and vertical scaling are costly in the long term

## Caching

Caching is a technique used to improve the performance and efficiency of a system. It involves storing a copy of certain data in a temporary storage area (the cache) so that future requests for that data can be served faster.

Caches can exist at all levels in architecture, but are often found at the level nearest to the front end, where they are implemented to return data quickly without taxing downstream levels.

Scope of caching typically applies to local storage or a specific system.

<img src="./assets/caching.png">

## Cache use cases

### Caching for storage

Using cache to facilitate reading from storage is the most common use case i.e. read-heavy workloads. Backend storage such as databases usually has a longer latency and a lower bandwidth than in-memory cache. Therefore, caching these objects reduce access latency, increases throughput, and shelters the backend from excessive read traffic.

Object popularity is an important characteristic of a caching workload. Popularity distribution is often used to describe the cachebility of a workload. Popularity distributions for read-heavy in-memory caching workloads typically follow **Power-law (Zipfian) distribution** with a large skew i.e. a small subset of objects account for a large proportion of requests.

### Caching for computation

As real-time stream processing and machine learning (ML) become increasingly popular, an increasing number of cache clusters are devoted to caching computation related data such as features, intermediate and final results of ML prediction, and hydration.

Caches under this category serve both read-heavy and write-heavy traffic depending on the workloads.

### Transient data with no backing store

Another typical usage evolves around objects that only live in the cache, often for short periods of time. Examples include rate limiters, deduplication caches, and negative result caches.

## Caching methods

### Client caching

Client-side caching stores data on the client’s device e.g. browser, mobile app. When a user revisits a site, the browser can load the site from the local cache rather than fetching everything from the server again.

The cache-control header directive tells the browser the duration to cache the file e.g. 1h.

### Server caching

Server caching involves storing frequently accessed data on the server, reducing the need for expensive operations like database queries.

Server-side caches are stored on the server itself or a separate cache server, either in memory (like Redis) or on disk. Typically, the server checks the cache for data before querying the database. If the data is in the cache, it is returned directly.

### Database caching

Database caching stands as a cornerstone in the realm of caching strategies, playing a pivotal role in enhancing the performance of applications that heavily rely on database interactions.

Database caching can be implemented in two primary ways:

- Internal Caching: This is where the database system itself maintains a cache. It’s akin to having a quick reference guide built right into the database
- External Caching: In this approach, an external cache (like Redis or Memcached) works in tandem with the database

### Content Delivery Networks (CDNs)

CDNs are a network of servers distributed geographically, generally used to serve static content such as JavaScript, HTML, CSS, images, and video assets. They cache the content from the original server and deliver it to users from the nearest CDN server.
