## Clustered Index

Clustered indexes are the unique index per table that uses the primary key to organize the data that is within the table. The clustered index ensures that the primary key is stored in increasing order, which is also the order the table holds in memory.

A clustered index stores the indexed row directly within an index, and does not use heap files as the extra hop from the index to the file can be too much of a performance penalty for reads i.e. all row data is stored within the index.

### MySQL

In MySQL, the primary key of a table is always a clustered index, and secondary indexes refer to the primary key.

## Nonclustered Index (Secondary Indexes)

Non-clustered indexes are sorted references for a specific field, from the main table, that hold pointers back to the original entries of the table. A non-clustered index is an index that refers to another data structure containing further table columns.

Non-clustered indexes point to memory addresses instead of storing data themselves. This makes them slower to query than clustered indexes but typically much faster than a non-indexed column.

Secondary indexes are common and are often crucial for performing joins efficiently. Can be easily constructed from a key-value index; however, the keys are not unique.

The key in an index could either store the actual row or reference to the row stored elsewhere. For the latter, the place where rows are stored is known as a **heap file**, and it stores data in no particular order.

## Multi-dimensional Indexes

When querying multiple columns of a table simultaneously, single key-value pair would not be sufficient. **The most common type is multi-column/concatenated index**, which combines several fields into one key by appending one column to another.

When querying several columns at once, a standard B-tree is not able to answer the query efficiently i.e. gives all the data in the range of first column and all of second column. One option is to translate a two-dimensional query into a single number using a space-filling curve, and then use a regular B-tree index. This is also known as R-trees which is implemented in Postgres.

```sql
SELECT * FROM restaurants WHERE
latitude > 51 AND latitude < 52 AND
longitude > 0 AND longitude < 2
```
