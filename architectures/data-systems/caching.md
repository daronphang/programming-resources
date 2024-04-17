## Challenges with low latency database reads

- Data retrieval speed from a disk has a threshold; beyond that, you cannot squeeze out more performance regardless of optimization on data model or queries
- Vertical scaling can take you far but assigning more resources by upgrading to better hosts has limitations
- Horizontal scaling by splitting your database into multiple partitions is a promising approach; however, it gets more operationally complex and doesn't eliminate issues such as **hot partitions**
- Both horizontal and vertical scaling are costly in the long term

## Cache invalidation

Cache invalidation is one of the two hard things in Computer Science.

### Time-to-Live (TTL)

One of the simplest cache invalidation strategies is configuring a TTL and letting the cache entries expire once they cross the TTL.

While this can work for many cases, most users expect changes to be reflected faster than the TTL. However, lowering the default TTL to a very small value can sink the cache hit rate and reduce its effectiveness.

### Data capture and streaming

You can tail the database's binlog events and publish the events to a list of consumers.

For cache invalidation, a new consumer was created that subscribes to the data events and invalidates/upserts the new rows in Redis.

Key advantages of this approach include:

- They could make the cache consistent with the database within seconds of the database change as opposed to minutes (depending on TTL)
- Using binlogs made sure that uncommitted transactions couldn’t pollute the cache
