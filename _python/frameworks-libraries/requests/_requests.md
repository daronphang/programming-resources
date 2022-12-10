## Pooling

The session object allows you to persist certain parameters across requests. It also persists cookies across all requests made from the Session instance, and uses urllib3's connection pooling.

If you are making several requests to the same host, the underlying TCP connection will be reused, which can result in significant performance increase.
