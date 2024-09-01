## Caching storage

Data on CDN edge servers is typically stored using a combination of filesystems (disk I/O) and in-memory storage (RAM), depending on the specific implementation and the type of content being cached.

### Distributed storage

In larger CDN architectures, there might be distributed filesystems or object storage solutions to manage and replicate cached content across multiple edge servers. This helps ensure reliability and availability.

The CDN might use techniques such as **sharding and replication** to improve performance and fault tolerance.

## Caching strategies

### Push caching

Origin servers proactively push content to edge servers before it is requested, ensuring faster delivery to users. This is suitable for static content.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

### Pull caching

Edge servers fetch content from origin servers in real-time when requested by users, reducing storage requirements and ensuring freshness of content. Suitable for dynamic content.

Contrary to the Push CDN, this requires less maintenance because cache updates on CDN nodes are performed based on requests from the client to the origin server. Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

## Cache management

### Indexes

To efficiently manage cached content, edge servers maintain indexes or metadata about the cached items. This information helps quickly locate and serve requested files.

### Eviction policies

CDNs employ eviction policies (like LRU—Least Recently Used) to decide which content to remove when cache space is needed. This helps manage storage and ensures that the most relevant content is kept readily accessible.
