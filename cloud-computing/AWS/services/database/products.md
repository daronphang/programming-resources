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

### Security

IAM policies can be used to define permissions for ElastiCache API actions but **not for data operations** within Redis and Memcached.

## MemoryDB for Redis

Instead of having to manage two separate databases (RDS and Redis), you can simplify into one using MemoryDB. Redis will be your primary database instead of just using it as a cache.

### Features

- Designed for extremely high throughput and low latency workloads
- Strong consistency for primary nodes and guaranteed eventual consistency for replica nodes

## RedShift

Amazon Redshift is a fully managed **data warehousing** service that you can use for big data analytics (based on PostgreSQL). It offers the ability to collect data from many sources and helps you to understand relationships and trends across your data.

Traditional databases handle structured data at a granular level, while data warehouses are designed to handle structured data at an aggregate level.

RedShift's fault-tolerant design includes automatic and synchronous data replication to three-different nodes within a cluster and continuous backups to S3.

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

### Spectrum

Using Amazon Redshift Spectrum, you can efficiently query and retrieve structured and semi-structured data from files in Amazon S3 without having to load the data into Amazon Redshift tables. Redshift Spectrum queries employ massive parallelism to run very fast against large datasets.

### Tokenization

If tokenization is required as a method to protect sensitive data, you need to integrate with a third-party tokenization solution before it is loaded into the data warehouse. Redshift does not have natively built-in tokenization feature.

## Amazon DocumentDB

Amazon DocumentDB is a document database service that supports MongoDB workloads i.e. has API compatibility with MongoDB.

### Features

- MongoDB compatible
- Storage auto-repair
- Cache warming
- Crash recovery
- Write durability
- Read preferences e.g. primary, primary-preferred, secondary, nearest

## Amazon Neptune

Amazon Neptune is a graph database service. You can use it to build and run applications that work with highly connected datasets i.e. recommendation engines, fraud detection, and knowledge graphs.

### Features

- Serverless
- High throughput and low latency
- Easy scaling with autoscaling storage
- ML predictions using graph neural network

## Amazon Quantum Ledger Database (QLDB)

Amazon QLDB is a financial transactions ledger database service that is fully managed and serverless. You can use it to review a complete history of all the changes that have been made to your application data.

Data is stored in journals. Journal blocks are sequenced and chained together with cryptographic hashing techniques.

Compared to Managed Blockchain, **QLDB does not have the concept of decentralization** i.e. it has a central authority DB component owned by Amazon.

### Why traditional databases are not suitable?

- Mutable
- Lack of transparency
- Centralized
- Single point of failure
- Lack of consensus mechanisms
- Do not provide the level of privacy and confidentiality required

## Amazon Managed Blockchain

Amazon Managed Blockchain is a service that you use to create and manage blockchain networks with open-source frameworks.

Blockchain is a distributed ledger system that lets multiple parties run transactions and share data without a central authority.

## Amazon Timestream

Timestream is a fast, scalable and serverless time series database service for **IoT and operational applications**. It makes it easy to store and analyze trillions of events per day, up to 1,000 times faster and for as little as one-tenth of the cost of relational databases.

Time series data is a sequence of data points recorded over a time interval. It is used for measuring events that change over time i.e. stock prices, temperature.

### Features

- Serverless
- Storage tiering e.g. memory stores for recent, magnetic for historical
- built-in analytics
- Custom query engine
- Flexible data model

## AWS OpenSearch

Forked from Elasticsearch as it was changed from open-source to proprietary license. With OpenSearch ingestion pipelines, you don't need third party such as Logstash to help you push data to OpenSearch. Instead, you configure your producers to send data to OpenSearch ingestion.

### Security flow

1. Client sends request with IAM credentials
2. Client connects to VPC
3. Security groups permit request to reach domain
4. IAM credentials are valid
5. Access policy allows user to reach URI
6. Fine-grained access control lets user perform action at index and document level

## Amazon Keyspaces

Used for Apache Cassandra. Supports encryption at rest without any additional configurations.

### Features

- Compatible with Cassandra Query Language (CQL)
- Fully managed Time-to-Live (TTL)
- Multi-region replication performed through asynchronous replication to propagate the writes across Regions
- Active-active configuration i.e. each Region handles read/write
- Consistency and conflict resolution
- Offers on-demand capacity that requires no capacity planning and scales automatically with the workload's read/write throughput
