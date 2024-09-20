## Controller

The controller is responsible for electing partition leaders, create and delete topics, and reassign replicas. The first broker that starts in the cluster becomes the controller by creating an ephemeral node in ZooKeeper. Each cluster will only have one controller at a time.

## ZooKeeper

In the existing architecture, ZooKeeper has two important functions:

1. Elect a controller
2. Store the cluster metadata (registered brokers, configuration, topics, partitions, replicas)

## Kraft

The Kafka community has shifted away from ZooKeeper-based controller to a Raft-based controller quorum. Several concerns motivated the change:

- Metadata updates are written to ZooKeeper synchronously but are sent to brokers asynchronously, leading to edge cases where metadata is inconsistent
- Whenever the controller is restarted, ZooKeeper has to read all the metadata for all brokers and partitions from the ZooKeeper and then send this metadata to all brokers which remains a major bottleneck for scaling
- Internal architecture around metadata ownership is not great i.e. some operations are done via the controllers, others via the broker, rest directly on ZooKeeper

## Raft architecture

Core idea behind the new controller design is that Kafka itself has a log-based architecture, where users represent state as a stream of events. The log establishes clear ordering between events and ensures that consumers always move along a single timeline.

The controller nodes are a Raft quorum that manages the log of metadata events. Everything that were previously stored in ZooKeeper (topics, partitions, configurations, etc) are stored in this log.

Using the Raft algorithm, the controller nodes will elect a leader from among themselves, without relying on any external system. The leader of the metadata log is called the active controller. The active controller handles all RPCs made from the brokers. The follower controllers replicate the data that is written to the active controller and serve as hot standbys if the active controller should fail.

Instead of the controller pushing out updates to the other brokers, those brokers will fetch updates from the active controller via a new MetadataFetch API. Brokers will track the offset of the latest metadata change they fetched, and will only request newer updates from the controller. Brokers will persist the metadata to disk.
