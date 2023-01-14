## Preventing Lost Updates

Two concurrent transactions can result in lost updates i.e. counter increments.

### Atomic Write Operations

Many databases provide atomic update operations, which remove the need to implement read-modify-write cycles in application code.

Implemented by taking an exclusive lock on the object when it is read so that no other transactions can read it until the update is completed (**cursor stability**). Other option is to **force all atomic operations to be executed on a single thread**.

```sql
-- concurrency safe in relational databases
UPDATE counters SET value = value + 1 WHERE key = 'foo';
```

### Explicit Locking

If the database does not provide built-in atomic operations, the application can perform an explicit lock on objects that are going to be updated. However, need to be careful so as not to introduce a race condition as adding locks can be missed.

### Compare-and-set

In databases that don't provide transactions, can use an atomic compare-and-set operation to avoid lost updates, by allowing an update to happen if the value has not changed since you last read it.

```sql
UPDATE wiki_pages SET content = 'new content'
    WHERE id = 1234 and content = 'old content'
```
