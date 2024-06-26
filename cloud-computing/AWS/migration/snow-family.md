## AWS Snow Family

The AWS Snow Family is a collection of offline physical devices that help to **physically transport data into and out of AWS**, or to **collect and process data at the edge**.

These devices offer different capacity points, and most include built-in computing capabilities. AWS owns and manages the Snow Family devices and integrates with AWS security, monitoring, storage management, and computing capabilities.

Both AWS Snowcone and Snowball Edge are ruggedized i.e. durable. They are portable and can provide compute power in locations with harsh conditions.

Challenges faced during migration:

- Limited connectivity/stability
- Limited/shared bandwidth
- High network cost

### Features

- Rugged and portable
- NFS endpoint
- On-board computing e.g. EC2 instances, Lambda, etc.
- Encryption of data
- Offline data migration
- Anti-tamper
- End-to-end tracking
- Secure erasure

## AWS Snowcone

AWS Snowcone is a small, rugged, secure edge computing and data transfer device. Features 2 CPUs, 4GB of memory, and up to **14TB** of usable storage.

## AWS Snowball Edge

### Storage Optimized

These devices are suited for large-scale data migrations and recurring transfer workflows, in addition to local computing with higher capacity needs.

- Storage: **80TB** of HDD capacity for block volumes and S3 compatible object storage, and 1TB of SATA SSD for block volumes
- Compute: 40 vCPUs, and 80GB of memory to support EC2 sbe1 instances

### Compute Optimized

Provides powerful computing resources for use cases such as machine learning, full motion video analysis, analytics, and local computing stacks.

- Storage: **80TB** of HDD for S3 compatible object storage, and 28TB of SSD capacity
- Compute: 104 vCPUs and 416GB of memory to support EC2 sbe-c and sbe-g instances

## AWS Snowmobile

AWS Snowmobile is an exabyte-scale data transfer service used to move large amounts of data to AWS. You can transfer up to **100PB** of data per Snowmobile, a 45-loot long ruggedized shipping container, pulled by a semi trailer truck. It is used for moving exabytes of data (1EB = 1000PB).

## AWS OpsHub

Historically, to use Snow Family devices, you needed a CLI which was difficult. Instead, you can use AWS OpsHub which is a software installed on your computer to manage your Snow Family devices.
