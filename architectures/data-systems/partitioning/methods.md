## Vertical partitioning

One easy way to segment your application’s database is to move tables related to specific features to their own servers. For instance, you could place user profile information on one server, friend lists on another, and a third for user-generated content like photos.

This approach is relatively simple to implement and has minimal impact on the overall application. However, if the site continues to grow, further sharding of the feature-specific databases across multiple servers may be necessary.

## Partitioning of key-value data (primary)

Goal is to spread the data and query load evenly across nodes. If it is skewed, partitioning will be less effective and may result in hotspots (a partition having a disproportionately high load).

Simplest approach is to assign records to nodes randomly. However, as you do not know which node the data is stored on, need to query all nodes.

### By key range (range-based partitioning)

Range-based sharding is a technique that involves dividing data based on ranges of a specific value i.e. boundaries between ranges. This approach allows for a more organized and efficient data distribution, making it easier to manage and query the database.

However, a key challenge with this approach is that if the value used for partitioning is not chosen carefully, it can result in uneven distribution of data across the servers.

### By hash key (key-based partitioning)

A good hash function takes skewed data and makes it uniformly distributed. Once you have a suitable hash function, you can assign each partition a range of hashes, and every key whose hash falls within a partition's range will be stored in that position.

However, we lose the ability to do efficient range queries, as adjacent keys are scattered across all the partitions. Another challenge is that it limits the flexibility to add more servers to the system, as it would require changing the hash function and this can be difficult to perform without causing downtime.

## Partitioning secondary indexes

A secondary index doesn't identify a record uniquely but rather is a way of searching for occurrences of a particular value i.e. all cars whose color is read.

Secondary indexes are teh bread and butter of relational databases, and common in document databases. However, they don't map neatly to partitions.

### By document

In this approach, each partition maintains its own secondary indexes, converting only the documents in that partition.

However, querying from a document-partitioned index requires scatter/gather, and makes it expensive. Nonetheless, it is widely used in MongoDB, Riak, Cassandra, ElasticSearch, and VoltDB.

```
Partition 0

Primary Index
191 (color: red, make: Honda)
214 (color: black, make: Dodge)
306 (color: red, make: Ford)

Secondary Index
color: red [191,306]
color: black [214]
```

### By term

Instead of each partition having its own secondary index, we can construct a global index that covers data in all partitions. The term is used to determine the partition of the index. This is useful for range scans i.e. asking price of a car.

```
Partition 0
Secondary Index (colors starting with letter a to r)

Partition 1
Secondary Index (colors starting with letter s to z)
```

## Hybrid

Examples include using a compound key, where one part of the key is used to identify the partition, and another for sort order.

## Directory-based partitioning

Directory-based partitioning involves having a lookup table that uses a shard key to keep track of which shard holds which data. This shard key is typically a unique identifier for each piece of data e.g. user ID. The lookup table is used to determine which shard a specific piece of data belongs to, allowing the system to efficiently retrieve and update the data as needed.

This approach allows for more flexibility in terms of adding or removing servers, or changing the partitioning scheme, without affecting the rest of the application.
