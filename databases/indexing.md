## Indexes

Indexes are used to efficiently find the value for a particular key in the database. Without an index, query will have to read through the entire table to find the relevant rows.

General idea behind them is to keep some additional metadata on the side, which acts as a signpost and helps you locate the data you want. If you want to search the same data is different ways, may need several different indexes on different parts of the data.

Index causes the database to create a data structure (B-tree) that is sorted to make searches more efficient. Indexes can either store the rows or pointers to it.

An index is an additional structure that is derived from the primary data. Many databases allow you to add and remove indexes which does not affect the content but the query performance. However, this incurs additional overhead on writes as the index also needs to be updated every time data is written. This is an important tradeoff between query performance and write speed.

## Hash Indexes (Log-Structured)

Similar to dictionary which is implemented as a hash map. Every append to the storage file will update the hash map to reflect the offset of the data you wrote. When updating a key, it will append to files and delete obsolete files but never modify them in place.

To ensure disk space doesn't run out, a solution would be to break the log into segments (log-structured) of a certain size by closing it once it reaches, and making subsequent writes to a new segment file.

## B-Trees

They remain the standard index implementation in almost all relational databases, and many non-relational use them too. B-trees keep key-value pairs sorted by key, which allows efficient key-value lookups and range queries.

B-trees break the database down into fixed-size blocks/pages, and read/write one page at a time. This design corresponds more closely to the underlying hardware, as disks are also arranged in fixed-size blocks.

Each page can be identified using an address or location, which allows one page to refer to another i.e. a pointer, but on disk instead of in-memory. Individual keys are also called **leaf page**, which contains the value for key inline. The number of references to child pages in one page is called the **branching factor**.

### Reliability

To make the database resilient to crashes, it is common for B-tree implementations to include an additional data structure on disk known as **write-ahead log**. This an append-only file to which every modification must be written before it can be applied to the pages of the tree itself. This log is used to restore the B-tree back to a consistent state. However, this means every data must be written at least twice: once to the B-tree and write-ahead log.

## Secondary Indexes

Secondary indexes are common and are often crucial for performing joins efficiently. Can be easily constructed from a key-value index; however, the keys are not unique.

The key in an index could either store the actual row or reference to the row stored elsewhere. For the latter, the place where rows are stored is known as a **heap file**, and it stores data in no particular order.

### Clustered Index

In MySQL, the primary key of a table is always a clustered index, and secondary indexes refer to the primary key. A clustered index stores the indexed row directly within an index, and does not use heap files as the extra hop from the index to the file can be too much of a performance penalty for reads i.e. all row data is stored within the index.

### Nonclustered Index

Have a structure separate from the data rows. A nonclustered index contains the nonclustered index key values and each key value has a pointer to the data row.

### Multi-dimensional Indexes

When querying multiple columns of a table simultaneously, single key-value pair would not be sufficient. **The most common type is multi-column/concatenated index**, which combines several fields into one key by appending one column to another.

When querying several columns at once, a standard B-tree is not able to answer the query efficiently i.e. gives all the data in the range of first column and all of second column. One option is to translate a two-dimensional query into a single number using a space-filling curve, and then use a regular B-tree index. This is also known as R-trees which is implemented in Postgres.

```sql
SELECT * FROM restaurants WHERE
latitude > 51 AND latitude < 52 AND
longitude > 0 AND longitude < 2
```
