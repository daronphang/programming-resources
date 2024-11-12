## LVS (Linux Virtual Server)

LVS is a patched Linux kernel that adds a load balancing facility. LVS acts as a network bridge to **load balance TCP/UDP stream (Layer 4)**. LVS has become part of the Linux standard kernel, and users can directly use the various functions provided by LVS.

LVS contains a routing table that completes the LVS negative balancing function, and distributes user requests to application servers in the cluster through the routing information. At the same time, the LVS load scheduler also needs to monitor the work of each application server and update the LVS routing table at any time according to whether the server is normal and available.

### IPVS

The core of LVS is **IP load balancing**, which is implemented by the IPVS module. It is installed on the load scheduler and provides users with a virtual IP address. Users must access the application services provided by the cluster through this virtual IP address, after which the load scheduler will select a suitable node from the application server list to respond to user requests.

IPVS has different implementation methods, such as NAT, TUN (IP Tunneling), and DR (Direct Routing).

### Benefits

- **Good performance**: LVS is integrated into the OS kernel and distributes user requests at layer 4 of OSI model
- **Simple configuration**: LVS has been widely supported by Linux and FreeBSD OS
- **Work is stable**: LVS has been proven to have strong reliability in practical applications, and has complete dual-machine hot backup plan such as LVS and Keepalived, and LVS and Heartbeat

## Algorithms

https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/load_balancer_administration/ch-initial-setup-vsa

## Components

### VIP (Virtual IP)

the VIP is the IP address that will be accessed by all clients.

### Real server

A real server hosting the application accessed by client requests.

### Server pool

A farm of real servers.

### Virtual server

The access point to a Server pool.

### Virtual service

A TCP/UDP service associated with the VIP.
