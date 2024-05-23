## AWS CloudFormation (Infrastructure-as-a-Service)

AWS CloudFormation is a declarative way of outlining your AWS infrastructure through a **template (JSON/YAML)** i.e. treating **infrastructure as code**. This means that you can build an environment by writing lines of code instead of using the AWS Management Console to individually provision resources.

Each resource within the stack is tagged with an identifier so you can easily see how much a stack costs you. You can also estimate the cost of your resources using the CloudFormation template. When designing, you can see the **relations between the components**.

AWS CloudFormation provisions your resources in a safe and **repeatable manner**, enabling you to frequently build your infrastructure and applications without having to perform manual actions ie. rebuilding architecture across different Regions, accounts, etc. It determines the right operations to perform when managing your stack and rolls back changes automatically if it detects errors.

### Features

- Infrastructure as Code (IAC)
- Consistent and repeatable deployments
- Version control
- Resource tracking
- Cost and efficiency

### StackSets

AWS CloudFormation StackSets extends the capability of stacks by enabling you to create, update, or delete stacks across multiple accounts and AWS Regions with a single operation.

## AWS Cloud Development Kit (CDK)

CDK allows you to define your cloud infrastructure using a programming language instead of YAML i.e. JS, Python, Java, etc. The code is compiled into a CloudFormation template (JSON/YAML).

```
CodeCommit -> Trigger CodePipeline -> Trigger CDK -> Generate CloudFormation Templates -> Deployment as stack
```

### Features

- Declarative approach
- Component reusability
- AWS construct library
- Automated synthesis
- Environment agnosticism

## AWS Elastic Beanstalk (Platform-as-a-Service)

Helps to scale and deploy web applications made with several programming languages. AWS Elastic Beanstalk handles the deployment of the code as soon as it is uploaded. Beanstalk is free but you have to pay for the underlying resources. **All resources are created by CloudFormation** behind the scenes.

With AWS Elastic Beanstalk, you **only provide code and configuration settings**, and EBS deploys the resources necessary to perform the following tasks:

- Instance configuration
- Deployment strategy
- Managed platform updates
- Load balancing and auto-scaling
- Application health monitoring (health agent pushes metrics to CloudWatch)

### X-Ray daemon

You can enable X-Ray daemon on EC2 instances to get insights into application performance and errors occurring in the production environment.

## AWS CodeDeploy

CodeDeploy is a hybrid service (EC2, on-premise) that deploys your application automatically. Servers must be provisioned and configured ahead of time with the CodeDeploy agent.

CodeDeploy allows you to upgrade your EC2 instances, applications, and your on-premise server applications from version 1 to version 2.

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

SAM is a toolkit that improves the developer experience of building and running serverless applications on AWS.

AWS SAM consists of three primary parts:

- SAM template specification: An open-source framework that you can use to define your serverless application infrastructure on AWS
- SAM template: An extension of CloudFormation templates
- SAM CLI: A command line tool that you can use with AWS SAM templates and supported third-party integrations to build and run your serverless applications

## Serverless Application Repository (SAR)

Other people can search and discover serverless applications in the repository. You can utilize the built-in semantic versioning during deployment for rollback.

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

A complete solution for building serverless web and mobile applications. Abstracts AWS services to simplify the process of deploying the applications. On the other hand, AppRunner runs containerized services.

### Features

- Rapid deployment
- Fullstack deployment e.g. authentication, API, storage, hosting, analytics
- Has pre-built React components for frontend usage
- Support multiple platforms
- Encrypts all data at-rest and in-transit automatically

### Amplify Studio

Amplify Studio is a visual development environment that integrates with Amplify CLI to manage backend services using graphical interface.

### DataStore

Amplify DataStore provides a persistent on-device storage repository for you to write, read, and observe changes to data if you are online or offline, and seamlessly sync to the cloud as well as across devices.

You can use Amplify DataStore for synchronized offline and online data storage to provide a consistent API layer. This helps to ensure that Amplify-generated APIs remain loosely coupled with the frontend, facilitating independent scalability and updates.

## AWS Launch Wizard

A service that simplifies the process of deploying well-known third party applications e.g. SQL Server, AD, SAP.

### How it works

1. Choose an application to deploy
2. Enter application specifications
3. Resource recommendation and cost estimate
4. Approval and resource provisioning
5. Configuration and template creation
6. Deployment and integration

### Features

- Simplified application deployment
- AWS resource selection
- Cost estimation
- Time-saving with repeatable code templates
- Cost-effectiveness

## AWS Service Catalog

Users that are new to AWS have too many options, and may create stacks that are not compliant with the rest of the organization. Service Catalog provides a quick self-service portal to launch a set of authorized products pre-defined by admins i.e. admins will curate and configure the services in the catalog. Users are given access to services based on their rules.

Service Catalog is a catalog of AWS resources that enables customers to store, share, and govern IaC templates and create individual stacks. **CloudFormation templates are used to deploy all the resources** i.e. each service in the catalog is a CloudFormation template. IAM policies are used to determine who has access to specific products within a catalog.

You can group products together in portfolios, and give users access to portfolios.

### Why use Service Catalog?

- Consistent deployments
- Governance and compliance
- Controlled spending

## AWS License Manager

A service that helps you manage software licenses across various vendors including Microsoft, SAP, Oracle, etc.

### Features

- Centralized license management
- License tracking
- Enforce licensing rules
- Cross-account management
- Discovery and reporting

## AWS Proton

AWS Proton is a deployment workflow tool for modern applications that helps platform and DevOps engineers achieve organizational agility. It can be used to manage Infrastructure as Code (IaC) templates build using tools like CloudFormation or Terraform. It helps to standardize the application stack and create a consistent environment across all deployments and services.

### Platform

1. Create Environment Templates that define shared resources using IaC
2. Deploy the environments
3. Create Service Templates that define the infrastructure, monitoring and CI/CD resources

### Developers

1. Choose a Service Template and link a source code package
2. Deploy a service that consists of service instances running the source code package as defined in the Service Template

### Benefits

- Automated deployments with CI/CD pipeline
- Flexible definitions
- Proton service components
- Multi-account support
- Template management
- Built-in security controls for ensuring environment and service templates are configured securely
