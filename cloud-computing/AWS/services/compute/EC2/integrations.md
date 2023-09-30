## SNS (Amazon Simple Notification Service)

SNS is a pub/sub service. In SNS, subscribers can be web servers, email addresses, AWS Lambda functions, etc. Each subscriber to the topic will get **all the messages**.

Subscribers from AWS include Email, Lambda, SQS, HTTP, and Mobile. There is no message retention.

## SQS (Simple Queue Service)

SQS is a message queuing service. Using SQS, you can send, store, and receive messages between software components, without losing messages or requiring other services to be available.

In SQS, an application sends messages into the queue. A user or service retrieves a message from the queue, processes it, and then deletes it from the queue. Messages are kept up to 14 days.

## Amazon Kinesis

Kinesis is a real-time big data streaming service to collect, process and analyze real-time streaming data at any scale. The event sources include click streams, IoT devices, metrics and logs, etc.

## Amazon MQ

SQS and SNS are cloud-native services and are using proprietary protocols from AWS. However, traditional applications running from on-premises may use open-source protocols including MQTT, AMQP, STOMP, Openwire, WSS, etc.

When migrating to the cloud, instead of re-engineering the application to use SQS and SNS, you can use Amazon MQ. Amazon MQ is a managed **message broker service for RabbitMQ and ActiveMQ**. MQ has both queue feature (SQS) and topic features (SNS). However, SQS and SNS scales better and are more integrated with the cloud.
