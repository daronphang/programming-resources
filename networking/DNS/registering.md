## Registering DNS

### DNS Manager

DNS manager provides an interface that allows you to add DNS records for all of your domain names. DNS setup are as follows:

1. Register/purchase a domain name from a domain registrar
2. Register nameservers on domain registrar's website
3. Use DNS Manager to add domain and basic DNS records
4. Set reverse DNS

https://www.linode.com/docs/guides/dns-manager/

### Domain Registrars

Need to purchase domain name from Domain Registrars e.g. NameCheap, GoDaddy, etc. After purchasing, need to register the personal nameservers for your domain name. Should specify at least two nameservers so that the other can continue to serve your DNS information if one of them is down.

https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/

```
ns1.linode.com
ns2.linode.com
ns3.linode.com
```

### Nameservers

Specifying nameservers is an essential part of domain ownership. Else, clients won't know where to find your DNS information and your domain won't resolve. Nameservers host a domain's DNS information in 'zone' text file or SOA (Start of Authority) records.

Can host your DNS information on nameservers as follows:

- Cloud nameservers
- Your domain registrar
- Your own DNS server
- Third-party DNS hosting

### Reverse DNS

Reverse DNS lookup resolves an IP address to a designated domain name. Should always set reverse DNS.
