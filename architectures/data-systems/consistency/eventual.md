## Eventual Consistency (Convergence)

In replicated database, nodes are likely to have different data if looked at the same time as write requests arrive on different nodes at different times. These inconsistencies occur no matter what replication method the database uses (single-leader, multi-leader, or leaderless).

Most replicated databases provide at least **eventual consistency** i.e. if writes are stopped, all read requests will eventually return the same value after some time. This means that **the inconsistency is temporary and eventually resolves itself**.

However, this is a very weak guarantee as it does not say anything about when the replicas will converge. Nonetheless, stronger consistency models may have worse performance or be less fault-tolerant than systems with weaker guarantees.
