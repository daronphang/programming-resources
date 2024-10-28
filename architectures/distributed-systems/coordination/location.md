## Location systems

When looking at large distributed systems that are dispersed across a wide- area network, it is often necessary to take proximity into account. If two processes that are in the same overlay network communicate a lot, it would be better to ensure that they are also physically placed in each other’s proximity.

### GPS

The positioning problem can be solved through GPS. However, a major drawback is that GPS generally cannot be used indoors. Also, the exact position will not be very accurate, due to many sources of errors e.g. atomic clocks in satellites, signal propagation speed, etc.

### Logical positioning of nodes

Instead of trying to find the absolute location of a node in a distributed system, an alternative is to use a logical, proximity-based location.

In **geometric overlay networks** each node is given a position in an m-dimensional geometric space, such that the distance between two nodes in that space reflects a real-world performance metric.

An example application of geometric overlay networks is CDN. When a client C requests for content, the CDN may decide to redirect that request to the server closest to C (best response time). If the geometric location of C is known, as well as those of each replica server, the CDN can then simply pick that server Si for which d(C,Si) is **minimal**.

Another example is optimal replica placement. If the CDN were to replicate content to N servers, it can compute the N best positions where to place replicas such that the average client-to-replica response time is minimal. Performing such computations is almost trivially feasible if clients and servers have geometric positions that reflect internode latencies.
