## Dynamic Host Configuration Protocol (DHCP)

Dynamic Host Configuration Protocol (DHCP) provides one of the most commonly used services in a TCP/IP network. The vast majority of hosts in a TCP/IP network are **user devices**, and the vast majority of user devices learn their IPv4 settings using DHCP.

### Benefits over manual configuration of IPv4 settings

Configuration of host IP settings sits in a DHCP server, with each client learning these settings using DHCP messages. Hence, host IP configuration is controlled by IT staff, rather than on local configuration on each host, resulting in fewer errors.

DHCP allows both the permanent assignment and temporary lease of host IP address. With these leases, the DHCP server can reclaim IP addresses when a device is removed from the network, making better use of the available addresses.

DHCP enables mobility. For example, every time a user moves to a new location with a tablet computer, the user’s device can connect to another wireless LAN, use DHCP to lease a new IP address in that LAN, and begin working on the new network. Without DHCP, the user would have to ask for information about the local network and configure settings manually, with more than a few users making mistakes.

## Concepts

As a DHCP client, the host begins with no IPv4 settings i.e. no IPv4 address, no mask, no default router, no DNS server IP addresses. However, a DHCP client does have knowledge of the DHCP protocol, so the client can use that protocol to:

1.  Discover a DHCP server
2.  Request to lease an IPv4 address

DHCP uses the following messages between client and server:

- Discover: Sent by the DHCP client to find a willing DHCP server
- Offer: Sent by a DHCP server to offer to lease to that client a specific IP address
- Request: Sent by the DHCP client to ask the server to lease the IPv4 address listed in the Offer message
- Acknowledgement: Sent by the DHCP server to assign the address and to list the mask, default router, and DNS server IP addresses

### Discover and Offer

As DHCP clients do not have an IP address initially, it makes use of two special IPv4 addresses that allow a host that has no IP address to send and receive messages on the local subnet:

- 0.0.0.0: An address reserved for use as a source IPv4 address for hosts that do not yet have an IP address
- 255.255.255.255: The local broadcast IP address; packets sent to this destination are broadcast on the local data link, but routers do not forward them

All hosts in the subnet receive the Offer message. However, the original Discover message lists a number called the client ID, which includes the host’s MAC address, that identifies the original host.

<img src="../assets/DHCP.png">
