## Anti-entropy

Permanent failures to nodes can result in replicas being inconsistent and un-synchronized, which is a threat to durability. To handle permanent failures, anti-entropy protocol can be implemented to keep replicas synchronized.

## Merkle trees

To detect the inconsistencies between replicas faster and to minimize the amount of transferred data, **Merkle trees** can be used.

A Merkle tree is a hash tree where leaves are hashes of the values of individual keys. Parent nodes higher in the tree are hashes of their respective children. The principal advantage of Merkle tree is that each branch of the tree can be checked independently without requiring nodes to download the entire tree or the entire data set. Moreover, Merkle trees help in reducing the amount of data that needs to be transferred while checking for inconsistencies among replicas.

For instance, if the hash values of the root of two trees are equal, then the values of the leaf nodes in the tree are equal and the nodes require no synchronization. If not, it implies that the values of some replicas are different.

### How it works

1. Each node maintains a separate Merkle tree for each key range (the set of keys covered by a virtual node) it hosts
2. This allows nodes to compare whether the keys within a key range are up-to-date
3. Two nodes exchange the root of the Merkle tree corresponding to the key ranges that they host in common
4. If they have differences, they perform the appropriate synchronization action

The disadvantage with this scheme is that many key ranges change when a node joins or leaves the system thereby requiring the tree(s) to be recalculated.

## Read repair

When using a quorum-based approach for read operations, the client will query from multiple nodes and choose the data that is the most recent through syntactic reconciliation.

To relieve the anti-entropy protocol from having to reconcile inconsistencies, the client can detect stale responses and update the data in those nodes with older versions. This process is called read repair because it repairs replicas that have missed a recent update at an opportunistic time.
