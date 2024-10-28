## HTTPS

Hyper Text Transfer Protocol secure. Appears in URL when a website is secured by an SSL/TLS certificate.

## Protocol versions

```
SSL v2      Has serious security vulnerabilities
SSL v3      Has serious security vulnerabilities
TLS 1.0     Does not support modern cipher suites
TLS 1.2     Recommended version
TLS 1.3
```

## SNI (Server Name Indication)

Domain name information is not passed during SSL handshake, and the server usually returns the first available certificate in the configuration. If multiple certificates are needed, you have to configure different SSL ports or add IP addresses, or purchase "multi-domain SSL certificate" or "wildcard certificate" that is very expensive.

SNI is a technology used to optimize SSL/TLS and is enabled in SSLv3/TLSv1. It allows the client to **specify the hostname** it is trying to reach when initiating an SSL handshake request, so the server can switch to the correct domain and return the corresponding certificate. This helps systems simplify the process of certificate deployment and adjustment, and reduce the time for adjusting resource coverage and reporting problems.
