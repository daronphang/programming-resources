## Eventual Consistency

Eventual consistency is a theoretical guarantee that, provided no new updates to an entity are made, all reads of the entity will eventually return the last update value. Also known as optimistic replication and is key to distributed systems.

Although replicas are always available to read, some may be inconsistent with the latest write on the originating node, at a particular moment in time.

An example as follows:

- Blogging site deployed to different geographical regions, with each zone having multiple clusters and nodes
- A user in Japan likes a post, but a user in America sees the old value
- Refreshing the page after a certain time will show the updated value eventually

## Strong Consistency

Data viewed immediately after an update will be consistent for all observers of the entity (immediate consistency). However, scalability and performance of the application will need to be compromised as data has to be locked during the period of update to ensure no other processes are updating the same data.
