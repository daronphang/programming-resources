## IP addresses

```sh
$ ifconfig -a       # private IP address
$ curl ifconfig.me  # public IP address
$ ip address show

$ sudo apt install speedtest-cli
$ speedtest
```

## ping

```sh
$ ping [option] [hostname/IP address]
$ ping google.com
```

## curl

Both nslookup and ping can be used the query DNS, but curl checks local `/etc/hosts` first then queries DNS.

## nslookup

nslookup is used to find a domain name's IP address or DNS record by querying information from the DNS server.

Response is returned by a nameserver from ISP or domain. There are two types of answers:

- **Authoritative**: Comes from a nameserver that is authoritative for the domain it is returning the record for. To get an authoritative answer, need to explicitly specify the authoritative eDNS server when performing nslookup
- **Non-authoritative**: A non-official nameserver that relays information

```sh
$ nslookup google.com
$ nslookup 127.253.118.113 # reverse DNS lookup
```

## dig (domain information groper)

Used to gather DNS information and troubleshoot DNS problems. By default, dig uses the local configuration (`/etc/resolv.conf`) to decide which nameserver to query.

```sh
# dig [server] [name] [type]
$ dig google.com ANY
$ dig @8.8.8.8 google.com   # google DNS server
```

### Answer section

```
# Server        TTL

google.com.		300	    IN	A	    74.125.200.102
google.com.		300	    IN	AAAA	2404:6800:4003:c00::8b
google.com.		300	    IN	AAAA	2404:6800:4003:c00::64
google.com.		86400	IN	NS	    ns3.google.com.
google.com.		300	    IN	A	    74.125.200.113
```

## Kill ports

```sh
$ sudo netstat -tulpn
$ sudo kill <PID>
```

## hostname

Used to obtain the DNS and set the system's hostname. Main purpose is to uniquely identify a computer over a network.

Used to view and change a system's domain and hostname. Can be confiured to be descriptive or structured i.e. [purpose]-[number]-[environment].

```
-a      Display alias
-A      Display every FQDN (Fully Qualified Domain Name) of the computer
-b      Always set a hostname
-d      Display DNS
-f      Display the FQDN
-F      Check a file to recover and display the hostname
-i      Display IP address
-I      Display all of the computer's network addresses
-s      Display short version of the hostname
-v      Verbose
-y      Display NIS domain name
```
