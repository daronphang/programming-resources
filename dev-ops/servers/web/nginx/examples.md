## Multiple Locations

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

## Multiple .conf Files

```conf
server {
    server_name daronphang.com www.daronphang.com;

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/daronphang.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/daronphang.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    root /var/www/daronphang.com;
    index index.html index.htm;

}

server {
    if ($host = www.daronphang.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = daronphang.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


  server_name daronphang.com www.daronphang.com;
    listen 80;
    return 404; # managed by Certbot
}
```

```conf
server {
    server_name api.daronphang.com;

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/daronphang.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/daronphang.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

    location / {
        proxy_pass http://localhost:8082;
    }
 }
server {
    if ($host = api.daronphang.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    server_name api.daronphang.com;
    listen 80;
    return 404; # managed by Certbot
}
```

## Reverse Proxy and Load Balancing

Nginx server directive defaults to port 80 if not specified. Do not include http inside upstream server directive.

```conf
upstream mpie {
    server fslram01:443;
}

upstream instacap {
    server fslma01;
}

upstream provisional {
    server localhost:5000;
}

upstream lead-lot-tracking {
    server localhost:5050;
}

server {
    listen 443 ssl;
    server_name tslma03;
    ssl_certificate "/etc/pki/tls/certs/certificate.crt";
    ssl_certificate_key "/etc/pki/tls/tslma03_micron_com.key";
    # add_header "Access-Control-Allow-Origin" "$http_origin" always;
    add_header 'Access-Control-Allow-Credentials' 'true' always;
    add_header "Access-Control-Allow-Methods" "*";
    add_header "Access-Control-Allow-Headers" "*";

     location /api/provisional {
        proxy_pass http://provisional;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /api/lead-lot-tracking {
        proxy_pass http://lead-lot-tracking;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /api/instacap {
        proxy_pass https://instacap;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /api/mpie {
        proxy_pass https://mpie;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
