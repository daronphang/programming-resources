## EC2 Pricing

With EC2, you pay only for the compute time that you use.

### On-Demand

Ideal for short-term, irregular workloads that cannot be interrupted. No upfront costs or minimum contracts apply. The instances run continuously until you stop them.

Sample use cases include developing and testing applications, and running applications that have unpredictable usage patterns. **They are not recommended for workloads that last a year or longer** as they can experience greater cost savings using Reserved instances.

On-demand charges by the second, but there is a one-minute minimum charge for Linux based EC2 instances.

### Reserved

Reserved instances are a billing discount applied to the use of On-Demand instances in your account. You can purchase for a 1-year or 3-year term.

For payment options, you can either pay with:

- No upfront
- Partial upfront
- All upfront (most discount )

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

#### Reserved Instance Marketplace (EC2 Console)

You can buy and sell in the Reserved Instance Marketplace if you do not need them anymore (root user can perform this).

### EC2 Instance Savings Plans

For EC2, AWS offers Savings Plans when you make an hourly spend commitment to an instance family and Region for a 1-year or 3-year term. The term commitment results in savings of up to 72% compared to On-Demand rates. Any usage up to the commitment is charged at the discounted rate (i.e. $10 per hour), but at regular On-Demand rates beyond the commitment.

EC2 Instance Savings Plans are a good option if you need flexibility in your EC2 usage over the duration of the commitment term:

- Instance family (locked)
- AWS Region (locked)
- Availability Zone (flexible)
- Instance size (flexible)
- OS (flexible)
- Tenancy (flexible)

You don't need to specify upfront what resource and instance type is required to get a discount. You also don't have to commit to a certain number of EC2 instances over a 1-year or 3-year term.

### Compute Savings Plan (most flexible)

- Up to 66% discount compared to On-Demand
- Regardless of Family, Region, size, OS, tenancy, compute options
- Applicable for EC2, Fargate, Lambda

### Spot Instances

Spot instances are ideal for workloads with flexible start and end times, or that can withstand interruptions i.e. **resilient to failure**. They use unused EC2 computing capacity and offer you cost savings at up to 90% off of On-Demand prices.

If you make a Spot request and EC2 capacity is not available, the request will not be successful until capacity becomes available. The unavailable capacity might delay the launch of your job/task.

After you have launched a Spot instance, if capacity is no longer available or demand for Spot instances increases, **your instance may be interrupted**.

### Dedicated Hosts

Physical servers with EC2 instance capacity that is fully dedicated to your use (most expensive). You have full control over instance placement. This will not change even if you restart EC2 instances.

Allows you to address **compliance requirements** and use your **existing server-bound software licenses**. Useful for software that have complicated licensing model i.e. per-socket, per-core VM software licenses.

You can either purchase On-Demand or Reserved.

### Dedicated Instances

No other customers will share your EC2 hardware. However, you may share hardware with other instances in the same account. However, if you reboot your EC2 instances, you may get a new physical server.

### Capacity Reservations

You can reserve On-Demand instances capacity in a specify Availability Zone for any duration. You will **always have access to EC2 capacity** when you need it.

There is no time commitment (create/cancel anytime) but is not qualified for any discounts. You are charged at **On-Demand** rate whether you run the instances or not. Suitable for short-term.
