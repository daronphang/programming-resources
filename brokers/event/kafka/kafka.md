## Kafka

A distributed publish-subscribe messaging system. Instead of using data packets, it uses a data stream to deliver messages which are suitable for both offline and online message consumption. An open-source platform developed by Apache written in Scala and Java. Kafka aims to provide solutions for large scale event-driven systems.

## Features

### High-Volume

Kafka works with a considerable volume of data in the data streams.

### Scalability

Scales easily without downtime by handling scalability in all four dimensions i.e. event producers, event consumers, event connectors and event processors.

### Fault Tolerance

Kafka connector can handle failures with three strategies summarized as fast-fail, ignore and requeue.

### Durability

Uses a distributed commit log which means no cascade failure and messages are persisted on a disk as fast as possible.

### Retention

Provides durable storage of messages for a certain period of time. Kafka brokers are configured with a default retention setting of 7 days or until the partition reaches a certain size. Once these limits are reached, messages are expired and deleted.

### Performance

Has high throughput for both publishing and subscribing to messages.

## Use Cases

### Activity tracking

A website's users interact with frontend applications, which generate messages regarding actions the user is taking i.e. page views, click tracking, or more complex actions such as adding data to their profile. The messages are published to one or more topics, which are then consumed by applications on the backend. These applications may be generating reports, feeding machine learning systems, updating search results, or performing other operations that are necessary to provide a rich user experience.

### Messaging

Kafka can be used for messaging, where applications need to send notifications (emails) to users. These applications can produce messages without needing to be concerned about formatting or how messages will be sent. A single application can then read all messages, apply formatting and user's preferences for how they want to receive messages.

### Metrics and logging

Kafka is ideal for collecting application and system metrics and logs, a use case in which the ability to have multiple applications producing the same type of message shines. Applications publish metrics on a regular basis to a Kafka topic, and those metrics can be consumed by systems for monitoring and alerting.

### Commit log

Since Kafka is based on the concept of a commit log, database changes can be published to Kafka, and applications can easily monitor this stream to receive live updates as they happen. This changelog stream can also be used for replicating database updates to a remote system, or for consolidating changes from multiple applications into a single database view.

### Stream processing

Stream processing is a term typically used to refer to applications that provide similar functionality to map/reduce processing in Hadoop. Stream processing operates on data in real time.
