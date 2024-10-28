## Atomicity

In a distributed system, atomicity is the guarantee that either both transactions succeed and their changes are committed, or that they fail without any side effects.

For instance, when sending money from one bank account to another, if they belong to different banks, atomicity is required.

### NoSQL

The first versions of NoSQL were focused entirely on scalability and lacked the guarantees of traditional relational databases, such as ACID transactions. However, in recent years, that has mostly changed as distributed data stores have continued to add features that only traditional databases offered.

For example, Google’s Spanner implements transactions across partitions using a combination of 2PC and state machine replication.
