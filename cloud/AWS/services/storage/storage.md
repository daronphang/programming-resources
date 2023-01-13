## Storage

AWS provides web data storage service for archiving data. Its primary advantage is disaster data recovery with high durability.

## Buckets

A bucket is used store objects (consisting of data, key, metadata). When data is added to a bucket, S3 creates a unique ID and allocates it to the object.

Users can define features to the bucket, including bucket policy, lifecycle policies, versioning control, etc.

## Lifecycle

Can choose which actions to define.

### Transition Action

You can choose to move objects to another storage class. If the data is not used frequently for 30 days, it would be moved to S3 infrequent access class. After 60 days, it is moved to Glacier.

### Expiration Actions

S3 removes all objects within the bucket when a specified date or time period in the object's lifetime is reached.

## Data Protection

S3 provides IT teams with a highly durable, protected and scalable infrastructure designed for object storage.

1. Data encryption
2. Versioning
3. Cross-region Replication
4. Transfer Acceleration
