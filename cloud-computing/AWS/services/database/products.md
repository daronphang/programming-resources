## Amazon Aurora

Amazon Aurora is an enterprise-class relational database. It is compatible with MySQL and PostgreSQL relational databases. It is up to **five times faster than standard MySQL databases** and up to **three times faster than standard PostgreSQL databases**.

Amazon Aurora helps to reduce your database costs by reducing unnecessary I/O operations, while ensuring that your database resources remain reliable and available.

The unit of measure is Aurora Capacity Unit (ACU), which equates to 2GB of memory, corresponding CPU, and networking.

Consider Amazon Aurora if your workloads require **high availability**. It replicates **six copies of your data across three Availability Zones**, and continuously backs up your data to Amazon S3.

### Features

- Purpose-built log structured distributed storage
- Storage volume is striped across storage nodes and multiple AZs
- Storage nodes with locally attached SSDs
- Continuous backup to Amazon S3
- Automatic scaling of storage without any management overhead or downtime
- Allows you to create up to 15 Aurora replicas across 3 AZs
- Offers fast database cloning for staging/development purposes without impacting the performance of the production database

### Provisioned vs Serverless

Provisioned has fixed capacity, useful for planned capacity, and has access to Aurora Global.

Serverless provides on-demand scaling, useful for variable/unpredictable workloads, and has access to Aurora Global.

### Global cluster

When you use Aurora Global database clusters, it acts as a container for several database clusters each located in different Regions.

A global database cluster comprises of:

- Primary database cluster that accepts read/writes
- Secondary clusters as read only

## Amazon ElastiCache

Amazon ElastiCache is a service that adds **caching layers** on top of your databases to help improve the read times of common requests. Supports two types of **in-memory** data stores: Redis and Memcached.

### Redis

- Read replicas
- Data persistence
- Encryption at rest
- Pub/sub message system

### Memcached

- Multi-AZ deployments
- Auto discovery
- Data partitioning and sharding

## MemoryDB for Redis

Instead of having to manage two separate databases (RDS and Redis), you can simplify into one using MemoryDB. Redis will be your primary database instead of just using it as a cache.

### Features

- Designed for extremely high throughput and low latency workloads
- Strong consistency for primary nodes and guaranteed eventual consistency for replica nodes

## RedShift

Amazon Redshift is a fully managed **data warehousing** service that you can use for big data analytics (based on PostgreSQL). It offers the ability to collect data from many sources and helps you to understand relationships and trends across your data.

Traditional databases handle structured data at a granular level, while data warehouses are designed to handle structured data at an aggregate level.

RedShift has two node types:

- Leader node: Manages query coordination, compilation and optimization
- Compute nodes: Store data and execute queries and computations

### Features

- Columnar storage for high efficiency
- Built on massively parallel processing (MPP)
- Data compression
- Scalability by adding nodes to the cluster
- Integration with many data sources
- Data ingestion
- SQL compatibility
- Provides encryption at rest

### Serverless

An on-demand data warehousing service that automatically manages the scaling and provisioning of resource, enabling you to run analytics without managing a cluster.

With regular Redshift deployments (provisioned), you get a combination of CPU, RAM and storage. Hence, you will end up incurring cost even when you are not querying data from Redshift i.e. underutilized, over-provisioned.

## Amazon DocumentDB

Amazon DocumentDB is a document database service that supports MongoDB workloads i.e. has API compatibility with MongoDB.

## Amazon Neptune

Amazon Neptune is a graph database service. You can use it to build and run applications that work with highly connected datasets i.e. recommendation engines, fraud detection, and knowledge graphs.

## Amazon Quantum Ledger Database (QLDB)

Amazon QLDB is a financial transactions ledger database service that is fully managed and serverless. You can use it to review a complete history of all the changes that have been made to your application data.

Compared to Managed Blockchain, **QLDB does not have the concept of decentralization** i.e. it has a central authority DB component owned by Amazon.

## Amazon Managed Blockchain

Amazon Managed Blockchain is a service that you use to create and manage blockchain networks with open-source frameworks.

Blockchain is a distributed ledger system that lets multiple parties run transactions and share data without a central authority.

## Amazon Timestream

Timestream is a fast, scalable and serverless time series database service for **IoT and operational applications**. It makes it easy to store and analyze trillions of events per day, up to 1,000 times faster and for as little as one-tenth of the cost of relational databases.

Time series data is a sequence of data points recorded over a time interval. It is used for measuring events that change over time i.e. stock prices, temperature.

## Amazon Athena

Amazon Athena is a **serverless query service** to perform analytics against **S3 objects**. Uses standard SQL language to query the files.

## Amazon QuickSight

Amazon QuickSight is a serverless machine learning-powered business intelligence service to create interactive dashboards.

## AWS Glue

AWS Glue is a serverless ETL service that is useful to prepare and transform data for analytics.

## AWS OpenSearch

Forked from Elasticsearch as it was changed from open-source to proprietary license. With OpenSearch ingestion pipelines, you don't need third party such as Logstash to help you push data to OpenSearch. Instead, you configure your producers to send data to OpenSearch ingestion.
