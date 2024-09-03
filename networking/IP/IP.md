## IP Address

IP addresses not reachable over the internet are private and enable communication between instances in the same network. IP address uses a combination of bits (32 bit, 32 digits) that is converted into decimal format.

The 32 bits are grouped into groups of 8 bits, separated by a period.

```
192.168.1.30
11000000
10101000
00000001
00011110

127.0.0.1:<host port>         localhost
```

## CIDR notation

To express IP addresses between the range of 192.168.1.0 and 192.168.1.255. CIDR notation is a compressed way of representing a range of IP addresses.

The number after the slash specifies how many bits of the IP address are **fixed**. The higher the number, the smaller the range of IP addresses you can work with.

The smallest IP range you can have is `/28`, which provides 16 IP addresses. The largest range is `/16`, which provides 65,536 IP addresses.

```
192.168.1.0/24  # the 0 is flexible, range of 256
192.168.1.0/16  # range of 65,536 (256*256, 8bits, 8bits)
192.168.1.0/22  # range of 1024 (2*2*256)
```

## Loopback address

In networking, the loopback address is a special IP address used to test and diagnose network software and configurations on a local machine. It **allows a computer to communicate with itself over the network interface**, effectively "looping back" the network traffic to the same machine.

Traffic sent to the loopback address **never leaves the host machine**. It is handled internally by the operating system, meaning that the loopback address is not reachable from any external network or other machines.

Since the loopback address is not accessible from outside the host, it is considered secure for internal testing and development.

### IPv4

- Address: 127.0.0.1
- Address range: 127.0.0.0 to 127.255.255.255
- Purpose: Address is used to verify that the TCP/IP stack on a computer is working correctly

### IPv6

- Address: ::1
