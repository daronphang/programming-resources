## Same-Origin Policy (SOP)

Today, browsers enforce that clients can only send requests to a resource with the same origin as the client's URL. The protocol, port, and hostname of the client's URL should all match the server it requests. SOP is highly secure but inflexible for genuine use cases.

**SOP prevents the response from being read by another domain in the browser, and is irrelevant to whether a CSRF attack is successful or not** i.e. it does not prevent the request from being sent by the browser. The only time SOP comes into play with CSRF is to prevent any token from being read by a different domain.

```
https://www.example.com:443
scheme      hostname    port
```
