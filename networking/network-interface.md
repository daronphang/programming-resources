## Network Interface

A network interface is the point of interconnection between a computer and a private or public network. Can exist as either an NIC or implemented in software.

A network interface is the network-specific software that communicates with the network-specific device driver and the IP layer in order to provide the IP layer with a consistent interface to all network adapters that might be present.

From the network’s point of view, network interfaces are the endpoints of the network, as here the network packets are injected into, respectively retrieved from the network. As all endpoints of a network must be uniquely addressable, each network interface is assigned a unique number.

When you send a packet to an IP address, your route table decides which network interface that packet goes through. This is one of the first things that happens in the network stack.

## Network Interface Card (NIC)

An NIC is a hardware component without which a computer cannot be connected over a network. It is a circuit board installed in a computer that provides a dedicated network connection to the computer.

## eth0, wlan0

To avoid ambiguity when having multiple network cards in a system, eth0 defaults to the ethernet interface that is used when connecting to the internet via LAN cable connection. Similarly, when using WiFi, it uses wlan0 (WirelessLAN).

```sh
$ ifconfig
$ ip link list
```
