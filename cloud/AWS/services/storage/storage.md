## Storage

AWS provides web data storage service for archiving data. Its primary advantage is disaster data recovery with high durability.

## S3 (Simple Storage Service)

Open cloud-based storage service that can store and retrieve data from anywhere including websites, mobile apps, IoT sensors, etc. It is durable, provides comprehensive security, and flexibility in managing data. Provides 99.99% durability and availability, up to 5TB.

### Buckets

A bucket is used store objects (consisting of data, key, metadata). When data is added to a bucket, S3 creates a unique ID and allocates it to the object.

Users can define features to the bucket, including bucket policy, lifecycle policies, versioning control, etc.

## EBS (Elastic Block Store)

Provides a high availability storage volume for persistent data. Mainly used by EC2 instances. Can be attached to any running EC2 instance in the same availability zone.

EBS volumes are used explicitly for primary storage such as file storage, database storage, and block-level storage.

## Glacier

Cloud storage service that is used for archiving data and long-term backup (low-cost solution).

## EFS (Elastic File System)

PRovides elastic file storage, which can be used with AWS Cloud Services and resources that are on-premises.
