## Hints

Applies to DELETE, INSERT, SELECT, UPDATE and MERGE. Table hints override the default behavior of the Query Optimizer for the duration of the statement by specifying the following:

- Locking method
- One or more indexes
- Query-processing operation such as table scan or index seek

As the Query Optimizer selects the best execution plan for a query, **hints should only be used as a last resort by experienced developers**.

SQL Server Database Engine uses a dynamic locking strategy that automatically chooses the best locking granularity for queries in most cases, and almost always chooses the correct locking level. **Disallowing a locking level can adversely affect concurrency. Adding hints can make queries slower and blocking worse**.

https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver15#Customize

https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table?redirectedfrom=MSDN&view=sql-server-ver16

### Lock Escalation

Adding locks take up memory, and SQL Server has an internal lock escalation threshold of 5000 which will replace smaller locks with a larger table level lock. This escalation would lead to an exclusive lock to the entire table which may be undesired.

```sql
--disabling lock escalation
ALTER TABLE agg.FirstNameByYear SET ( LOCK_ESCALATION = DISABLE);
GO
```

https://littlekendra.com/2016/02/04/why-rowlock-hints-can-make-queries-slower-and-blocking-worse-in-sql-server/

### Hint Types

```
INDEX
HOLDLOCK    Synonym for SERIALIZABLE
NOLOCK
PAGLOCK
ROWLOCK
SNAPSHOT
TABLOCK
UPDLOCK
XLOCK
```

```sql
UPDATE [dbo].[prices] WITH (ROWLOCK)
SET UnitPrice = 50
WHERE ProductKey = 150;
```
