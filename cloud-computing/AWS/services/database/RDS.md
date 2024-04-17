## RDS (Relational Database Service)

Amazon RDS is a service that enables you to run relational databases in the AWS Cloud. The service automates tasks such as hardware provisioning, database setup, patching, and backups. You can integrate RDS with other services to fulfill your business and operational needs, such as AWS Lambda to query your database from a serverless application.

Amazon RDS provides a number of different security options. Many RDS database engines offer **encryption at rest** (protecting data while it is stored) and **in transit** (protecting data while it is being sent and received).

Amazon RDS is available on the following engines:

- Amazon Aurora
- PostgreSQL
- MySQL
- MariaDB
- Oracle Database
- Microsoft SQL Server

### Features

- Routine database operations
- Backup and restore
- Automatically manages DBA task e.g. patching
- High availability and fault tolerance
- Scalability
- Monitoring, audit and performance
- Security
- Blue/green deployment
- Multi-AZ deployments

### Database instances

Amazon RDS is built from compute (EC2 instance) and storage. A DB instance can contain multiple databases with the same engine, and each DB can contain multiple tables.

Underneath the DB instance is an EC2 instance. However, this instance is managed through the Amazon RDS console instead of the Amazon EC2 console.

### Storage

The storage portion of DB instances uses Amazon EBS volumes for database and log storage.

### Read replicas

You can scale the read workload of your DB by creating replicas (maximum of 15 replicas). However, **write is only performed to the main DB**.

For multiple Availability Zones, you can create a **failover DB** in case of an outage. It is only active if the failover is triggered.

### RDS Proxy

RDS Proxy is a fully managed database proxy for RDS instances that make your application more scalable and resilient. It establishes a pool of database connections and reuses it if a query is performed. By offloading query caching from the database, RDS Proxy can reduce database load and improve query response times, contributing to more stable overall performance.

RDS Proxy avoids the problem of oversubscribing and creating too many connections leading to higher memory and CPU utilization. Failover times can be reduced because the proxy automatically reconnects to a new database instance in the case of a failure.
