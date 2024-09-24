## Client-centric consistency

Eventually consistent data stores generally work fine as long as clients always access the same replica. However, problems arise when **different replicas are accessed** by the same client over a short period of time. Nonetheless, such differences should be made transparent. The problem can be alleviated by introducing **client-centric consistency**.

In essence, client-centric consistency models ensure that whenever a client connects to a new replica, that replica is brought up to date with the data that had been manipulated by that client before, and which may reside at other replica sites.

This consistency provides guarantees for a **single client** concerning the consistency of accesses to a data store by that client. No guarantees are given concerning concurrent accesses by different clients. It is also relatively straightforward if performance issues are ignored.

### How it works

In a native implementation, each write operation W is assigned a globally unique identifier. Then, for each client, we keep track of two sets of writes:

1. Read set: Consists of the writes relevant for the read operations
2. Write set: Consists of writes performed by the client

## Monotonic reads

The first client-centric consistency model is that of monotonic reads. A distributed data store is said to provide monotonic-read consistency if the following condition holds:

- If a process reads the value of a data item x, any successive read operation on x by that process will always return that same value or a more recent value

In other words, monotonic-read consistency guarantees that once a process has seen a value of x, it will never see an older version of x.

### Implementation

1. when a client wants to perform a read operation at a server, that server is handed the client's read set to check whether all identified writes have taken place locally
2. If not, it contacts other servers to ensure that is is brought up-to-date before carrying out the read operation
3. After read operation is performed, the write operations that have taken place at the selected server and that are relevant for the read operation are added to the client's read set

## Monotonic writes

In many situations, it is important that write operations are propagated in the correct order to all copies of the data store. This property is expressed in monotonic-write consistency. In a monotonic-write consistent store, the following condition holds:

- A write operation by a process on a data item x is completed before any successive write operation on x by the same process

Monotonic-write consistency resembles data-centric FIFO consistency. The essence of FIFO consistency is that write operations by the same process are performed in the correct order everywhere.

### Implementation

1. When a client initiates a new write operation at a server, the server is handed over the client's write set and ensures that the identified write operations are performed first and in the correct order
2. After performing the new write operation, the operation's write handler is added to the write set

### Implementation

## Read your own writes

A data store is said to provide read-your-writes consistency, if the following
condition holds:

- The effect of a write operation by a process on data item x will always be seen by a successive read operation on x by the same process

In other words, **a write operation is always completed before a successive read operation** by the same process, no matter the location where that read operation takes place.

The absence of read-your-writes consistency is sometimes experienced when updating Web documents and subsequently viewing the effects. Similar effects occur when updating passwords.

### Implementation

1. All write operations in the client's write set is performed
2. Read operation is then executed

## Writes follow reads

In this model, updates are propagated as the result of previous read operations. A data store is said to provide writes-follow-reads consistency, if the following holds:

- A write operation by a process on a data item x following a previous read operation on x by the same process is guaranteed to take place on the same or a more recent value of x that was read

In other words, any successive write operation by a process on a data item x will be performed on a copy of x that is up to date with the value most recently read by that process.

### Implementation

1. Bring the selected server up-to-date with the write operations in the client’s read set
2. Add the identifier of the write operation to the write set, along with the identifiers in the read set

## Improving efficiency

It is easy to see that the read set and write set associated with each client can become very large. Each set consists of a number of identifiers for write operations. Whenever a client forwards a read or write request to a server, a set of identifiers is handed to the server as well to see whether all write operations relevant to the request have been carried out by that server.

To keep these sets manageable, a client’s read and write operations are grouped into **sessions**. A session is typically associated with an application: it is opened when the application starts and is closed when it exits. Nonetheless, if a client opens a session that it never closes, the associated read and write sets can still become very large.

This information can be more efficiently represented by **vector timestamps**. Whenever a server accepts a new write operation W, it assigns that operation a globally unique identifier along with a timestamp ts(W). Subsequent write operation submitted to that server S is assigned a higher-valued timestamp. Each server maintains a vector timestamp as follows:

```
vector timestamp = WVCi
WVCi[j] = timestamp of write operation from Sj that has been processed by Si
```

The timestamp of a session always represents the latest write operations that have been seen by the applications that are being executed as part of that session. The compactness is obtained by representing all observed write operations originating from the same server through a single timestamp.
