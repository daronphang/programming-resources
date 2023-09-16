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
