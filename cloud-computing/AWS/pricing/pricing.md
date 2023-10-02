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

### Networking Costs

- Free for traffic inbound
- Free if two EC2 instances communicate with each other in the same Availability Zone using private IP
- $0.01 and $0.02 per GB using private IP and public IP respectively for two instances communicating in different Availability Zones

## Savings Plan

### EC2 Savings Plan

- Up to 72% discount compared to On-Demand
- Commit to instance families in a Region
- Regardless of Availability Zone, size, OS, or tenancy
- All upfront, partial upfront, no upfront

### Compute Savings Plan (most flexible)

- Up to 66% discount compared to On-Demand
- Regardless of Family, Region, size, OS, tenancy, compute options
- Applicable for EC2, Fargate, Lambda

## AWS Pricing Calculator

The AWS Pricing Calculator lets you explore AWS services and create an estimate for the cost of your use cases on AWS. You can provide details such as OS, memory requirements, location, etc.

## AWS Compute Optimizer

Reduce costs and improve performance by recommending optimal AWS resources for your workloads using ML to analyze your resources' configurations and their utilization CloudWatch metrics. Helps you choose optimal configurations and right-size your workloads (over/under provisioned).
