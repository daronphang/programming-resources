## RAFT Consensus Algorithm

Consensus is a fundamental problem in fault-tolerant distributed systems involving multiple servers agreeing on values. Consensus algorithms make progress when any majority of servers is available i.e. cluster of 5 servers can operate with 2 failures. Tolerates up to (n-1)/2 failures.

Manager nodes implement this algorithm to manage global cluster state to ensure all Managers are storing the same consistent state. Having the same consistent state across cluster means in failure, any Manager node can pick up tasks and restore services to stable state.
