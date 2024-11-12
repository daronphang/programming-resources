## Content Delivery Network (CDN)

A Content Delivery Network (CDN) is a geographically distributed network of servers and data centers designed to deliver web content to users more efficiently and reliably. It caches content such as images, videos, and other static assets.

The Internet consists of a network layer (TCP/IP) and an application layer (WWW). The network layer is a neutral "pipeline" that is not optimized for specific content, while the application layer includes various Internet services. During the Internet transmission process, there are issues that can cause content transmission delays and affect user experience, including "first kilometer" (server bandwidth), "last kilometer" (user access bandwidth), peer-to-peer interconnection gateways, long-distance backbone transmission, etc.

The primary purpose of a CDN is to reduce latency and high WAN bandwidth cost, optimize content transmission and improve the overall performance of web applications by serving content from the server nearest to the user. CDNs can also help improve reliability, availability, and security of web applications.

<img src="../assets/CDN.png">

### How it works

1. Browser requests local DNS to resolve domain name. If it caches the resolution result of the domain name, it responds directly back to the user. Otherwise, a recursion request is made to the entire DNS system for resolution, which points to the CDN dedicated DNS server by CNAME. DNS server returns the IP address of the CDN's GSLB back to the user
2. User initiates a content URL access request to the GSLB
3. GSLB selects a regional LB in the user's region based on the user's IP address and the requested content URL
4. User initiates a content URL access request to the regional LB
5. Regional LB selects a suitable cache node based on heuristics including user's IP address, CPU and memory usage, bandwidth, etc.
6. User initiates a request to the cache server

## Benefits

### Reduced latency and improved customer experience

By serving content from geographically distributed edge servers, CDNs reduce the time it takes for content to travel from the server to the user, resulting in faster page load times and improved user experience.

### Improved performance and reduced origin server costs

As website content keeps diversifying, the load on origin server also increases. Scaling up the origin server or implementing distributed deployment for user access often result in higher costs.

CDNs can offload static content delivery from the origin server, freeing up resources for dynamic content generation and reducing server load. This can lead to improved overall performance for web applications.

### Enhanced reliability and availability

With multiple edge servers in different locations, CDNs can provide built-in redundancy and fault tolerance. If one server becomes unavailable, requests can be automatically rerouted to another server, ensuring continuous content delivery.

### Scalability

CDNs can handle sudden traffic spikes and large volumes of concurrent requests, making it easier to scale web applications to handle growing traffic demands.

### Security

Many CDNs offer additional security features, such as DDoS protection, Web Application Firewalls (WAF), and SSL/TLS termination at the edge, helping to safeguard web applications from various security threats.

## Value analysis

### Professional segmentation

CDN is a key part of the Internet industry chain, and has obvious personalized features due to the lack of internationally unified standards and specifications. The accumulation of professional experience accelerates the sustainable development of division of labor.

### Outsourcing services

CDN services not only provide distribution technology, but also a nationwide outsourcing service network. Content providers are often concentrated in one location, but users are spread across different geographical regions. Nowadays, rich media applications (high-definition videos) require content to be provided as close to users as possible.

The global maintenance system established by CDN operators can help to solve the operation and maintenance of websites globally. Moreover, it can fully utilize resource price difference and staff training and employment mechanism in different regions to assume the responsibility of serving users.

### Centralized procurement

CDN operators need to purchase hardware and data center bandwidth resources needed to set up CDN networks in large quantities, thus establishing a complete resource procurement system. Some CDN operators also operate IDC hosting services.

When purchasing bandwidth and rack resources from telecom operators, they have stronger bargaining power due to the large procurement volume.

### Available on-demand

The actual bandwidth requirements of the website are constantly changing based on business content, user behavior, consumption patterns, and pricing methods, often resulting in sudden increases and decreases. If all bandwidth is purchased by oneself and accurate estimations cannot be made, this will result in excessive reserve resources such as bandwidth wastage. Conversely, if resources are insufficient, bandwidth becomes a bottleneck and create inconvenience to users.

During actual operations, due to the relatively stable number of networks in a certain area, the online habits and time of the network are also relatively stable. When examining the overall behavior of the network, its bandwidth demand is generally a **stable curve**. Therefore, the operational pressure of CDN service nodes that provide multiple website content to the network is generally in a **stable state**, which is more predictable and controllable than a single website.
