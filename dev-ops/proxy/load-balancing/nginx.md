## Nginx

Nginx is a high-performance HTTP and reverse proxy server, as well as an IMAP/POP3/SMTP proxy server.

Nginx is often used to handle **load balancing at Layer 7**. the core of Nginx load balancing is the **Upstream module**:

1.  When Nginx receives an HTTP request from a user, it will create an Upstream request to the backend application server
2.  After the application server sends back the response data, Nginx will forward the data in the backend Upstream to the user
3.  The load scheduling algorithms supported by Upstream mainly include source IP-based hash, destination-based URL hash, and fair scheduling based on response time
