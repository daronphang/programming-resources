## Consumer Offsets

The consumer offset is a way of tracking the sequential order in which messages are received by Kafka topics. Keep track of the offset/position is important and can be an absolute necessity in certain instances, such as financial services.

The consumer offset allows processing to continue from where it last left off, if the stream application is turned off or encountered an unexpected failure. By having offsets persist in a data store (Kafka/Zookeeper), **data continuity is retained even when the stream application shuts down or fails**.

## New Consumer Groups

### New Topic

Offset begins at 0 when a consumer starts for a new topic.

### Existing Topic

Offset will either begin from the beginning or end of the topic. Whether you start at the beginning or end is determined by your use case.

If you start from the beginning, you will be replaying data, and this approach is good for building out new server and populating it with data, or for doing load testing on a Kafka cluster.

## Existing Consumer Groups

If a consumer instance consumes 12 messages and then fails, it will continue from where it left off in the offset as it is stored by Kafka/ZooKeeper.