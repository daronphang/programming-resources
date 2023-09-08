## Scalability

Scalability involves beginning with only the resources you need and designing your architecture to automatically respond to changing demand by scaling out or in.

## EC2 Auto Scaling

This feature enables you to automatically add or remove EC2 instances in response to changing application demand. Two approaches include:

- Dynamic Scaling: Responds to changing demand
- Predictive Scaling: Automatically schedules the right number of EC2 instances based on predicted demand

With auto scaling, you define the **minimum capacity**, **desired capacity** (defaults to your minimum capacity), and **maximum capacity**.

## Elastic Load Balancing

ELB is the AWS service that automatically distributes incoming application traffic across multiple resources.
