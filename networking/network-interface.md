## Network Interface

Network interfaces are hardware or software components that enable a computer or other device to connect to and communicate over a network. They serve as the **points of interaction between the device and the network**, facilitating the sending and receiving of data.

A network interface is the point of interconnection between a computer and a private or public network. Can exist as either an NIC or implemented in software. As all endpoints of a network must be uniquely addressable, each network interface is assigned a unique number.

A network interface is the network-specific software that communicates with the network-specific device driver and the IP layer in order to provide the IP layer with a consistent interface to all network adapters that might be present.

When you send a packet to an IP address, your route table decides which network interface that packet goes through. This is one of the first things that happens in the network stack.

### Physical

- Ethernet Interfaces: Uses MAC addresses for communication
- Wi-Fi Interfaces
- Fiber Optic Interfaces

### Virtual

- Virtual Network Interface Cards (vNICs): Software network interfaces used in virtualized environments for VMs to connect to virtual networks
- Loopback Interface: A special virtual network interface used primarily for testing and diagnostics

## Network Interface Card (NIC)

An NIC is a hardware component without which a computer cannot be connected over a network. It is a circuit board installed in a computer that provides a dedicated network connection to the computer.

### eth0, wlan0

To avoid ambiguity when having multiple network cards in a system, eth0 defaults to the ethernet interface that is used when connecting to the internet via LAN cable connection. Similarly, when using WiFi, it uses wlan0 (WirelessLAN).

```sh
$ ifconfig
$ ip link list
```

## Key functions

### Data transmission

Network interfaces handle the transmission and reception of data packets over a network. They manage the physical and data link layers of the OSI model (for physical interfaces) or higher layers (for virtual and software interfaces).

### Addressing

Each network interface typically has a unique identifier, such as a MAC (Media Access Control) address for physical interfaces or IP (Internet Protocol) addresses for network interfaces in general. These addresses ensure that data is delivered to the correct device on the network.

### Configuration

Network interfaces can be configured with various settings, including IP addresses, subnet masks, DNS servers, and other network parameters. This configuration determines how the device communicates with other devices on the network and the internet.
