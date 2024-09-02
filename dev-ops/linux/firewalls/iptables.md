## IPtables

Iptables was built over two decades ago as a packet filter and firewall tool within the Linux kernel. It analyzes, modifies, and filters network packets on a set of user-defined rules based on IP addresses or port-based rules (TCP/UDP).

Iptables is a standard firewall included in most Linux distributions by default. It is a command-line interface to the kernel-level netfilter hooks that can manipulate the Linux network stack. It works by matching each packet that crosses the networking interface against a set of rules to decide what to do.

## Components

### Chains

An iptables chain is the ordered list of rules that is evaluated sequentially when a packet traverses the chain.

There are 5 chains in iptables and each is responsible for a specific task:

- PREROUTING: Decides what happens to a packet as soon as it arrives at the network interface i.e. NAT, dropping a packate, or do nothing at all
- INPUT: This chain handles all packets that are addressed to your server; used when you want to open/block a port
- OUTPUT: This chain contains rules for traffic created by your server
- FORWARD: This chain is used to deal with traffic destined for other servers that are not created on your server. This chain is a way to configure your server to route requests to other machines
- POSTROUTING: This chain is where packets leave their trace last, before leaving our computer

A user can create chains as needed. There are three chains defined by default: INPUT, OUTPUT, FORWARD.

```sh
$ # drop incoming traffic on port 80
$ iptables -A INPUT -p tcp --dport 80 -j DROP 
```

### Tables

An iptables table is a way to group together chains of rules, iptables has five tables:

- Filter: Decide whether a packet is allowed in/out your computer
- NAT: Responsible for creating new connection
- Mangle: Responsible for changing something inside the packet either before coming in or leaving out
- Raw: Dealing with raw packets i.e. tracking the connection state
- Security: Responsible for securing your computer after the filter table (SELinux)

### Targets

When the defined pattern matches, the action that takes place is called a **target**. A target can be a final policy decision for the packet (ACCEPT, DROP). It can also move the packet to a different chain for processing, or log the encounter.

Common targets include:

- ACCEPT: Allows the packet to pass through the firewall
- DROP: Discards the packet without informing the sender
- REJECT: Discards the packet and returns and error response to the sender
- LOG: Records packet information into a log file
- SNAT (Source NAT): Alters the packet's source address
- DNAT (Destination NAT): Changes the packet's destination address
- MASQUERADE: Alters a packet's source address for dynamically assigned IPs

### How it works

The iptables firewall operates by comparing network traffic against a set of rules. The rules define the characteristics that a network packet needs to have to match, and the action that should be taken for matching packets.

## Commands

```sh
$ iptables -L -n -v --line-numbers
```
