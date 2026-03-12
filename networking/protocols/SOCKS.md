## SOCKS (Socket Secure)

SOCKS proxy is a low-level proxy protocol that forwards network traffic between a client and a server. Unlike HTTP proxies, SOCKS operates at the session layer (layer 5) and can handle any type of traffic (TCP, UDP).

### How it works

1. Client connects to a SOCKS proxy server
2. Client tells the proxy: “Connect me to this destination”
3. The proxy establishes the connection on behalf of the client
4. Traffic flows through the proxy transparently

### Versions

- SOCKS4: Basic TCP support, no authentication
- SOCKS5: Supports authentication, UDP, IPv6

## SSH and SOCKS proxy

You can create an encrypted SSH connection while running a SOCKS proxy inside it.

```sh
$ ssh -D 1080 user@server
```
