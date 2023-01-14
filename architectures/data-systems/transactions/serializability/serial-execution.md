## Actual Serial Execution

The simplest way of avoiding concurrency problems is to remove concurrency entirely i.e. executing one transaction at a time on a single thread. However, this limits the transaction throughput to the speed of a single CPU core. Nonetheless, this was implemented in 2007 due to the following developments:

- RAM became cheap enough that for many use cases is now feasible.
- OLTP transactions are usually short and only make a small number of reads and writes, whereas long-running queries are typically read-only

### Encapsulating Transactions in Stored Procedures

A database transaction could encompass an entire flow of user activity i.e. for booking airline tickets, need to search for routes, book seats on flights, and making payment.

In an application code, this would result in multiple queries and results sent back and forth between the database server and application machine. If concurrency is disabled, the throughput would be dreadful as the database would spend most of its time waiting for an application to issue the next query for the current transaction.

Hence, for systems with single-threaded serial transaction processing, stored procedures are used as it does not have to wait for any network or disk I/O, and can achieve good throughput on a single thread.

### Partition

To scale to multiple CPU cores or nodes, need to partition the data, so that each transaction only needs to read/write within a single partition. and each partition can have its own transaction processing thread running independently from others.

However, for any transaction that needs to access multiple partitions, the database must coordinate the transaction across all the partitions that it touches.

### Constraints

- Every transaction must be small and fast
- Limited to use cases where the active dataset can fit in memory as reading from disk in a single-threaded transaction would be very slow
- Write throughput must be low enough to be handled by a single CPU core
- Cross-partition transactions are possible, but there is a hard limit to the extent to which they can be used
