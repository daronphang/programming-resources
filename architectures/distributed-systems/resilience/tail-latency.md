## Causes of high-latency episodes

Variability of response time that leads to high tail latency in individual components of a service can arise for many reasons including hardware trends:

- **Shared resources**: Different applications contending for shared resources e.g. CPU cores, processor caches, memory bandwidth, network bandwidth, etc.
- **Background daemons**: Though they may use limited resources, they can generate multi-millisecond hiccups when scheduled
- **Maintenance activities**: Data reconstruction in distributed file systems, garbage collection, etc.
- **Queuing**: Multiple layers of queuing in intermediate servers and network switches amplify this variability
- **Energy management**: Power-saving modes save considerable energy but add additional latency when moving from inactive to active modes

Rare performance hiccups can affect a significant portion of all requests in large-scale distributed systems. Nonetheless, eliminating all sources of latency variability is impractical. Using an approach analogous to fault-tolerant computing form a predictable whole out of less-predictable parts.

## Reducing variability in service responsiveness

### Parallelize requests

A common technique for reducing latency in large-scale online services is to parallelize sub-operations across many different machines, where each sub-operation is co-located with its portion of a large dataset.

Parallelization happens by fanning out a request from a root to a large number of leaf servers, and merging responses via a request-distribution tree.

However, variability in latency distribution is magnified at the service level: if a typical response time is 10ms but with a 99th-percentile latency of 1s, one user request in 100 will be slow. If 100 servers are required, 63% of user requests will take more than one second.

### Differentiating service classes and higher-level queuing

Differentiated service classes can be used to prefer scheduling requests for which a user is waiting over non-interactive requests.

Low-level queues can be kept short so higher-level policies take effect more quickly. Queues allow servers to issue incoming high-priority interactive requests before older requests for latency-insensitive batch operations are served.

### Reducing head-of-line blocking

It is sometimes useful for the system to **break long-running requests into a sequence of smaller requests to allow interleaving of the execution of other short-running requests**.

### Managing background activities and synchronized disruption

Background tasks can create significant CPU, disk, or network load; examples are log compaction in log-oriented storage systems and garbage-collector activity in garbage-collected languages.

A combination of throttling, breaking down heavyweight operations into smaller operations, and triggering such operations at times of lower overall load is often able to reduce the effect of background activities on interactive request latency.

For large fan-out services, it is sometimes useful to **synchronize** background activity across many different machines. This synchronization enforces a brief burst of activity on each machine simultaneously, slowing only those interactive requests during the brief period of background activity. In contrast, without synchronization, a few machines are always doing some background task, pushing out the latency tail on all requests.

### Caching

**Caching do not directly address tail latency**, aside from configurations where it is guaranteed that the entire working set of an application can reside in a cache.

## Tail-tolerant techniques

The scale and complexity of modern web services makes it impossible to eliminate all latency variability, even if such perfect behavior could be achieved. Hence, it is advantageous to develop tail-tolerant techniques that mask temporary latency pathologies, instead of eliminating them together.

Although approaches that address particular sources of latency variability are useful, the most powerful tail-tolerant techniques reduce latency hiccups **regardless of root cause**.

### Hedged requests with replication

A simple way to curb latency variability is to issue the same request to multiple replicas and use the results from whichever replica responds first. The client then cancels remaining outstanding requests once the first result is received.

Although naive implementations of this technique typically add unacceptable additional load, many variations exist that give most of the latency-reduction effects while increasing load only modestly.

#### Deferment

One approach is to **defer** sending a secondary request until the first request has been outstanding for more than the 95th-percentile expected latency. The overhead of hedged requests can be further reduced by **tagging them as lower priority** than primary requests.

#### Tied requests

The hedged request approach limits the benefits to only a small fraction of requests. Permitting **more aggressive** use of hedged requests with moderate resource consumption requires faster cancellation of requests.

A common source of variability is queueing delays on the server before a request begins execution. Allowing a client to **enqueue copies of a request in multiple servers simultaneously** and allowing servers to communicate updates on the status of these copies to each other can prove to be effective.

Requests where servers perform cross-server updates are called **tied requests**. The simplest form is having the client send the request to two different servers, each tagged with the identity of the other server. When a request begins execution, it sends a cancellation request to its counterpart.

Due to network delays, there is a brief window where both servers may start executing while the cancellation messages are both in flight to the other server i.e. when both queues are empty. Hence, it is useful to introduce a small delay of two times the average network message delay of `2 * 1ms` before sending the second request.

#### Probing remote queues

An alternative to tied requests is to probe remote queues first, then submit the request to the least-loaded server. However, it is less effective than submitting work to two queues simultaneously:

- Load levels can change between probe and request time
- Request service times can be difficult to estimate due to underlying system and hardware variability
- Clients can create temporary hot spots by all clients picking the same least-loaded server at the same time

### Micro-partitioning

For reducing latency variability caused by coarser-grained phenomena, many systems try to partition data, with a single partition to each machine. However, in practice, this is rarely sufficient:

- Performance of underlying machines is neither uniform nor constant over time
- Outliers can cause data-induced load imbalance i.e. hot partition

To combat imbalance, micro-partitions can be created i.e. creating many more partitions than there are machines in the service. Failure-recovery speed is also improved through micro-partitioning, since many machines pick up one unit of work when a machine failure occurs. This is similar to vnodes in consistent hashing.

### Selective replication

An enhancement of the micro-partitioning scheme is to detect or even predict certain items that are likely to cause load imbalance and create additional replicas of these items. Load-balancing systems can then use the additional replicas to spread the load of these hot micro-partitions across multiple machines without having to actually move micro-partitions.

### Latency-induced probation

By observing the latency distribution of responses from the various machines in the system, intermediate servers sometimes detect situations where the system performs better by **excluding a particularly slow machine**, or putting it on **probation**.

The source of the slowness is frequently temporary phenomena like interference from unrelated networking traffic or a spike in CPU activity for another job on the machine, and the slowness tends to be noticed when the system is under greater load.

## Mutations

Tolerating latency variability for operations that mutate state is somewhat easier for a number of reasons:

- Scale of latency-critical modifications is generally small
- Updates can often be performed off the critical path i.e. asynchronous
- Many services can be structured to tolerate inconsistent update models
- Services that require consistent updates are inherently tail-tolerant as they commit when they have the majority of votes e.g. Paxos, Raft
