## Instance Store

An Instance Store provides temporary **block-level storage** (behave like physical hard drives) for an EC2 instance. It is a disk storage that is physically attached to the host computer, and therefore has the same lifespan as the instance. When the instance is terminated, you lose any data in the instance store.

## EBS (Elastic Block Store)

An AWS EBS is a service that provides block-level storage volumes that you can use with EC2 instances (drives separated from host computer), and gets persisted. After creating an EBS volume (with configuration provided), you can attach to an EC2 instance.

Amazon EBS is meant for data that **changes frequently** and must persist through instance stops, terminations, or hardware failures.

An EBS volume stores data in a **single Availability Zone**. To attach an EBS volume to an EC2 instance, **both must reside within the same Availability Zone**.

As EBS volumes are for data that needs to persist, it is important to backup the data. You can take incremental backups by creating **EBS snapshots**. Nonetheless, EBS is **automatically replicated** in its Availability Zone to prevent data loss from single points of failure.

EBS volumes act similarly to external drives:

- Detachable: You can detach an EBS volume from one EC2 instance and attach it to another
- Distinct: The external drive is separate from the computer
- Size-limited: Volume has a max limitation of how much content you can store on it
- 1-to-1 connection: Most EBS volumes can only be connected with one computer at a time

### Volume Types

EBS volumes are organized into SSDs and HDDs. SSDs are used for transactional workloads with frequent read/write operations with small I/O size. HDDs are used for large streaming workloads that need **high throughput** performance.

### EBS Snapshots

An EBS snapshot is an incremental backup:

- First backup copies all the data
- Subsequent backups copy blocks of data that have changed since the most recent snapshot are saved

## Amazon EFS (Elastic File System)

Amazon EFS provides highly optimized file storage for a broad range of workloads and applications. It is a scalable file system that can be used with AWS Cloud services and on-premises resources.

As you add and remove files, EFS grows and shrinks automatically. It **can scale on demand to petabytes without disrupting applications**. It is the only cloud-native shared file system with fully automatic lifecycle management. There is no need for provisioning or managing storage capacity and performance.

Amazon EFS is a **regional** service and stores data in and across **multiple Availability Zones**. The duplicate storage enables you to access data concurrently from all the Availability Zones in the Region where a file system is located. Additionally, on-premises servers can access EFS using AWS Direct Connect.

## Amazon FSx

Amazon FSx provides native compatbility with third-party file systems. With Amazon FSx, you don't need to worry about managing file servers and storage. This is because Amazon FSx automates time consuming administration task such as hardware provisioning, software configuration, patching, and backups.

You can choose from NetApp ONTAP, OpenZFS, Windows File Server, and Lustre.
