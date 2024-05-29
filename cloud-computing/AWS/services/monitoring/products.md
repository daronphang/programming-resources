## Amazon CloudWatch

Amazon CloudWatch **collects and visualizes real-time logs, metrics, and event data** in automated dashboards to streamline your infrastructure and application maintenance. You can also configure alarm actions based on data from those metrics. AWS resources send metrics and logs to CloudWatch, which uses them to create graphs automatically and show how performance has changed over time.

CloudWatch is built for DevOps engineers, developers, site reliability engineers (SREs) and IT managers. It provides data and actionable insights to monitor applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health.

For instance, you can create an alarm that automatically stops an EC2 instance when the CPU utilization percentage remains below a certain threshold for a specified period.

### Metrics

Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch. AWS resources send metrics to CloudWatch for free at a rate of 1 data point per metric per 5-minute interval.

Built-in metrics available include:

- CPU utilization
- Network utilization
- Disk reads

### Custom Metrics

Metrics that require scripts include:

- Memory utilization
- Disk swap utilization
- Disk space utilization
- Page file utilization
- Log collection

Options for custom metrics include:

- High-resolution: Data at a granularity of one second (similar to detailed monitoring)
- Statistic sets: For data aggregation

### Unified CloudWatch agent

The unified CloudWatch agent enables you to do the following:

- Collect internal system-level metrics from Amazon EC2 instances and on-premise servers
- Retrieve custom metrics from your applications or services using the StatsD and collectd protocols
- Collect logs from Amazon EC2 instances and on-premises servers

### SDK

Developers can integrate their custom applications with CloudWatch CDK to send custom logs and metrics.

### Logs

By default, no logs from your EC2 instance are pushed to CloudWatch. You need to run a CloudWatch agent on EC2 to push the log files you want.

### Canaries

You can use CloudWatch Canaries to create scripted interactions and simulate user behavior to ensure that the applications are responsive and functioning correctly around the clock.

## AWS X-Ray

Allows you to get visual analysis of your applications by **tracing requests made through your distributed applications**. Can be used for the following:

- Troubleshooting performance (bottlenecks)
- Understanding dependencies in a microservice architecture
- Pinpoint service issues
- Review request behavior
- Find errors and exception
- Meeting SLA (service level agreements)

## AWS Health Dashboard (Service, Personal)

AWS Health provides ongoing visibility into your resource performance and the availability of your AWS services and accounts.

For service, shows the health for all Regions and services. For account, it provides alerts and remediation guidance when AWS is experiencing events that may impact you.

While the Service Health Dashboard displays the general status of AWS services, Personal Health dashboard gives you a personalized view of the performance and availability of the AWS services underlying your AWS resources.

### Features

- Reduce downtime and improve reliability
- Event visibility
- Service and Personal Health Dashboard
- Integration and automation

## AWS Prometheus

Open-source monitoring solution that stores data in a time-series database.

### Features

- Scalability
- Integrated with AWS
- Fully-managed
- PromQL support
- Cost efficient

## AWS Grafana

AWS Grafana does not use IAM roles for authorization; instead, use Amazon Identity Center or 3rd party Identity Providers for user authentication and authorization to control access to Grafana dashboards.

For permissions, implement customer-managed permissions to provide fine-grained access control tailored to specific user groups and roles within the organization.

### Features

- Can be used to query metrics from services including Prometheus, CloudWatch, TimeStream, X-Ray, etc.
- Single sign-on (SSO) integration

## AWS Trusted Advisor

AWS Trusted Advisor is a web service that inspects your AWS environment and provides **real-time recommendations** to help you provision your resources in accordance with AWS best practices.

Trusted Advisor compares its findings to AWS best practices in five categories:

- Cost optimization
- Performance
- Security
- Fault tolerance
- Service limits

In the dashboard, it has three categories:

- Green check indicates items for which it detected no problems
- Orange triangle represents recommended investigations
- Red circle represents recommended actions

### Support Plans

There are core checks for each category.

#### Basic & Developer

- S3 Bucket permissions
- Security Groups (unrestricted ports)
- IAM user (one IAM user minimum)
- MFA on Root Account
- EBS Public Snapshots
- RDS Public Snapshots
- Service Limits

#### Business & Enterprise

Inclusive of basic, with additional of:

- Ability to set CloudWatch alarms when reaching limits
- Programmatic access using AWS Support API

## AWS Compute Optimizer

A service that performs resource analysis for compute resources and identifies over-provisioned, under-provisioned, or already optimized. It offers recommendations on instance types and sizes based on usage patterns, but **does not directly address security concerns**.

Reduce costs and improve performance by recommending optimal AWS resources for your workloads using ML to analyze your resources' configurations and their utilization CloudWatch metrics. Helps you choose optimal configurations and right-size your workloads (over/under provisioned). Resources include EC2 instance types, EBS volume configurations and Lambda function memory sizes.

### Features

- Performance and risk analysis
- Cost-saving recommendations
- EC2 instance type recommendations
- EBS volume recommendations
- Optimization for Fargate
