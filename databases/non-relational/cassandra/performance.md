## Optimizing data storage for reading and writing

Writes are cheaper than reads in Cassandra due to its storage engine. Writing data means simply appending data to a commit-log.

Reading is more expensive, because it might require checking different disk locations until all the query data is eventually found.

### Compaction

The foundation for storing data are the **SSTables**. SSTables are immutable data files Cassandra uses to persist data on disk.

You can set various strategies for a table that define how data should be merged and compacted. These strategies affect read and write performance:

- **SizeTieredCompactionStrategy**: Default, performant if you have more writes than reads
- **LeveledCompactionStrategy**: Optimizes for reads over writes but can be costly
- **TimeWindowCompactionStrategy**: Optimized for time-series data

```sql
CREATE TABLE learn_cassandra.users_by_country_with_leveled_compaction (
    country text,
    user_email text,
    age smallint,
    first_name text,
    last_name text,
    PRIMARY KEY (country, user_email)
) WITH CLUSTERING ORDER BY (user_email ASC)
    AND bloom_filter_fp_chance = 0.1
    AND caching = {'keys': 'ALL', 'rows_per_partition': 'NONE'}
    AND comment = ''
    AND compaction = {'class': 'org.apache.cassandra.db.compaction.LeveledCompactionStrategy'}
    AND compression = {'chunk_length_in_kb': '64', 'class': 'org.apache.cassandra.io.compress.LZ4Compressor'}
    AND crc_check_chance = 1.0
    AND dclocal_read_repair_chance = 0.1
    AND default_time_to_live = 0
    AND gc_grace_seconds = 864000
    AND max_index_interval = 2048
    AND memtable_flush_period_in_ms = 0
    AND min_index_interval = 128
    AND read_repair_chance = 0.0
    AND speculative_retry = '99PERCENTILE';
```

## Indexing

There are index-like features in Cassandra that can reduce the number of tables you need to maintain on your own. One feature is called secondary indexes.

Secondary indexes only operate locally to a node. Using it means talking to all nodes because the coordinator doesn’t know which nodes contain the data if you use other columns to query data than the actual partition key.
