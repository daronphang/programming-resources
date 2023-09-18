## Amazon CloudWatch

Amazon CloudWatch is a web service that enables you to monitor and manage various metrics and configure alarm actions based on data from those metrics. AWS resources send metrics to CloudWatch, which uses them to create graphs automatically and show how performance has changed over time.

For instance, you can create an alarm that automatically stops an EC2 instance when the CPU utilization percentage remains below a certain threshold for a specified period.

### Metrics

Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch. AWS resources send metrics to CloudWatch for free at a rate of 1 data point per metric per 5-minute interval.

### Custom Metrics

To gain more granular visibility, you can use high-resolution custom metrics, which makes it possible for you to collect custom metrics down to a 1-second resolution.

## AWS CloudTrail

AWS CloudTrail records API calls for your account i.e. trail of breadcrumbs or log of actions that someone has left behind them. **You can use API calls to provision, manage and configure your AWS resources**. The recorded information includes (non-exhaustive):

- Identity of the API caller
- Time of the API call
- Source IP address

Events are typically updated in CloudTrail within 15 minutes after an API call. You can also filter events by specifying your criteria.

### CloudTrail Insights

This optional feature allows CloudTrail to automatically detect unusual API activities in your AWS account.

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
