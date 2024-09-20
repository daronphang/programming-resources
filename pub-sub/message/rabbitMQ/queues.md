## Scaling queues

Queue processes reside on single nodes and hence, adding more nodes gives you more room to host the queue processes. However, all the routing information (queue, exchange, binding records) is stored in memory on each node. Having a significant number of binding records is unlikely to fit into physical memory.
