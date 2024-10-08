## Sharding

For very large datasets, or very high query throughput, need to break data up into **sharding to achieve scalability**. Sharding is mainly employed for **horizontal partitioning** across multiple machines or databases.

When a database is sharded, a replica of the schema is created. This is then used to divide data to be stored in a shard based on a shard key. Sharding is typically implemented for distributing load across a cluster to enhance scalability.

Different partitions can be placed on different nodes in a shared-nothing cluster. Hence, a large dataset can be distributed across many disks, and the query load can be distributed across many processors.

For queries that operate on a single shard, each node can independently execute the queries for its own shard, and query throughput can be scaled by adding more nodes.

Sharding the database is a common solution in **scale-up scenarios**. Splitting data can help reduce index growth and reduce write locking on a single instance. Sharding is also, however, **the only way to achieve a writeable scale-out database for the vast majority of SQL users** e.g. PostgreSQL.

### Vertical

Vertical sharding is the technique of moving a table to a separate server. Vertical sharding allows to keep different tables with different database leaders. This approach improves the write scalability.

Another approach is to divide data based on columns, with each shard holding a subset of columns.

### Horizontal

Horizontal sharding divides data based on rows, with each shard holding a subset of rows.

There are two levels to horizontally sharding a database:

- Logical database level: Each shard contains the same set of tables
- Table level: Only large tables are sharded

If secondary indexes are heavily used, sharding at table level would be preferred. This is because secondary indexes are stored within a shard, and querying on secondary indexes may have to query all the shards of the table which may be expensive i.e. scatter and gather.

### How sharding works

1. Data is partitioned based on specific criteria e.g. user ID
2. Each partition (shard) resides on a dedicated server
3. Applications determine the correct shard for a given query
4. Data within a shard can be replicated for high availability

### Client vs server sharding

Client-side sharding is entirely transparent to the application which is able to connect to any node in the cluster and have queries automatically access the correct shards. Instead of relying on automatic coordination, applications determine where data is located and route queries accordingly.

Some companies have implemented horizontal sharding at the application level. Pinterest took this approach after trying out the available NoSQL technology. Pinterest mapped their data by primary key and used it to map data to the shard where it resided. Sharding in this way provided scale but traded off cross shard joins and the use of foreign keys.

Similarly, Etsy took this approach when moving to a sharded database system but added a two-way lookup primary key to the shard_id and packed shards onto hosts, automating some of the work of managing shards. In both cases, however, ongoing management of shards, including splitting shards after the initial resharding, presented significant challenges.

From experiences like these, there is an increasing need to separate sharding logic from the application as it introduces a plethora of complexity, making the application and your database harder to manage, which, in turn, drains developer capacity and pulls your team away from building and improving on great products for your customer base. Examples include shardingsphere and Vitess.

In contrast, server-side database sharding is a method of distributing data across multiple databases on the server side, meaning that the server infrastructure is responsible for directing queries to the appropriate database. Examples include Dynamo, Cassandra, CockroachDB.

## Benefits

### Simpler architecture

Sharding eliminates the complexities of inter-node communication and automatic data distribution, resulting in a simpler system to understand and manage.

### Independent scaling

Individual shards can be scaled independently, offering more granular control over resource allocation.

### Clear data ownership

Each shard has a well-defined responsibility for a specific subset of data, eliminating the ambiguity of ownership that can arise in clusters.

### Simplified algorithm

The logic for data placement is significantly simpler than complex cluster management algorithms, reducing the likelihood of catastrophic failures.

## Drawbacks

### No database-level joins

Since data is spread across multiple shards, performing joins across different shards becomes challenging. This is because the data has to be compiled from multiple servers, which can add significant overhead and negatively impact performance.

However, there are ways to mitigate this issue. Utilizing caching and fast networks can help to speed up the process and ensure that page load times remain fast. Additionally, de-normalizing the database by merging related data into a single table can also be a viable solution, as it allows for the execution of previously complex join queries on a single table.

### Referential integrity

Maintaining data integrity, such as using foreign keys, can be a challenge when using a sharded database. Most relational database management systems don’t support foreign keys across different servers, making it difficult to enforce referential integrity.

Applications that rely on this feature may need to implement it in their code and run regular SQL jobs to keep the data consistent. This can add extra complexity and maintenance to the application.

### No database-level transactions

Transactions spanning multiple shards are not possible, requiring application-level logic to maintain data consistency and integrity. Moreover, ACID properties don't hold across shards.

### Increased application complexity

Applications must handle shard routing and manage data consistency across shards, adding complexity to the development process.

### Schema changes are more involved

Modifying database schemas requires applying changes to all individual shards.

### Reporting complexity

Generating reports that span multiple shards requires retrieving data from each shard and aggregating the results manually.

### Rebalancing

As data grows or shrinks, shards may need to be rebalanced, which can be a complex and resource-intensive process.
