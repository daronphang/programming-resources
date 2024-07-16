## Partitioning

While partitioning is just a general term referring to splitting up the database, it is commonly used to mean **vertical partitioning**, which is the process of dividing tables in a database instance into smaller sub-tables or partitions. This division occurs within a single database system, eliminating the need for distribution across multiple servers.

By splitting a large table into smaller, individual tables, queries that access only a fraction of the data can run faster because there is **less data to scan**. These partitions can be accessed and managed separately to enhance performance, maintainability, and availability of the database.

```sql
-- vertical partitioning

create table data (
    id integer primary key,
    status char(1) not null,
    data1 varchar2(10) not null,
    data2 varchar2(10) not null
);

create table data_main (
    id integer primary key,
    status char(1) not null,
    data1 varchar2(10) not null
);

create table data_rarely_used (
    id integer primary key,
    data2 varchar2(10) not null,
    foreign key (id) references data_main (id)
);
```

```sql
-- horizontal partitioning
CREATE TABLE sales (
    sale_id INT NOT NULL,
    product_name VARCHAR(255) NOT NULL,
    sale_date DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL
) PARTITION BY RANGE (YEAR(sale_date)) (
    PARTITION p2018 VALUES LESS THAN (2019),
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022)
);
```

## Benefits

### Improved query performance

By segregating data into partitions, databases can achieve enhanced query performance. Partitioning allows for more efficient data access and manipulation, ensuring that operations are executed on relevant subsets of data, thereby reducing processing time and improving overall system responsiveness.

### Ease of maintenance

Partitioning simplifies maintenance tasks by allowing operations such as backups, data purges, or schema changes to be performed more efficiently and with less impact on the overall database availability. This segmentation means that maintenance can be limited to only the relevant partitions without affecting the rest of the database.

## Drawbacks

### Complexity in data management

While partitioning simplifies maintenance in certain aspects, it can introduce complexity in data management. Designing and implementing a partitioning scheme requires upfront planning and a deep understanding of the data’s access patterns. Incorrect partitioning strategies can lead to data skew, where one partition is significantly larger than others, negatively impacting performance.

### Query performance overhead

If queries are not well-aligned with the partitioning key, there could be a performance penalty. Specifically, queries that need to access multiple partitions or that do not make use of the partition key in their predicates might perform worse than those running on a non-partitioned dataset.

## Hot partition/shard

A “hot partition or shard refers to a specific partition within a distributed data storage system or database that is experiencing a disproportionately high level of data traffic or activity compared to other shards or partitions i.e. a bottleneck. This imbalance can lead to performance degradation for the entire system.

Causes include:

- Uneven data distribution
- Popular data that are frequently accessed
- Inefficient queries

## Partitioning and replication

Partitioning is usually combined with replication, so that copies of each partition are stored on multiple nodes i.e. each record belongs to one partition, but stored on several nodes for fault tolerance.

A node may store more than one partition. If a leader-follower replication is used, each partition's leader will be assigned to one node, and its followers are assigned to other nodes.

```
Node A
Partition 1 (leader)
Partition 2 (follower)
Partition 3 (follower)

Node B
Partition 1 (follower)
Partition 2 (leader)
Partition 3 (follower)

Node C
Partition 1 (follower)
Partition 2 (follower)
Partition 3 (leader)
```
