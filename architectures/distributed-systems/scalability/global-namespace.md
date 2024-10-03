## Global partitioned namespace

Key goals of storage system is to provide a single global namespace that allows clients to address all of their storage in the cloud and scale to arbitrary amounts of storage needed over time. This capability can be provided by leveraging **DNS** as part of the storage namespace and breaking the storage namespace into three parts:

- **Account**: Customer account used to locate the primary storage cluster of where the data is stored
- **Partition**: Used to scale out access to data across storage nodes; atomic transactions with the same partition name is provided
- **Object**: Identifies individual objects within a partition
