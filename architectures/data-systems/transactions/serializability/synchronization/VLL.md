## VLL (very lightweight locking)

Lock managers are increasingly becoming a bottleneck in database systems that use pessimistic concurrency control. VLL is an alternative approach that avoids almost all overhead associated with traditional lock manager operations, and tracks less total information about contention between transactions, both in the context of a **single (multi-core) server** and in **distributed systems** that partition data across machines in a shared-nothing cluster.

https://www.cs.umd.edu/~abadi/papers/vldbj-vll.pdf

### Lock managers

Although locking protocols are not implemented in a uniform way across all database systems, the most common way to implement is as a hash table that maps each lockable record's primary key to a linked list of lock requests for that record. This list is typically preceded by a lock head that tracks the current lock state for that item.

For thread safety, the lock head generally stores a mutex object, which is acquired before lock requests and releases to ensure that adding or removing elements from the linked list always occurs within a critical section. Every lock release also invokes a traversal of the linked list for the purpose of determining what lock request should inherit the lock next.

These hash table lookups, latch acquisitions, and linked list operations are operations that are not negligible in main memory database systems (unlike disk). These operations can exceed the costs of executing the actual transaction logic. Moreover, as the increase in cores and processors per server leads to an increase in concurrency (and therefore lock contention), the size of the linked list of transaction requests per lock increases.

### High contention workloads

Under high-contention workloads, this can result in reduced concurrency and poor CPU utilization. To ameliorate this problem, an optimization called **selective contention analysis (SCA)** is proposed.

SCA, only when needed, efficiently computes the most useful subset of the contention information that is tracked in full by traditional lock managers at all times.

### Architecture optimizations

The VLL protocol is designed to be as general as possible, with specific optimizations for the following architectures:

- Multiple threads execute transactions on a single-server, shared memory system
- Data are partitioned across processors (possibly multiple servers), and each partition limits its pool of worker threads to one (single thread) that executes transactions serially
- Data are partitioned arbitrarily (across multiple machines in a cluster), and within each partition, worker threads operate on data

## Algorithm

The biggest difference between VLL and traditional lock manager implementation is that VLL stores each record's 'lock table entry' not as a linked list in a separate lock table, but rather as a **pair of integer values `(Cx, Cs)`**, which represents the number of transactions requesting exclusive and shared locks respectively. When no transaction is accessing a record, both values are 0. Also, the raw data is co-located with the lock information by supplementing the tuple with additional attributes. Hence, a single memory access retrieves both the data and lock information in a single cache line, potentially removing cache misses.

The basic technique is to force all locks to be requested by a transaction at once, and order the transactions by the order in which they request their locks.

A global queue of transaction requests (TxnQueue) is also kept at each partition, tracking all active transactions in the order in which they requested their locks.

### Process flow

1. When a transaction arrives at a partition, it attempts to request locks on all records at that partition that it will access in its lifetime
2. Each lock request takes the form of incrementing the corresponding record's Cx or Cs value
3. Exclusive locks are granted if Cx = 1 and Cs = 0
4. Shared locks are granted if Cx = 0
5. Once a transaction has requested its locks, it is added to the TxnQueue
6. Both the requesting of locks and adding of transaction to the queue happen inside the same critical section
7. Upon leaving the critical section, VLL determines how to proceed based on two factors: whether the **transaction is local or distributed**, and whether the **transaction has successfully acquired all of its locks** immediately upon requesting them (free vs blocked)
8. A local transaction is one whose read and write sets include records that all reside on the same partition
9. Free transactions are immediately executed and releases its locks once completed
10. For distributed transactions, it may have to wait for remote read results, and may therefore not complete immediately
11. Blocked transactions are tagged in the TxnQueue as blocked, and are not allowed to execute until they are explicitly unblocked by the VLL algorithm

### Unblocking transactions

Since there is no lock management data structure to record which transactions are waiting for data locked by other transactions, there is no way for a transaction to hand over its locks directly to another transaction when it finishes.

Fortunately, this situation can be resolved by a simple observation: a blocked transaction that reaches the **front of the TxnQueue will always be able to be unblocked and executed**, no matter how large Cx or Cs are for the data it accesses. This is because of the following:

- Each transaction requests all locks and enters the queue within the same critical section
- If a transaction makes it to the front of queue, it means all transactions that requested their locks before it have been completed
- All transactions that requested after it will be blocked if their read/write set conflict

In addition to reducing lock manager overhead, this technique guarantees that there will be no deadlock within a partition. A blocked transaction now has two ways to become unblocked:

- When it reaches the front of the queue
- All transactions that requested its locks before it have completed

### Handling large requests

One problem that VLL sometime faces is that as the TxnQueue grows in size, the probability of a new transaction being able to immediately acquire all of its locks decreases. This can be mitigated by placing an **artificial limit** on the number of transactions that may enter the TxnQueue.

If the size exceeds the threshold, the system temporarily stops to process new transactions, and shifts its processing resources to finding transactions in the TxnQueue that can be unblocked.

### Arrayed VLL vs Co-located VLL

VLL prefers to colocate Cx and Cs values for each record with the record itself. This leads to improved cache/memory bandwidth utilization, as a single request from memory brings both the record and lock information about the record into cache. However, it spreads out lock information across the entire dataset.

It would be preferable to keep all lock management data together in order to ensure that the cache local to the core is filled with lock data and not polluted with record data as well. Hence, an arrayed VLL which uses vector/array to store the Cx and Cs values separately is used. The ith element of each vector corresponds to the Cx and Cs values for the ith record.

### Impediments to acquiring all locks at once

VLL requires that all locks for a transaction be acquired together in a critical section. However, there are two possibilities that make this nontrivial:

- Read and write sets of a transaction may not be known before running the transaction and thus, hard to predict what records the transaction will access and lock i.e. doing secondary index lookup
- Each partition has its own TxnQueue and critical section in which it is modified local to the partition; **different partitions may not process transactions in the same order** which may lead to distributed deadlock

To overcome the first problem, the transaction is allowed to perform whatever reads it needs to (at no isolation) for it to figure out what data it will access. Once the transaction gets its locks, it is handed over to the execution thread, and runs normally unless it discovers it does not have a lock for something. In such scenario, the transaction aborts, releases its locks, and adds itself back to the queue.

For the second problem, an approach is to coordinate across partitions to ensure that multi-partition transactions are added to the TxnQueue in the same order on each partition.

## Optimization

VLL's primary strength lies in its extremely low overhead in comparison with traditional lock management approaches by compressing a linked list of lock requests into two integers. Furthermore, by placing these integers inside the tuple itself, both the lock information and the data itself can be retrieved with a single memory access, minimizing total cache misses.

However, the main disadvantage of VLL is a potential loss in concurrency. Traditional lock managers use the information contained in lock request queues to figure out whether a lock can be granted to a particular transaction.

```
Txn     Write set
A       x
B       y
C       x,z
D       z

TxnQueue
A,B,C,D -> A completes
B,C,D -> C can also run, but VLL cannot detect it
```

### Selective contention analysis (SCA)

For high-contention and high-percentage multi-partition workloads, VLL spends a growing percentage of CPU cycles in the state where no transaction can be found that is known to be safe to execute, whereas a standard lock manager would have been able to find one immediately. Hence, in order to maximize CPU resource utilization, SCA is introduced.

SCA simulates the standard lock manager's ability to detect which transactions should inherit released locks by examining contention only when CPUs would otherwise be sitting idle i.e. TxnQueue is full. **SCA enables VLL to selectively increase its lock management overhead when it is beneficial to do so**.

Any transaction in blocked state is conflicted with one of the transactions that preceded it in the queue at the time it was added. However, the conflicted transactions may have completed and released their locks. As the transactions get closer to the head of the queue, it becomes less likely to be blocked.

SCA starts at the front of the queue and traverses through the queue, looking for a transaction that is ready to run and does not conflict with any older transactions.
