## Writing Software for Managed Compute

The move from a world of hand-managed lists of machines to the automated scheduling and rightsizing made management of the fleet took profound changes to the way we write and think about software.

### Architecting for Failure

#### Pet vs Cattle

If your server is a pet, when it is broken a human comes to look at it, understand what went wrong, and hopefully nurse it back to health. If your servers are cattle and if one fails, automation will remove it and provision a new one in its place. This allows for the self-healing property without human intervention.

If your servers are pets, your maintenance burden will grow linearly. If your servers are cattle, your system will be able to return to a stable state after a failure.

#### Sharding

Having your containers be cattle is not enough to guarantee that your system will behave well in the face of failure. When your work is shard across multiple machines, it is very likely that one of the machine will be killed, and more than once.

To deal with this gracefully, the architecture of the processing needs to be different: instead of statically assigning the work, we instead divide the entire set of workload into chunks i.e. for one million documents, divide into 1000 chunks of 1000 documents each.

Whenever a worker is finished with a chunk, it reports the results, and picks up another. **Work is not assigned equally to the set of workers at the start of computation**; it is **dynamically assigned** during the overall processing in order to account for workers that fail.

### Batch vs Serving

Batch jobs are programs that are expected to complete some specific task (i.e. data processing) and that run to completion. Canonical examples include log analysis or machine learning. In constrast, serving jobs are programs that are expected to run indefinitely and serve incoming requests.

Both jobs have typically different characteristics:

- Batch jobs are primarily interested in throughput of processing while serving jobs care about the latency of serving a single request
- Batch jobs are short lived while serving jobs are long lived (longer startup times)

Serving jobs are more naturally suited to failure resistance than batch jobs. Their work is naturally chunked into small pieces (individual user requests) that are assigned dynamically to workers.

### Managing State

When treating your jobs like cattle, whenever you replace them, you lose all the in-process state and local storage. This means that the **in-process state should be treated as transient/ephemeral**, whereas 'real storage' needs to occur elsewhere in some persistent and durable storage. Similarly, these durable, persistent storage should be implemented as cattle, and this could be done through **state replication**.

For local storage, types that cattle can use covers 're-creatable' data that is held locally to improve serving latency. **Caching** is an obvious example, which allows for better performance characteristics on average.

Another case of using local storage is **batching writes**. This is a common strategy for monitoring data i.e. gathering CPU utilization statistics. Nonetheless, it can be used anywhere where it is acceptable for a fraction of data to perish, either because we do not need 100% data coverage, or because the data that perishes can be re-created.

In many cases, even if a particular calculation has to take a long time, it can be split into smaller time windows by **periodic checkpointing of state to persistent storage**.

### Connecing to a Service

If anything in the system has the name of the host on which your program runs hardcoded or as a configuration parameter, your program replicas are not cattle. **Avoid hardcoding hostnames**.

This can be resolved by having an extra layer of indirection i.e. other applications refer to your application by some identifier that is durable across restarts of the specific 'backend' instances. That identifier can be resolved by another system that the scheduler writes to when it places your application on a particular machine.

For network issues, **retrying** is the standard practice, but it might be less intuitive for things like a server communicating with its database. For mutating requests, the property that you want to guarantee is some variant of **idempotency**.
