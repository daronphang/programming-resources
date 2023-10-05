## AWS Billing & Cost Management dashboard

Use the AWS Billing & Cost Management dashboard to pay your AWS bill, monitor your usage, and analyze and control your costs.

### Cost Allocation Tags

Use cost allocation tags to track your AWS costs on a detailed level. For each resource, each tag key must be unique, and each tag key can only have one value. You must also activate both AWS generated tags and user-defined tags separately before they can appear in Cost Explorer or on a cost allocation report.

## AWS Organizations

You can use AWS Organizations to consolidate and manage multiple AWS accounts within a central location i.e. a company having multiple AWS accounts. You can use it to share resources across your AWS accounts.

You can centrally control permissions for the accounts in your organization (individual member account, OUs) by using **service control policies** (SCPs). SCPs enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.

### Organization units (OUs)

You can group accounts into OUs to make it easier to manage accounts with similar business or security requirements i.e. HR, Prod, Finance, etc.

### Consolidated billing

AWS Organizations provides the option for consolidated billing i.e. receive a single bill for all AWS accounts in your organization. **The default maximum number of accounts allowed for an organization is 4**, but you can contact AWS Support to increase your quota, if needed.

Another benefit is the ability to share bulk discount pricing, Savings Plans, and Reserved Instances across the accounts in your organization. For instance, one account may not have enough monthly usage to qualify for discount pricing. However, when multiple accounts are combined, their aggregated usage may qualify for this benefit.

## AWS Control Tower

An easy way to setup and govern a secure and compliant multi-account AWS environment based on best practices. Runs on top of AWS Organizations i.e. automatically sets up AWS Organizations to organize accounts and implement SCPs.

## AWS Budgets

In AWS Budgets, you can create budgets to plan your service usage, service costs, and instance reservations.

The information in AWS Budgets updates **three times a day**. This helps you to accurately determine how close your usage is to your budgeted amounts or to the AWS Free Tier limits.

You can set custom alerts that will notify you when your service usage exceeds the amount you have budgeted. your budget can be based on cost or usage. You can also set reservation utilization or coverage targets and receive alerts when your utilization drops below the threshold you define.

## AWS Cost Explorer

AWS Cost Explorer is a tool that lets you visualize, understand, and manage your AWS costs and usage over time. You can **forecast usage up to 12 months based on previous usage**.

AWS Cost Explorer includes a default report of the costs and usage for your top five cost-accruing AWS services. You can apply custom filters and groups to analyze your data.

The rightsizing recommendations features helps you to identify cost-saving opportunities by downsizing or terminating EC2 instances. You can see all of your underutilized EC2 instances across member accounts in a single view.

## AWS Resource Access Manager (RAM)

Share AWS resources that you own with other AWS accounts to avoid resource duplication.

## AWS Service Catalog

Users that are new to AWS have too many options, and may create stacks that are not compliant with the rest of the organization. Service Catalog provides a quick self-service portal to launch a set of authorized products pre-defined by admins.

## AWS Service Quotas

Notify you when you are close to a service quota value threshold through CloudWatch alarms. You can request a quota increase from AWS Service Quotas or shutdown resources before limit is reached.

## AWS Cost & Usage Report (CUR)

CUR contains the most comprehensive set of cost and usage data available. You can receive reports that break down your costs by the hour or month, by product or resource, or by tags that you define yourself.
