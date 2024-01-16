## Heavyweight Frameworks

Heavyweight/streaming frameworks provide mechanisms and APIs for handling streams of data, and are often used for consuming and producing events to an event broker.

### Characteristics

#### Cluster of resources

Requires an independent cluster of processing resources to perform its operations. Cluster typically constitutes a number of shareable worker nodes, along with master nodes that schedule and coordinate work. Leading Apache solutions traditionally rely on **Apache Zookeeper**, another clustered service, to provide high-availability support and coordinate cluster leader elections.

#### Internal mechanisms

Uses its own internal mechanisms for handling failures, recovery, resource allocation, task distribution, data storage, communication and coordination between processing instances and tasks.

### Examples

Apache Spark, Apache Flink, Apache Storm, Apache Heron, and Apache Beam model.

## Benefits

They provide significant value around analyzing large volumes of events in near-real time to enable quicker decision making. Common patterns of usage include:

- Extract data, transform it, and load into a new data store (ETL)
- Perform session and window-based analysis
- Detect abnormal patterns of behavior
- Aggregate streams and maintain state
- Perform any sort of stateless streaming operations

## Drawbacks

### Not designed for microservice style

Deploying applications requires a dedicated resource cluster beyond that of the event broker and CMS (container management system) i.e. Docker, Kubernetes.

### JVM-based

Most frameworks are JVM (Java Virtual Machine)-based, which limits the implementation languages you can use to create singular microservice applications.
