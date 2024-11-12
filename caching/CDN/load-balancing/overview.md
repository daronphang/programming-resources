## Load balancing

The load balancing system acts as the nerve center of a CDN system, and is responsible for scheduling access to users who initiate service requests. Most CDN systems implement load balancing systems in a hierarchical manner, such as the **two-level scheduling system**:

- **GSLB**: Determines the physical location of the cache that provides services to users by DNS resolution
- **SLB (local)**: Responsible for load balancing of devices within the local region

## Load balancing strategies

### Static

- **IP address**: Using CIDR range to resolve to nodes e.g. 10.2.0.0/24 resolved to nodes with addresses 10.2.4.200
- **Weighted IP address**
- **Weighted PoP nodes**
- **Based on cost**: Different CDN operators have different charging methods in different locations due to differences in IDC rental costs in different regions
- **Geographical distance**

### Dynamic

- **Health checks**
- **Session retention**
- **Response time**
- **Session capability threshold**
- **RTT**
- **Based on traffic**
- **Based on the number of new connections**

## Layer 4 switch

Layer 4 switch device is equivalent to a gateway device. All requests and responses to the cache server must be scheduled through the Layer 4 switching device for load balancing. Therefore, the Layer 4 switching device and the attached cache server are combined into one or more virtual servers for external services, and the IP address of the cache server will not appear externally.

## Layer 4-7 switch (web switch)

A network switch that analyzes layer 4 and layer 7 data in the packets. These switches are used to manage network traffic and optimize infrastructure by providing advanced features.

### Features

- **Load balancing**: Distributes traffic across groups of servers, such as for HTTP, HTTPS, VPN, or TCP/IP traffic
- **NAT**: Can be performed at wire speed
- **SSL encryption and decryption**: Reduces the load on servers receiving traffic
- **Digital certificate management**: Can be centralized
- **Stickiness**: Directs repeated requests from a client to the same application server
