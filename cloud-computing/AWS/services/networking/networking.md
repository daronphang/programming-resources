## Networking and Delivery of Content

Offers a highly secure cloud platform and connects your physical network to VPN with a high transfer speed.

## Elastic IP Addresses

Elastic IP addresses are static/persistent public IPs that come with your account. If any software/instances fail, they can be remapped to another instance quickly i.e. not allocated to an instance.

## Network Access control List (ACLs)

A network ACL is a virtual firewall that controls inbound and outbound traffic at the **subnet level**. Each AWS account includes a default network ACL. By default, your account's default network ACL allows all inbound and outbound traffic.

You need to include **both the inbound and outbound ports** used for the protocol, else your server would respond but traffic would never leave the subnet i.e. 443 inbound, 1025-65535 TCP outbound.

### Stateless packet filtering

Network ACLs perform **stateless** packet filtering. They remember nothing and check packets that cross the subnet border each way i.e. inbound and outbound, double checking.

After a packet has entered a subnet, it must have its permissions evaluated for resources within the subnet. The VPC component that checks packet permissions for an EC2 instance is a **Security Group**.

## Security Groups

A Security Group is a virtual firewall that controls inbound and outbound traffic for an EC2 instance. By default, it denies all inbound traffic and allows all outbound traffic. You can add custom rules to configure which traffic should be allowed.

### Stateful packet filtering

Security Groups perform **stateful** packet filtering. They remember previous decisions made for incoming packets.

## Gateway

An internet gateway is a redundant, horizontally scaled, and highly available VPC component that enables communication between instances in the VPC and the internet. Imposes no availability risks or bandwidth constraints on your network traffic.

Only one gateway can be attached per VPC.

## NAT Devices (Network Address Translation)

A NAT device can be used to enable instances in a private subnet to connect to the internet or AWS services, but this prevents the internet from initiating connections with the instances in a private subnet.

AWS provides two kinds of NAT devices: NAT gateway and NAT instance. NAT gateway is recommended as it is a managed service that provides better bandwidth and availability compared to NAT instances.

### NAT Gateway

Must be launched in a public subnet because it needs internet connectivity, and requires an elastic public IP address.
