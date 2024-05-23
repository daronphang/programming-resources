## Route 53

Amazon Route 53 is a highly available, scalable and global Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.

Route 53 gives developers and businesses a reliable way to route end users to internet applications hosted in AWS. It connects user requests to infrastructure running in AWS (EC2, load balancers, etc). It can also route users to infrastructure outside of AWS.

Another feature of Route 53 is the ability to manage the DNS records for domain names. You can register new domain names directly in Route 53. You can also transfer DNS records for existing domain names by other domain registrars. This enables you to manage all of your domain names within a single location.

### Hosted zones

A hosted zone is where you define all the records and rules i.e. a collection of DNS records. AWS will automatically provision 4 DNS servers for your hosted zone.

### Application recovery controller

A service that continuously monitors application's ability to recover from failures and to control applications across multiple AWS Regions and AZ. It helps to automate the whole process of continuously checking if your backup location or site is up and running. It can also be used to manually redirect traffic from a deployment.

A **cell** groups all resources required for an application to operate independently. A **recovery group** is a collection of cells that represent an application that you want to check for failover readiness. A **resource set** is a set of AWS resources that can span multiple cells.

### Records

In AWS the most common records are:

- www.google.com -> 12.34.56.78 == A record (IPv4)
- www.google.com -> 2001:0db8:85a3:0000 == AAAA record (IPv6)
- search.google.com -> www.google.com == CNAME:hostname to hostname
- example.com -> AWS resource == Alias (ELB, CloudFront, S3, RDS, etc)

### Routing policies

- Simple routing policy (no health checks)
- Weighted routing policy (using weight to route to resource)
- Latency routing policy (minimizes latency)
- Failover routing policy (disaster recovery)
- Geolocation routing policy (different geographic locations)

### How CloudFront works with Route 53

1. Customer requests data from an application by going to AnyCompany's website
2. AWS Route 53 uses DNS resolution to identify the IP address, and is sent back to the customer
3. Customer's request is sent to the nearest edge location through AWS CloudFront
4. AWS CloudFront connects to the application's Load Balancer, which sends incoming packets to an EC2 instance

### Route 53 vs ELBs

- ELBs are intended to load balance across EC2 instances in a single Region
- DNS load-balancing (Route 53) is intended to balance traffic across Regions
- Both Route53 and ELB perform health check and route traffic to only healthy resources
- Route 53 only change the address that your clients' requests resolve to
- ELB actually reroutes traffic
- Autoscaling can be configured automatically for ELB
- Route 53 have to either manually replace the old failed instance with the new one in the route as DNS is cached; unhealthy targets will still be in the visitors cache for some time

## AWS Global Accelerator

When a request traverses through the internet, it may not take the most efficient path.

Improves global application availability and performance by leveraging the **AWS internal network** (similar to S3 Transfer Acceleration). Provides static IP addresses that act as a fixed entry point to your applications.

Global Accelerator is a good fit for non-HTTP use cases i.e. useful for applications over TCP/UDP by proxying packets at the edge of the locations running in one or more AWS Regions.

### CloudFront vs Global Accelerator

- Cloudfront caches content using edge location
- Global Accelerator performs no caching but proxies packets at the edge to applications running in one or more AWS Regions
