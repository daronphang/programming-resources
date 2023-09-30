## AWS CloudFormation (Infrastructure-as-a-Service)

AWS CloudFormation is a declarative way of outlining your AWS infrastructure through a **template (JSON/YAML)** i.e. treating **infrastructure as code**. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.

Each resource within the stack is tagged with an identifer so you can easily see how much a stack costs you. You can also estimate the cost of your resources using the CloudFormation template. When designing, you can see the **relations between the components**.

AWS CloudFormation provisions your resources in a safe and **repeatable manner**, enabling you to frequently build your infrastructure and applications without having to perform manual actions ie. rebuilding architecture across different Regions, accounts, etc. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors.

## AWS Cloud Development Kit (CDK)

CDK allows you to define your cloud infrastructure using a programming language instead of YAML i.e. JS, Python, Java, etc. The code is compiled into a CloudFormation template (JSON/YAML).

## AWS Elastic Beanstalk (Platform-as-a-Service)

Helps to scale and deploy web applications made with several programming languages. AWS Elastic Beanstalk handles the deployment of the code as soon as it is uploaded. Beanstalk is free but you have to pay for the underlying resources. **All resources are created by CloudFormation** behind the scenes.

With AWS Elastic Beanstalk, you **only provide code and configuration settings**, and EBS deploys the resources necessary to perform the following tasks:

- Instance configuration
- Deployment strategy
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
