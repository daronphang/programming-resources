## High availability for writes

High-availability writes in a distributed database with leaderless replication requires a **heuristic for conflict resolution** between concurrent writes. This is essential because every replica of data is considered equal and concurrent writes on the same record at two different replicas are considered perfectly valid.

### Last write wins

In last-write-wins, the latest change to a data-point alone is retained. However, it could lead to potential data loss for concurrent writes.

## Temporary failures

Temporary failures occur when a replica is unavailable for read and/or write operations for a small duration of time. This could arise because of GC stalls, network and hardware outages, memory exhaustion, or maintenance shutdowns.

### Hinted handoff

Hinted handoff can be employed to ensure that read and write operations are not failed due to temporary node or network failures.

## Partitioning and replication with consistent hashing

In consistent hashing, the output range of a hash function is treated as a fixed circular space or “ring”. Each data item identified by a key is assigned to a node hashing the data item’s key to yield its position on the ring, and then walking the ring clockwise to find the first vnode with a position larger than the item’s position.

Consistent hashing is also a part of the **replication strategy** in Dynamo-family databases. In Cassandra, two strategies exist.

In SimpleStrategy, a node is anointed as the location of the first replica by using the ring hashing partitioner. Subsequent replicas are placed on the next nodes clockwise on the ring.

In NetworkTopologyStrategy, for each datacenter, the same steps are performed with a difference when choosing subsequent replicas: subsequent replicas are placed on the next node clockwise on the ring which belongs to a different rack than the location of the previous replica.

## Handling permanent failures with anti-entropy using Merkle trees

The distributed nature of data means data in a replica can become inconsistent with other replicas over time.

Anti-entropy is a process of comparing the data of all replicas and updating each replica to the newest version. It relies on Merkle tree hash exchanges between nodes.

Merkle trees are binary hash trees whose leaves are hashes of the individual key values. The leaf of a Cassandra Merkle tree is the hash of a row value. Each Parent node higher in the tree is a hash of its respective children. Because higher nodes in the Merkle tree represent data further down the tree, Casandra can check each branch independently without requiring the coordinator node to download the entire data set.

## Failure detection with gossip protocols

Gossip protocols are a class of peer-to-peer communication protocols inspired by information dissemination in real-life social networks. In Dynamo, decentralized failure detection protocols use a simple gossip-style protocol that enable each node in the system to learn about the arrival (or departure) of other nodes. Failure detection helps nodes in avoiding communication with unresponsive peers during read and write operations.
