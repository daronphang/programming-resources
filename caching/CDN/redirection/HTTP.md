## HTTP redirection/retargeting

HTTP-based redirection involves the proxy server redirecting the client to a closer server using HTTP status codes such as **301** (moved permanently), **302** (temporarily moved), and **meta fresh** (retargeting to a new network after a specific time). When the client sends a request to the proxy server, the server evaluates the client’s location and redirects the request to the nearest server for data retrieval.

For load balancing, 302 redirect is used as it needs to achieve immediate and temporary retargeting of the user to another service device.

Compared with DNS scheduling, HTTP retargeting has better scheduling accuracy as it uses client's IP address and not the IP address of the local DNS server. Also, it is more flexible and can be customized according to customer's requirements.

```http
# www.CDNbook.com

HTTP/1.1 302 Found
Date: Wed, 17 Mar 2010 08:11:11 GMT
Server: Apache/2.2.15 （Unix） mod_391/2.2.15 OpenSSL/0.9.7a DAV/2
PHP/5.2.9
X-Powered-By: PHP/5.2.9
Location: http://bj.CDNbook.com
Content-Length:0
```

### Drawbacks

- HTTP retargeting is only suitable for HTTP applications. For instance, Microsoft's MMS protocol and RTSP protocol cannot use this method for retargeting
- As HTTP retargeting process requires additional resolution of the domain name URI, it needs to **establish a TCP connection** with the URL and send HTTP requests, increasing the response time
- Unlike DNS method, no user request can be terminated by an external system. All requests must go through the HTTP retargeting system, which will become a**bottleneck for performance and reliability**
