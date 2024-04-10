## AWS Migration Hub

AWS Migration Hub is a service that helps plan and track application migrations. Migration Hub does not perform system migrations.

### Workflow

1. Discover on-premise applications (ADS)
2. Reports the requirements including services, CPU/memory usage, etc. to help plan your migration strategy
3. Performs assessment and provides recommendations of AWS services
4. Call on Migration services to perform migration

## AWS Application Migration Service (MGN)

AWS MGN is an automated lift-and-shift solution. This solution can migrate physical servers and any databases or applications that run on them to EC2 instances in AWS.

MGN minimizes time-intensive and error-prone manual processes by automating the conversion of your source servers to run on AWS.

### Use cases

- On-premise application e.g. SAP, Oracle, SQL Server, VMWare
- Cloud-based application
- Between AWS Regions

### Features

- Assessment and planning
- Replication and continuous data-sync
- Automated cutover and testing

## AWS Application Discovery Service (ADS)

AWS Application Discovery Service collects information about the usage and configuration of on-premises servers to help plan a migration to AWS. Application Discovery Service does not actually perform migration operations.

Offers both agent or agentless discovery.

## Database Migration Service (DMS)

DMS migrates databases (relational, nonrelational) to AWS in a quick, secure, and resilient manner.

With AWS DMS, you move data between a source database and a target database. They both can be of the **same type (homogenous) or different types (heterogeneous)**. During migration, your source database remains operational.

### Use cases

- Enabling developers to test applications against production data without affecting production users
- Combining several databases into a single database
- Sending ongoing copies of data to other target sources (replication)

### Migration types

- Full load: Migrates data from source to target, creating tables as necessary
- Full load with CDC: Performs full load while simultaneously capturing changes on the source
- CDC only

### Features

- Schema migration
- Continuous data replication

## AWS Elastic Disaster Recovery (DRS)

AWS DRS minimizes data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.

### Components

- Replication Agent: Installed on source servers
- Staging Subnet: Spinning up of EC2 instances to handle the replication with data from Replication Agent and stored in EBS
- Recovery Subnet: EC2 instances launched with point-in-time snapshots

### Features

- Real-time sync and point-in-time recovery
- Automated DR drills
- Faster recovery
- Fail back to source after recovery

## AWS Mainframe Modernization

AWS Mainframe Modernization helps to modernize and migrate your mainframe application to AWS managed runtime environments.

### Features

- Refactoring legacy codebase
- Replatforming without changes to source code
- Developer IDE
- Manages runtime

## AWS DataSync

AWS DataSync facilitates fast and secure data transfers between on-premise/AWS storage systems and AWS storage services. It is designed to simplify, automate and accelerate the process of moving large amounts of data.

### Components

- Agent: VMware, Linux KVM, Microsoft Hyper-V
- Location: Source and destination
- Task: Describes a DataSync transfer
- Task Execution: Executing the instructions in the task

### Features

- High-speed data transfer
- Simple management
- Data integrity and verification
- Automation and scheduling
- Support for multiple protocols
- Incremental transfers
- Security and encryption (at-rest and transit)
- Monitoring and logging

## AWS Transfer Family (FTP/AS2)

AWS Transfer Family is a secure transfer service that enables you to transfer files in/out of AWS services. Supports S3 or EFS. It is a full-managed and highly-available FTP server.

### Features

- Support protocols including SSH-SFTP, FTPS, FTP, AS2
