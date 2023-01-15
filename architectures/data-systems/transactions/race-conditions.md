## Dirty Reads

One client reads another client's writes before they have been committed. The read committed isolation level and stronger levels prevent dirty reads.

## Dirty Writes

One client overwrites data that another client has written, but not yet committed. Almost all transaction implementations prevent dirty writes.

## Lost Updates

Two clients concurrently perform a read-modify-write cycle. One overwrites the other's write without incorporating its changes i.e. counter increments. Some implementations of SSI prevent this anomaly automatically, while others require a manual lock.

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

## Phantom Reads

A transaction reads objects that match some search condition. Another client makes a write that affects the results of that search. SSI prevents straightforward phantom reads, but phantoms in the context of write skew require special treatment, such as index-range locks.

## Write Skew and Phantom

Write skew is neither a dirty nor a lost update, but can occur if two transactions read the same objects and then update some of those objects (different transactions may update different objects). This requires **serializable isolation**, particularly SSI which is implemented with MVCC.

Phantom refers to one transaction changing the results of another's search query. Phantoms causing write skew follow a similar pattern:

1. A SELECT query checking whether some requirement is satisfied
2. Depending on the results for the first query, the application code decides how to continue
3. If the application decides to go ahead, it makes a WRITE

Best way to prevent this is to implement explicit locking yourself.

```sql
-- on_call must be >=2 to take leave; however, concurrent reads will result in both transactions succeeding (write skew)

-- Alice
SELECT count(*) FROM doctors WHERE on_call = true and shift_id = 1234
-- on_call >= 2
UPDATE doctors SET on_call = false WHERE namne = 'Alice' AND shift_id = 1234

-- Bob
SELECT count(*) FROM doctors WHERE on_call = true and shift_id = 1234
-- on_call >= 2
UPDATE doctors SET on_call = false WHERE namne = 'Bob' AND shift_id = 1234
```
