## Cassandra

Apache Cassandra is an open source, distributed, NoSQL database. It presents a partitioned wide column storage model with eventually consistent semantics.

Cassandra is a decentralized multi-node database that physically spans separate locations and uses replication and partitioning to infinitely scale reads and writes.

Systems like Cassandra are designed for these challenges and seek the following design objectives:

- Full multi-master database replication
- Global availability at low latency
- Scaling out on commodity hardware
- Linear throughput increase with each additional processor
- Online load balancing and cluster growth
- Partitioned key-oriented queries
- Flexible schema

### Decentralization

Cassandra is decentralized because no node is superior to other nodes, and every node acts in different roles as needed without any central controller.

### Every node is a coordinator

The coordinator is responsible for request batching, repairing data, or retries for reads and writes.

Data is replicated to different nodes. If certain data is requested, a request can be processed from any node.

This initial request receiver becomes the coordinator node for that request. If other nodes need to be checked to ensure consistency then the coordinator requests the required data from replica nodes.

The coordinator calculates which nodes contains the data using **consistent hashing algorithm**.
