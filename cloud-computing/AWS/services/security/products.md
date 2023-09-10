## IAM (Identity Access Management)

A web service that helps in maintaining access to AWS services in a secure way. Enables you to create and control services for user authentication or limit access to a certain set of people who use your AWS resources.

## AWS Organizations

You can use AWS Organizations to consolidate and manage multiple AWS accounts within a central location i.e. a company having multiple AWS accounts.

You can centrally control permissions for the accounts in your organization (individual member account, OUs) by using **service control policies** (SCPs). SCPs enable you to place restrictions on the AWS services, resources, and individual API actions that users and roles in each account can access.

### Organization units (OUs)

You can group accounts into OUs to make it easier to manage accounts with similar business or security requirements.

## AWS Artifact

AWS Artifact is a service that provides on-demand access to AWS security and compliance reports and select online agreements for audit purposes.

### Artifact Agreements

You can use AWS Artifact Agreements if your company needs to sign an agreement with AWS regarding your use of certain types of information throughout AWS services.

### Artifact Reports

AWS Artifact Reports provide compliance reports from third-party auditors. You can provide them to your auditors or regulators as evidence of AWS security controls.

## Customer Compliance Center

The Customer Compliance Center contains resources to help you learn more about AWS compliance. You can read compliance stories to discover how companies in regulated industries have solved various compliance, governance, and audit challenges.

## AWS Shield

AWS Shield is a service that protects applications against DDoS attacks.

### Standard

Automatically protects all AWS customers at no cost. It protects your AWS resources from the most common, frequently occurring types of DDoS attacks.

As network traffic comes into your applications, AWS Shield Standard uses a variety of analysis techniques to detect malicious traffic in real time and automatically mitigates it.

### Advanced

A paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks.

It also integrates with other services such as Amazon CloudFront, Amazon Route 53, and Elastic Load Balancing.

## AWS Key Management Service (KMS)

You must ensure that your applications' data is secure while in storage (**encryption at rest**) and while it is transmitted (**encryption in transit**).

AWS KMS enables you to perform encryption operations through the use of cryptographic keys. You can use AWS KMS to create, manage and use cryptographic keys. Your keys never leave KMS, and you are always in control of them.

## AWS Web Application Firewall (WAF)

AWS WAF is a web application firewall that lets you monitor network requests that come into your web applications.

AWS WAF works together with Amazon CloudFront and an Application Load Balancer. It works in a similar way as network ACLs by using a **web ACL** to protect your AWS resources i.e. by restricting IP addresses.

## Amazon Inspector

Amazon Inspector helps to improve the security and compliance of applications by running **automated security assessments**. It checks applications for security vulnerabilities and deviations from security best practices, such as open access to EC2 instances and installations of vulnerable software versions.

After assessment, it provides you with a list of security findings. However, AWS does not guarantee that following provided recommendations resolves every potential security issue.

## Amazon GuardDuty

Amazon GuardDuty is a service that provides intelligent threat detection for your AWS infrastructure and resources. It identifies threats by continuously monitoring the network security and account behavior within your AWS environment by analyzing data from multiple AWS sources including VPC Flow Logs and DNS logs.

## Amazon Macie

Amazon Macie is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS.

## AWS Secrets Manager

AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources.
