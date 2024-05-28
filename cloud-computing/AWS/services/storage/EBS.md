## EBS (Elastic Block Storage)

An AWS EBS is a **network drive** that provides block-level storage volumes that you can use with EC2 instances (drives separated from host computer), and gets persisted. After creating an EBS volume (with configuration provided), you can attach to an EC2 instance.

Amazon EBS is meant for data that **changes frequently** and must persist through instance stops, terminations, or hardware failures.

An EBS volume stores data in a **single Availability Zone**. To attach an EBS volume to an EC2 instance, **both must reside within the same Availability Zone**.

As EBS volumes are for data that needs to persist, it is important to backup the data. You can take incremental backups by creating **EBS snapshots**. Nonetheless, EBS is **automatically replicated** in its Availability Zone to prevent data loss from single points of failure.

EBS volumes act similarly to external drives:

- Detachable: You can detach an EBS volume from one EC2 instance and attach it to another
- Distinct: The external drive is separate from the computer
- Size-limited: Volume has a max limitation of how much content you can store on it
- 1-to-1 connection: Most EBS volumes can only be connected with one computer at a time (one computer can be connected to multiple EBS volumes)

### Features

- Supports live configuration changes i.e. you can modify the volume type, size, IOPS capacity without service disruptions

### Pricing

Pay for what you are provisioned. Charged per GB per month.

## Volume Types

EBS volumes are organized into SSDs and HDDs. SSDs are used for transactional workloads with frequent read/write operations with small I/O size. HDDs are used for streaming large workloads that need **high throughput** performance.

### General purpose SSD (gp2/gp3)

They balance price and performance and are great for a wide variety of transactional workloads e.g. virtual desktops, latency sensitive development applications, medium size desktops, etc.

### Provisioned IOPS SSD volumes

Classified as the highest performance EBS storage volumes which are designed for critical IOPS intensive throughput workloads.

Three categories include:

- io2 block express: Up to 64TB, 256,000 IOPS per volume, and 4000 MiB/s
- io2: More durability, up to 64,000 IOPS per volume, 1000 MiB/s
- io1: Up to 16TB

### Throughput optimized HDD volumes

Low cost hard disk drive designed for frequently accessed throughput intensive workloads. Does not support multi-attach EBS.

### Cold HDD volumes

Lowest cost hard drive. Does not support multi-attach EBS.

### Magnetic

Previous generation of volumes that are backed by magnetic drives. Used when performance is not of primarily importance.

## EBS Snapshots

An EBS snapshot is an incremental backup that stores data in S3:

- First backup copies all the data
- Subsequent backups copy **blocks of data that have changed** since the most recent snapshot are saved
- Snapshots will retain encryption property

With EBS Snapshots, you can **replicate data across Availability Zones**.

### EBS Snapshot Archive

You can move a Snapshot to an archive tier that is cheaper to store, but takes between 24-72h for restoring the archive.

## Amazon Data Lifecycle Manager

You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion of EBS snapshots and EBS-backed AMIs.

## AWS Recycle Bin

Recycle Bin is a data recovery feature that enables you to restore accidentally deleted Amazon EBS snapshots and EBS-backed AMIs. When using Recycle Bin, if your resources are deleted, they are retained in the Recycle Bin for a time period that you specify before being permanently deleted.
