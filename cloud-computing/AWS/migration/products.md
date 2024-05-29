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

AWS Application Discovery Service collects information about the usage and configuration of on-premises servers to help plan a migration to AWS e.g. CPU, disk, memory, network. Data collected is encrypted at-rest and in-transit. Application Discovery Service does not actually perform migration operations.

The parameters can be discovered in one of the following ways:

- Agentless discovery: Suited for VMware hosts
- Agent-based discovery: Suited for hosts other than VMware e.g. Windows, Linux

## Database Migration Service (DMS)

DMS migrates databases (relational, nonrelational) to AWS in a quick, secure, and resilient manner.

With AWS DMS, you move data between a source database and a target database. They both can be of the **same type (homogenous) or different types (heterogeneous)**. During migration, your source database remains operational.

DMS has a single point of failure in the replication instance. Nonetheless, you can use multi-AZ replication instance for redundant replication servers. However, it does not have automatic failover i.e. you have to restart the instance if it fails.

DMS has an advanced logging feature called **time travel logs**, which enables users to store, encrypt and access logs in S3, offering flexibility and improved troubleshooting.

### Use cases

- Enabling developers to test applications against production data without affecting production users
- Combining several databases into a single database
- Sending ongoing copies of data to other target sources (replication)

### Migration types

- Full load: Migrates data from source to target, creating tables as necessary
- Full load with Change Data Capture (CDC): Performs full load while simultaneously capturing changes on the source
- CDC only to capture and replicate ongoing changes from the source database

### Features

- Schema migration
- Continuous data replication

## AWS Mainframe Modernization

AWS Mainframe Modernization helps to modernize and migrate your mainframe application to AWS managed runtime environments.

### Features

- Refactoring legacy codebase
- Replatforming without changes to source code
- Developer IDE
- Manages runtime

## AWS DataSync

AWS DataSync facilitates fast and secure data transfers between on-premise/AWS storage systems and AWS storage services. It is designed to simplify, automate and accelerate the process of moving large amounts of data.

When you use DataSync with a private VPC endpoint, the DataSync agent can communicate directly with AWS without the need to cross the public internet.

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
- Incremental transfers (transferring changed or new data since the last synchronization)
- Security and encryption (at-rest and transit)
- Monitoring and logging

## AWS Transfer Family

AWS Transfer Family is a full-managed and highly-available FTP server that securely scales your recurring business-to-business file transfers to AWS Storage services using SFTP, FTPS, FTP, and AS2 protocols. Supports S3 or EFS.

You can configure a custom security policy that aligns with the company's specific security requirements and industry regulations.

### Features

- Support protocols including SSH-SFTP, FTPS, AS2 (Applicability Statement 2)
