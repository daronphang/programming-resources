## Nginx File Locations

```
/var/www/html                   Static HTML content
/etc/nginx                      Location of main Nginx application files
/etc/nginx/nginx.conf           Main Nginx conf file
/etc/nginx/sites-available      List of all websites configured through Nginx
/etc/nginx/sites-enabled        List of sites actively served by Nginx
/var/log/nginx/access.log
/var/log/nginx/error.log
```

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

## Setting Up Server Blocks

When using Nginx server, server blocks (similar to virtual hosts in Apache) can be used to encapsulate configuration details and host more than one domain from a single server.

Nginx on Ubuntu has one server block enabled by default that is configured to server documents out of a directory at /var/www/html, which works for single site. For hosting multiple sites, can create a directory structure within /var/www for your_domain_name website.

### Creating index.html

```console
$ sudo mkdir -p /var/www/your_domain/html
$ sudo chown -R $USER:$USER /var/www/your_domain/html   # $USER is an env variable
$ sudo chmod -R 755 /var/www/your_domain

$ sudo vi /var/www/your_domain/html/index.html
```

```html
<html>
  <head>
    <title>Welcome to test_new_domain!</title>
  </head>
  <body>
    <h1>Success! The test_new_domain server block is working!</h1>
  </body>
</html>
```

### Setting Up Directives

```console
$ sudo vi /etc/nginx/sites-available/your_domain
```

```conf
server {
        listen 80;
        listen [::]:80;

        root /var/www/your_domain/html;
        index index.html index.htm index.nginx-debian.html;

        server_name your_domain.com www.your_domain.com;

        location / {
                try_files $uri $uri/ =404;
        }
}
```

### Example

```conf
server {
    listen 443 ssl;
    server_name tslma03;
    ssl_certificate "/etc/pki/tls/certs/certificate.crt";
    ssl_certificate_key "/etc/pki/tls/tslma03_micron_com.key";
    # add_header "Access-Control-Allow-Origin" "$http_origin" always;
    add_header 'Access-Control-Allow-Credentials' 'true' always;
    add_header "Access-Control-Allow-Methods" "*";
    add_header "Access-Control-Allow-Headers" "*";



    location /MLLA {
        if ($request_method = OPTIONS ) {
            add_header "Access-Control-Allow-Origin" "$http_origin";
            add_header 'Access-Control-Allow-Credentials' 'true';
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
            add_header "Access-Control-Allow-Headers" "*";
            return 200;
        }
        proxy_pass http://127.0.0.1:8081;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /MDE {
        proxy_pass http://127.0.0.1:8082;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        if ($request_method = GET ) {
            add_header "Access-Control-Allow-Origin" "$http_origin";
            add_header 'Access-Control-Allow-Credentials' 'true';
            add_header 'Access-Control-Allow-Methods' 'GET, POST, OPTIONS';
            add_header "Access-Control-Allow-Headers" "*";
        }
        alias /data/;
    }

    error_page 502 /502.json;
    location /502.json {
        internal;
        add_header 'Content-Type' 'application/json charset=UTF-8';
        return 502 '{"error": "request timeout error"}';
    }
}

```

## Creating Symlinks

After updating config file to new directory, need to enable the file by creating a link from it to the sites-enabled directory, which Nginx reads from during startup.

Nginx uses a common practice called **symlinks** (symbolic links) to track which of your server blocks are enabled. Creating a symlink is like creating a shortcut on disk, so that you could later delete the shortcut from the sites-enabled directory while keeping the server block in sites-available if you wanted to enable it.

After server block is enabled, Nginx is configured to respond to requests based on their 'listen' and 'server_name' directives in the config file.

```
your_domain     Responds to requests for your_domain and www.your_domain
default         Responds to any requests on port 80 that do not match any blocks
```

```console
$ sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
```

## Updating Bucket Size

To avoid possible hash bucket memory problem that can arise from adding additional server names, can configure bucket size.

```console
$ sudo vi /etc/nginx/nginx.conf
```

```conf
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
```

## Modifying Host File

If your new domain name isn't registered or public, the /etc/hosts file may need to be configured. After configuration, navigate to 'http://test_new_domain.com'.

```console
$ hostname -i           # should be 127.0.1.1
$ sudo vi /etc/hosts
```

```
# add this line at end
127.0.1.1 test_new_domain www.test_new_domain.com
```

## HTTPS

Use Certbot to enable HTTPS with Nginx on Ubuntu.

https://www.linode.com/docs/guides/enabling-https-using-certbot-with-nginx-on-ubuntu
