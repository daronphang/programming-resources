## DC network

```
      E-CORE
        |
AGGREGATION (AGG)
        |
TOP OF RACK (TOR)
        |
    Servers
```

### ECORE (Edge Core, Extended Core)

The ECORE layer sits at the top of the data center network and connects the internal network to external networks. It is responsible for north–south traffic, including connections to WANs, ISPs, IXPs, and other data centers. ECORE switches focus on high throughput, high availability, and large-scale routing (typically BGP).

### AGG (Aggregation/Distribution)

The aggregation layer collects and consolidates traffic from multiple TOR switches. It acts as a control and policy boundary where routing, ACLs, and traffic segmentation are often applied. AGG switches are designed to handle large volumes of east–west traffic within the data center.

### TOR

ToR (Top of Rack) is a switch located at the top of a server rack. Its primary function is to connect all servers within the rack and aggregate traffic to upper-layer network devices, such as core switches or aggregation switches. It is the first-hop switch for servers. This configuration helps improve network performance, reduce latency, and simplify data center network management, making it suitable for internal data center network communication and management scenarios. Many downlinks (10G/25G/50G) to servers, but few uplinks (40G/100G) to AGG.

## POPs

### Neutral

Neutral POPs are located in carrier-neutral DCs which can contain multiple ISPs, IXPs, CDNs and clouds in the same physical building. You choose who to interconnect with, e.g. PNI with many ISPs, PPI via IXPs, IPT to multiple ISPs. Neutral POPs provide maximum peering options with best eyeball coverage (traffic heavy regions).

### Private

Private POPs are located inside ISP networks/facilities, i.e. CDN is a guest inside the ISP. Usually only provides PNI with that ISP, with little or no IXP access. Split between IPT (small traffic, 100MB~1G) and PNI is usually performed by ISP themselves. Typical usecases include large eyeball ISPs, mobile networks, or regional markets with poor IX.
