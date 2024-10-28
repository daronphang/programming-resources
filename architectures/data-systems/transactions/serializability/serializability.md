## Serializability

Serializability is a guarantee about transactions, or groups of one or more operations over one or more objects. It guarantees that the execution of a set of transactions (usually containing read and write operations that may be in parallel) over multiple items is equivalent to some serial execution (total ordering) of the transactions.

Unlike linearizability, serializability does not impose any real-time constraints on the ordering of transactions. For instance, tx1 begins earlier than tx2, but the result behaves as if tx2 was executed before tx1.

When handling race conditions, isolation levels are difficult to understand and inconsistently implemented across different databases. Using **serializable isolation** is the best solution; however, not everyone uses it as either it doesn't scale (serial execution) or perform well (2PL).

Serializability can be achieved either with a **pessimistic** or an **optimistic** concurrency control mechanism.
