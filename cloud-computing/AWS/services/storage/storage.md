## Block storage

Instance Store and EBS.

## Object storage

In object storage, each object consists of:

- Data: Might be an image, video, text document, or any type of file
- Metadata: Contains information about what the data is, how it is used, etc.
- Key: Unique identifier

## File storage

In file storage, multiple clients (users, applications, servers) can access data that is stored in shared file folders. In this approach, a storage server uses **block storage with a local file system to organize files**.

Compared to block storage and object storage, file storage is ideal for use cases in which a large number of services and resources need to access the same data at the same time.
