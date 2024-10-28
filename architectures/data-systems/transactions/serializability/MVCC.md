## MVCC (Multi-Version Concurrency Control)

MVCC is a database optimization technique that creates duplicate copies of records so that data can be safely read and updated at the same time (**optimistic approach**). This means that when querying a database, each transaction sees a snapshot of data as it was some time ago, regardless of the current state of the underlying data, providing transaction isolation for each database session.

The main difference between MVCC and lock models is that in MVCC, locks acquired for querying don't conflict with locks acquired for writing i.e. with MVCC, DBMS' reads and writes don't block each other.

By maintaining several version of the object, MVCC ensures a transaction never has to wait to read a database object, making it non-blocking. Hence, it has much better concurrency than 2PL.

DBMS that uses this technique include PostgreSQL.

## SSI (Serializable Snapshot Isolation)

Implemented by MVCC. For the database to know if a query result has changed, it can consider:

- Detecting reads of a stale MVCC object version (uncommitted write occurred before the read)
- Detecting writes that affect prior reads

### Performance

Big advantage of SSI is that one transaction does not need to block waiting for locks held by another transaction. However, SSI is less sensitive to slow transactions than 2PL or serial execution.
