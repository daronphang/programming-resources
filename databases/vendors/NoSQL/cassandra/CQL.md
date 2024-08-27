## Cassandra Query Language (CQL)

CQL offers a model similar to SQL. The data is stored in tables containing rows of columns.

## Keyspaces

CQL stores data in tables, whose schema defines the layout of the data in the table. Tables are located in keyspaces i.e. similar to SQL database. A keyspace defines options that apply to all the keyspace’s tables.

The replication strategy is an important keyspace option, as is the replication factor. A good general rule is one keyspace per application. It is common for a cluster to define only one keyspace for an entire application.

## Primary key

A primary key is composed of one or more of the defined columns in the table. It is composed of two parts:

- Partition key
- Clustering columns

If a row is inserted with the same primary key, an **upsert** occurs and the existing row is replaced.

```
PRIMARY KEY (a)
PRIMARY KEY (a, b, c)
PRIMARY KEY ((a, b), c)
```

### Partition key

The **partition key** is the first component of the primary key definition. It can be a single column or multiple columns (enclosed with parenthesis). It is used to define the location of data within a Cassandra cluster.

The most important property of partition is that all the rows belonging to the same partition are guaranteed to be stored on the same set of replica nodes. The localization of data is important to the efficient retrieval of data, requiring the Cassandra coordinator to contact as few nodes as possible. However, this may create a **hotspot** for both reading and writing.

the partition key must be specified in all queries of the table.

### Clustering key

**Clustering columns** are columns that follow the partition key in the primary key definition. All rows are ordered by that clustering order.

If a table has no clustering columns, then every partition of that table has a single row.

## Updates

In Cassandra, everything is append-only. Hence, an update is the same as insert.

## Querying

As Cassandra is a key-value store, you can only query a table by the columns defined in your primary key. The relationship for clustering columns must specify a contiguous set of rows to order.

```sql
CREATE TABLE posts (
    userid text,
    blog_title text,
    posted_at timestamp,
    entry_title text,
    content text,
    category int,
    PRIMARY KEY (userid, blog_title, posted_at)
);
```

```sql
-- Allowed
SELECT entry_title, content FROM posts
 WHERE userid = 'john doe'
   AND blog_title='John''s Blog'
   AND posted_at >= '2012-01-01' AND posted_at < '2012-01-31';

-- Not allowed
SELECT entry_title, content FROM posts
 WHERE userid = 'john doe'
   AND posted_at >= '2012-01-01' AND posted_at < '2012-01-31';
```

If you want to query columns other than the primary key, you need to create a **secondary index** on them.

### Non-partition key

Cassandra tries to avoid harmful queries. If you want to filter by a column that is not a partition key, you need to tell Cassandra explicitly that you want to filter by a non-partition key column.

```sql
CREATE TABLE users (
    username text PRIMARY KEY,
    firstname text,
    lastname text,
    birth_year int,
    country text
);

CREATE INDEX ON users(birth_year);
```

```sql
-- All users are returned
SELECT * FROM users;

-- All users with a particular birth year are returned
SELECT * FROM users WHERE birth_year = 1981;

-- Rejected
SELECT * FROM users WHERE birth_year = 1981 AND country = 'FR';

-- Allowed
SELECT * FROM users WHERE birth_year = 1981 AND country = 'FR' ALLOW FILTERING;
```

The ALLOW FILTERING option explicitly executes a full scan. Thus, the performance of the query can be unpredictable. Without ALLOW FILTERING, the query would not be executed to prevent harm to the cluster by accidentally running expensive queries.

### Datetime of write

A table contains a timestamp representing the date/time that a write occurred to a column. Use WRITETIME in a SELECT statement to return the date/time in microseconds.

```sql
SELECT WRITETIME (name) FROM excelsior.clicks
  WHERE url = 'http://apache.org' ALLOW FILTERING;
```

Otherwise, can use toTimestamp(now()).

## Insert

Unlike in SQL, INSERT does not check the prior existence of the row by default. The row is created if none existed before, and updated otherwise. Furthermore, there is no means of knowing which action occurred.

```sql
INSERT INTO NerdMovies (movie, director, main_actor, year)
   VALUES ('Serenity', 'Joss Whedon', 'Nathan Fillion', 2005)
   USING TTL 86400;

INSERT INTO NerdMovies JSON '{"movie": "Serenity", "director": "Joss Whedon", "year": 2005}';
```

## Update

You can expect Cassandra performance to degrade over time if your model requires you to update the same row over and over. This is due to the fact that the same row spans over dozen of SSTables.

## Tombstones

Cassandra is a multi-node cluster that contains replicated data on different nodes. Therefore, a delete can not simply delete a particular record.

For a delete operation, a new entry is added to the commit-log like for any other insert and update mutation. **These deletes are called tombstones**, and they flag a specific value for deletion.

By default, after 10 days, data that is marked by a tombstone is freed with a compaction execution. This time can be configured and reduced using the gc_grace_seconds option in the Cassandra configuration.

### TTL

You can set a time to live on inserted data. After the time passed, the record will be automatically deleted. When you set a time to live (TTL), a tombstone is created with a date in the future.

### tombstone_failure_threshold

If you have many tombstones, you might run into an issue that prevents a query from being executed.

This happens when the tombstone_failure_threshold is reached, which is set by default to 100,000 tombstones. This means that, when a query has iterated over more than 100,000 tombstones, it will be aborted.

## Batch

Multiple INSERT, UPDATE and DELETE can be executed in a single statement by grouping them through a BATCH statement. It serves several purposes:

- It saves network round-trips between the client and the server (and sometimes between the server coordinator and the replicas) when batching multiple updates
- All updates in a BATCH belonging to a given partition key are performed in isolation
- By default, all operations in the batch are performed as logged, to ensure all mutations eventually complete (or none will)

```sql
BEGIN BATCH
   INSERT INTO users (userid, password, name) VALUES ('user2', 'ch@ngem3b', 'second user');
   UPDATE users SET password = 'ps22dhds' WHERE userid = 'user3';
   INSERT INTO users (userid, password) VALUES ('user4', 'ch@ngem3c');
   DELETE name FROM users WHERE userid = 'user1';
APPLY BATCH;
```

### Unlogged batches

By default, Cassandra uses a batch log to ensure all operations in a batch eventually complete or none will (note however that operations are only isolated within a single partition).

There is a performance penalty for batch atomicity when a batch spans multiple partitions. If you do not want to incur this penalty, you can tell Cassandra to skip the batchlog with the UNLOGGED option. If the UNLOGGED option is used, a failed batch might leave the patch only partly applied.

## Nullable columns

Inserting a null value creates a tombstone; this should be avoided:

- Tombstone takes up space
- Querying tables with a large number of tombstones cause performance problems

Nonetheless, Cassandra's storage engine has the ability to not store values. Hence, for columns that are null, skip those columns when performing inserts.

```sql
-- Avoid!
INSERT INTO mytable (v1,v2,v3) VALUES ("hello", null, null);

-- ok
INSERT INTO mytable (v1) VALUES ("hello");
```
