## ADN (Application Delivery Networking)

The Internet has undergone an evolution from highly centralized model to large-scale distributed client/server model. Moreover, globalization is inevitable, with more organizations becoming increasingly dispersed. This has brought about two challenges:

- Information security and data consistency issues
- Performance issues of the application system

To cope with these challenges, many enterprises plan to re-centralize their information infrastructure:

- Centralize information storage and application control points to reduce security risks
- Centralize IT infrastructure to further improve maintenance efficiency and reduce costs

However, a centralized infrastructure requires high-speed network connectivity and high-performance guarantee i.e. function like a local network. To resolve this, ADN was introduced.

ADN utilizes network optimization and acceleration equipment to ensure that customer business applications can be delivered quickly, safely and reliably to internal staff and external user groups. Its application goals are summarized as follows:

- Improve the productivity of users and IT departments
- Accelerate various applications
- Save bandwidth usage of the domain network
- Reduce the demand for IT facilities from remote organizations

Applying accelerated networking is an upgrade and extension of traditional network load balancing, which comprehensively utilizes various technologies including load balancing, TCP optimization management, link management, SSL VPN, compression optimization, intelligent NAT, advanced routing, and intelligent port mirroring.

## Wide network acceleration

Usually, domain network acceleration devices are deployed in pairs at both ends of the domain network and are **transparent to users**. The working principle of domain network acceleration mainly includes several important steps such as data cutting, data index compression, data concatenation, data reconstruction and recovery.

### How it works

1. Data requests are sent directly from client to server
2. Server sends response back to client
3. During the transmission process, the server-side network acceleration device intercepts the response and segments the data
4. After data segmentation, response data and cached data is compared to identify duplicated content, and only new bytes are sent. Compression processing is required before formal sending
5. After compression, data is transmitted over WAN and received by the domain network acceleration device
6. Domain network acceleration device reconstructs the received data and sends it to the client

### TCP protocol optimization

TCP protocol optimization is an attempt to optimize the protocol setting. High-speed TCP transmission technology is a relatively common TCP protocol optimization technique, which allows users to obtain up to 800 Mb/s bandwidth in a single TCP connection. This avoids situations such as rapid attenuation and poor bandwidth utilization rate.

The key technologies used in high-speed TCP transmission includes:

- **Self-adaptive congestion window**: Based on network latency and other heuristics, the window size can be automatically adjusted to achieve highest bandwidth transmission
- **Limited fast retransmission**: Sets the priority of retransmitted packets to be higher than other data packets, resulting in faster responses and reduced application waiting time
- **Connection pooling**: The network acceleration device maintains a pre-established TCP connection pool. When data transmission is required, it selects an available connection from the pool. This saves TCP connection establishment time

## SSL acceleration

HTTPS achieves transmission encryption and prevent important data such as user data and transaction data from being stolen. However, SSL encryption is a processor-intensive encryption algorithm that consumes a lot of CPU resources if processed by server software. Therefore, dedicated SSL acceleration devices are generally deployed around servers that provide business capabilities and implemented using hard decryption methods.

In an SSL session, the most computationally expensive part is the SSL **grip stage**, where its main task is to negotiate the session symmetric key that will be used throughout corresponding session process. Moreover, the encryption and signature of the SSL grip message itself are asymmetric keys included in the certificate, which consumes more computing resources than symmetric keys.

To resolve this, SSL acceleration technology will **delegate the SSL gripping process to specialized hardware devices**. Some implementations retain symmetric encryption and decryption operations on the server for software implementation, while others allow SSL-specific hardware to handle SSL operations as a proxy and hand over the HTTP content without the SSL layer to the server.

### SSL acceleration board

Installing an SSL acceleration board on the server can effectively share the pressure of the server CPU processing SSL transactions. SSL acceleration boards usually have one or more coprocessors used to implement SSL calculations.

However, the use of SSL acceleration boards results in the inability to maintain session persistence. Usually, a web server cluster is connected through a 4-layer switch, and the load balancing device maintains session persistence by checking the HTTP request header and cookie information. If SSL is managed by the board, the **load balancing device cannot decrypt** and inspect content for session routing.

To solve this problem, a method based on SSL session identification has been proposed.

### SSL acceleration device

The SSL acceleration device is an independent device embedded in the SSL acceleration board. It is used to decrypt encrypted traffic and send decrypted information to the backend server, and vice versa.

SSL acceleration devices are implemented together with load balancers, mainly due to cost considerations and the ability to meet the needs of supporting session persistence.

### Challenges

The biggest challenge faced by administrators is certificate management. Each server in the cluster must have a unique digital certificate; the purchase, deployment, maintenance, etc. of the certificate will greatly increase the overall cost of SSL implementation.
