## Locking mechanisms

Concurrent data access requires mechanisms to prevent adverse effects when multiple users try to modify resources simultaneously. Side effects include **lost updates, dirty reads (uncommitted dependency), inconsistent analysis, and phantom reads.** Locking is designed to ensure data integrity and consistency while enabling concurrent data access.

### Locking

Each transaction would request locks of different types on the resources (rows, tables, pages). The locks block other transactions from modifying the resources, and is released once the transaction no longer has a dependency on the locked resources.

### Row versioning

Database engine maintains versions of each row that is modified. Applications can specify that a transaction use the row versions to view data as it existed at the start of the transaction. The chance that a read operation would block others is greatly reduced.

## Concurrency controls

### Pessimistic

A system of locks prevents users from modifying data in a way that affects other users. After a user performs an action that causes a lock to be applied, other users cannot perform actions until the owner releases it. Used in environments where there is high contention for data.

### Optimistic

Users do not lock data when they read it. Instead, the system checks if another user changed the data after it was read; an error is raised and rollback performed if true. Used in environments where there is low contention for data.

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
