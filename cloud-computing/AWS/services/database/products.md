## RDS (Relational Database Service)

Amazon RDS is a service that enables you to run relational databases in the AWS Cloud. The service automates tasks such as hardware provisioning, database setup, patching, and backups. You can integrate RDS with other services to fulfill your business and operational needs, such as AWS Lambda to query your database from a serverless application.

Amazon RDS provides a number of different security options. Many RDS database engines offer **encryption at rest** (protecting data while it is stored) and **in transit** (protecting data while it is being sent and received).

Amazon RDS is available on on the following engines:

- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

### Database instances

Amazon RDS is built from compute (DB instance) and storage. A DB instance can contain multiple databases with the same engine, and each DB can contain multiple tables.

Underneath the DB instance is an EC2 instance. However, this instance is managed through the Amazon RDS console instead of the Amazon EC2 console.

### Storage

The storage portion of DB instances uses Amazon EBS volumes for database and log storage.

### Amazon Aurora

Amazon Aurora is an enterprise-class relational database. It is compatible with MySQL and PostgreSQL relational databases. It is up to **five times faster than standard MySQL databases** and up to **three times faster than standard PostgreSQL databases**.

Amazon Aurora helps to reduce your database costs by reducing unncessary I/O operations, while ensuring that your database resources remain reliable and available.

Consider Amazon Aurora if your workloads require **high availability**. It replicates **six copies of your data across three Availability Zones**, and continuously backs up your data to Amazon S3.

## DynamoDB

Amazon DynamoDB is a key-value and flexible NoSQL that offers fast and reliable performance with no scalability issues. It is serverless, which means that you do not have to provision, patch, and manage servers.

DynamoDB is a fully managed service that handles the operations work. You can offload the administrative burdens of operating and scaling distributed databases to AWS.

DynamoDB provides **automatic scaling**. As the size grows/shrinks, it automatically scales to adjust for changes in capacity while maintaining consistent performance. This makes a suitable choice that require **high performance while scaling**.

### Core components

In DynamoDB, there are three core components:

- Table: A collection of data
- Item: A group of attributes that is uniquely identifiable among all other items
- Attribute: A fundamental data element that does not need to be broken down any further i.e. fields

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

Amazon DocumentDB is a document database service that supports MongoDB workloads i.e. has API compatibility with MongoDB.

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

## Amazon Timestream

Timestream is a fast, scalable and serverless time series database service for **IoT and operational applications**. It makes it easy to store and analyze trillions of events per day, up to 1,000 times faster and for as little as one-tenth of the cost of relational databases.

Time series data is a sequence of data points recorded over a time interval. It is used for measuring events that change over time i.e. stock prices, temperature.
