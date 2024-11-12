## ARP (Address Resolution Protocol)

ARP is a protocol that connects an ever-changing (dynamic) IP address to a **fixed physical machine address**, also known as a **media access control (MAC) address**, in a LAN.

This mapping procedure is important because the lengths of the IP and MAC addresses differ, and a translation is needed so that the systems can recognize one another. The most used IP today is IP version 4 (IPv4). An IP address is 32 bits long. However, MAC addresses are 48 bits long. ARP translates the 32-bit address to 48 and vice versa.

### How it works

- When a new computer joins a LAN, the network assigns it a unique IP address for identification and communication
- When an incoming packet destined for a host machine on a LAN arrives at a gateway, the gateway asks the ARP to find a MAC address that matches the IP address
- The ARP cache table maintains a record of each IP address and its corresponding MAC address
- ARP caches are kept on all OS in an IPv4 Ethernet network
- ARP cache is purged regularly to free up space, and to prevent IP addresses from being stolen or spoofed by cyberattackers

### Why is ARP needed

ARP is necessary because the virtual IP address of the host or computer connected to the network needs to be translated to a MAC address on a LAN, in order to provide the **layer 2 destination information**. Without ARP, a host would not be able to figure out the hardware address of another host. Network interface cards are using Ethernet and hence, they understand MAC addresses and need them to communicate.
