## Amazon CloudWatch

Amazon CloudWatch is a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics. AWS resources send metrics and logs to CloudWatch, which uses them to create graphs automatically and show how performance has changed over time.

For instance, you can create an alarm that automatically stops an EC2 instance when the CPU utilization percentage remains below a certain threshold for a specified period.

### Metrics

Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch. AWS resources send metrics to CloudWatch for free at a rate of 1 data point per metric per 5-minute interval.

### Custom Metrics

To gain more granular visibility, you can use high-resolution custom metrics, which makes it possible for you to collect custom metrics down to a 1-second resolution.

### Logs

By default, no logs from your EC2 instance are pushed to CloudWatch. You need to run a CloudWatch agent on EC2 to push the log files you want.

## Amazon EventBridge (CloudWatch Events)

Used to react to events in AWS i.e. IAM root user signing in, or trigger a rule on a schedule i.e. CRON jobs.

### Event Bus

An event bus is a router that receives events and delivers them to zero or more destinations (targets). Event buses are well-suited for routing events from many sources to many targets, with optional transformation of events prior to delivery to a target.

You can send events to the following event buses:

- Default Event Bus (AWS Services)
- Partner Event Bus (external parties)
- Custom Event Bus

## AWS CloudTrail

AWS CloudTrail provides **governance, compliance and audit** for your AWS account by recording API calls made within your AWS account i.e. trail of breadcrumbs or log of actions that someone has left behind them. **You can use API calls to provision, manage and configure your AWS resources**.

The API calls made within your AWS accounts can come from:

- Console
- SDK
- CLI

The recorded information includes (non-exhaustive):

- Identity of the API caller
- Time of the API call
- Source IP address

Events are typically updated in CloudTrail within 15 minutes after an API call. You can also filter events by specifying your criteria. You can put logs from CloudTrail into CloudWatch Logs or S3 for longer term retention.

### CloudTrail Insights

This optional feature allows CloudTrail to automatically detect unusual API activities in your AWS account.

## AWS X-Ray

Allows you to get visual analysis of your applications by **tracing requests made through your distributed applications**. Can be used for the following:

- Troubleshooting performance (bottlenecks)
- Understanding dependencies in a microservice architecture
- Pinpoint service issues
- Review request behavior
- Find errors and exception
- Meeting SLA (service level agreements)

## AWS Health Dashboard (Service, Account)

For service, shows the health for all Regions and services. For account, it provides alerts and remediation guidance when AWS is experiencing events that may impact you.

## AWS Trusted Advisor

AWS Trusted Advisor is a web service that inspects your AWS environment and provides **real-time recommendations** in accordance with AWS best practices.

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
- IAM use (one IAM user minimum)
- MFA on Root Account
- EBS Public Snapshots
- RDS Public Snapshots
- Service Limits

#### Business & Enterprise

Inclusive of basic, with additional of:

- Ability to set CloudWatch alarms when reaching limits
- Programmatic access using AWS Support API
