## Quorum

Quorum is a consensus algorithm commonly used in distributed systems to ensure that the nodes can agree on a value or decision. The reason why Quorum requires an odd number of nodes is to prevent situations known as "split-brain" scenarios or "deadlock" situations. For a cluster with n members, quorum is (n/2)+1.

In a split-brain scenario, an even number of nodes can result in a tie vote, where half the nodes vote one way and the other half vote the other way. This can lead to a lack of consensus and potentially conflicting decisions, leading to system instability.

### Why odd number of nodes?

The odd number of nodes **help** but is **not necessary** to elect a leader in a cluster. This is because a majority of the initial cluster votes are required for leader election.

In terms of fault tolerance, although adding a node to an odd-sized cluster appears better since there are more machines, the **fault tolerance is worse** since exactly the same number of nodes may fail without losing quorum but there are more nodes that can fail i.e. an even-number cluster does not buy additional fault tolerance.

### Leader election

Leader election requires the majority of the **initial cluster size** and not the majority of active nodes for the following reasons: stability, scalability, and fault tolerance.

The initial cluster size provides a stable reference point for the algorithm, ensuring that the leader election process can reliably handle changes in the active nodes. If leader election were based solely on the number of active nodes, **constant fluctuations in the network could lead to frequent leader re-elections** and potential instability.

Consensus algorithms are designed to work efficiently with large-scale distributed systems. By basing leader election on the initial cluster size, the algorithm can handle a wide range of network sizes without being adversely affected by the dynamic nature of active nodes. **It allows for flexibility in adding or removing nodes without requiring a complete reconfiguration of the consensus protocol**.

Consensus algorithms aim to maintain system integrity and availability even in the presence of failures or network partitions. By considering the initial cluster size, **the algorithm can handle failures or temporary unavailability of nodes without disrupting the leader election process**. It ensures that decisions can still be made and progress can continue even if some nodes are temporarily inactive.

### Network partition

In the event of a network partition, where a network becomes divided into two or more isolated sub-networks, **an odd number quorum is still able to make progress and resolve the partition**.

When a partition occurs, each sub-network can continue operating independently with its own subset of nodes. Since the quorum requires an odd number of nodes, **at least one of the partitions will have a majority of nodes**.

The partition that contains the majority of nodes **can continue to function as normal**, maintaining quorum and making consistent decisions. This allows the system to proceed and make progress, even if the other partition(s) are unable to communicate with it.

Once the network partition is resolved and the sub-networks are able to communicate again, the system can reconcile any differences that may have occurred during the partition. Depending on the specific implementation, this may involve merging conflicting data or making decisions based on the most recent updates.
