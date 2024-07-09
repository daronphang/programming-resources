## Scatter/gather pattern

The scatter/gather pattern is a tree pattern with a root that distributes requests and leaves the processing to those requests. Requests are simultaneously farmed out to all replicas in the system. Each replica does a small amount of processing and then returns a fraction of the result to the root. The root server then combines the various partial results together to form a single complete response to the request.

Scatter/gather is quite useful when you have a large amount of mostly independent processing that is needed to handle a particular request. Scatter/gather can be seen as sharding the computation necessary to service the request, rather than sharding the data.

### Choosing the right number of leaves

It might seem that in the scatter/gather pattern, replicating out to a very large number of leaves would always be a good idea. You parallelize your computation and consequently reduce the clock time required to process any particular request. However, increased parallelization comes at a cost, and thus choosing the right number of leaf nodes in the scatter/gather pattern is critical to designing a performant distributed system.

Processing any particular request has a certain amount of overhead e.g. sending HTTP across the wire, time spent parsing a request, etc. However, the cost of this overhead scales with the number of leaf nodes.

In addition, scatter/gather problems suffer from the "strangler" problem. As the root node needs to wait for requests from all leaf nodes to return before sending a response, the overall time it needs to process a request is defined by the slowest leaf node.

```
99th percentile latency of 2 seconds, or 1% chance

For 5 nodes:
0.99 * 0.99 * 0.99 * 0.99 * 0.99 = 0.95
5% chance of having latency of 2 seconds
```

Together, these complications of scatter/gather pattern lead us to some conclusions:

- Increased parallelism does not always speed things up because of overhead on each node
- Increased parallelism doesn't always speed things up because of the straggler problem
- The performance of the 99th percentile is more important than in other systems as each request actually becomes numerous requests to the service
