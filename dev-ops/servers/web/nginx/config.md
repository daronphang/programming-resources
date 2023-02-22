## Checking if File Exists

```conf
server {
    root /var/www/example.com;
    location / {
        # checks if $uri exists, else check if directory exists, else serves index/html as fallback 
        try_files $uri $uri/ /index.html;
        try_files $uri $uri/ $uri.html =404;
    }
}
```

## Root vs Alias

```
root    location part is appended to root part i.e. path = root + location
alias   location part is replaced by alias part i.e. path = alias
```

```
# final path is /var/www/app/static/static
location /static {
  root /var/www/app/static/;
  autoindex off;
}

# final path is /var/www/app/static
location /static {
  alias /var/www/app/static/;
  autoindex off;
}
``` 
