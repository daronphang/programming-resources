## Changelog Event Stream

A changelog is a record of all changes made to the data of the state store. The changelog can be used to rebuild state, and serve as a way of checkpointing event processing progress and allows a recovering processor to avoid reprocessing all input events.

Changelog streams are stored in the event broker and should be compacted since they only need the most recent key/value pair to rebuild the state. 

Changelogs can scale and recover state in a highly performant manner, especially for internal state stores. The newly created application instance just needs to load the data from the associated changelog partitions.

Changelogs are either provided as a built-in feature, such as in Kafka Streams, or implemented by the application developer.

<img src="../../assets/changelog.png">

