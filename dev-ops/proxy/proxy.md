## Reverse proxy

Reverse proxy is used by the server such as web server to achieve load balancing and high availability. Reverse proxies are used to protect servers. Takes requests from the browser and forwards them to one of the backend web servers. Nginx, Apache and HAProxy can act both as a web server and reverse proxy. Client only communicates directly with the reverse proxy server and does not know that other servers actually processed its request.

- Server that sits in front of web server that accepts a request from client, forwards it to another web server that can fulfill it, and return server's response to client
- Enhances security as information about backend servers are not visible outside of internal network and protects against DDoS attacks
- Increases scalability and flexibility as clients see only reverse proxy's IP address i.e. can change configuration of backend infrastructure
- Reduces time taken to generate response with compression (reducing bandwidth required for transmitting responses), SSL termination (decrypts incoming requests and encrypts server responses) and caching (stores copy of response locally)

## Forward proxy

Forward proxy is used by the client such as web browser. Can reside in the same internal network as the client, or it can be on the internet. Can be used to bypass firewall restrictions in order to visit websites that are blocked by school, government, etc. For instance, forward proxy can be used to hide the real IP of the client. Forward proxies are used to protect clients.

- Provides proxy services to a client or group of clients
- Request from client are forwarded to proxy which can be allowed or denied depending on proxy's settings
- Different clients can send out various requests to different servers through forward proxy
- Easier to enforce authentication, SSL encryption or other security policies; used in tandem with firewall
- Can act as a cache server in an internal network i.e. downloading of same resource

## Reverse proxy vs load balancer

Reverse proxy servers and load balancers are components in client-server computing architecture whereby both act as intermediaries in communication between clients and servers, performing functions that improve efficiency.
