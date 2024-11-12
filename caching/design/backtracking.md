## Backtracking

When the cache node does not cache the requested resource or it has expired, it sends a request to the origin.

### Backtrack HOST

Backtracking HOST determines which site on the IP the backtracking request accesses:

- Source site: www.a.com
- Backtrack HOST: www.b.com

### Protocol backtracking

Protocol backtracking means that the protocol used when backtracking is consistent with the protocol used by the client to access resources e.g. HTTP, HTTPS.

### Filter parameters

Filter parameters switch allows you to ignore the parameters in the user request URL (e.g. www.a.com/user?hello=world)according to business needs:

- On: Cache node will intercept the URL without parameters to request the source site
- Off: Cache node will cache a different copy for each URL
