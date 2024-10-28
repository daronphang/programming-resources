## Layering of security mechanisms

An important issue in designing secure systems is to decide at which level security mechanisms should be placed. A level in this context is related to the logical organization of a system into a number of layers.

### VPN

A VPN sets up a tunnel between two remote local networks, or between a host and a remote network. The effect is that a computer on one network seems to be directly connected to the remote network. Although not strictly necessary, a VPN normally encrypts all traffic between its end points and operates at the level of the data link layer or the network layer.

### TLS

TLS can be used to securely send messages across a TCP connection. TLS forms the standard approach for secure communication with Websites employing HTTPS. HTTPS establishes an authenticated connection to a Website through which all data exchanged between a client and the server is encrypted.

### SSH

SSH is used to establish a secure remote login. Unlike HTTPS, SSH comes with its own security protocol and does not rely on a transport-layer security service.

### End-to-end application level security

All secure communication within the distributed application is handled by the application itself. There is no reliance on middleware security services. This can be done by encrypting any data first before sending it off.
