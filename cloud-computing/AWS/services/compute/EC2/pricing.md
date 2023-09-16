## EC2 Pricing

With EC2, you pay only for the compute time that you use.

### On-Demand

Ideal for short-term, irregular workloads that cannot be interrupted. No upfront costs or minimum contracts apply. The instances run continuously until you stop them.

Sample use cases include developing and testing applications, and running applications that have unpredictabe usage patterns. **They are not recommended for workloads that last a year or longer** as they can experience greater cost savings using Reserved instances.

### Reserved

Reserved instances are a billing discount applied to the use of On-Demand instances in your account. You can purchase for a 1-year or 3-year term.

There are two types of Reserved instances:

- Standard Reserved instances
- Convertible Reserved instances

Standard Reserved instance is a good fit if you know the EC2 instance type and size you need for your steady-state applications. You are required to provide:

- Instance type and size i.e. m5.xlarge
- Platform OS i.e. Windows, Linux
- Tenancy i.e. default or dedicated
- Availability Zone (optional)

Convertible instances might serve better if you need to run your EC2 instance in different Availability Zones or different instance types.

At the end of the term, you can continue to use without interruption. However, you are charged On-Demand rates until you purchase a new Reserved instance.

### EC2 Instance Savings Plans

For EC2, AWS offers Savings Plans when you make an hourly spend commitment to an instance family and Region for a 1-year or 3-year term. The term commitment results in savings of up to 72% compared to On-Demand rates. Any usage up to the commitment is charged at the discounted rate (i.e. $10 per hour), but at regular On-Demand rates beyond the commitment.

EC2 Instance Savings Plans are a good option if you need flexibility in your EC2 usage over the duration of the commitment term. You have the benefit of saving costs on running any EC2 instance within an EC2 instance family in a chosen region, regardless of Availability Zone, instance size, OS, or tenancy.

You don't need to specify upfront what resource and instance type is required to get a discount. You also don't have to commit to a certain number of EC2 instances over a 1-year or 3-year term.

### Spot Instances

Spot instances are ideal for workloads with flexible start and end times, or that can withstand interruptions. They use unused EC2 computing capacity and offer you cost savings at up to 90% off of On-Demand prices.

If you make a Spot request and EC2 capacity is not available, the request will not be successful until capacity becomes available. The unavailable capacity might delay the launch of your job/task.

After you have launched a Spot instance, if capacity is no longer available or demand for Spot instances increases, **your instance may be interrupted**.

### Dedicated Hosts

Physical servers with EC2 instance capacity that is fully dedicated to your use (most expensive).