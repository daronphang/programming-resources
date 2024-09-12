## Replication lag

For asynchronous replications involving distributed databases, if the follower has fallen behind the leader, will lead to inconsistencies as all writes have been reflected in the leader. However, this is just a temporary state, and this effect is known as **eventual consistency**. If the replication lag is large, the inconsistencies can become a problem for applications. This becomes more crucial and unacceptable for time-sensitive reads.

Hence, need to design systems that provides a stronger guarantee for read-after-write.

### Tight consistency

To deal with replication lag, can enforce tight consistency. This means all replicas are guaranteed to be up to date with the primary server. However, this solution **negates the benefits of using replica** and also reduces the overall availability of write operations. Even if one of the replicas is down, the write operation can fail.

### Reading your own writes

To implement read-after-write consistency, can either read data that is editable by the user from the leader i.e. social media profile, and others from followers.

Alternative is to track the time of the last update, and make all reads from the leader before a certain duration has passed i.e. one minute.

### Monotonic reads

Monotonic reads means that if one user makes several reads in a sequence, they will not read older data that has not been updated by followers, even if the data read is not real-time. This is achieved by making sure each user is reading from the **same replica**.

This can be achieved by supplying a unique identifier within a series of requests that require read consistency.

### Consistent prefix reads

This guarantee says that if a sequence of writes happens in a certain order, then anyone reading those writes will see them appear in the same order.

Solution is to ensure that any writes that are casually related to each other are written to the same partition by using algorithms.