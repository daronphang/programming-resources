## AWS Billing & Cost Management dashboard

Use the AWS Billing & Cost Management dashboard to pay your AWS bill, monitor your usage, and analyze and control your costs.

### Cost Allocation Tags

Use cost allocation tags to track your AWS costs on a detailed level. For each resource, each tag key must be unique, and each tag key can only have one value. You must also activate both AWS generated tags and user-defined tags separately before they can appear in Cost Explorer or on a cost allocation report.

### Guardrails

When you spin up a new account, it is going to have all the necessary guardrails:

- Preventive: Proactive measures to prevent issues; usually implemented through IAM policies, AWS Config
- Detective: Reactive measures to detect and respond to issues

### Features

- Simplified multi-account environments
- Reduce risk of human error when creating an account
- Automated policy enforcement
- Improve operational efficiency
- Continuous monitoring for policy compliance

## AWS Budgets

AWS Budgets is about limiting and notifying and not for analysis. In AWS Budgets, you can create budgets to plan your service usage, service costs, and instance reservations.

The information in AWS Budgets updates **three times a day**. This helps you to accurately determine how close your usage is to your budgeted amounts or to the AWS Free Tier limits.

You can set custom alerts that will notify you when your service usage exceeds the amount you have budgeted. your budget can be based on cost or usage. You can also set reservation utilization or coverage targets and receive alerts when your utilization drops below the threshold you define.

## AWS Cost Explorer

AWS Cost Explorer is a tool that lets you visualize, understand, and manage your AWS costs and usage over time. You can **forecast usage up to 12 months based on previous usage**.

AWS Cost Explorer includes a default report of the costs and usage for your top five cost-accruing AWS services. You can apply custom filters and groups to analyze your data.

The rightsizing recommendations features helps you to identify cost-saving opportunities by downsizing or terminating EC2 instances. You can see all of your underutilized EC2 instances across member accounts in a single view.

## AWS Resource Access Manager (RAM)

Share AWS resources that you own with other AWS accounts to avoid resource duplication.

### Workflow

1. Create a resource share
2. Select resources to share
3. Choose principals
4. Accept the resource share request
5. Monitor and manage resource share

## AWS Service Quotas

Notify you when you are close to a service quota value threshold through CloudWatch alarms. You can request a quota increase from AWS Service Quotas or shutdown resources before limit is reached.

## AWS Cost & Usage Report (CUR)

CUR contains the most comprehensive set of cost and usage data available. You can receive reports that break down your costs by the hour or month, by product or resource, or by tags that you define yourself.
