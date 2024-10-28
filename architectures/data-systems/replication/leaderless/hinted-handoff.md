## Handling failures with hinted handoff

If a traditional strict quorum membership approach is used, it would be unavailable during server failures and network partitions, and would have reduced durability even under the simplest of failure conditions. Instead, a "sloppy quorum" can be employed using hinted handoff.

Hinted handoff is a distributed system pattern to perform repairs in the write path. It ensures that the read and write operations are not failed due to temporary node or network failures i.e. offers **eventual consistency and improved availability**. Hinted Handoff serves two purposes:

- It allows the database to offer full write availability when consistency is not required
- It improves response consistency after temporary outages

Hinted handoff works best if the system membership churn is low and node failures are transient.

Applications that need the highest level of availability can set W (write quorum) to 1, which ensures that a write is accepted as long as a single node hs durably written the key in its local store.

### How it works

In Hinted Handoff, when a write is performed and a replica node for the row is either known to be down ahead of time, or does not respond to the write request, the coordinator (backup node) will store a hint locally.

A hint indicates that a write needs to be replayed to one or more unavailable nodes. The hint consists of:

- The location of the replica that is down
- Version metadata
- The actual data being written

Nodes that receive hinted replicas will keep them in a separate local database that is scanned periodically. **Eventual consistency** is attained through the relay of the hints by the backup node when the target node is healthy again. The backup node may delete the object from its local store once the transfer succeeds.

Upon detecting node A has recovered, node B will attempt to deliver the replica to A. Once the transfer succeeds, node B may delete the object from its local store without decreasing the total number of replicas in the system.

## Strict vs sloppy quorum

Quorum is the number of replicas which should acknowledge a particular read or write operation; it is closely associated with the replication factor. The use of hinted writes to meet consistency requirements in read paths decides whether a quorum is strict or sloppy.

The sloppy quorum is a variant of the quorum-based approach that leverages hinted handoff pattern to reach quorum when multiple target nodes become unavailable.

For strict quorum, hinted writes do not count towards read or write consistency requirements.
