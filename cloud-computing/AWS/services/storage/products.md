## Instance Store

An Instance Store provides temporary **block-level storage** (behave like physical hard drives) for an EC2 instance. It is a disk storage that is physically attached to the host computer, and therefore has the same lifespan as the instance. When the instance is terminated, you lose any data in the instance store.

## AWS Storage Gateway

AWS Storage Gateway is a hybrid service that provides on-premises applications with access to virtually unlimited cloud storage. Behind the scenes, the Storage Gateway will be using Amazon EBS, S3 and Glacier. All data transferred between the gateway and AWS storage is **encrypted** using SSL.

The storage gateway is either a VM or physical server installed in your on-premise environment, and acts as a bridge between your on-premise and AWS environment. Can provide caching locally in on-premise environment.

### Benefits

- An extension for your on-premise storage needs
- Assists migrations into the cloud
- Perform backups
- Disaster recovery tool

### Modes

Depending on the protocols, there's a mode within AWS Storage Gateway that will make it compatible for your solution.

- **Volume Storage Gateway** with Cached (frequently accessed data stored on-prem) and Stored Mode (entire dataset stored in AWS and on-prem), utilizes iSCSI protocol and use S3 as primary data storage
- **File Storage Gateway** with data stored in S3, utilizes NFS/SMB protocol
- **Tape Gateway** that emulates a tape library with data stored in S3 (Virtual Tape Library) or Glacier (Tape Shelf), utilizes iSCSI protocol

#### Volume Storage Gateway

In **Stored Mode**, data is stored locally on-premise i.e. data is stored in physical disks. Data is then replicated asynchronously to S3 as EBS Snapshots by Storage Gateway. It does not increase datacenter storage capacity i.e. limited by the physical disks size.

In **Cached Mode**, data is stored in AWS S3. For data that are accessed frequently, they are stored in cache locally. It helps to extend overall storage capacity i.e. unlimited.
