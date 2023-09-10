## Instance Store

An Instance Store provides temporary **block-level storage** (behave like physical hard drives) for an EC2 instance. It is a disk storage that is physically attached to the host computer, and therefore has the same lifespan as the instance. When the instance is terminated, you lose any data in the instance store.

## EBS (Elastic Block Store)

An AWS EBS is a service that provides block-level storage volumes that you can use with EC2 instances (drives separated from host computer), and gets persisted. After creating an EBS volume (with configuration provided), you can attach to an EC2 instance.

An EBS volume stores data in a **single Availability Zone**. To attach an EC2 instance to an EBS volume, **both must reside within the same Availability Zone**.

As EBS volumes are for data that needs to persist, it is important to backup the data. You can take incremental backups by creating **EBS snapshots**.

### EBS Snapshots

An EBS snapshot is an incremental backup:

- First backup copies all the data
- Subsequent backups copy blocks of data that have changed since the most recent snapshot are saved

## EFS (Elastic File System)

An AWS EFS is a scalable file system used with AWS Cloud services and on-premises resources. As you add and remove files, EFS grows and shrinks automatically. It **can scale on demand to petabytes without disrupting applications**.

EFS is a **regional** service and stores data in and across **multiple Availability Zones**. The duplicate storage enables you to access data concurrently from all the Availability Zones in the Region where a file system is located. Additionally, on-premises servers can access EFS using AWS Direct Connect.

## S3 (Simple Storage Service)

AWS S3 is a service that provides object-level storage. S3 stores data as objects in buckets.

You can upload any type of file to AWS S3, and offers **unlimited storage space**. The maximum file size for an object is 5TB.

When you upload a file, you can set permissions to control visibility and access to it. You can also use the **versioning feature to track changes to your objects** over time.

## RDS (Relational Database Service)

Amazon RDS is a service that enables you to run relational databases in the AWS Cloud. The service automates tasks such as hardware provisioning, database setup, patching, and backups. You can integrate RDS with other services to fulfill your business and operational needs, such as AWS Lambda to query your database from a serverless application.

Amazon RDS provides a number of different security options. Many RDS database engines offer **encryption at rest** (protecting data while it is stored) and **in transit** (protecting data while it is being sent and received).

### RDS Database Engines

Amazon RDS is available on on the following engines:

- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

### Amazon Aurora

Amazon Aurora is an enterprise-class relational database. It is compatible with MySQL and PostgreSQL relational databases. It is up to **five times faster than standard MySQL databases** and up to **three times faster than standard PostgreSQL databases**.

Amazon Aurora helps to reduce your database costs by reducing unncessary I/O operations, while ensuring that your database resources remain reliable and available.

Consider Amazon Aurora if your workloads require **high availability**. It replicates **six copies of your data across three Availability Zones**, and continuously backs up your data to Amazon S3.

## DynamoDB

Amazon DynamoDB is a key-value and flexible NoSQL that offers fast and reliable performance with no scalability issues. It is serverless, which means that you do not have to provision, patch, and manage servers.

DynamoDB provides **automatic scaling**. As the size grows/shrinks, it automatically scales to adjust for changes in capacity while maintaining consistent performance. This makes a suitable choice that require **high performance while scaling**.

## RedShift

Amazon Redshift is a data warehousing service that you can use for big data analytics. It offers the ability to collect data from many sources and helps you to understand relationships and trends across your data.

## DMS (Database Migration Service)

AWS DMS enables you to migrate relational databases, nonrelational databases, and other types of data stores.

With AWS DMS, you move data between a source database and a target database. They both can be of the **same type or different types**. During migration, your source database remains operational.

Use cases include:

- Enabling developers to test applications against production data without affecting production users
- Combining several databases into a single database
- Sending ongoing copies of data to other target sources (replication)

## Amazon DocumentDB

Amazon DocumentDB is a document database service that supports MongoDB workloads.

## Amazon Neptune

Amazon Neptune is a graph database service. You can use it to build and run applications that work with highly connected datasets i.e. recommendation engines, fraud detection, and knowledge graphs.

## Amazon Quantum Ledger Database

Amazon QLDB is a ledger database service. You can use it to review a complete history of all the changes that have been made to your application data.

## Amazon Managed Blockchain

Amazon Managed Blockchain is a service that you use to create and manage blockchain networks with open-source frameworks.

Blockchain is a distributed ledger system that lets multiple parties run transactions and share data without a central authority.

## Amazon ElastiCache

Amazon ElastiCache is a service that adds caching layers on top of your databases to help improve the read times of common requests. Supports two types of data stores: Redis and Memcached.

## Amazon DynamoDB Accelerator

Amazon DAX is an in-memory cache for DynamoDB.
