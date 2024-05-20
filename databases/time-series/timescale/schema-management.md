## Indexing data

If you have a lot of data in your hypertable, you can use an index to speed up read operations from non-compressed chunks.

You can create an index on any combination of columns, **as long as you include the time column**. The columns that you choose to index depends on what kind of data you have stored. Moreover, when you create a hypertable, set the datatype for the time column as **timestamptz** and not **timestamp**.
