## Domain Name Server (DNS)

https://www.linode.com/docs/guides/dns-records-an-introduction/

### DNS records

- A: Maps your domain/subdomain to one or more IP addresses e.g. example.com
- AAAA: For mapping IPv6
- CNAME: Maps a name to another name; should only be used when there are no other records on that name
- ALIAS: Maps a name to another name, but can coexist with other records on that name e.g. www.example.com

```
example.com     A       12.34.56.78
*.example.com   A       12.34.56.78
```

### FQDN (Fully Qualified Domain Name)

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

## Registering DNS

### DNS Manager

DNS manager provides an interface that allows you to add DNS records for all of your domain names. DNS setup are as follows:

1. Register/purchase a domain name from a domain registrar
2. Register nameservers on domain registrar's website
3. Use DNS Manager to add domain and basic DNS records
4. Set reverse DNS

https://www.linode.com/docs/guides/dns-manager/

### Domain Registrars

Need to purchase domain name from Domain Registrars. After purchasing, need to register the personal name servers for your domain name. Should specify at least two name servers so that the other can continue to serve your DNS information if one of them is down.

https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/

```
NameCheap
Google Domains
Domain.com
goDaddy
```

```
ns1.linode.com
ns2.linode.com
ns3.linode.com
```

### Name Servers

Specifying name servers is an essential part of domain ownership. Else, clients won't know where to find your DNS information and your domain won't resolve. Name servers host a domain's DNS information in 'zone' text file or SOA (Start of Authority) records.

Can host your DNS information on name servers as follows:

- Linode
- Your domain registrar
- Your own DNS server
- Third-party DNS hosting

### Reverse DNS

Reverse DNS lookup resolves an IP address to a designated domain name. Should always set reverse DNS.

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
