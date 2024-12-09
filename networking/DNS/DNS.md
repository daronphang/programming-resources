## Domain Name Server (DNS)

DNS is a crucial component of the internet that translates human-readable domain names (www.example.com) into machine-readable IP addresses (192.0.2.1). This process allows users to access websites and services using familiar names instead of having to remember numerical addresses.

## Resource records

```
example.com         A       12.34.56.78
*.example.com       A       12.34.56.78
blog.example.com    CNAME   example.com
```

- **A**: Maps your domain/subdomain to one or more IP addresses e.g. example.com
- **AAAA**: For mapping IPv6
- **CNAME**: Points from an alias domain to a canonical domain. All CNAME records must point to a domain and never to an IP address
- **ALIAS**: Maps a name to another name, but can coexist with other records on that name e.g. www.example.com
- **NS (Nameserver)**: Used to indicate which DNS servers in the area are responsible for resolution
- **SOA (Start of Authority)**: Indicate which DNS server is the authoritative domain nameserver for the zone. Each zone is allowed to have only one SOA record
- **MX (Mail Exchanger)**: Used to indicate DNS servers for mail records
- **SRV (Server)**: SRV records are defined in RFC2052; used to indicate what kind of services a server can provide, and they play an important role in AD

### CNAME

When you have multiple subdomains pointing to a root domain, if the IP address of the host changes, only the DNS A record for the root domain needs to be updated.

A frequent misconception is that a CNAME record must always resolve to the same website as the domain it points to, but this is not the case. The web server that the user connects to from the root domain resolution will still handle the URL accordingly i.e. example.com will deliver the blog page for blog.example.com rather than the home page.

CNAME records can point to other CNAME records, but this would be inefficient.

## FQDN (Fully Qualified Domain Name)

FQDNs are complete addresses of websites, computers and other entities that can be accessed on the internet. Consists of three levels, separated by a dot:

1. Hostname
2. Second-level domain name
3. Top-level domain name (TLD)

```
app.datadoghq.com

subdomain: app
parent domain: datadoghq
domain extension: com
```

```sh
$ hostname --fqdn
$ hostnamectl
```

## Dynamic DNS

An essential extension of DNS is the Dynamic DNS (DDNS). This service allows users to automatically update the mapping between domain names and IP addresses whenever the IP address changes. The primary use-case for Dynamic DNS is to support hosts that have dynamic IP addresses, like those assigned by many residential ISPs. DDNS is invaluable for individuals and small businesses wanting to host services, websites, or devices on networks with dynamic IP addresses. It ensures consistent remote access by providing a stable domain name that always points to the current IP address, even if that address changes frequently.

## DNS Security Extensions (DNSSEC)

All top-level domains support DNSSEC. DNSSEC is a straight-forward system by which resource records are signed by the organization owning a zone.

## Updating hosts file

Hosts file creates static associations between IP addresses and hostnames/domains. The system gives those associations higher priority than hostnames/domains that must be resolved by DNS i.e. enables you to override the DNS for a domain on a specific machine.

Modifying hosts file causes your local machine to look directly at the IP address specified. This is useful if you want to test your site without the test link prior to going live with SSL. **This should be done on your local instance and not the server** i.e. connecting from local computer to server prior to registering domain for your server.

Map both domain and alias to the IP address. The domain you assign as your system's FQDN should have "A" record in DNS pointing to your instance's IP address.

https://www.linode.com/docs/guides/using-your-systems-hosts-file/

```sh
$ vi /etc/hosts
$ vi /etc/hostname

$ sudo hostnamectl set-hostname mail.linuxize.com
```

```
# example-hostname is the local hostname
# hostname.example.com is the FQDN
127.0.0.1 localhost.localdomain localhost
203.0.113.10 example-hostname.example.com example-hostname

# for IPv6
2600:3c01::a123:b456:c789:d012 example-hostname.example.com example-hostname
```
