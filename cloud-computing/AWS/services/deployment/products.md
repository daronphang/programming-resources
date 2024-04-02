## AWS CloudFormation (Infrastructure-as-a-Service)

AWS CloudFormation is a declarative way of outlining your AWS infrastructure through a **template (JSON/YAML)** i.e. treating **infrastructure as code**. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.

Each resource within the stack is tagged with an identifier so you can easily see how much a stack costs you. You can also estimate the cost of your resources using the CloudFormation template. When designing, you can see the **relations between the components**.

AWS CloudFormation provisions your resources in a safe and **repeatable manner**, enabling you to frequently build your infrastructure and applications without having to perform manual actions ie. rebuilding architecture across different Regions, accounts, etc. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors.

## AWS Cloud Development Kit (CDK)

CDK allows you to define your cloud infrastructure using a programming language instead of YAML i.e. JS, Python, Java, etc. The code is compiled into a CloudFormation template (JSON/YAML).

## AWS Elastic Beanstalk (Platform-as-a-Service)

Helps to scale and deploy web applications made with several programming languages. AWS Elastic Beanstalk handles the deployment of the code as soon as it is uploaded. Beanstalk is free but you have to pay for the underlying resources. **All resources are created by CloudFormation** behind the scenes.

With AWS Elastic Beanstalk, you **only provide code and configuration settings**, and EBS deploys the resources necessary to perform the following tasks:

- Instance configuration
- Deployment strategy
- Managed platform updates
- Load balancing and auto-scaling
- Application health monitoring (health agent pushes metrics to CloudWatch)

## AWS CodeDeploy

CodeDeploy is a hybrid service (EC2, on-premise) that deploys your application automatically. Servers must be provisioned and configured ahead of time with the CodeDeploy agent.

CodeDeploy allows you to upgrade your EC2 instances, applications, and your on-premise server applications from version 1 to version 2.

## AWS Systems Manager (SSM)

SSM helps you to manage your EC2 and on-premise systems at scale (hybrid). It allows you to get operational insights about the state of your infrastructure. Most important features include:

- Patching automation for enhanced compliance
- Running commands across an entire fleet of servers
- Storing parameter configuration with the SSM Parameter Store

The SSM agent needs to be installed on the systems we want to control.

### SSM Session Manager

Allows you to start a secure shell on your EC2 and on-premise servers. You do not need to provide SSH access, bastion hosts, or SSH keys for your compute instances (enhanced security). You need to attach an IAM role to the EC2 instance to allow it to talk to the SSM service.

Sends session log data to S3 or CloudWatch logs.

## AWS OpsWorks

Chef and Puppet (external software) help you to perform server configuration automatically or repetitive actions. They integrate with EC2 and on-premise VM. OpsWorks was created to give you a managed Chef and Puppet in the cloud (alternative to SSM). However, it allows you to **only provision standard AWS resources**.

## AWS App Runner

AWS App Runner is a fully managed application service that lets you build, deploy, and run web applications and API services without prior infrastructure or container experience.

AWS App Runner builds and deploys web applications automatically, load balances traffic with encryption, scales to meet your traffic needs, and allows for the configuration of how services are accessed and communicate with other AWS applications in a private Amazon VPC.

You can either push code to ECR or git repository.

```
Developer -> push to ECR -> Deploy on App Runner
```

```
Developer -> push to git -> trigger AWS CodeBuild to run tests and push to ECR -> Deploy on AWS Runner
```

To securely access AWS services in private VPCs, you can use a **VPC connector**.

### Features

- Manages infrastructure
- Creates CI/CD pipeline automatically
- Automatically deployment
- Scalability
- Cost-effective

## Serverless Application Model (SAM)

SAM helps to simplify developer's experience in getting out the infrastructure and deployed on AWS Lambda. SAM template is a configuration file that you need to define. Comes with CLI tool.

## Serverless Application Repository (SAR)

Other people can search and discover serverless applications in the repository.

```
Select from SAR -> Create CloudFormation templates from SAM templates -> Deploy resources e.g. API Gateway, Lambda
```

### Features

- Integrated with AWS SAM
- Centralized repository
- Rapid deployment
- Reusable applications
- Public and private sharing

## AWS Amplify

A complete solution for building web and mobile applications. Abstracts AWS services to simplify the process of deploying the applications.

### Features

- Rapid deployment
- Fullstack deployment e.g. authentication, API, storage, hosting, analytics
- Amplify Studio is a visual development environment that integrates with Amplify CLI to manage backend services using graphical interface
- Has pre-built React components for frontend usage
- Support multiple platforms
