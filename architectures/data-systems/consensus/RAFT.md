## RAFT

RAFT is a consensus algorithm used to manage a replicated log in distributed systems. It is designed to be easy to understand and implement while providing a strong guarantee of consistency.

### Logs and consensus

Each server maintains a **log of operations**, some of which have already been executed, as well as pending operations. Consensus is expressed in terms of these logs: committed operations have the same position in each of the respective server’s logs.

Raft achieves consensus by electing a leader among the nodes (servers). This leader is responsible for managing the log and ensuring that all nodes (followers) are kept up to date. The algorithm handles leader election, log replication, and safety guarantees. The system continues to function correctly even if some nodes fail, as long as a majority (quorum) of nodes remain operational.

Raft guarantees that operations that have been registered as committed, have been performed by a majority of the servers, and that the result has been returned to the original client.

### Re-election

When a leader crashes, a new one is elected, and its log is the collective state of the server group. However, if that log misses committed operations, then it is not representative for what the majority of servers has decided on.

For this reason, during an election, a server S will not vote for a candidate if it turns out that its log is more up to date than the candidate's.

### Clusters

Manager nodes implement this algorithm to manage global cluster state to ensure all Managers are storing the same consistent state. Having the same consistent state across cluster means in failure, any Manager node can pick up tasks and restore services to stable state.
