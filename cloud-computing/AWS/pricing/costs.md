## AWS Costs

There are three fundamental drivers of cost with AWS: compute, storage and outbound data transfer. Outbound data transfer is aggregated across services and then charged at the outbound data transfer rate.

Charges are as follows:

- No charge for inbound data transfer across all services in all Regions
- No data transfer charges if IGW is used to access public endpoints of AWS services in the same Region
- Data passing through NAT gateway incurs data processing charge per GB
- Charge for data transfer across Regions
- Data transfer within the same AZ is free using private IPs
- Data transfer charges apply for cross-AZ communication between EC2 in the same Region
- VPC gateway endpoints for S3 and DynamoDB does not incur data transfer charges within the same Region
- VPC interface endpoints incur hourly service charges and data transfer charges

## AWS Pricing

Has the following three categories:

- Pay for what you use
- Pay less when you reserve (as compared to On-Demand)
- Pay less with volume-based discounts when you use more

### Free Tier

Three types of offers:

- Always free (Lambda)
- 12 Months free (EC2)
- Trials

## AWS Pricing Calculator

The AWS Pricing Calculator lets you explore AWS services and create an estimate for the cost of your use cases on AWS. You can provide details such as OS, memory requirements, location, etc.
