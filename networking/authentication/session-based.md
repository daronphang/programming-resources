## Session-Based

A session is a small file (i.e. JSON) that stores information about the user. It is generated and stored on the server so that the server can keep track of user requests.

### How it works

- User sends a login request to the server
- Server authenticates the login request
- Server stores the session in a persistent storage or in-memory and returns a cookie containing the session ID of the user
- User sends new requests with cookie
- Server looks up the session ID in stored memory and if found, sends the requested resources to the user

## Benefits

### Easy to use

Cookies are supported by the browser on the client-side.

### Small storage size

Session cookies are small in size and makes it efficient for storage.

## Drawbacks

### Limited scalability

As session is stored on the server, it becomes inherently difficult to scale.

### Multiple domains challenge

Cookies typically work on a single domain or subdomains, and becomes problematic for API requests that are sent to services of different domains.

### Security

Cookies are relatively susceptible to CSRF attacks and protective measures should be employed in servers.
