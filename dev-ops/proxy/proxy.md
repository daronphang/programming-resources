## Reverse proxy

Reverse proxy is used by the server such as web server to achieve load balancing and high availability. Reverse proxies are used to protect servers. Takes requests from the browser and forwards them to one of the backend web servers. Nginx, Apache and HAProxy can act both as a web server and reverse proxy. Client only communicates directly with the reverse proxy server and does not know that other servers actually processed its request.

- Server that sits in front of web server that accepts a request from client, forwards it to another web server that can fulfill it, and return server's response to client
- Enhances security as information about backend servers are not visible outside of internal network and protects against DDoS attacks
- Increases scalability and flexibility as clients see only reverse proxy's IP address i.e. can change configuration of backend infrastructure
- Reduces time taken to generate response with compression (reducing bandwidth required for transmitting responses), SSL termination (decrypts incoming requests and encrypts server responses) and caching (stores copy of response locally)

### Benefits

- Server anonymity (security)
- Caching
- Load balancing
- Offloading TLS encryption
- DDoS protection
- Canary experimentation
- URL/content rewriting

### Reverse proxy vs load balancer

Reverse proxy servers and load balancers are components in client-server computing architecture whereby both act as intermediaries in communication between clients and servers, performing functions that improve efficiency.

## Forward proxy

Forward proxy is used by the client such as web browser. Can reside in the same internal network as the client, or it can be on the internet. Can be used to bypass firewall restrictions in order to visit websites that are blocked by school, government, etc. For instance, forward proxy can be used to hide the real IP of the client. Forward proxies are used to protect clients.

- Provides proxy services to a client or group of clients
- Request from client are forwarded to proxy which can be allowed or denied depending on proxy's settings
- Different clients can send out various requests to different servers through forward proxy
- Easier to enforce authentication, SSL encryption or other security policies; used in tandem with firewall
- Can act as a cache server in an internal network i.e. downloading of same resource

### Benefits

- Client anonymity
- Caching
- Traffic control
- Logging
- Request/response transformation (adding/removing headers, encrypting/decrypting, compressing)
- Collapsed forwarding by combining same data access requests into one request

## Transparent proxy (inline/intercepting/forced proxy)

A transparent proxy is a server that acts as a middleman between a user's device and the internet, intercepting and forwarding network traffic **without modifying it**. Squid Transparent Proxy Server is a popular open source transparent proxy tool. This method is mainly used for enterprise users.

With this method, the user's browser does not need to configure the proxy server address, but the user's routing device needs to support the **WCCP (Web Cache Control Protocol)**. After the router is configured with the WCCP function, it will forward the specified user traffic to the Cache, which will provide services to the user. Another solution is to use a layer-4 switch to forward the user's traffic to the cache.

### Client-side

Use cases for client-side transparent proxies include:

- **Content filtering**: Filter out unwanted content
- **Gateway proxies**: Modify or block network traffic based on rules
- **Caching**
- **Traffic monitoring**: Monitor user traffic and behavior
- **Authentication**

### Server-side

Use cases for server-side transparent proxies include:

- TCP intercept for DDoS protection
- CDN for front-end optimization
