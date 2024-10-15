## Locking mechanisms

Concurrent data access requires mechanisms to prevent adverse effects when multiple users try to modify resources simultaneously. Side effects include **lost updates, dirty reads (uncommitted dependency), inconsistent analysis, and phantom reads.** Locking is designed to ensure data integrity and consistency while enabling concurrent data access.

### Locking

Each transaction would request locks of different types on the resources (rows, tables, pages). The locks block other transactions from modifying the resources, and is released once the transaction no longer has a dependency on the locked resources.

### Row versioning

Database engine maintains versions of each row that is modified. Applications can specify that a transaction use the row versions to view data as it existed at the start of the transaction. The chance that a read operation would block others is greatly reduced.

## Concurrency controls

### Pessimistic

A system of locks prevents users from modifying data in a way that affects other users. After a user performs an action that causes a lock to be applied, other users cannot perform actions until the owner releases it. Used in environments where there is high contention for data.

For write-heavy loads, a pessimistic protocol is more efficient as it avoids retrying the same transactions repeatedly.

### Optimistic

Users do not lock data when they read it. Instead, the system checks if another user changed the data after it was read; an error is raised and rollback performed if true. Used in environments where there is low contention for data.

Optimistic concurrency makes sense when you have read-heavy workloads that only occasionally perform writes, as reads don’t need to take any locks.

## Lock locations (resources)

```
RID         Row identifier, lock a single row within a heap
KEY         Row lock within an index to protect key ranges
PAGE        Data or index pages
TABLE       Entire table, including all data and indexes
FILE        Database file
DATABASE    Entire database
```

## Lock modes

```
Shared (S)      Used for read operations that do not change data
Update (U)      Prevents deadlock during concurrent operations
Exclusive (X)   Used for modifying data i.e. INSERT,UPDATE,DELETE
```

## Examples

```sql
BEGIN TRANSACTION;
SELECT ITEM_ID
FROM TABLE_ITEM
WITH(XLOCK, ROWLOCK)
WHERE ITEM_PRIORITY > 10 AND ITEM_CATEGORY = 'CT1' AND ITEM_STATUS = 'available' AND ROWNUM = 1;
UPDATE [locked item_id] SET ITEM_STATUS = 'unavailable';
COMMIT TRANSACTION;
```

## Lock usage

### Fine-grained

A fine-grained lock is generally used for a small object e.g. a row in a table. It is also one that might be held for a short duration e.g. seconds.

One advantage is that it reduces the overhead of locking by **not maintaining locks across lock server failure**. Clients must be prepared to lose locks during network partitions, and the loss of locks on lock server failover introduces no new recovery paths.

### Coarse-grained

A coarse-grained lock typically controls larger structures e.g. an entire table or database. It might be held for a long duration e.g. hours, days. They are acquired rarely as compared to fine-grained locks. Benefits include:

- They impose far less load on the lock server i.e. the lock-acquisition rate is weakly related to the transaction rate of client applications. Hence, performance and ability to add new servers are not a concern
- As they are acquired rarely, temporary lock server unavailability delays client less
- Brief unavailability does not cause clients to stall as opposed to fine-grained locks

However, a failover of a lock server would mean locks would need to be transferred from client to client, and this would require a costly recovery process. Hence, it is good for coarse-grained locks to survive lock server failures.
