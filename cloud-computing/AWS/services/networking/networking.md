## Networking and Delivery of Content

Offers a highly secure cloud platform and connects your physical network to VPN with a high transfer speed.

## Elastic IP Addresses

Elastic IP addresses are static/persistent public IPs that come with your account. If any software/instances fail, they can be remapped to anotehr instance quickly i.e. not allocated to an instance.

## Subnet

Subnet is a range of IP addresses in your VPC. Subnet is always mapped to a single availability zone. Two types of subnets: public and private.

Should use private subnets to secure resources that do not need to be available to the internet i.e. database.

## Gateway

An internet gateway is a redundant, horizontally scaled, and highly available VPC component that enables communication between instances in the VPC and the internet. Imposes no availability risks or bandwidth constraints on your network traffic.

Only one gateway can be attached per VPC.

## Route Table

Route table is a set of rules (routes) which are used to determine where network traffic is directed.

Each subnet has to be linked to a route table, and a subnet can only be linked to one route table. Every VPC has a default route table, and is good practice to leave it in the original state, and create a new table to customize network traffic associated with your VPC.

## NAT Devices (Network Address Translation)

A NAT device can be used to enable instances in a private subnet to connect to the internet or AWS services, but this prevents the internet from initiating connections with the instances in a private subnet.

AWS provides two kinds of NAT devices: NAT gateway and NAT instance. NAT gateway is recommended as it is a managed service that provides better bandwidth and availability compared to NAT instances.

### NAT Gateway

Must be launched in a public subnet because it needs internet connectivity, and requires an elastic public IP address
