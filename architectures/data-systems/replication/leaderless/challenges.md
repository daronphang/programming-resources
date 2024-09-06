## High availability for writes

High-availability writes in a distributed database with leaderless replication requires a **heuristic for conflict resolution** between concurrent writes. This is essential because every replica of data is considered equal and concurrent writes on the same record at two different replicas are considered perfectly valid.

### Last write wins

In last-write-wins, the latest change to a data-point alone is retained. However, it could lead to potential data loss for concurrent writes.

## Temporary failures

Temporary failures occur when a replica is unavailable for read and/or write operations for a small duration of time. This could arise because of GC stalls, network and hardware outages, memory exhaustion, or maintenance shutdowns.

### Hinted handoff

In Hinted Handoff, when a write is performed and a replica node for the row is either known to be down ahead of time, or does not respond to the write request, the coordinator (backup node) will store a hint locally. This hint is basically a wrapper around the mutation indicating that it needs to be replayed to the unavailable node(s).

Eventual consistency is attained through the relay of the hints by the backup node when the target node is healthy again. The technique of transmitting the data mutation post-failure resolution is known as hinted handoff In other words, hinted handoff is a distributed system pattern to perform repairs in the write path.

The hinted handoff pattern offers **eventual consistency and improved availability** on temporary node failures. The high availability of nodes is also a requirement to maintain the replication factor (RF) across the system. The hinted handoff pattern allows the system to manage the same amount of write operations despite operating at a reduced capacity.

Once a node discovers via gossip that a node for which it holds hints has recovered, it will send the data row corresponding to each hint to the target.

Hinted Handoff serves two purposes:

- It allows the database to offer full write availability when consistency is not required
- It improves response consistency after temporary outages

### Strict vs sloppy quorum

Quorum is the number of replicas which should acknowledge a particular read or write operation; it is closely associated with the replication factor. The use of hinted writes to meet consistency requirements in read paths decides whether a quorum is strict or sloppy.

The sloppy quorum is a variant of the quorum-based approach that leverages hinted handoff pattern to reach quorum when multiple target nodes become unavailable.

For strict quorum, hinted writes do not count towards read or write consistency requirements.

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
