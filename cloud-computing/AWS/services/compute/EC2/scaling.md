## Scalability

Scalability involves beginning with only the resources you need and designing your architecture to automatically respond to changing demand by scaling out or in.

## EC2 Auto Scaling

This feature enables you to automatically add or remove EC2 instances in response to changing application demand i.e. adjusts the capacity to maintain steady, predictable performance at the lowest possible cost. Two approaches include:

- Dynamic Scaling: Responds to changing demand
- Predictive Scaling: Automatically schedules the right number of EC2 instances based on predicted demand

With auto scaling, you define the **minimum capacity**, **desired capacity** (defaults to your minimum capacity), and **maximum capacity**.

### Benefits

- Better fault tolerance
- High availabity of resources
- Better cost management
- High reliability of resources
- High flexibility of resources

### Scaling Plans

- **Manual scaling**: Helps in managing the task of building or terminating EC2 instances on its own
- **Scaling based on schedule**: Developers can predict future traffic and schedule the time for executing AWS autoscaling
- **Scaling based on demand**: Scaling lets developers define required scaling in response to client demand
- **Maintaining the current instance-level**: Developers configure an Auto Scaling group for managing running instances

### Components:

- Launch template: configuration template for EC2 instances
- Scaling policies: Configuration for a group to scale based on the occurrence of specified conditions or on a schedule
- Auto Scaling group: minimum, maximum, and desired capacity
