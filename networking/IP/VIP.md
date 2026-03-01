## VIP

A VIP is a logical IP address that represents a service (stable front-door IP), not a specific machine. It lets traffic keep flowing even when the backend servers change or fail. Clients connect to the VIP, and the network/load balancer decides which real server actually handles the request. With a VIP:

- Clients connect to one fixed IP
- Backends can change freely
- Failover is transparent

### Usecases

- L4/L7 load balancers including F5, Nginx, HAProxy, Envoy (VIPs are bound to the LB)
- HA VIP (Keepalived/VRRP) whereby VIP floats between nodes (active/passive)
- Anycast VIP
