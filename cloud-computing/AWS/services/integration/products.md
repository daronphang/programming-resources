## Amazon API Gateway

The Amazon API Gateway is a serverless and scalable service used for building a serverless API service with AWS Lambda. It will proxy the request to AWS Lambda. Supports RESTful APIs and WebSocket APIs.

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

## Amazon Kinesis

Kinesis is a real-time big data streaming service to collect, process and analyze real-time streaming data at any scale. The event sources include click streams, IoT devices, metrics and logs, etc.

## Amazon MQ

SQS and SNS are cloud-native services and are using proprietary protocols from AWS. However, traditional applications running from on-premises may use open-source protocols including MQTT, AMQP, STOMP, Openwire, WSS, etc.

When migrating to the cloud, instead of re-engineering the application to use SQS and SNS, you can use Amazon MQ. Amazon MQ is a managed **message broker service for RabbitMQ and ActiveMQ**. MQ has both queue feature (SQS) and topic features (SNS). However, SQS and SNS scales better and are more integrated with the cloud.

## AWS EventBridge

AWS EventBridge is a serverless, fully-managed and scalable event bus that enables integrations between AWS services, software services, and your applications.

### Features

- Decoupling and scalability
- Event processing at scale
- Event routing and filtering capabilities
