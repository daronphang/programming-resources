## Elastic Load Balancing (ELB)

ELB is a service that can distribute incoming application traffic across EC2 instances, containers, IP addresses, and Lambda functions in **multiple Availability Zones**. Key features include:

- **Hybrid mode**: As ELB can load balance to IP addresses, it can work in hybrid mode i.e. load balances to on-premises servers
- **High availability**: ELB is highly available
- **Auto-scaling**: ELB automatically scales to meet the demand of the incoming traffic (by attaching an ASG)

### Benefits

- Highly available and distributes website traffic across multiple targets
- Provides high security through user authentication and TLS
- Handles drastic changes in website traffic without human intervention
- Helps improve the visibility of your applications through continuous monitoring and auditing
- Supports hybrid load balancing

### Health checks

Monitoring is an important part of load balancers as they should route traffic to only healthy EC2 instances.

### Cross-zone load balancing

Load balancer nodes can only route traffic to instances in the same AZ by default. Cross-zone load balancer can help to equally distribute traffic across all instances in all AZs.

### Access logs

You can use **access logs** to capture detailed information about requests sent to the ALB. They can then be stored in S3.

## Algorithms

### Round Robin Method

Simple algorithm that is used to distribute client's request across a group of servers. Once a server has received a request, it will be moved to the bottom of the queue. Client request is sent to each server one by one, based on availability.

### Least Connection Method

Directs network traffic to the server, and is specifically used when there is a large number of client requests unevenly distributed between the servers.

### Least Response Time Method

Directs client requests to the server with the lowest average response time, and ensures that the load is balanced adequately among servers.

### IP Hash

Uses client's IP address to route network traffic to the available backend server.

## Components

### Rules

To associate a target group to a listener, you must use a rule. Rules are made up of two conditions:

- Source IP address of the client
- Target group to send the traffic to

### Listener

The client connects to the listener. To define a listener, a port must be provided in addition to the protocol i.e. HTTP at port 80, depending on the load balancer type. There can be many listeners for a single load balancer.

### Target group

The backend servers are defined in one or more target groups i.e. EC2 instances, Lambda functions, or IP addresses. A health check must also be defined for each target group.

## Types of load balancers

### Application Load Balancer (ALB)

An ALB functions at **Layer 7** of the OSI and is ideal for load balancing **HTTP and HTTPS traffic**. After it receives a request, it evaluates the listener rules in priority order to determine which rule to apply. Primary features include:

- Routes traffic based on request data
- Sends responses directly to client
- Uses TLS offloading (HTTP/HTTPS is terminated on ALB instead of EC2 and hence, SSL certificates reside on the ALB)
- Authenticates users (OIDC, LDAP, Active Directory, Amazon Cognito)
- Secures traffic (prevents unapproved traffic)
- Supports sticky sessions (stateful applications) by using HTTP cookie
- Supports integration with Security Groups

### Network Load Balancer (NLB)

A NLB is ideal for load balancing **TCP, UDP and TLS traffic** if you require **ultra-high performance**. It functions at **Layer 4** of the OSI model, routing connections from a target in the target group based on IP protocol data. Primary features include:

- Sticky sessions
- Low latency
- Preserves client-side source IP address
- Static/elastic IP support (an ALB cannot be assigned an EIP)
- DNS failover with Amazon Route 53
- Security Groups for target EC2 instances

When you create NLB, a network interface is created for each AZ. Each load balancer node will use the network interface to get a static IPv4 address. You can also associate one elastic IP address per subnet.

AWS has launched ALB-type target groups for NLB. With this launch, you can register ALB as a target of NLB to forward traffic from NLB to ALB without needing to actively manage ALB IP address changes through Lambda. This is useful in scenarios whereby client-side has firewall whitelist as you cannot assign an EIP to an NLB, but you can assign an EIP to an NLB. When configuring ALB and NLB, **place the ALB behind the NLB to handle all incoming traffic**. NLB forwards TCP connections to instances, unlike ALB which terminates HTTP/HTTPS.

### Gateway Load Balancer (GLB)

A GLB helps you to deploy, scale, and manage your **third-party appliances** i.e. firewalls, intrusion detection and prevention systems, deep packet inspection systems. These appliances enable you to improve security, compliance, and policy controls.

It provides a gateway for distributing traffic across multiple virtual appliances while scaling them up and down based on demand. It functions at **Layer 3** of the OSI model. Primary features include:

- High availability
- Monitoring (with CloudWatch metrics)
- Streamlined deployments
- Private connectivity

When GLB receives requests, it routes them to third-party appliances, which are then forwarded back to the GLB to perform a secondary routing to the EC2 instances (acts as a **middleware**). It can be used for **intrusion detection or deep packet inspection**.

GLB uses GENEVE protocol which encapsulates and forwards traffic to the virtual appliances for processing.

<img src="../assets/glb.png">

<img src="../assets/glb2.png">

## Deployment modes

- Public: Deployed on public subnets and accessible across the internet
- Private: Deployed on private subnets and accessible by users within the AWS network
