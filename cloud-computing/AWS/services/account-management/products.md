## AWS Organizations

You can use AWS Organizations (free service) to consolidate and manage multiple AWS accounts within a central location i.e. a company having multiple AWS accounts. You can use it to share resources across your AWS accounts.

### Service Control Policies (SCPs)

You can centrally control permissions for the accounts in your organization (individual member account, OUs) by using SCPs. SCPs enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.

SCPs are similar to IAM policies but **never grant permissions**.

### Organization units (OUs)

You can group accounts into OUs to make it easier to manage accounts with similar business or security requirements i.e. HR, Prod, Finance, etc.

### Consolidated billing

AWS Organizations provides the option for consolidated billing i.e. receive a single bill for all AWS accounts in your organization. **The default maximum number of accounts allowed for an organization is 4**, but you can contact AWS Support to increase your quota, if needed.

Another benefit is the ability to share bulk discount pricing, Savings Plans, and Reserved Instances across the accounts in your organization. For instance, one account may not have enough monthly usage to qualify for discount pricing. However, when multiple accounts are combined, their aggregated usage may qualify for this benefit.

## AWS Control Tower

An easy way to setup and govern a secure and compliant multi-account AWS environment based on best practices. Helps to automate/streamline the process of creating a new account with the necessary permissions and guardrails.

Runs on top of AWS Organizations i.e. automatically sets up AWS Organizations to organize accounts and implement SCPs.

### Guardrails

AWS Control Tower applies preventive and detective controls (guardrails) to help keep your organizations and accounts from divergence from best practices (drift):

- Preventive: Proactive measures to prevent issues; usually implemented through IAM policies, AWS Config
- Detective: Reactive measures to detect and respond to issues

### Features

- Simplified multi-account environments
- Reduce risk of human error when creating an account
- Automated policy enforcement
- Improve operational efficiency
- Continuous monitoring for policy compliance
