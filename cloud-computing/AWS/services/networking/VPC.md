## VPC (Virtual Private Cloud)

Millions of customers are using AWS services and resources; without boundaries, network traffic would be able to flow between them unrestricted.

AWS VPC is a networking service that you can use to **establish boundaries around your AWS resources** i.e. EC2. It enables you to provision an isolated section of the AWS Cloud. Within a VPC, you can organize resources into **subnets**. Subnets can communicate with each other in a VPC.

Gives you control over the complete cloud network environment, including IP address range, subnets, route table configuration, and network gateways.

Instances launched into a VPC cannot communicate with your network unless you setup VPC peering (one-to-one relationship) or virtual private gateway.

### Subnet

A subnet is a section of a VPC that you can contain/group resources such as EC2 instances. Think of subnets as smaller networks inside your base network, or virtual local area networks (VLANs) in a traditional on-premises network. In AWS, subnets are used to provide **high availability and connectivity** options for your resources.

Subnet is a range of IP addresses in your VPC which must be a subset of the VPC CIDR block. **Subnet is always mapped to a single Availability Zone**. There are two types of subnets:

- **Public**: Has access to the internet gateway; contains resources that need to be accessible by the public
- **Private**: Does not have access to the internet gateway; contains resources that should be accessible only through your private network i.e. databases

### Region

A VPC spans all the Availability Zones within the selected Region.

### IP Addresses

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

## Internet Gateway

To allow public traffic from the internet to access your VPC, you attach an **internet gateway** to the VPC. An internet gateway is **highly available and scalable**.

## Virtual Private Gateway

A virtual private gateway connects your VPC to another private network i.e. it is the component that allows protected internet traffic to enter into the VPC. However, it still uses the same traffic as public users.
When you create and attach a virtual private gateway to a VPC:

- The gateway acts as an anchor on the AWS side of the connection
- A customer gateway to the other private network is required on the other side
- A customer gateway device is a physical device or software application
- When you have both gateways, you can then establish an encrypted virtual private network (VPN)

### Virtual Private Network (VPN)

A virtual private gateway enables you to establish a virutal private network (VPN) connection between your VPC and a private network, such as an on-premise data center or internal corporate network. **It allows traffic into the VPC only if it is coming from an approved network**.

## AWS Direct Connect

AWS Direct Connect is a service that lets you to establish a dedicated private connection between your **data center** and a VPC. As a different traffic is used as compared to public users, it helps you to reduce network costs and increase the amount of bandwidth that can travel through your network.

```
Data Center -> AWS Direct Connect -> VPC (Virtual Private Gateway)
```

### Network Traffic

When a customer requests data from an application hosted in the AWS Cloud, the request is sent as a **packet**. A packet is a unit of data sent over the internet or network.

Before a packet can enter into or exit from a subnet, the **network ACL** checks for permissions. These permissions indicate who sent the packet and how the packet is trying to communicate with the resources in a subnet.
