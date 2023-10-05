## AWS Lambda

Serverless compute service that is **event-driven** and responsible for executing code on schedule. No need for provisioning and managing servers, and executes code only when required (pay by compute time or number of invoked calls). Useful for executing CRON jobs.

With serverless computing, you can focus more on innovating new products and features instead of maintaining servers. Another benefit is the flexibility to scale serverless applications automatically.

### How Lambda Works

1. You upload code (containing a function) to Lambda
2. Set your code to trigger from an event source i.e. HTTP endpoints, AWS services
3. An event is a JSON-formatted document that contains data for a Lambda function to process
4. Lambda runs your code only when triggered
5. You pay only for the compute time you use (number of times invoked and time taken to run)

## Amazon API Gateway

The Amazon API Gateway is a serverless and scalable service used for building a serverless API service with AWS Lambda. It will proxy the request to AWS Lambda. Supports RESTful APIs and WebSocket APIs.

## Lightsail

Enables a VPS to be launched and managed with ease. It is a simpler alternative to using EC2, RDS, ELB, EBS, Route 53, etc. It is great for people with minimal cloud experience.

It has high availability but no auto-scaling, and limited AWS integrations with other resources.

## Amazon Elastic Container Service (ECS)

Containers provide you a standard way to package your application's code and dependencies into a single object. You can use containers for processes and workflows in which there are essential requirements for security, reliability and scalability.

AWS ECS is a highly scalable, high-performance container management system that enables you to run and scale containerized applications on AWS.

ECS supports Docker containers. You can use API calls to launch and stop Docker-enabled applications.

To prepare your application to run on Amazon ECS, you create a **task definition**. It is a text file in JSON format that describes one or more containers. A task definition is similar to a blueprint that describes the resources that you need to run a container i.e. CPU, memory, ports, images, storage, and networking information.

```json
{
  "family": "webserver",
  "containerDefinitions": [
    {
      "name": "web",
      "image": "nginx",
      "memory": "100",
      "cpu": "99"
    }
  ],
  "requiresCompatibilities": ["FARGATE"],
  "networkMode": "awsvpc",
  "memory": "512",
  "cpu": "256"
}
```

### Running containers in EC2 instances

If you choose to have more control by running and managing your containers on a cluster of EC2 instances, you will need to install ECS container agent on your EC2 instances. An EC2 instance with the container agent is often called a **container instance**. The container agent is responsible for communicating to Amazon ECS service about cluster management details.

## Amazon Elastic Kubernetes Service (EKS)

AWS EKS is a fully managed service that you can use to run Kubernetes on AWS.

### EKS vs ECS

Both are conceptually similar but with the following differences:

- In Amazon ECS, the machine that runs the containers is an EC2 instance that has an ECS agent installed and configured (container instance)
- In Amazon EKS, the machine that runs the containers is called a Worker Node
- An ECS container is called a task, while an EKS container is a called a pod
- Amazon ECS runs on AWS native technology, while EKS runs on Kubernetes

## Fargate

AWS Fargate is a serverless compute engine for containers. It works with both ECS and EKS. When using Fargate, you don't need to provision or manage servers. AWS Fargate manages your server infrastructure for you.

## Amazon Elastic Container Registry (ECR)

ECR is a private Docker Registry on AWS that is used to store your Docker images so that they can be run by ECS or Fargate.

## AWS Batch

AWS Batch is fully managed service that performs batch processing at any scale. Batch will **dynamically launch EC2 instances or Spot Instances**, and will provision the right amount of compute and memory.

Batch jobs are defined as Docker images and run on ECS.

### Batch vs Lambda

AWS Lambda has time limit (15 minutes), limited runtimes, and limited temporary disk space, and is serverless.

AWS Batch has no time limit with any runtime, relies on EBS/Instance Store for disk space and relies on EC2.

## Amazon EMR

Amazon EMR is the industry-leading cloud big data platform for processing vast amounts of data using open source tools such as Hadoop, Apache Spark, Apache Hive, Apache HBase, Apache Flink, Apache Hudi, and Presto.
