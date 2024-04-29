## Virtual Private Cloud (VPC)

Millions of customers are using AWS services and resources; without boundaries, network traffic would be able to flow between them unrestricted.

AWS VPC is a networking service that you can use to **establish boundaries around your AWS resources** i.e. EC2. It enables you to provision an isolated section of the AWS Cloud. Within a VPC, you can organize resources into **subnets**. Subnets can communicate with each other in a VPC.

Gives you control over the complete cloud network environment, including IP address range, subnets, route table configuration, and network gateways.

Instances launched into a VPC cannot communicate with your network unless you setup VPC peering (one-to-one relationship) or virtual private gateway.

### Region

A VPC is **isolated to a specific Region**, and spans all the Availability Zones within the selected Region.

### Talking to other VPCs in a region

When you deploy resource in VPC, they cannot talk to resources in another VPC i.e. isolated by default. Need to explicitly allow communication.

### IP Addresses

Every VPC has a range of IP addresses assigned to it called the CIDR block. A CIDR block defines the IP addresses that resource in the VPC can use.

The size of the network is determined by the IP range for the VPC in CIDR notation. Each VPC can have up to five CIDRs (between `/28` and `/16` in size):

- One primary IPv4
- Four secondaries IPv4

#### Reserved IPs

There are five IP addresses that are reserved by AWS.

```
10.0.0.0    Network address
10.0.0.1    VPC local router
10.0.0.2    DNS server
10.0.0.3    Future use
10.0.2.255  Network broadcast address
```

### High availability with a VPC

To maintain redundancy and fault tolerance, create at least two subnets configured in two Availability Zones i.e. minimum of four subnets.

### Network Traffic

When a customer requests data from an application hosted in the AWS Cloud, the request is sent as a **packet**. A packet is a unit of data sent over the internet or network.

Before a packet can enter into or exit from a subnet, the **network ACL** checks for permissions. These permissions indicate who sent the packet and how the packet is trying to communicate with the resources in a subnet.

### DNS

Only private instances will automatically be assigned a DNS entry; for public, need to enable DNS hostnames. To enable DNS resolution through AWS DNS server, need to enable DNS resolution (can be used for resolving local DNS queries).

AWS DNS server can be accessed either via 169.254.169.253 or on the second IP of the VPC CIDR block.

```sh
$ cat /etc/resolv.conf
$ nslookup google.com
```

## Subnet

A subnet is a section of a VPC that you can contain/group resources such as EC2 instances. Think of subnets as smaller networks inside your base network, or virtual local area networks (VLANs) in a traditional on-premises network. In AWS, subnets are used to provide **high availability and connectivity** options for your resources.

A subnet within a VPC:

- Must be within the CIDR range
- A subnet block size must be between /16 and /28
- Applications deployed in the subnet will have an IP address within the subnet CIDR block
- Always mapped to a single Availability zone
- Cannot overlap with other subnets in the VPC
- Allows for an optional IPv6 CIDR
- Can be configured to be IPv6 only i.e. no IPv4 addresses
- Can communicate with other subnets in the VPC

There are two types of subnets:

- **Public**: Has access to the internet gateway; contains resources that need to be accessible by the public
- **Private**: Does not have access to the internet gateway; contains resources that should be accessible only through your private network i.e. databases

## Route table

When you create a VPC, AWS creates a main route table that contains a set of rules (routes) that are used to determined where network traffic is directed. AWS assumes that when you create a new VPC with subnets, you want traffic to flow between them. Hence, the default configuration is to allow traffic between all subnets in the local network.

The following rules apply to the main route table:

- You cannot delete the main route table
- You cannot set a gateway route table as the main route table
- You can replace the main route table with a custom subnet route table
- You can add, remove, and modify routes in the main route table
- You can explicitly associate a subnet with the main route table

**Each subnet has to be linked to a route table, and a subnet can only be linked to one route table**. Every VPC has a default route table, and is good practice to leave it in the original state, and create a new table to customize network traffic associated with your VPC.

```
Destination             Target
172.31.0.0/16           local (default)
0.0.0.0/0               igw-12345 (internet gateway)
```

### Custom route table

The main route table is used implicitly by subnets that do not have an explicit route table association. You can create separate subnets for the resources and provide different routes for each of them.

If you associate a subnet with a custom route table, the subnet will use it **instead** of the main route table. Each custom route table will have the **local route already inside it**, allowing communication to flow between all resources and subnets in a VPC.

## Internet Gateway

To allow public traffic from the internet to access your VPC, you attach an **internet gateway** to the VPC. An internet gateway is **highly available and scalable**.

## Virtual Private Network (VPN)

A virtual private gateway enables you to establish a virtual private network (VPN) connection between your VPC and a private network, such as an on-premise data center or internal corporate network. **It allows traffic into the VPC only if it is coming from an approved network**. However, it goes over the public internet (encrypted) and may have limited bandwidth, but relatively fast to setup.

There are two types of VPN:

- Site-to-Site VPN: VPN over public internet between on-premises DC and AWS
- ClientVPN: OpenVPN connection from your computer into your VPC

### Virtual Private Gateway (VPG)

A VPG connects your VPC to another private network i.e. it is the component that allows protected internet traffic to enter into the VPC. However, it still uses the same traffic as public users.

### How it works

- The VPG is attached to the VPC (terminates VPN on the AWS side)
- A customer gateway to the other private network is required on the other side (terminates VPN on the customer side)
- A customer gateway device is a physical device or software application
- When you have both gateways, you can then establish an encrypted virtual private network (VPN)

### Routing

You can configure statically by defining routes in the routing table. Alternatively, you can configure a dynamic routing protocol to exchange routes between VPG and CG using BGP.

### Pricing

Charged for:

- Each available VPN connection per hour
- Data transfer out from EC2 to the internet

## VPC Peering

VPC Peering is used to connect two VPCs privately using AWS network. With VPC Peering, you can setup a connection between VPCs in different Regions and AWS accounts.

To setup routing, need to configure routing table in each VPC to the VPC Peering target.

VPC Peering:

- **Must not have overlapping CIDR**
- VPC Peering connection is **not transitive** (must be established for each VPC that needs to communicate with one another, does not inherit existing peerings)

### Pricing

- No cost for VPC peering connection creation
- Data transfer within an AV is free
- Data transfer across AV incurs charges

## VPC Endpoints

Endpoints allows customers to private connect their VPC to supported AWS services powered by PrivateLink using a private network instead of the public network (www). This gives you enhanced security and lower latency to access AWS services.

There are two kinds of endpoints:

- VPC Endpoint Gateway: S3 and DynamoDB (or if IP address is not available as it does not take IP address off from your subnet)
- VPC Endpoint Interface: Rest of AWS services

## AWS PrivateLink (VPC Endpoint Service)

For an EC2 to connect to an S3 Bucket, need to create an IG and give EC2 full internet access which is not desirable.

AWS PrivateLink is a technology that provides the most secure and scalable way to expose a public AWS service to other VPCs e.g. S3 Bucket. Does not require VPC peering, internet gateway, NAT, route tables, etc. Allows 2 VPCs to connect that have **overlapping CIDR ranges**.

PrivateLink is a technology for **interface endpoints**, not for a gateway endpoint.

- Third party VPC exposes an ENI (Elastic Network Interface)
- Your VPC exposes a network load balancer
- You establish a private link between both VPCs

## AWS Direct Connect (DX)

AWS Direct Connect is a service that lets you to establish a dedicated **physical** private connection between your **data center** and a VPC which allows for high speed. As a different traffic is used as compared to public users, it helps you to reduce network costs and increase the amount of bandwidth that can travel through your network. However, it takes at least a month to establish.

For secure connection, you can implement a VPN over Direct Connect to add an additional layer of network security for data in transit.

### How it works

Cross connect is a connection between a port on AWS router and customer router in the DX location.

```
On-premise network -> Customer Gateway -> Customer Router (located in DX) -> AWS Router -> VPN Gateway -> VPC
```

### Pricing

- Port hours
- Outbound data transfer

## Transit Gateway

A single gateway to provide transitive peering between thousands of VPC and on-premises, through hub-and-spoke (star) connection.

You need to specify **one subnet from each AZ** to be used by the Transit Gateway to route traffic. Transit Gateway can also establish peering with other Transit Gateways in different Regions and AWS accounts.
