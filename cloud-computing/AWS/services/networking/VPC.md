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

## VPC Endpoints

Endpoints allows customers to private connect their VPC to supported AWS services using AWS network instead of the public network (www). This gives you enhanced security and lower latency to access AWS services. Traffic between a VPC and a service does not leave the Amazon network.

### VPC Gateway Endpoint

A gateway endpoint targets specific IP routes in an Amazon VPC route table, in the form of a prefix-list, used for traffic destined to DynamoDB or S3. **Gateway endpoints do not enable AWS PrivateLink**.

A gateway endpoint is also used if an IP address for a service is not available as it does not take IP address off from your subnet.

### VPC Interface Endpoint

Interface endpoints enable connectivity to services over AWS PrivateLink. All other AWS services use interface endpoints.

An interface endpoint is a collection of one or more elastic network interfaces with a private IP address that serves as an entry point for traffic destined to a supported service.

### AWS PrivateLink

For an EC2 to connect to an S3 Bucket, need to create an IG and give EC2 full internet access which is not desirable.

AWS PrivateLink is a technology that provides the most secure and scalable way to expose a public AWS service to other VPCs e.g. S3 Bucket. Does not require VPC peering, internet gateway, NAT, route tables, etc. Allows 2 VPCs to connect that have **overlapping CIDR ranges**.

PrivateLink is a technology for **interface endpoints**, not for a gateway endpoint.

- Third party VPC exposes an ENI (Elastic Network Interface)
- Your VPC exposes a network load balancer
- You establish a private link between both VPCs

## VPC Lattice

VPC Lattice is an overlay network. Services can discover and communicate without peering.
