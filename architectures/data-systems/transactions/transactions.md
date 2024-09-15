## Transactions

Many things can wrong in data systems, including:

- Database software or hardware may fail at any time
- Application may crash at any time
- Interruptions in the network
- Clients may write to the database at the same time, overwriting each other's changes
- Race conditions between clients

For decades, transactions have been the mechanism of choice for simplifying these issues. A transaction is a way for an application to group several reads and writes together into a logical unit. Either the transaction succeeds (commit) or fails (rollback). Handling of errors become much simpler as we don't have to worry about partial failure.

## Handling errors

A key feature of a transaction is that it can be aborted and safely retried if an error occurred, and ACID databases are based on this philosophy: if the database is in danger of violating its guarantee of ACID, it would rather abandon the transaction entirely than allow it to remain half-finished.

Although retrying is a simple and effective error handling mechanism, it isn't perfect:

- If the transaction actually succeeded but network failed, the transaction will be performed twice
- If error is due to overload, retrying will make the problem worse. To avoid such feedback cycles, can limit the number of retries i.e. exponential backoff
- It is worth retrying transient errors i.e. deadlock, isolation violation, network interruptions, etc.
- Transactions may have side effects i.e. sending an email, and using **two-phase commit** can help
