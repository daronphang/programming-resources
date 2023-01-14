## Transactions

Many things can wrong in data systems, including:

- Database software or hardware may fail at any time
- Application may crash at any time
- Interruptions in the network
- Clients may write to the database at the same time, overwriting each other's changes
- Race conditions between clients

For decades, transactions have been the mechanism of choice for simplifying these issues. A transaction is a way for an application to group several reads and writes together into a logical unit. Either the transaction succeeds (commit) or fails (rollback). Handling of errors become much simpler as we don't have to worry about partial failure.

### Handling Errors

A key feature of a transaction is that it can be aborted and safely retried if an error occurred, and ACID databases are based on this philosophy: if the database is in danger of violating its guarantee of ACID, it would rather abandon the transaction entirely than allow it to remain half-finished.

Although retrying is a simple and effective error handling mechanism, it isn't perfect:

- If the transaction actually succeeded but network failed, the transaction will be performed twice
- If error is due to overload, retrying will make the problem worse. To avoid such feedback cycles, can limit the number of retries i.e. exponential backoff
- It is worth retrying transient errors i.e. deadlokc, ioslation violation, network interruptions, etc.
- Transactions may have side effects i.e. sending an email, and using **two-phase commit** can help

### Write Skew and Phantoms

Write skew is neither a dirty nor a lost update, but can occur if two transactions read the same objects and then update some of those objects (different transactions may update different objects). This requires **serializable isolation**.

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
