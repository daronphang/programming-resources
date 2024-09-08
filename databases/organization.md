## Organization

For relational databases, two ways to organize are **row oriented** and **column oriented (C-Store)**.

## Row oriented

Traditional way of organizing data in OLTP databases by keeping all of the data associated with a record next to each other. Optimized for reading and writing rows efficiently. Examples include MySQL and Postgres.

When writing, data is appended to the end. However, when performing aggregation, extra data columns are brought into memory before extracting relevant data which can hinder performance.

```
Matt | Los Angeles | 27 | Dave | San Francisco | 30 |
Matt | Los Angeles | 27 | Dave | San Francisco | 30 | Tim | Oakland | 33 |
```

## Column oriented

Data is organized by field i.e. data associated with a field are kept next to each other in memory. Optimized for reading and computing on columns efficiently. Examples include Redshift, BigQuery and Snowflake.

When writing a new record, have to navigate around the data to plug each column into where it should be. However, this has significant benefits when each column is stored on separate disks. Moreover, parsing aggregation would be more efficient as the CPU needs only to retrieve from one disk, and no extra memory is consumed.

```
Matt | Dave | 27 | 30 | Los Angeles | San Francisco |
Matt | Dave | Tim | 27 | 30 | 33 | Los Angeles | San Francisco | Oakland
```

### Column compression

Besides only loading those columns from disk that are required from query, can further reduce the demands on disk throughput by compressing data (for similar/repetitive). Technique that is effective in data warehouses is **bitmap encoding**.

### Memory bandwidth and vectorized processing

For data warehouse that need to scan over millions of rows, a big bottleneck is the bandwidth for getting data from disk into memory and CPU cache. C-Stores are good for making efficient use of CPU cycles.

Query engine can take a chunk of compressed column data that fits comfortably into the CPU's cache and iterate through it in a tight loop. CPU can execute a loop faster than code that requires function calls and conditions for each record to be processed.

### Sorting data

In a C-Store, it doesn't matter in which order the rows are stored. However, we can impose an order and use that as an indexing mechanism.

#### Different sort orders

Having multiple sort orders in C-Store is similar to having multiple secondary indexes in row-oriented store. This means the same data is stored in several different ways of sorting. Also, as data is replicated to multiple machines, you will not lose data if one machine fails i.e. more fault tolerant. However, this means there are more tables to update when writing.

```
Matt | Dave | Tim   # original
Dave | Matt | Tim   # asc
Tim | Matt | Dave   # desc
```
