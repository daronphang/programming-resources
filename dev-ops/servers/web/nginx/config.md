## File Structure

https://www.digitalocean.com/community/tutorials/understanding-the-nginx-configuration-file-structure-and-configuration-contexts

```conf
# main context
http {
    # http context

    server {
        # first server context

        location /match/criteria {
          # first location context
        }

        location /other/criteria {
            # second location context
            location nested_match {
                # first nested location
            }
        }

    server {
        # second server context
    }
}
```

### Keywords Docs

http://nginx.org/en/docs/http/ngx_http_core_module.html

### Directives

Nginx consist of modules which are controlled by directives specified in the configuration file. Directives are divided into simple and block directives:

- Simple: Consists of the name and parameters separated by spaces and ends with a semicolon
- Block: Same structure as simple, but ends with additional instructions surrounded by braces

### Context

A block directive that can have nested directives i.e events, http, server, location. As contexts can be layered within on another, Nginx allows configurations to be inherited. the child contexts can override values defined in the broader context.

```
events      main context
http        main context
server      http context
location    server context
```

### Splitting Servers

Multiple servers are usually decomposed into smaller config files by server_name and port.

### Location

```
# prefixes

=       Exact match, speeds up processing of requests, nesting not allowed
~       Regex, case-sensitive matching
~*      Regex, case-insensitive matching
^~      Regular expressions are not checked
```

Location can either be defined by a prefix string, or by a regular expression. To find location matching a given request, order of Nginx checking is as follows:

1. Locations defined using prefix strings (longest matching prefix is selected and remembered)
2. Regular expressions in the order of their appearance in the configuration file
3. If regex is not found, the configuration of the prefix location remembered earlier is used

```conf
location = / {
    [ configuration A ]
}

location / {
    [ configuration B ]
}

location /documents/ {
    [ configuration C ]
}

location ^~ /images/ {
    [ configuration D ]
}

location ~* \.(gif|jpg|jpeg)$ {
    [ configuration E ]
}
```

```
/                           Matches config A
/index.html                 Matches config B
/documents/document.html    Matches config C
/images/1.gif               Matches config D
/documents/1.jpg            Matches config E
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
                try_files $uri $uri/ $uri.html =404;
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
