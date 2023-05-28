## Nginx

An open-source web server that can also be used as a reverse proxy, HTTP cache, and load balancer. Built to offer low memory usage and high concurrency. Rather than creating a new process for each web request, Nginx uses an asynchronous, event-driven approach where requests are handled in a single thread.

With Nginx, one master process can control multiple worker processes. The master maintains the worker processes, while the workers do the actual processing.

## Installation

Once loaded, can test by navigating to http://127.0.0.1 or http://localhost.

https://www.linode.com/docs/guides/how-to-install-and-use-nginx-on-ubuntu-20-04/#use-nginx

```console
$ sudo apt update
$ sudo apt install nginx
$ systemctl nginx status

$ sudo unlink /etc/nginx/sites-enabled/default  # disable default config file
```

## Adjusting Firewall

Nginx registers itself as a serice with ufw upon installation, making it straightforward to allow Nginx access.

```console
$ sudo ufw app list
$ sudo ufw allow 'Nginx HTTP'
$ sudo ufw status
```

```
Nginx Full      Opens both port 80 and port 443
Nginx HTTP      Opens port 80 (normal, unencrypted web traffic)
Nginx HTTPS     Opens port 443 (TLS/SSL encrypted traffic)
```

## Services

```console
$ sudo systemctl status nginx

$ sudo nginx -t     # test for syntax errors in nginx files

$ sudo systemctl stop nginx
$ sudo systemctl enable nginx
$ sudo systemctl disable nginx
$ sudo systemctl reload nginx       # reload config files
$ sudo systemctl restart nginx      # hard restart

$ curl -4 icanhazip.com         # to find server's IP address
```
