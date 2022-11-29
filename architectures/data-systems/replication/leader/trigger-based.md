## Trigger-Based Replication

Sometimes may need more flexibility in terms of replication i.e. replicating a subset of data, and requires moving replication up from the database system to the application layer. This can be done through **triggers and stored procedures**.

A trigger lets you register custom application code that is automatically executed when a data change (write transaction) occurs in a database system. Hence, it has the opportunity to log this change into a separate table, from which it can be read by an external process.

However, it has greater overheads than other replication methods and is more prone to bugs and limitations, but it can be useful due to its flexibility.
