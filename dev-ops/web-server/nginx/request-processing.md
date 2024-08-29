## How Nginx Processes a Request

1. If IP address and port are provided, Nginx first tests them against the listen directives of the server blocks
2. Nginx tests the request's header field 'Host' against the server_name to determine which server the request should be routed to
3. If no value is found, Nginx routes to the default server
4. Requests without 'Host' header field will have server_name set to an empty string (default setting since v0.8.48)

A default server is a property of the listen port, and different default servers may be defined for different ports.

```conf
server {
    listen      192.168.1.1:80;
    server_name example.org www.example.org;
    ...
}

server {
    listen      192.168.1.1:80 default_server;
    server_name example.net www.example.net;
    ...
}

server {
    listen      192.168.1.2:80 default_server;
    server_name example.com www.example.com;
    ...
}
```
