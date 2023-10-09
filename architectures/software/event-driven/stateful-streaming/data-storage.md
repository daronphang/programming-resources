# Internal State Store

## Advantages

### Scalability requirements are offloaded from the developer

A major benefit of using internal state stores on local disk is that all scalability requirements are fully offloaded to the event broker and compute resource clusters. This approach ensures a single unit of scalability, where each application can be scaled simply by increasing and decreasing the instance count. 

### High-performance disk-based options

Maintaining all state within main memory is not always possible; nonetheless, local disk implementations can be quite performant for the majority of microservice use cases. Norm for SSD is 15.4k requests/second, while in-memory can serve millions of requests per second.

### Flexibility to use network-attached disk

Microservices may also use network-attached disk instead of local disk, which significantly increases the read/write latency. As events typically must be processed one at a time to maintain temporal and offset order, the single processing thread will spend a lot of time awaiting read/write responses, resulting in significantly lower throughput per processor.

However, accessing network-attached disk has a much higher latency than physical local disk, and this can significantly reduce throughput cap.

One major benefit of network-attached disk is that the state can be maintainede in the volume and migrated to new processing hardware as needed. When the processing node is brought back up, the network disk can be reattached and processing can resume where it left off, instead of being rebuilt from the changelog stream.

## Drawbacks

### Limited to using runtime-defined disk

Internal state stores are limited to using only disk that is defined and attached to the node at the service's runtime. Changing either the size or quantity of attached volumes typically requires that the service be halted.

### Wasted disk space

Data patterns are cyclical in nature, such as the traffic generated to a shopping website at 3pm versus 3am.

## Scaling and Recovery

The new or recovered instance needs to materialize any state defined by its topology first before it can begin processing new events.

### Using hot replicas

Most common to have a single replica of materialized state for each partition i.e. leader and replica. Each replica must manage its own offsets to ensure that it is keeping up with the offsets of the leader replica.

### Using changelogs

When a newly created microservice instance joins the consumer group, any stateful partitions that it is assigned can be reloaded simply by consuming from its changelog. 

# External State Store

External state stores exist outside of the microservice's container or VM, but are typically located within the same local network. Examples include relational databases, document databases, etc.

It is important to keep data set logically isolated from all other microservice implementations although they may share the same data storage platform. This can lead to tight coupling and should be avoided.

## Advantages

### Full data locality

External state stores can provide access to all materialized data for each microservice instance, though each instance is still responsible for materializing its own assigned partitions.

### Technology

External data stores can leverage technology that the organization is already familiar with, reducing the time and effort it takes to deliver a microservice to production.

## Drawbacks

### Management of multiple technologies

External state stores are managed and scaled independently of the microservice business logic solution. Each team must ensure that their data service is suitable and resilient for the microservice's load. 

### Performance loss due to network latency

While caching and paralleization can reduce the impact of the network latency, the tradeoff is often added complexity and an increased cost for additional memory and CPU.

## Scaling and Recovery

For external state stores, scaling and recovery simply require that you add a new instance with the necessary credentials to access the state store.

