## Amazon Elastic File System (EFS)

Amazon EFS is a **network file system (NFS) that works only on Linux** (not Windows) provides highly optimized file storage for a broad range of workloads and applications. It is a scalable file system that can be used with AWS Cloud services and on-premises resources.

As you add and remove files, EFS grows and shrinks automatically. It **can scale on demand to petabytes without disrupting applications**. It is the only cloud-native shared file system with fully automatic lifecycle management. There is no need for provisioning or managing storage capacity and performance.

Amazon EFS is a **regional** service and stores data in and across **multiple Availability Zones**. The duplicate storage enables you to access **data concurrently across multiple Availability Zones, Regions and VPCs**. Additionally, on-premises servers can access EFS using AWS Direct Connect.

EFS deploys mount targets in VPCs with specific IP addresses, and EC2 instances can connect to EFS by mounting the IP address.

```sh
$ sudo apt install -y amazon-efs-utils
$ sudo mount.efs efs:id /directory
```

### EFS Standard

Multi-AZ resilience and the highest levels of durability and availability.

### EFS Infrequent Access (EFS-IA)

You can setup a lifecycle policy to automatically move files to EFS-IA based on the last time they were accessed. Provides lower cost compared to EFS Standard.

### One Zone

Additional savings by choosing to save your data in a single AZ.

### General Purpose Performance Mode

For latency-sensitive applications e.g. web applications, general file serving, content-management systems.

### Elastic Throughput Mode

Automatically scales throughput performance up or down to meet the needs of your workload activity.

### Max I/O Performance Mode

Higher levels of aggregate throughput and operations per second.

### Provisioned Throughput Mode

Level of throughput the filesystem can drive independent of the file system's size or burst credit balance.

### Bursting Throughput Mode

Scales with the amount of storage in your filesystem and supports bursting to higher levels for up to 12h per day.
