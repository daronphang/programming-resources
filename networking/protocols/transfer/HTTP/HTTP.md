## Hypertext Transfer Protocol Secure (HTTP)

HTTP is an application layer protocol for fetching resources such as HTML documents. It is the foundation of any data exchange on the World Wide Web and it **follows a client-server model** i.e. requests are initiated by the recipient, usually the web browser.

HTTP defines how messages are formatted and transmitted across the web, with instructions for browsers and servers on how to respond to various requests and commands. HTTP is through port 80 while HTTPS is through port 443.

Clients and servers communicate by exchanging individual messages (as opposed to a stream of data). Each request is sent to a web server, which handles it and provides a response. Between the client and server there are numerous entities called proxies, which perform different operations and acts as gateways or caches.

## What is in an HTTP Request?

Each HTTP request made across the Internet carries with it a series of encoded data that carries different types of information. A typical HTTP request contains:

1. HTTP version type
2. URL
3. HTTP method
4. HTTP request headers
5. Optional HTTP body

### Request methods

- GET: Obtain a resource
- POST: Create a new resource
- PUT: Modify an existing resource
- HEAD
- DELETE
- PATCH: Replace an existing resource
- CONNECT
- TRACE
- OPTIONS

### Media types (MIME)

Formats of resource representations are specified through the use of media types in the Content-Type header.

```
Content-Type: application/json; charset=utf-8
Content-Type: application/xml
```

### Headers

Headers contain important identifier information as to the request's metadata, including authorization, URI, caching, cookies, etc.

- Host: Specifies the host and port number of server to which the request is being sent
- Cache-control
- Authorization
- WWWW-Authenticate
- Accept-Charset
- Content-Type
- Location: URL for the browser to redirect to when it receives a 301

## What can be controlled by HTTP

- Caching
- Relaxing origin constraint
- Authentication
- Proxy and tunneling
- Sessions through HTTP cookies

## Features

### HTTP is simple

HTTP is generally designed to be simple and human readable, even with the added complexity introduced in HTTP/2 by encapsulating HTTP messages into frames.

### HTTP is extensible

Introduced in HTTP/1.0, HTTP headers make this protocol easy to extend and experiment with. New functionality can even be introduced by a simple agreement between client and server about a new header's semantics.

### HTTP is stateless, but not session-less

There is no link between two requests sent successively on the same connection. Nonetheless, HTTP cookies allow the use of stateful sessions.

## HTTP flow

When a client wants to communicate with a server or an intermediate proxy, it performs the following steps:

1. Open a TCP connection (client can open a new connection, reuse an existing connection, or open several TCP connections to servers)
2. Send an HTTP message (HTTP/2 encapsulates messages into frames and hence, impossible to read directly)

```
GET / HTTP/1.1
Host: developer.mozilla.org
Accept-Language: fr
```

3. Read response sent by server

```
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT
ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes
Content-Length: 29769
Content-Type: text/html

<!DOCTYPE html... (here come the 29769 bytes of the requested web page)
```

4. Close or reuse the connection for further requests

## Participants

### Client

Browser is always the entity initiating the request. The procedure for a browser to display a webpage is as follows:

1. Browser translates URL into a request message according to HTTP
2. Browser sends an original request to fetch the HTML document that represents the page
3. Parses the file i.e. makes additional requests corresponding to execution scripts, layout information (CSS) to display, and sub-resources contained within the page (usually images and videos)
4. Combines resources to present the complete document
5. Scripts executed by the browser can fetch additional resources in later phases and browser updates accordingly

### Web Page

A webpage is a hypertext document i.e. some parts of the displayed content are links which can be activated.

### Web Server

Serves the document as requested by the client. A server may be collection of servers sharing the load (load balancing), or a complex piece of software interrogating other computers i.e. cache, DB server, or e-commerce servers.

### Proxies

Computers/machines located between the web browser and server that relay the HTTP messages. They may perform caching, filtering, load balancing, authentication, and logging. Proxies operate at the Application layer and can be:

- Transparent: Forwarding on the requests they receive without altering them in any way
- Non-Transparent: Change the request in some way before passing it along to the server
