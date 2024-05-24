## AWS Backup

**Backup** creates copies of data to restore it in case of data loss. It is an essential part of disaster recovery. **Disaster recovery** encompasses a broader strategy, and includes planning for system and application recovery e.g. EBS Snapshots, S3. A solid disaster recovery plan ensures business continuity, minimizes downtime, and safeguards data integrity.

With AWS Backup:

- you have a single, unified console for managing AWS services
- Automates backup scheduling and retention policies
- Backup resources in different Regions and different accounts
- Can perform backups across a wide variety of services e.g. EC2, EBS, EFS, RDS, etc.

### Components

- Backup vault
- Backup plan i.e. frequency
- Recovery point e.g. checkpoint

### Locks

- Vault lock: Prevents deletion on data in a single vault (has compliance and governance mode)
- Legal hold: Locks resources across all backups

## AWS Elastic Disaster Recovery (EDR)

AWS EDR minimizes data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.

EDR uses block replication to replicate server volumes incrementally at the block level.

**Failback** is the process of reverting systems back to the primary environment after a failover test.

<img src="../../assets/edr.png">

### Components

- Source servers: Represent the servers/data that you want to replicate
- Replication Agent: Installed on source servers
- Launch template: Used to configure the specifications of the recovery servers e.g. size, region/subnet, security group, etc.
- Staging Subnet: Spinning up of EC2 instances to handle the replication with data from Replication Agent and stored in EBS
- Recovery Subnet: EC2 instances launched with point-in-time snapshots

### Features

- Fully managed disaster recovery service for physical, virtual and cloud-based servers
- Customers can use AWS as a recovery site instead of investing in on-premises disaster recovery infrastructure
- Keeps things in a continual replication state
- Easy to access with a diaster recovery infrastructure
- Failover from on-premise/other cloud platforms/AWS Regions to AWS
- Real-time sync and point-in-time recovery
- Automated DR drills
- Faster recovery
- Fail back to source after recovery
- Automatically applies security groups from source EC2 instances to replicated instances

## AWS Recycle Bin

Recycle Bin is a data recovery feature that enables you to restore accidentally deleted Amazon EBS snapshots and EBS-backed AMIs. When using Recycle Bin, if your resources are deleted, they are retained in the Recycle Bin for a time period that you specify before being permanently deleted.
