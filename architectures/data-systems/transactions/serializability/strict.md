## Strict serializability

To add a real-time requirement on the order of transactions, strict serializability is required. This level combines serializability with the real-time guarantees that linearizability provides so that when a transaction completes, its side effects become immediately visible to all future transactions.

Strict serializability is slow as it requires coordination, which creates contention in the system. s a result, there are many different isolation levels that are simpler to implement and also perform better.

## 2PL (Two-Phase Locking)

Only widely used algorithm for serializability in databases (**pessimistic** concurrency control mechanism).

Locks are often used to prevent dirty writes, and this algorithm makes lock requirements much stronger: several transactions are allowed to concurrently read the same object as long as nobody is writing to it.

2PL is used in MySQL and SQL Server. As 2PL provides serializability, it protects against all the race conditions including lost updates and write skew.

### Locks

2PL has two types of locks:

- **Read lock (shared lock)**: Can be shared by multiple transactions, but blocks transactions trying to acquire a write lock
- **Write lock (exclusive lock)**: Can be acquired by a single transaction, and blocks any transaction trying to acquire either a read or write lock on the data item

### Phases

1. **Growing Phase**: New locks on data items may be acquired but none can be released
2. **Shrinking Phase**: Existing locks may be released but no new locks can be acquired

If these rules are obeyed, it can be formally proven that the protocol guarantees serializability.

### Implementation

- If a transaction wants to read an object, it must first acquire the lock in shared mode. Several transactions are allowed to hold the lock in shared mode. If another transaction already has an exclusive lock, other transactions must wait
- Writes are performed in exclusive mode
- As many locks are in use, deadlock situations may arise
- However, the database will automatically detect it and aborts one of them so that others can make progress

## Predicate locking

Predicate lock is similar to shared/exclusive lock, but rather than belonging to a particular object (one row in a table), it belongs to all objects that match some search condition.

```sql
SELECT * FROM bookings
WHERE room_id = 123 AND
end_time > '2018-01-01 12:00' AND
start_time < '2018-01-01 13:00';
```

## Index-range locks

To prevent phantoms causing write skew, most databases with 2PL implement index-range locking (next-key locking), which is a simplified approximation of **predicate locking**.

This works by simplifying a predicate by making it match a greater set of objects:

- A predicate lock for bookings of room 123 between 12-1pm is acquired
- Approximate it by locking room 123
- Approximate it by locking all rooms between 12-1pm

## Performance

Big downside of 2PL is that transaction throughput and response times of queries are significantly worse than under weak isolation.

This is partly due to the overhead of acquiring and releasing all those locks, and due to reduced concurrency.
