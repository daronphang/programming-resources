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

A paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks, and with **24/7 support**.

It also integrates with other services such as Amazon CloudFront, Amazon Route 53, and Elastic Load Balancing.

## AWS Key Management Service (KMS)

You must ensure that your applications' data is secure while in storage (**encryption at rest**) and while it is transmitted (**encryption in transit**).

AWS KMS enables you to perform encryption operations through the use of cryptographic keys. You can use AWS KMS to create, manage and use cryptographic keys. Your keys never leave KMS, and you are always in control of them.

Types of Customer Master Keys (CMK):

- Customer managed CMK: Created by the customer
- AWS managed CMK: Used by AWS services
- AWS owned CMK: Used to protect resources in your account
- **CloudHSM** Keys: Keys generated from your own CloudHSM hardware device

## AWS Web Application Firewall (WAF)

AWS WAF is a web application firewall that lets you monitor network requests that come into your web applications. Fucntions at Layer 7 (HTTP/HTTPS).

AWS WAF works together with Amazon CloudFront and an Application Load Balancer. It works in a similar way as network ACLs by using a **web ACL** to protect your AWS resources i.e. by restricting IP addresses, SQL injection, XSS, etc.

## Amazon Inspector

Amazon Inspector helps to improve the security and compliance of applications by running **automated security assessments**. It checks applications for security vulnerabilities and deviations from security best practices, such as open access to EC2 instances and installations of vulnerable software versions.

After assessment, it provides you with a list of security findings with a risk score for prioritization. However, AWS does not guarantee that following provided recommendations resolves every potential security issue.

## Amazon GuardDuty

Amazon GuardDuty is a service that provides intelligent threat detection for your AWS infrastructure and resources. It identifies threats by continuously monitoring the network security and account behavior within your AWS environment by analyzing data from multiple AWS sources including:

- VPC Flow Logs
- CloudTrail Events Logs
- DNS Logs

If an anomaly is detected, an event can be created in EventBridge to trigger automations including SNS or Lambda functions. GuardDuty can protect against cryptocurrency attacks (has a dedicated 'finding').

## Amazon Macie

Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern maching to discover and protect your sensitive data in AWS. Macie helps identify and alert you to sensitive data, such as personally identifiable information (PII).

## AWS Secrets Manager

AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. Secrets are encrypted using KMS.

## AWS Network Firewall

Protects your entire VPC from Layer 3 to Layer 7. You can inspect, in any direction:

- VPC to VPC traffic
- Outbound to internet
- Inbound from internet
- To/from Direct Connect and Site-to-Site VPN

## Penetration Testing

You can perform pentration testing on your AWS infrastructure. However, prohibited activities include:

- DNS zone walking
- DoS, DDoS, Simulated DoS, Simulated DDoS
- Port flooding
- Protocol flooding
- Request flooding

## AWS Certificate Manager (ACM)

Allows you to easily provision, manage and deploy SSL/TLS certificates. Supports both public (free) and private TLS certificates.

## AWS Config

Helps with auditing and compliance of your AWS resources by recording configurations and changes over time.

## AWS Security Hub

Central security tool to manage security across several AWS accounts and automate security checks. Aggregates alerts and findings from various AWS services into a consolidated dashboard:

- Config
- GuardDuty
- Inspector
- Macie
- IAM Access Analyzer

## Amazon Detective

Amazon Detective analyzes, investigates, and quickly identifies the root cause of security issues or suspicious activities using ML and graphs. Automatically collects and processes events from:

- VPC Flow Logs
- CloudTrail
- GuardDuty

## AWS Abuse

Service used to report AWS resources suspected of using abusive or illegal purposes including:

- Spam
- Port scanning (sending packets to your ports to discover unsecured ones)
- DDoS
- Intrusion attempts (logging into your resources)
- Hosting copyrighted content
- Distributing malware

## IAM Access Analyzer

Service used to find out which resources are shared externally including:

- S3 Buckets
- IAM Roles
- KMS Keys
- Lambda functions
- Secrets Manager Secrets

Need to define Zone of Trust, and any access outside will be flagged as findings.
