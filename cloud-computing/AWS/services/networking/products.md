## VPC (Virtual Private Cloud)

Millions of customers are using AWS services and resources; without boundaries, network traffic would be able to flow between them unrestricted.

AWS VPC is a networking service that you can use to **establish boundaries around your AWS resources** i.e. EC2. It enables you to provision an isolated section of the AWS Cloud. Within a VPC, you can organize resources into **subnets**. Subnets can communicate with each other in a VPC.

Gives you control over the complete cloud network environment, including IP address range, subnets, route table configuration, and network gateways.

Instances launched into a VPC cannot communicate with your network unless you setup VPC peering (one-to-one relationship) or virtual private gateway.

### Internet Gateway

To allow public traffic from the internet to access your VPC, you attach an **internet gateway** to the VPC.

### Virtual Private Gateway

If your VPC includes private resources, you can access them via **virutal private gateway**. The virtual private gateway is the component that allows protected internet traffic to enter into the VPC. However, it still uses the same traffic as public users.

A virtual private gateway enables you to establish a virutal private network (VPN) connection between your VPC and a private network, such as an on-premise data center or internal corporate network. **It allows traffic into the VPC only if it is coming from an approved network**.

### Direct Connect

AWS Direct Connect is a service that lets you to establish a dedicated private connection between your data center and a VPC. As a different traffic is used as compared to public users, it helps you to reduce network costs and increase the amount of bandwidth that can travel through your network.

```
Data Center -> AWS Direct Connect -> VPC (Virtual Private Gateway)
```

### Network Traffic

When a customer requests data from an application hosted in the AWS Cloud, the request is sent as a **packet**. A packet is a unit of data sent over the internet or network.

Before a packet can enter into or exit from a subnet, the **network ACL** checks for permissions. These permissions indicate who sent the packet and how the packet is trying to communicate with the resources in a subnet.

## Route 53

AWS Route 53 is a DNS (Domain Name System) web service. It gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. It connects user requests to infrastructure running in AWS (EC2, load balancers, etc). It can also route users to infrastructure outside of AWS.

Another feature of Route 53 is the ability to manage the DNS records for domain names. You can register new domain names directly in Route 53. You can also transfer DNS records for existing domain names by other domain registrars. This enables you to manage all of your domain names within a single location.

## ELB (Elastic Load Balancing)

Automatically diverts incoming traffic into multiple targets.

## CloudFront

AWS CloudFront is a content delivery service (CDN).

### How CloudFront works with Route 53

1. Customer requests data from an application by going to AnyCompany's website
2. AWS Route 53 uses DNS resolution to identify the IP address, and is sent back to the customer
3. Customer's request is sent to the nearest edge location through AWS CloudFront
4. AWS CloudFront connects to the application's Load Balancer, which sends incoming packets to an EC2 instance
