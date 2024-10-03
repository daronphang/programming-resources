## Clustering

Database clustering is the process of connecting more than one single database instance or server to your system. In most common database clusters, multiple database instances are usually managed by a single database server called the master.

Clustering involves having a group of servers in master-master replication. With clustering, **each of the server can accept write requests**, and they all will have the data.

Clustering takes out the single point of failure that is having just one (write) server. As writes must be coordinated (a write transaction is finished when all or enough servers in the cluster did it), it can have the slowest writes of all.

### How clustering works

1. A new piece of data arrives
2. The clustering algorithm determines the optimal node for this data
3. Data is replicated across multiple nodes for redundancy
4. If a node fails, other nodes take over, ensuring data availability

## Benefits

### Automatic scaling

Adding new nodes automatically expands capacity.

### Ease of setup

The clustering technology manages data placement and distribution, simplifying initial setup.

### Geographical data distribution

Clusters can be spread across different geographical locations, improving data locality and resilience to datacenter outages.

### High availability

Data replication and automatic failover ensure continuous operation even when individual nodes fail.

### Load balancing

The workload is distributed across nodes, preventing any single node from becoming overwhelmed.

## Drawbacks

### Complexity

Clustering introduces complex interactions between nodes, making troubleshooting and maintenance more difficult.

### Upgrading challenges

Upgrading a cluster can be complicated due to the need for coordinated changes across multiple nodes

### Single point of failure

The cluster management algorithm, responsible for coordinating activities, can become a single point of failure. Issues with this algorithm can impact the entire cluster.
