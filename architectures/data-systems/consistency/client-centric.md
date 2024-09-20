## Client-centric consistency

Eventually consistent data stores generally work fine as long as clients always access the same replica. However, problems arise when **different replicas are accessed** by the same client over a short period of time. The problem can be alleviated by introducing **client-centric consistency**. This consistency provides guarantees for a **single client** concerning the consistency of accesses to a data store by that client. No guarantees are given concerning concurrent accesses by different clients.

### Monotonic reads

The first client-centric consistency model is that of monotonic reads. A distributed data store is said to provide monotonic-read consistency if the following condition holds:

- If a process reads the value of a data item x, any successive read operation on x by that process will always return that same value or a more recent value

In other words, monotonic-read consistency guarantees that once a process has seen a value of x, it will never see an older version of x.

### Monotonic writes

In many situations, it is important that write operations are propagated in the correct order to all copies of the data store. This property is expressed in monotonic-write consistency. In a monotonic-write consistent store, the following condition holds:

- A write operation by a process on a data item x is completed before any successive write operation on x by the same process

Monotonic-write consistency resembles data-centric FIFO consistency. The essence of FIFO consistency is that write operations by the same process are performed in the correct order everywhere.

### Read your own writes

A data store is said to provide read-your-writes consistency, if the following
condition holds:

- The effect of a write operation by a process on data item x will always be seen by a successive read operation on x by the same process

In other words, **a write operation is always completed before a successive read operation** by the same process, no matter the location where that read operation takes place.

The absence of read-your-writes consistency is sometimes experienced when updating Web documents and subsequently viewing the effects. Similar effects occur when updating passwords.

### Writes follow reads

In this model, updates are propagated as the result of previous read operations. A data store is said to provide writes-follow-reads consistency, if the following holds:

- A write operation by a process on a data item x following a previous read operation on x by the same process is guaranteed to take place on the same or a more recent value of x that was read

In other words, any successive write operation by a process on a data item x will be performed on a copy of x that is up to date with the value most recently read by that process.
