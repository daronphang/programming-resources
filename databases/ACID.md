## Atomicity

Atomic refers to something that cannot be broken down into smaller parts. In databases, atomicity describes what happens if a client wants to make several writes, but a fault occurs after some of the writes have been processed. If the writes are grouped together into an atomic transaction, it cannot be completed and is rollback/discarded.

Atomicity simplifiers the problem that if a transaction is aborted, the application can be sure that it didn't change anything and hence, can be safely retried.

## Consistency

The idea of ACID consistency is that you have certain statements about your data (invariants) that must always be true i.e. credits/debits in accounting system must always be balanced. 

However, this is the application's responsibility to define its transactions correctly so that they can preserve consistency. 

## Isolation

Most databases are accessed by several clients at the same time, and can present a problem due to race conditions. Isolation means that concurrently executing transactions are isolated from each other (serializable isolation) i.e. database guarantees that transactions have the same effect as if they ran serially.

In practice, isolation is not that simple and has a performance cost. Hence, it is common for systems to use weaker levels of isolation, which protect against some concurrency issues.

### Read Committed

Most basic level of transaction isolation that is implemented in Oracle, PostgreSQL, SQL Server, MemSQL. Implementation is performed by using locks on the object to be modified, and only one transaction can hold the lock for any given object. Makes two guarantees:
1. When reading from the database, you will only see data that has been committed (no dirty reads).
2. When writing to database, you will only overwrite data that has been committed (no dirty writes).

However, read committed does not prevent the race condition between two counter increments, and can lead to incorrect data.

### Snapshot Isolation

Idea is that each transaction reads from a consistent snapshot of the database i.e. transaction sees all the data that was committed in the database at the start of the transaction. Even if the data is subsequently changed by another transaction, each transaction sees only the old data from that particular point of time.

Reads do not require any locks, but typically use write locks to prevent dirty writes.

## Durability

Durability is the promise that once a transactions has committed successfully, any data it has written will not be forgotten, even if the database crashes.

In a single-node, durability means that the data has been written to nonvolatile storage i.e. hard-drive, SSD, and involves a write-ahead log which allows recovery. 

More recently, durability has been adapted to mean replication. 