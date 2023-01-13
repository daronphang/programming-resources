## Request Routing

When a client makes a request, need to know which node to connect to. This is an instance of a general problem called 'service discovery', and isn't limited to databases, but any software that is accessible over the network and aiming for high availability.

Many companies have written their own in-house service discovery tools, some of which are open source. Few approaches are as follows:
1. Allow clients to contact any node via a round-robin load balancer. If that node doesn't own the partition, it forwards the request to the appropriate node, and passes the reply back to the client
2. Send all requests from clients to a routing tier (acts as a partition-aware load balancer), which determines the node that should handle each request and forwards it accordingly
3. Require that clients be aware of the partitioning and assignment of partitions to nodes

### Partition Changes

The key challenge is for the component making the routing decision to learn about changes in the assignment of partitions to nodes. Many distributed data systems rely on a separate coordination service such as **Zookeeper or Helix**, to keep track of the cluster metadata.

Zookeeper maintains the authoritative mapping of partitions to nodes. Other actos, such as the routing tier, can subscribe to this information in ZooKeeper.