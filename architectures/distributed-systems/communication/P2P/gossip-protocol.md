## Gossip protocol

The peer-to-peer state management approach is inclined towards high availability and **eventual consistency**. The gossip protocol algorithm can be used to implement peer-to-peer state management services with high scalability and improved resilience.

The gossip protocol is a **decentralized peer-to-peer communication** technique to transmit messages in a large distributed system. It relies on epidemic behavior i.e. based on theory of infectious diseases. It is based on probabilistic broadcast.

Gossip protocol can be used to keep nodes consistent only if:

- Operations are commutative
- Serializability is not needed

Use cases include:

- Failure detection
- Database replication
- Information dissemination
- Generating aggregations
- Leader election

https://highscalability.com/gossip-protocol-explained/

### Anti-entropy

A popular propagation model is that of anti-entropy. In this model, a node P picks another node Q at random, and subsequently exchanges updates with Q. There are three approaches to exchanging updates:

1. P only pulls in new updates from Q i.e. push approach
2. P only pushes its own updates to Q i.e. pull approach
3. P and Q send updates to each other i.e. a push-pull approach (**most effective**)

When it comes to rapidly spreading updates, a pure push-based approach is the worst choice. This is because updates can be propagated only by infected nodes. Moreover, if many nodes are infected, the probability of each one selecting a susceptible node is relatively small. This approach consumes considerable resources and causes many redundant transmissions, in order to achieve reliable delivery with high probability.

In contrast, pull-based approach works much better as spreading updates is essentially triggered by susceptible nodes. Chances are big that such a node will contact an infected one to subsequently pull in the updates and become infected as well.

The most effective approach is using a hybrid of push-pull approach with multiple phases. In the first phase, push-style broadcast is used until many processes are infected e.g. half. In the second phase, it switches to a pulling mechanism.

### How it works

The key concepts are:

- Every node periodically sends out a message to a subset of other random nodes
- Data can include timestamp of data, health, etc.
- Application-level data can be piggybacked in gossip messages as key-value pairs
- If it receives data about the same node, it will trust the most recent data by either deleting it or using a tombstone as an entry to invalidate it

The gossip protocol is reliable because a node failure can be overcome by the retransmission of a message by another node. First-in-first-out (FIFO) broadcast, causality broadcast, and **total-order broadcast** can be implemented with gossip protocol.

### Parameters

The gossip protocol parameters such as cycle and fanout can be tuned to improve the probabilistic guarantees of the gossip protocol:

- **Fanout**: Number of nodes that will receive the message
- **Cycle**: The count of gossip rounds required to spread a message across the entire cluster, equivalent to O(logN) to the base of fanout where N is the total number of nodes

## Advantages

### Scalability

The gossip protocol cycle requires logarithmic time to achieve convergence. In addition, every node interacts with only a fixed number of nodes and sends only a fixed number of messages independent of the number of nodes in the system. A node doesn’t wait for an acknowledgment to improve latency.

### Fault tolerance

The distributed system employing the gossip protocol is fault tolerant due to tolerance towards unreliable networks. The redundancy, parallelism, and randomness offered by the gossip protocol improve the fault tolerance of the system.

Furthermore, the symmetric and decentralized nature of the nodes strengthens the fault tolerance of the gossip protocol. The same message is usually transmitted several times across multiple nodes.

### Robustness

The gossip protocol is not robust against a malfunctioning node or a malicious gossip message unless the data is self-verified.

A score-based reputation system for nodes can be used to prevent gossip system corruption by malicious nodes. Appropriate mechanisms and policies such as encryption, authentication, and authorization must be implemented to enforce the privacy and security of the gossip system.

### Decentralization

The gossip protocol offers an extremely decentralized model of information discovery through peer-to-peer communication

### Simplicity

Most variants of the gossip protocol can be implemented with very little code and low complexity.

## Drawbacks

### Eventually consistent

There is also an overhead associated with gossip messages and the gossip behavior depends on the network topology and node heterogeneity. Therefore, there will be some delay to recognize a new node or a node failure by the cluster.

### Bandwidth and redundancy

The gossip protocol is not known for efficiency as the same message might be retransmitted to the same node multiple times consuming unnecessary bandwidth i.e. induces a significant amount of redundancy in message exchanges as a given process may receive the same message many times.

### Latency

The usage of the gossip protocol results in increased latency because the node must wait for the next gossip cycle (interval) to transmit the message.

### Network partition unawareness

When a network partition occurs, the nodes in the sub-partition will still gossip with each other. Hence, the gossip protocol is unaware of network partitions and might significantly delay message propagation.
