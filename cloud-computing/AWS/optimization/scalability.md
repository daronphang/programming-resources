## Scalability

Scalability involves beginning with only the resources you need and designing your architecture to automatically respond to changing demand by scaling out or in.

## EC2 Auto Scaling

This feature enables you to automatically add or remove EC2 instances in response to changing application demand i.e. adjusts the capacity to maintain steady, predictable performance at the lowest possible cost. Two approaches include:

- Dynamic Scaling: Responds to changing demand
- Predictive Scaling: Automatically schedules the right number of EC2 instances based on predicted demand

With auto scaling, you define the **minimum capacity**, **desired capacity** (defaults to your minimum capacity), and **maximum capacity**.

**Autoscaling usually crosses AZs by default**. However, if cross-zone LB is not enabled, you may see uneven connection numbers.

### Benefits

- Better fault tolerance
- High availability of resources
- Better cost management
- High reliability of resources
- High flexibility of resources

### Termination policies

- Default
- AllocationStrategy
- OldestLaunchTemplate
- OldestLaunchConfiguration
- ClosestToNextInstanceHour: Terminate instance closest to the billing cycle
- NewestInstance
- OldestInstance

## Components

- Launch template: configuration template for EC2 instances
- Scaling policies: Configuration for a group to scale based on the occurrence of specified conditions or on a schedule
- Auto Scaling group: minimum, maximum, and desired capacity (horizontal scaling)

### Launch template

Features include:

- Instance configuration
- Versioning and update
- Customization
- Specify different instance type and purchase options
- Tagging and metadata
- API support
- Instance termination protection
- Pass user data at runtime

### Scaling policies

- **Manual scaling**: Helps in managing the task of building or terminating EC2 instances on its own
- **Schedule scaling**: Developers can predict future traffic and schedule the time for executing AWS autoscaling
- **Dynamic scaling**: Scaling lets developers define required scaling in response to client demand
- **Predictive scaling**: Uses machine learning algorithms and historical data to forecast future demand and proactively adjust the number of EC2 instances in your ASG
- **Maintaining the current instance-level**: Developers configure an ASG for managing running instances

### Dynamic scaling

You can use scaling policies to increase or decrease the number of instances in your group dynamically to meet changing conditions. When the scaling policy is in effect, the Auto Scaling group adjusts the desired capacity of the group, between the minimum and maximum capacity values that you specify, and launches or terminates the instances as needed.

- **Simple scaling** by setting CloudWatch alarms of fixed value
- **Step scaling** based on range e.g. add 2 instances if above 60%, 3 instances above 70%
- **Target tracking scaling (recommended)** e.g. CPU utilization, network, etc.

## Auto-scaling group (ASG)

An Auto Scaling group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management.

### Troubleshooting/software upgrades

- Put the instance in Standby mode to prevent ASG from terminating as part of health check
- Move instance back to InService mode

### Integration

- Elastic load balancer
- Amazon CloudWatch
- SNS
- EC2 instance
