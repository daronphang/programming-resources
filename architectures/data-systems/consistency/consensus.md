## Distributed Transactions and Consensus

Consensus is one of the most fundamental problems in distributed computing. The goal is to get several nodes to agree on something.

## Example Situations

### Leader Election

In a database with single-leader replication, all nodes need to agree on which node is the leader. The position might become contested if some nodes can't communicate with others due to a network fault, and may result in a **split brain situation** in which two nodes both believe themselves to be the leader. **This would cause data to diverge, leading to inconsistency and data loss.**

### Atomic Commmit

In a database that supports transactions spanning several nodes/partitions, we have the problem that a transaction may fail but succeed on others. To maintain atomicity, need to get all nodes to agree on the outcome of the transaction: either all abort or commit (if succeeds).

## 2PC (Two-Phase Commit)

2PC is an algorithm used in distributed databases for achieving atomic transaction commit across multiple nodes i.e. ensures all nodes commit or abort.

2PC uses a new component that does not appear in single-node transactions known as the coordinator/transaction manager. The coordinator is often implemented as a library within the same application process that is requesting the transaction, but can be a separate process or service. Examples include Narayana, JOTM, BTM or MSDTC.

### Process

Similar to a traditional marriage ceremony whereby the minister asks the bride and groom individually.

1. **Reading/Writing:** Transaction begins with application reading and writing data on multiple database nodes
2. **Phase 1:** Coordinator sends a prepare request to each of the nodes, asking if they are able to commit
3. **Phase 2:** Coordinator sends a commit request to all nodes if all reply 'yes', else an abort request if any replies 'no'

### Why it Works

Although the prepare and commit requests can just as easily be lost, 2PC ensures atomicity:

1. When the application begins a distributed transaction, it requests a transaction ID from the coordinator
2. Application begins a single-node transaction on each node
3. When application is ready to commit, the coordinator sends a prepare request to all nodes, tagged with the global transaction ID. If any of the requests fails, the coordinator sends an abort request to all nodes
4. When a participant receives the prepare request, it makes sure it can definitely commit under all circumstances (crash, power failure, insufficient disk space are not acceptable excuses)
5. When the coordinator has received all responses, it makes a definitive decision to commit or abort the transaction. It must write that decision to its transaction log on disk (known as the commit point or 'point of no return')
6. Coordinator sends commit request to all participants. If request fails, the coordinator must retry forever until it succeeds and there is no more going back

## Distributed Transactions in Practice

Although 2PC helps to provide an important safety guarantee, distributed transactions are often criticized for causing operational problems, killing performance, and promising more than they can deliver. Hence, many cloud services choose not to implement distributed transactions.
