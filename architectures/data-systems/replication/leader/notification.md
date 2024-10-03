## Notification strategies

### Statement-based replication

Leader logs every write request (INSERT, UPDATE, DELETE) that it executes and sends that statement log to its followers. However, there are various ways in which this approach can break down:

- Any statement that calls a non-deterministic function i.e. NOW() to get the current date, is likely to generate a different value on each replica
- Statements that have side effects (triggers, stored procedures, user-defined functions) may result in different side effects occurring in each replica unless they are deterministic

Although it is possible to workaround by replacing non-deterministic function calls with a fixed return value, there are too many edge cases, and other methods are preferred.

### Trigger-based replication

Sometimes may need more flexibility in terms of replication i.e. replicating a subset of data, and requires moving replication up from the database system to the application layer. This can be done through **triggers and stored procedures**.

A trigger lets you register custom application code that is automatically executed when a data change (write transaction) occurs in a database system. Hence, it has the opportunity to log this change into a separate table, from which it can be read by an external process.

However, it has greater overheads than other replication methods and is more prone to bugs and limitations, but it can be useful due to its flexibility.

### Write-ahead log (WAL)

The log is an append-only sequence of bytes containing all writes to the database. Besides writing the log to disk, the leader sends it across the network to its followers.

This method is used in PostgreSQL and Oracle. However, as the log describes data on a very low level, it makes replication closely coupled to the storage engine. Hence, it is not possible to perform zero-downtime upgrade if the follower uses a newer software version than its leader.

### Logical log (row-based)

Logical log helps to decouple replication log from storage engine, which involves a sequence of records describing writes to database tables at the granularity of a row.
