## Generating TLS/SSL Certificate

## Certbot

Use Certbot to enable HTTPS with Nginx on Ubuntu. Certbot generates SSL/TLS certificates for free with validity of 90 days. Responsible for communicating with Let's Encrypt to request the certificate, performing required ACME challenges, installing the certificate, and configuring the web server.

https://www.linode.com/docs/guides/enabling-https-using-certbot-with-nginx-on-ubuntu/

### Installation

Remove any prior installation from apt and install from snap.

```bash
$ sudo apt update
$ sudo apt install snapd

$ sudo snap install core
$ sudo snap refresh core

$ sudo apt remove certbot
$ sudo snap install --classic certbot
$ sudo ln -s /snap/bin/certbot /usr/bin/certbot   # configure a symbolic link
```

### Requesting

Should request separate certificates with and without www prefix if Certbot is unable to display the names of eligible domains.

```bash
$ sudo certbot --nginx
```

### Renewing

Certbot is configured to renew any certificates automatically by scheduling a task in the background.

```bash
$ sudo certbot renew --dry-run  # testing if auto works
$ sudo certbot renew    # manual
```
