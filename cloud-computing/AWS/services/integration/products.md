## Amazon API Gateway

The Amazon API Gateway is a serverless and scalable service used for building a serverless API service with AWS Lambda. It will proxy the request to AWS Lambda. Supports RESTful APIs and WebSocket APIs.

### REST vs HTTP APIs

REST APIs and HTTP APIs are both RESTful API products. REST APIs support more features than HTTP APIs, while HTTP APIs are designed with minimal features so that they can be offered at a lower price.

REST APIs have additional features including:

- API keys
- Per-client throttling
- Request validation
- AWS WAF integration
- Private API endpoints

### Features

- Simplify backend integration with Lambda, EC2, ECS, etc.
- API management and deployment
- Request and response transformation, validation, model mapping
- Security and access control
- Rate limiting and throttling (API abuse) for resiliency
- Monitoring and analytics
- SDK generation (automatically handle API keys and AWS credentials)
- Lifecycle management for managing releases e.g. alpha, beta, production

### Integrations

- AWS Lambda
- AWS Elastic Beanstalk
- EC2
- Amazon S3
- Amazon DynamoDB
- AWS Step Functions
- Amazon Kinesis Video Streams

## AWS AppFlow

AWS ApFlow is a fully managed integration service that enables you to securely exchange data between software as a service application e.g. Salesforce, S3, RedShift. Also allows you to perform data mappings between source and destination.

### Components

- Connector: Facilitate the transfer of data by storing necessary configuration parameters, credentials that AppFlow will need to communicate with the different applications between source and destination
- Trigger: Determines how a flow runs e.g. on-demand, on-event, on-schedule

### Features

- Speed and automation to integrate applications
- Security and privacy
- Scalability

## SNS (Amazon Simple Notification Service)

SNS is a pub/sub service. In SNS, subscribers can be web servers, email addresses, AWS Lambda functions, etc. Each subscriber to the topic will get **all the messages**.

Subscribers from AWS include Email, Lambda, SQS, HTTP, and Mobile. There is no message retention.

You can batch messages per API request (1-10) to save cost. Each message has a maximum size of 256KB; if you want to publish larger payload, can store the data in S3 and publish the S3 link to SNS.

### Topics

- Standard: Best-effort ordering and may contain duplication (unlimited messages per second)
- FIFO: Order is guaranteed (300 messages per second)

## SQS (Simple Queue Service)

SQS is a message queuing service. Using SQS, you can send, store, and receive messages between software components, without losing messages or requiring other services to be available.

In SQS, an application sends messages into the queue. A user or service retrieves a message from the queue, processes it, and then deletes it from the queue. Messages are kept up to 14 days.

### Queues

- Standard
- FIFO

### Features

- Message retention
- Message prioritization
- Dead Letter Queue (DLQ)

## Amazon MQ

SQS and SNS are cloud-native services and are using proprietary protocols from AWS. However, traditional applications running from on-premises may use open-source protocols including MQTT, AMQP, STOMP, Openwire, WSS, etc.

When migrating to the cloud, instead of re-engineering the application to use SQS and SNS, you can use Amazon MQ. Amazon MQ is a managed **message broker service for RabbitMQ and ActiveMQ**. MQ has both queue feature (SQS) and topic features (SNS). However, SQS and SNS scales better and are more integrated with the cloud.

## AWS EventBridge

AWS EventBridge is a serverless, fully-managed and scalable event bus that enables integrations between AWS services, software services, and your applications.

By default, you will have a default event bus. You can also create custom event bus or partner event bus. You also need to define rules to forward the events to the necessary locations e.g. Lambda, SNS, etc.

### Pipes

Pipe is about routing events from a single source to a single target i.e. point-to-point integrations between producer and consumer. It can also perform filtering, data transformation and enrichment i.e. similar to RxJS pipes.

### Features

- Decoupling and scalability
- Event processing at scale
- Event routing and filtering capabilities
- Event replay
- Low code integrations
- Schema registry
- Automatic retries with exponential backoff
- High availability

## AWS Simple Email Service (SES)

Utilizes AWS infrastructure to reliably send out emails.

### Features

- Verified identities i.e. proof that you own domain
- Reduce email bounces and delivery failures
- High-volume traffic
- Sender identity management and security i.e. Domain Keys Identified Mail (DKIM), Sender Policy Framework (SPF), Domain-Based Message Authentication, Reporting and Conformance (DMARC)
- Reputation dashboard
- Email templates
- Mailbox simulator
- Dedicated IP pool allows the firm to manage its own email sending reputation i.e. ensure emails are not marked as spam

## AWS Step Functions

Step functions help to solve complex workflows using Saga Pattern. Step Function ensures seamless and reliable order fulfillment.

### Features

- Workflow orchestration
- Parallelized steps
- Error handling, retries and escalations
- Workflow visualization

### Integration

- Compute
- Database
- Messaging service
- Machine learning
- analytics services
- API gateway

## AWS Simple Workflow Service (SWS)

Similar to Step Functions, and should be used in general. However, you can use SWS if you require external signals to intervene in your processes e.g. launch child processes from a parent and return a result.

### Features

- State tracker and task coordinator
- Workflow orchestration
- Task assignment and scheduling
- Use programming languages to build out orchestration logic (flexible)

## AWS Managed Apache Airflow (MWAA)

A managed instance of Apache Airflow. MWAA coordinates ETL jobs, and can be used to prepare ML data.

### Features

- Abstracts the infrastructure and simplifies the deployment and management
- Scalability and performance optimization
- High availability and fault tolerance
- Managed environment with Control Plane
- Built-in security with AWS KMS

## Amazon Kinesis

Kinesis is a real-time big data streaming service to collect, process and analyze real-time streaming data at any scale. The event sources include click streams, IoT devices, metrics and logs, etc.

### Features

- Real-time data processing
- Scalability by using shards
- Data durability and availability (replicated across AZ)
- Custom application building

### Data Firehose

Have the ability to perform ETL before streaming the data to its output.

## AWS Managed service for Kafka (MSK)

### Features

- Server/Serverless
- Automated cluster management
- Scalability and performance
- Security and compliance
- Reliability and high availability

## AWS Glue

AWS Glue is a serverless ETL service that is useful to prepare and transform data for analytics.

### Features

- Serverless
- Centralized data catalog for multiple sources
- Automatic schema discovery
- Visual ETL job authoring
- Built-in transformation libraries e.g. PySpark to run natively

## AWS Elastic MapReduce (EMR)

EMR runs in managed cluster and can be used to process data at scale for analytics purposes.

### Cluster

A cluster in a collection of EC2 instances/nodes with different responsibilities:

- Primary: Manages the cluster and coordinates the distribution of data and tasks among other nodes
- Core: Stores and crunches data
- Task (optional): Data processing only

### Features

- Managed Hadoop framework
- Scalability and availability
- Cost-effective processing e.g. spot pricing
- Integrates with other AWS services
- Security and compliance

## AWS Glue Databrew

Glue Databrew is a visual preparation tool that allows you to clean and normalize data (no code needed).

### How it works

1. Create projects
2. Select datasets i.e. input sources
3. Select recipes i.e. transformations
4. Run jobs
5. Data stored in S3

### Features

- Visual data preparation
- Data profiling
- Scalability and performance
- Job scheduling and reusability
