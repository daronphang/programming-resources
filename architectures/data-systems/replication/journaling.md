## Durability and journaling with append-only system

The durability contract for a data system is that when data is acknowledged as written by a primary, there must be at least three durable copies of data stored. This contract allows the system to maintain data durability even in the face of a cluster-wide power failure.

As part of maintaining the durability contract while still achieving good performance, an important optimization is that on each node, we reserve a whole disk drive or SSD as a **journal drive** for all writes into the node.

The journal drive is dedicated solely for writing a single sequential journal of data, which allows us to reach the **full write throughput potential** of a device. When each node performs an append (replica or primary):

1. It writes all of the data for the append to the journal drive
2. Queues up the append in memory to go to the data disk
3. When either append succeeds, success can be returned back to the client
4. Reads can be served from in-memory until the data is written to the data disk
5. Once data is saved to the disk, all reads will be served from the data disk

### Benefits

- Enables the contiguous writes into larger writes to the data disk
- Better scheduling of concurrent writes and reads to get the best throughput i.e. writes do not need to contend with reads on the same disk drive
- Better latency

### Drawbacks

- Extra write off the critical path
