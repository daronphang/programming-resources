## Bigtable

Bigtable is a distributed storage system for managing structured data that is designed to scale to a very large size e.g. low-latency NoSQL database service. Bigtable has achieved several goals: wide applicability, scalability, high performance, and high availability. Bigtable is used by more than sixty Google products and projects e.g. Google Analytics, Google Finance, Google Earth, etc.

## Data model

Bigtable resembles a database: it shares many implementation strategies with databases. However, Bigtable does not support a full relational data model.Instead, it provides clients with a simple data model that supports **dynamic control over data layout and format**, and allows clients to reason about the locality properties of the data represented in the underlying storage.

A Bigtable is a sparse, distributed, persistent multi-dimensional **sorted map**. The map is indexed by a row key, column key, and a timestamp; each value can be an arbitrary string. Bigtable also treats data as uninterpreted strings, although clients often serialize various forms of structured and semi-structured data into these strings.

```
(row:string, column:string, time:int64) → string
```

### Rows

Bigtable maintains data in lexicographic order by row key. The row range for a table is dynamically partitioned. Each row range is called a **tablet**, which is the unit of distribution and load balancing.

Reads of short row ranges are efficient and typically require communication with only a small number of machines. Clients can exploit this property by selecting their row keys so that they get good locality for their data accesses.

### Column families

Column keys are grouped into sets called column families i.e. related columns are grouped together to avoid needing to design complex filters. Column families form the basic unit of access control. All data stored in a column family is usually of the same type, and are compressed together.

A column family must be created before data can be stored under any column key in that family; after a family has been created, any column key within the family can be used.

Access control and both disk and memory accounting are performed at the column-family level.

### Schema design

- Bigtable is a key/value store, not a relational store. Hence, it does not support joins and transactions across multiple rows
- Each table has only one index, the row key
- Rows are sorted lexicographically by row key
- Column families are not stored in any specific order
- Columns are grouped by column family and sorted in lexicographic order within the column family
- The intersection of a row and column can contain multiple timestamped cells
- All operations are atomic at the row level

## Implementation

Each tablet server manages a set of tablets, between ten to a thousand tablets. The tablet server handles read and write requests to the tablets that it has loaded, and also splits tablets that have grown too large.

As with many single-master distributed storage systems, client data does not move through the master: **clients communicate directly with tablet servers for reads and writes**. As Bigtable clients do not rely on the master for tablet location information, most clients never communicate with the master. As a result, the master is lightly loaded in practice.

A Bigtable cluster stores a number of tables. Each table consists of a set of tablets, and each tablet contains all data associated with a row range. Initially, each table consists of just one tablet. As a table grows, it is automatically split into multiple tablets.

### Tablet location

A three-level hierarchy analogous to that of a B+ tree is used to store tablet location information:

- **First level**: File stored in Chubby that contains the location of the root tablet. The root tablet contains the location of all tablets in a special METADATA table
- **Second level**: METADATA table stores the location of a tablet under a row key that is an encoding of the tablet’s table identifier and its end row
- **Third level**: User table that stores data for clients

The client library caches tablet locations. If the client does not know the location of a tablet, or if it discovers that cached location information is incorrect, then it recursively moves up the tablet location hierarchy. If the client’s cache is stale, the location algorithm could take up to six round-trips, because stale cache entries are only discovered upon misses.

### Tablet assignment

Each tablet is assigned to one tablet server at a time. The master is responsible for assigning tablets to tablet servers, detecting the addition and expiration of tablet servers, balancing tablet-server load, and garbage collection of files in GFS. In addition, it handles schema changes such as table and column family creations.

Bigtable uses Chubby to keep track of tablet servers:

1. When a tablet server starts, it creates, and acquires an exclusive lock on, a uniquely-named file in a specific Chubby directory
2. The master monitors this directory to discover tablet servers
3. A tablet server stops serving its tablets if it loses its exclusive lock
4. If the file no longer exists, then the tablet server will never be able to serve again, so it kills itself

Tablet discovery and assignment is performed as follows:

1. The master acquires a unique master lock in Chubby
2. The master scans the servers directory in Chubby to find the live servers
3. The master communicates with every live tablet to discover what tablets are already assigned to each server
4. The master scans the METADATA table to learn the set of tablets
5. Whenever this scan encounters a tablet that is not already assigned, the master adds the tablet to the set of unassigned tablets, which makes the tablet eligible for tablet assignment
