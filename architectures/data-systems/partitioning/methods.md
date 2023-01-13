## Partitioning of Key-Value Data (Primary)

Goal is to spread the data and query load evenly across nodes. If it is skewed, partitioning will be less effective and may result on hotspots (a partition having a disproportionately high load).

Simplest approach is to assign records to nodes randomly. However, as you do not know where node the data is stored on, need to query all nodes.

### By Key Range

One way of partitioning is to assign a continuous range of keys (minimum to maximum) to each partition i.e. boundaries between ranges. However, data may not be evenly distributed. 

### By Hash Key

A good hash function takes skewed data and makes it uniformly distributed. Once you have a suitable hash function, you can assign each partition a range of hashes, and every key whose hash falls within a partition's range will be stored in that position.

However, we lose the ability to do efficient range queries, as adjacent keys are scattered across all the partitions.

### Hybrid

Examples include using a compound key, where one part of the key is used to identify the partition, and another for sort order.

## Partitioning Secondary Indexes

A secondary index doesnt identify a record uniquely but rather is a way of searching for occurrences of a particular value i.e. all cars whose color is read. 

Secondary indexes are teh bread and butter of relational databases, and common in document databases. However, they don't map neatly to partitions.

### By Document

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

### By Term

Instead of each partition having its own secondary index, we can construct a global index that covers data in all partitions. The term is used to determine the partition of the index. This is useful for range scans i.e. asking price of a car. 

```
Partition 0
Secondary Index (colors starting with letter a to r)

Partition 1
Secondary Index (colors starting with letter s to z)
```


```