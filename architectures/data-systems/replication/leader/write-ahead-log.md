## Write-ahead log (WAL)

The log is an append-only sequence of bytes containing all writes to the database. Besides writing the log to disk, the leader sends it across the network to its followers.

This method is used in PostgreSQL and Oracle. However, as the log describes data on a very low level, it makes replication closely coupled to the storage engine. Hence, it is not possible to perform zero-downtime upgrade if the follower uses a newer software version than its leader.

## Logical log (Row-Based)

Logical log helps to decouple replication log from storage engine, which involves a sequence of records describing writes to database tables at the granularity of a row.
