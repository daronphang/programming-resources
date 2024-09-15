## RAFT

RAFT is a consensus algorithm used to manage a replicated log in distributed systems. It is designed to be easy to understand and implement while providing a strong guarantee of consistency.

Raft achieves consensus by electing a leader among the nodes (servers). This leader is responsible for managing the log and ensuring that all nodes (followers) are kept up to date. The algorithm handles leader election, log replication, and safety guarantees. The system continues to function correctly even if some nodes fail, as long as a majority (quorum) of nodes remain operational.

Manager nodes implement this algorithm to manage global cluster state to ensure all Managers are storing the same consistent state. Having the same consistent state across cluster means in failure, any Manager node can pick up tasks and restore services to stable state.
