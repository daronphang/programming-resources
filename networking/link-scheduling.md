## Link scheduling

Link scheduling in a CDN or network context refers to how traffic is dynamically routed or balanced across multiple upstream links. Traffic attribution and billing to customers are primarily based on logs as they reflect the full-amount of traffic data, with dimensions like country, province, ISP, domain, URI, bytes, etc.

### PNI (Private Network Interconnect)

A dedicated physical connection (public peering) between PoP and specific ISP (point-to-point) with no third party involved, i.e. direct peering with ISP to serve its eyeballs only. It gives good performance (low latency, high availability, high bandwidth) and helps to predict forecasts (one time setup and port costs, but no recurring cost and per-bit traffic cost). PNI is used when traffic is big, important and performance-sensitive. Although PNIs do not need to pay for traffic, not all ISPs provide PNI. Over a PNI, we receive routes that are behind a single ASN, unlike IPT which provide full routes.

### PPI (Paid Peering Interconnect)

PPI is basically the same as PNI, but it is not settlement free (we pay for pushing traffic) and there is money exchanged between two parties. Normally acts as a backup for PNI, and is preferred over IPT whenever peering can carry the traffic reliably. IPT acts more of a safety net.

### PCI (Private Cache Interconnect)

A private interconnect between cache clusters or cache nodes (in the same DC or metro area), usually by bypassing public peering. It is basically a PNI but specific to private POPs. Offers high reliability and consistent latency. More expensive than IXP and PNI for local peering, but cheaper and faster than transit for consistent cloud access. These links can be paid or might be settlement free based on the agreement with the provider. Local preference is not required since a private PoP only has one PCI provider, hence, no traffic manipulation is required.

### IXP (Internet Exchange Point)

A neutral exchange facility that functions as a shared peering platform (One-to-many connection) where many networks interconnect and exchange traffic via a common switch fabric (connects a switch to many ISPs). Traditionally, when an ISP needed to exchange traffic with another ISP, it would need to use a third-party provider to facilitate the exchange. This often involved paying for transit services or peering agreements, which could be expensive and add latency to the network. By connecting to an Internet exchange, ISPs can bypass the need for a third-party provider and exchange traffic directly with one another. This not only reduces costs, but it can also improve network performance by reducing latency and increasing available bandwidth. Examples include London-INX, Amsterdam-IX, DE-CIX.

IXP enables PPI. IXPs are usually placed in carrier-neutral DCs, and these DCs may also host ISP POPs, CDN POPs, cloud on-ramps. Most IXPs are run by non-profits and neutral companies. Capacity is shared across ISPs, but monitoring may not be visible, and may result in traffic congestion. Over an IXP we do not receive the entire Internet routes, we only receive the local routes for the networks connected to the IXP.

### IPT (IP Transit)

A commercial connection to the global internet, purchased from an ISP. It gives full access to the entire internet routing table via BGP (full routes). An IP transit link enables an ISP to connect its network to the rest of the internet, which allows its customers to access content and services hosted outside of the ISP's network. Hence, we receive the entire Internet routing table via the IPT link.

PPI and PNI only have partial routes (prefix provided by ISP) while IPT has full routes. Both PPI and PNI have direct peerings with local ISPs (PNI with TELIN, TSEL), which are used for local ISP eyeballs only.

Usually charged by 95th percentile or Mbps (pay to reach everyone, burstable billing). Most expensive option per Mbps but most flexible (can reach any destination globally). Common IPT providers include Lumen, Arelion, NTT, GTT, etc.

### ISP (Internet Service Provider)

An ISP is a company that connects users or organizations to the internet. An upstream ISP is a provider that gives internet connectivity, while a downstream ISP is a provider/customer that receives internet connectivity from upstream. Types of ISPs include:

- Last-mile/Access/Local ISP: Connects end users to the internet (home broadband, mobile data)
- Transit ISP: Sells internet connectivity to other ISPs or enterprises, carries large volumes of traffic
- Tier 1 ISP: Global networks that don't buy transit and is connected to many other ISPs, e.g. TATA, ARELION, NTT, COGENT, LUMEN.

### Zenlayer

Zenlayer is a global edge cloud and private network service provider that helps companies build low-latency, cross-border (CN <-> overseas), and multi-cloud connectivity, i.e. a bridge between ISPs, IXPs, and clouds. It operates its own private global network (backbone that bypasses congested public internet paths) and bare-metal/edge nodes in many cities worldwide. Zenlayer interconnects with many different ISPs in different countries.

### EBB (Edge Backbone)

A private backbone network connecting edge PoPs or regions (cross-region or country), used internally by CDN or cloud providers. EBB is a backbone circuit between edge POPs for cache fill and other internal functions (L1 -> L2, L2 -> Origin). PCI is not used as it does not scale over long distances. EBB has fixed cost.

### BBONE

BBONE are internal circuits between regional L2 POPs and IDC Origin POPs.
