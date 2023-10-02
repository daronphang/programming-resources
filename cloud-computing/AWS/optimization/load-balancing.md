## Elastic Load Balancing (ELB)

ELB is a service that can distribute incoming application traffic across EC2 instances, containers, IP addresses, and Lambda functions in **multiple Availability Zones**. Key features include:

- **Hybrid mode**: As ELB can load balance to IP addresses, it can work in hybrid mode i.e. load balances to on-premises servers
- **High availability**: ELB is highly available
- **Scalability**: ELB automatically scales to meet the demand of the incoming traffic.

### Health checks

Monitoring is an important part of load balancers as they should route traffic to only healthy EC2 instances.

### Components

#### Rules

To associate a target group to a listener, you must use a rule. Rules are made up of two conditions:

- Source IP address of the client
- Target group to send the traffic to

#### Listener

The client connects to the listener. To define a listener, a port must be provided in addition to the protocol i.e. HTTP at port 80, depending on the load balancer type. There can be many listeners for a single load balancer.

#### Target group

The backend servers are defined in one or more target groups i.e. EC2 instances, Lambda functions, or IP addresses. A health check must also be defined for each target group.

## Types of load balancers

### Application Load Balancer

An Application Load Balancer functions at **Layer 7** of the OSI and is ideal for load balancing **HTTP and HTTPS traffic**. After it receives a request, it evaluates the listener rules in priority order to determine which rule to apply. Primary features include:

- Routes traffic based on request data
- Sends responses directly to client
- Uses TLS offloading
- Authenticates users (OIDC, LDAP, Active Directory)
- Secures traffic (prevents unapproved traffic)
- Supports sticky sessions (stateful applications) by using HTTP cookie

### Network Load Balancer

A Network Load Balancer is ideal for load balancing **TCP, UDP and TLS traffic** if you require **ultra-high performance**. It functions at **Layer 4** of the OsI model, routing connections from a target in the target group based on IP protocol data. Primary features include:

- Sticky sessions
- Low latency
- Preserves client-side source IP address
- Static/elastic IP support
- DNS failover with Amazon Route 53

### Gateway Load Balancer

A Gateway Load Balancer helps you to deploy, scale, and manage your **third-party appliances** i.e. firewalls, intrusion detection and prevention systems, deep packet inspection systems. These appliances enable you to improve security, compliance, and policy controls.

It provides a gateway for distributing traffic across multiple virtual appliances while scaling them up and down based on demand. It functions at **Layer 3** of the OSI model. Primary features include:

- High availability
- Monitoring (with CloudWatch metrics)
- Streamlined deployments
- Private connectivity

When GLB receives requests, it routes them to third-party appliances, which are then forwarded back to the GLB to perform a secondary routing to the EC2 instances (acts as a **middleware**). It can be used for **intrusion detection or deep packet inspection**.
