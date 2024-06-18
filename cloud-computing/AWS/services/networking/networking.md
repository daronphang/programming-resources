## Networking and delivery of content

Offers a highly secure cloud platform and connects your physical network to VPN with a high transfer speed.

## Elastic IP addresses

Elastic IP addresses are static/persistent public IPs that come with your account. If any software/instances fail, they can be remapped to another instance quickly i.e. not allocated to an instance.

An elastic IP must be associated with an instance or network interface, and are specific to a Region.

## AWS Network Firewall

Protects your entire VPC from Layer 3 to Layer 7. Provides deep packet inspection and intrusion detection. An alternative to using GLB with third party appliances.

You can inspect, in any direction:

- VPC to VPC traffic
- Outbound to internet
- Inbound from internet
- To/from Direct Connect and Site-to-Site VPN

### Firewall endpoints

Firewall endpoint serves as the entry/exit points for traffic to be inspected. **A separate subnet needs to be created specifically for the firewall**. You can't deploy a firewall in a subnet with resources because it can't protect applications that run in the same subnet.

### Rule engines

- Stateless engine: Rule processing ordered by rule priority setting
- Stateful engine: Rule processing ordered by action (pass, drop, alert)

### Features

- Simplified rule management
- Granular control
- Advanced threat protection

## Network Access control List (ACLs)

A network ACL is a virtual firewall that controls inbound and outbound traffic at the **subnet level** (ALLOW/DENY). Each AWS account includes a default network ACL. By default, your account's default network ACL allows all inbound and outbound traffic.

Every subnet within a VPC must be associated with a network ACL. You can associate a network ACL with multiple subnets, but a subnet can only be associated with one network ACL at a time.

Network ACLs do not filter traffic destined to and from the following:

- Amazon Domain Name Services (DNS)
- Amazon Dynamic Host Configuration Protocol (DHCP)
- Amazon EC2 instance metadata
- Amazon ECS task metadata endpoints
- License activation for Windows instances
- Amazon Time Sync Service

### Inbound and outbound ports

You need to include **both the inbound and outbound ports** used for the protocol, else your server would respond but traffic would never leave the subnet i.e. 443 inbound, 1025-65535 TCP outbound.

When a client connects to a server, a random port is generated from the ephemeral port range with this becoming the **client's source port**, which becomes the destination port for return traffic. The port range varies depending on the OS:

- Linux: 32768-61000
- ELB: 1024-65535
- Windows: 1025-5000
- NAT gateway: 1024-65535
- Lambda: 1024-65535

### Rule evaluation

A network ACL contains a numbered list of rules and **evaluates them in the increasing order** while deciding whether to allow the traffic i.e. once the first set of rules matches, it stops. You should DENY rules above ALLOW rules.

### Stateless packet filtering

Network ACLs perform **stateless** packet filtering. They remember nothing and check packets that cross the subnet border each way i.e. inbound and outbound, double checking. Stateless firewalls must be configured to allow **both inbound and outbound** traffic i.e. ingress and egress directions.

After a packet has entered a subnet, it must have its permissions evaluated for resources within the subnet. The VPC component that checks packet permissions for an EC2 instance is a **Security Group**.

## Security Groups

A Security Group is a virtual firewall that controls inbound and outbound traffic for an EC2 instance (only ALLOW). By default, it denies all inbound traffic and allows all outbound traffic. You can add custom rules to configure which traffic should be allowed.

Security groups can be attached to multiple EC2 instances and are locked down to a **Region/VPC combination**. You can assign multiple security groups to a single resource i.e. rules for both groups get merged.

### Stateful packet filtering

Security Groups perform **stateful** packet filtering. They remember previous decisions made for incoming packets. As it is stateful, **only the direction of the request needs to be permitted (INBOUND)**.

## Internet Gateway (IGW)

An IGW is a redundant, horizontally scaled, and highly available VPC component that enables communication between instances in the VPC and the internet i.e. region resilient, covers all Availability Zones within a Region. Imposes no availability risks or bandwidth constraints on your network traffic.

Only one IGW can be attached per VPC. To allow internet access, destination in route table must be set to `0.0.0.0/0` targeting the IGW.

### Exposing resources to the internet

1. Create an IGW
2. Attach IGW to VPC
3. Create custom route table
4. Configure default route i.e. if a packet comes in does not match any route (0.0.0.0/0), it will automatically point to the IGW
5. Associate subnet with route table

## Egress-Only Internet Gateway

Similar to an IGW but for IPv6-enabled applications. You can configure route tables to direct all traffic from the application through it.

## NAT (Network Address Translation) devices

A NAT device can be used to enable instances in a private subnet (or private IP networks) to connect to the internet or AWS services, but this prevents the internet from initiating connections with the instances in a private subnet. NAT translates private IP addresses in an internal network to a public IP address before packets are sent to an external network. An **IGW is still required** for access to the internet.

AWS provides two kinds of NAT devices: NAT gateway and NAT instance. NAT gateway is recommended as it is a managed service that provides better bandwidth and availability compared to NAT instances. A NAT instance is an EC2 instance that is converted into a NAT server.

## NAT gateway

Each NAT gateway is created in a specific AZ and implemented with redundancy in that zone. There is also a quota with the number of NAT gateways you can create in each AZ.

To improve resiliency, create a NAT gateway in each AZ, and configure your routing to ensure that resources use the NAT gateway in the same AZ.

Charged per hour and per GB of data processed. Supports 5Gbps of bandwidth and automatically scales up to 100Gbps.

### NAT instance

The NAT instance must have internet access, so it must be in a **public subnet** (a subnet that has a route table with a route to the internet gateway), and it must have a public IP address or an Elastic IP address.

Each instance performs source/destination checks by default. This means that the instance must be the source or destination of any traffic it sends or receives. However, a NAT instance must be able to send and receive traffic when the source or destination is not itself. Therefore, you must disable source/ destination checks on the NAT instance.

### Public

To provide instances in private subnets connectivity to the internet, but cannot receive unsolicited inbound connections. Must be created in a **public subnet** (to have public IP and internet access) and associate an elastic IP address with the NAT gateway.

Route table for private subnets should point to NAT gateway i.e. you route traffic from the private instances to the NAT gateway to the internet gateway.

### Private

Instances in private subnets can connect to other VPCs or your on-premises network through a private NAT gateway. You can route traffic from the NAT gateway through a **transit gateway or a virtual private gateway**. You cannot associate an elastic IP address with a private NAT gateway.

### Connecting to transit gateway or virtual private gateways

You can use either a public or private NAT gateway to route traffic to transit gateways and virtual private gateways:

- Private NAT gateway: Private IP address of private NAT gateway is used
- Public NAT gateway: Private IP address of public NAT gateway is used
- Public NAT gateway with IGW: Public IP address of public NAT gateway is used

### NAT vs IGW

- IgW allows both inbound and outbound access to the internet whereas the NAT Gateway only allows outbound access
- IgW allows instances with public IPs to access the internet whereas NAT Gateway allows instances with private IPs to access internet
- You only need one Internet Gateway per VPC whereas you need one NAT Gateway per Availability Zone as it is deployed to a subnet
- There is no additional cost to use Internet Gateway whereas NAT Gateway incurs charges based on the creation and usage
