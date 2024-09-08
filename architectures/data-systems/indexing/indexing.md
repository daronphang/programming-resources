## Indexes

An index is a structure that holds the field the index is sorting and a pointer from each record to their corresponding record in the original table where the data is actually stored. Indexes are used to efficiently find the value for a particular key in the database. Without an index, query will have to read through the entire table to find the relevant rows.

General idea behind them is to keep some additional metadata on the side, which acts as a signpost and helps you locate the data you want. If you want to search the same data is different ways, may need several different indexes on different parts of the data.

Index causes the database to create a data structure (B-tree) that is sorted to make searches more efficient. Indexes can either store the rows or pointers to it.

An index is an additional structure that is derived from the primary data. Many databases allow you to add and remove indexes which does not affect the content but the query performance. However, this incurs additional overhead on writes as the index also needs to be updated every time data is written. This is an important tradeoff between query performance and write speed.

### Searching

After indexes are created, you can begin querying them. Indexes use an optimal search method known as **binary search**.

### When not to use Indexes

When data is written to the database, the original table (clustered index) is updated first, followed by all the secondary indexes of the table. Every time a write is made, the indexes are unusable until they have been updated.

For OLTP databases that is constantly receiving writes, indexes will never be usuable. Hence, they are typically applied to databases in data warehouses that get new data updated on a scheduled basis and not production databases.
