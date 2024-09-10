## Read-heavy vs write-heavy

Designing systems for read-heavy versus write-heavy workloads involves different strategies, as each type of system has unique demands and challenges.

## Designing read-heavy systems

- Caching at different levels (application, database), materialized views
- Database replication to create read replicas
- Using CDNs to cache static and dynamic content
- Load balancing to distribute incoming read requests evenly across multiple servers or replicas
- Optimize data retrieval such as indexing, SQL query optimization
- Data partitioning
- Asynchronous processing

## Designing write-heavy system

- Choosing database optimized for write-heavy such as Cassandra, MongoDB, etc.
- Batch/buffer multiple write operations together
- Asynchronous processing with message queues
- Separate read and write commands using CQRS
- Data partitioning
- Using write-ahead logging (WAL) before applying to database to ensure data integrity and improve write performance
- Persist changes as a sequence of immutable events rather than modifying the database state directly through **event sourcing**; useful for aggregates
