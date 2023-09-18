## EC2 (Elastic Cloud Compute)

Provides compute capacity in the cloud that is secure and resizable based on the user's requirements. Web service that allows developers to rent VMs and automatically scales the compute capacity when required.

Offers various instance types so that developers can choose required resources including CPU, memory, storage and networking capacity.

## Lambda

Serveless compute service that is responsible for executing code on schedule. No need for provisioning and managing servers, and executes code only when required (pay only for compute time).

With serverless computing, you can focus more on innovating new products and features instead of maintaining servers. Another benefit is the flexibility to scale serverless applications automatically.

### How Lambda Works

1. You upload code (containing a function) to Lambda
2. Set your code to trigger from an event source i.e. HTTP endpoints, AWS services
3. An event is a JSON-formatted document that contains data for a Lambda function to process
4. Lambda runs your code only when triggered
5. You pay only for the compute time you use (number of times invoked and time taken to run)

## Elastic Beanstalk

Helps to scale and deploy web applications made with several programming languages. AWS Elastic Beanstalk handles the deployment of the code as soon as it is uploaded.

With AWS Elastic Beanstalk, you provide code and configuration settings, and EBS deploys the resources necessary to perform the following tasks:

- Adjust capacity
- Load balancing
- Automatic scaling
- Application health monitoring

## Lightsail

Enables a VPS to be launched and managed with ease.

## Amazon ECS (Elastic Container Service)

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

## Amazon EKS (Elastic Kubernetes Service)

AWS EKS is a fully managed service that you can use to run Kubernetes on AWS.

### EKS vs ECS

Both are conceptually similar but with the following differences:

- In Amazon ECS, the machine that runs the containers is an EC2 instance that has an ECS agent installed and configured (container instance)
- In Amazon EKS, the machine that runs the containers is called a Worker Node
- An ECS container is called a task, while an EKS container is a called a pod
- Amazon ECS runs on AWS native technology, while EKS runs on Kubernetes

## Fargate

AWS Fargate is a serverless compute engine for containers. It works with both ECS and EKS. When using Fargate, you don't need to provision or manage servers. AWS Fargate manages your server infrastructure for you.

## CloudFormation

With AWS CloudFormation, you can treat infrastructure as code. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.

AWS CloudFormation provisions your resources in a safe, repeatable manner, enabling you to frequently build your infrastructure and applications without having to perform manual actions. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors.

## Elastic Load Balancing (ELB)

ELB is a servie that can distribute incoming application traffic across EC2 instances, containers, IP addresses, and Lambda functions. Key features include:

- **Hybrid mode**: As ELB can load balance to IP addresses, it can work in hybrid mode i.e. load balances to on-premises servers
- **High availability**: ELB is highly available
- **Scalability**: ELB automatically scales to meet the demand of the incoming traffic.

### Health checks

Monitoring is an important part of load balancers as they should route traffic to only healthy EC2 instances.
