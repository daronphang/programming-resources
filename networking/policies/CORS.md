## Cross-Origin Resource Sharing (CORS)

CORS is an HTTP-header based mechanism for integrating applications. CORS defines a way for client web applications that are **loaded in one domain to interact with resources in a different domain**. This is useful because complex applications often reference third-party APIs and resources in their client-side code.

CORS is an **extension of SOP**. You need CORS when you want to pull data from external APIs that are public/authorized. You also need CORS if you want to allow third-party access to your own server resources.

However, provides potential for cross-domain based attacks such as cross-site request forgery (CSRF).

### Simple requests

Simple requests don't trigger a CORS preflight. Hence, even if Access-Control-Allow-Origin header is invalidated, the **request can still be made to the server**, but CORS will **block the browser from reading the response body**.

### Preflight requests

Some HTTP requests are considered complex and requires server confirmation before the actual request is sent. This is because they **may have implications for user data**. The pre-approval process is called preflight request.

Cross-origin requests are complex if they meet any of the following:

- Methods other than GET, POST, or HEAD
- Headers other than Accept-Language, Accept, or Content-Language
- Content-Type headers other than multipart/form-data, application/x-www-form-urlencoded, or text/plain

#### How preflight requests work

The browser sends the preflight request before the actual request message:

1. Client makes a preflight request to browser (OPTIONS). OPTIONS request requires three headers:

- Access-Control-Request-Method
- Access-Control-Request-Headers
- Origin

```http
OPTIONS /doc HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Connection: keep-alive
Origin: https://foo.example
Access-Control-Request-Method: POST
Access-Control-Request-Headers: X-PINGOTHER, Content-Type
```

2. Server responds with information about the cross-origin requests the server is willing to accept from the client URL. The **server response headers must include** the following:

- Access-Control-Allow-Methods
- Access-Control-Allow-Headers
- Access-Control-Allow-Origin
- Access-Control-Max-Age (Optional, for browser caching)

```http
HTTP/1.1 204 No Content
Date: Mon, 01 Dec 2008 01:15:39 GMT
Server: Apache/2
Access-Control-Allow-Origin: https://foo.example
Access-Control-Allow-Methods: POST, GET, OPTIONS
Access-Control-Allow-Headers: X-PINGOTHER, Content-Type
Access-Control-Max-Age: 86400
Vary: Accept-Encoding, Origin
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
```

3. Client sends actual request to the server
4. Server sends actual response back to client

### Credentialed requests

The most interesting capability exposed by fetch() or XMLHttpRequest and CORS is the ability to make 'credentialed' requests that are aware of HTTP cookies and HTTP authentication information. By default, cross-origin fetch() or XMLHttpRequest calls **will not send credentials or cookies**.

When a server is responding to a credentialed request during preflight, the browser will **accept** the response and make it available to the invoking web content if all of the following conditions are met:

- Access-Control-Allow-Credentials header must be true
- Access-Control-Allow-Origin header must not contain '\*' wildcard
- Access-Control-Allow-Headers header must not contain '\*' wildcard
- Access-Control-Allow-Methods header must not contain '\*' wildcard
- Access-Control-Expose-Headers header must not contain '\*' wildcard

Also, if the response has **Set-Cookie** header, it will be prohibited if Access-Control-Allow-Origin contains '\*' wildcard.

### CORS and CSRF

CORS does prevent a specific type of CSRF attack, but not all scenarios. CORS is only implemented in browsers and prevent third-party websites from masquerading as a user in order to **read private data** from another site, but it does not prevent modifying of data through POST request.

## Postman and CORS

Postman does not throw CORS error because:

- CORS standard is implemented by browser which prevents call from completing and generates error message.
- Postman does not implement CORS restrictions as CORS defines restrictions relative to origin of page which initiates the request.
- Postman does not originate from a page with an URL.
