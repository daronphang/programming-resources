## Distributed transactions and consensus

Consensus is one of the most fundamental problems in distributed computing. The goal is to get several nodes to agree on something.

## Example situations

### Leader election

In a database with single-leader replication, all nodes need to agree on which node is the leader. The position might become contested if some nodes can't communicate with others due to a network fault, and may result in a **split brain situation** in which two nodes both believe themselves to be the leader. **This would cause data to diverge, leading to inconsistency and data loss.**

### Atomic commit

In a database that supports transactions spanning several nodes/partitions, we have the problem that a transaction may fail but succeed on others. To maintain atomicity, need to get all nodes to agree on the outcome of the transaction: either all abort or commit (if succeeds).
