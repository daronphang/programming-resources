## Setup

### .bashrc

Setup for environment variables whenever user opens an interactive login shell.

```sh
$ sudo vim ~/.bashrc
```

### Proxies

Proxy configuration is setup but disabled by default.

```sh
$ vim /etc/profile.d/proxy.sh   # uncomment proxy_on fn
```

### Installing Repositories

When performing yum install for repositories, need to specify proxy individually.

```conf
[main]
gpgcheck=1
installonly_limit=3
clean_requirements_on_remove=True
best=True
skip_if_unavailable=False
proxy=http://proxy-web.micron.com:80/   # enable this!
```

```sh
$ /etc/yum.conf     # modifying proxy globally
$ /etc/yum.repos.d/some.repo
```

To bypass local redhat repositories and enable curl to use proxy, need to temporarily disable checking for repos. Make sure proxy is enabled in /etc/yum.conf.

```sh
$ sudo yum repolist
$ sudo yum install <package> --disablerepo=ansible-2.9-for-rhel-8-x86_64-rpms --disablerepo=rhel-8-for-x86_64-appstream-rpms --disablerepo=rhel-8-for-x86_64-baseos-rpms --disablerepo=satellite-client-6-for-rhel-8-x86_64-rpms
```

### Dependencies

Install git net-tools. For supervisor and freetds, requires epel-release.

```
$ sudo yum install net-tools git unixODBC nginx
$ touch /etc/odbcinst.ini
```

```ini
[FreeTDS]
Description = FreeTDS Driver
Driver = /usr/lib64/libtdsodbc.so.0
```

### Git

Disable proxies in git config.

```sh
$ git config --global http.proxy ""
$ git config --global https.proxy ""
$ git config --global http.sslVerify false
```

### Python

Python3.6 is only available through yum repository. To install later versions, need to download manually.

```sh
$ sudo dnf install gcc openssl-devel bzip2-devel libffi-devel
$ cd download/path
$ wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
$ tar xzf Python-3.7.9.tgz
$ cd Python-3.7.9
$ sudo ./configure --enable-optimizations
$ sudo make install  # altinstall to prevent replacing default python binary file in /usr/bin/python

$ python3 --version
$ pip3 --version
$ python3 -m venv venv
$ source venv/bin/activate
```

### Supervisor

When installing through pip, both supervisord and supervisorctl will be stored in /usr/local/bin. Need to add this to global path.

https://www.nixknight.com/2020/03/setup-supervisor-with-python-pip-on-ubuntu-debian/

```
supervisord             /usr/local/bin/supervisord
supervisorctl           /usr/local/bin/supervisorctl
supervisord.conf        /etc/supervisord
supervisord.service     /lib/systemd/system
```

```sh
$ sudo pip3 install --trusted-host pypi.org --trusted-host files.pythonhosted.org --proxy http://proxy-web.micron.com:80 supervisor
$ which supervisord
$ sudo systemctl enable supervisord
$ sudo touch /etc/profile.d/supervisor.sh
$ sudo vim /etc/profile.d/supervisor.sh

$ sudo start supervisord
$ supervisorctl
```

```sh
echo path=$PATH:/usr/local/bin
```

#### Logs

All logs are located in /var/log/supervisord.

#### supervisord.service

```
[Unit]
Description=Supervisor process control system for UNIX
Documentation=http://supervisord.org
After=network.target

[Service]
ExecStart=/usr/local/bin/supervisord -n -c /etc/supervisord/supervisord.conf
ExecStop=/usr/local/bin/supervisorctl $OPTIONS shutdown
ExecReload=/usr/local/bin/supervisorctl -c /etc/supervisord/supervisord.conf $OPTIONS reload
KillMode=process
Restart=on-failure
RestartSec=20s

[Install]
WantedBy=multi-user.target
```

#### conf

Logs to be stored in /var/log/supervisord.

```conf
[supervisord]
logfile=/var/log/supervisord/supervisord.log ; (main log file;default $CWD/supervisord.log)
pidfile=/var/run/supervisord/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
childlogdir=/var/log/supervisord            ; ('AUTO' child log dir, default $TEMP)

[inet_http_server]
port = 127.0.0.1:9001

[supervisorctl]
serverurl = http://127.0.0.1:9001

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[include]
files = /etc/supervisord/conf-enabled/*.conf
```

```conf
[program:df_api_gateway]
user=daronphang
directory=/home/daronphang/df_microservices/df_api_gateway
command=/home/daronphang/df_microservices/df_api_gateway/venv/bin/python3 -m uvicorn src.main:app
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_api_gateway.err.log
stdout_logfile=/var/log/supervisord/df_api_gateway.out.log

[program:df_email_service]
user=daronphang
directory=/home/daronphang/df_microservices/df_email_service
command=/home/daronphang/df_microservices/df_email_service/venv/bin/python3 -m src.main
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_email_service.err.log
stdout_logfile=/var/log/supervisord/df_email_service.out.log

[program:df_adhoc_service]
user=daronphang
directory=/home/daronphang/df_microservices/df_adhoc_service
command=/home/daronphang/df_microservices/df_adhoc_service/venv/bin/python3 -m src.main
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_adhoc_service.err.log
stdout_logfile=/var/log/supervisord/df_adhoc_service.out.log

[program:df_adhoc_celery_service]
user=daronphang
directory=/home/daronphang/df_microservices/df_adhoc_service
command=/home/daronphang/df_microservices/df_adhoc_service/venv/bin/python3 -m celery -A src.tasks.worker.app worker --loglevel=info -P solo -Q adhoc
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_adhoc_celery_service.err.log
stdout_logfile=/var/log/supervisord/df_adhoc_celery_service.out.log

[program:df_espec_service]
user=daronphang
directory=/home/daronphang/df_microservices/df_espec_service
command=/home/daronphang/df_microservices/df_espec_service/venv/bin/python3 -m src.main
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_espec_service.err.log
stdout_logfile=/var/log/supervisord/df_espec_service.out.log

[program:df_espec_celery_service]
user=daronphang
directory=/home/daronphang/df_microservices/df_espec_service
command=/home/daronphang/df_microservices/df_espec_service/venv/bin/python3 -m celery -A src.tasks.worker.app worker --loglevel=info -P solo -Q espec
autostart=true
autorestart=true
environment=HOME=/home/daronphang,USER=daronphang
stderr_logfile=/var/log/supervisord/df_espec_celery_service.err.log
```

### Docker

Take note Docker is not supported for RedHat, but CentOS has support. Make sure proxies are configured.

1. Follow instructions from Docker website for CentOS (removing old Docker and installing RPM repository).

https://docs.docker.com/engine/install/centos/

2. Modify repo files to include proxy.

```sh
$ vim /etc/yum.repos.d/docker-ce.repo
```

```
 [docker-ce-stable]
name=Docker CE Stable - $basearch
baseurl=https://download.docker.com/linux/centos/$releasever/$basearch/stable
enabled=1
gpgcheck=1
gpgkey=https://download.docker.com/linux/centos/gpg
proxy=http://proxy-web.micron.com:80
```

3. Install Docker Engine. If encounter dependencies error, check the error message and resolve.

```sh
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Might need to remove dependencies buildah and podman.

```sh
$ sudo yum remove buildah podman
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

If require dependencies i.e. container-selinux, need to update epel-release and install.

```sh
$ sudo yum install epel-release
$ sudo yum install container-selinux
```

4. Configure Docker group.

```sh
$ sudo groupadd docker
$ sudo usermod -aG docker $USER jenkins
$ grep /etc/group -e "docker"
```

5. Configure Docker proxy.

```sh
$ sudo mkdir -p /etc/systemd/system/docker.service.d
$ sudo touch /etc/systemd/system/docker.service.d/http-proxy.conf
$ sudo vim /etc/systemd/system/docker.service.d/http-proxy.conf
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

```conf
[Service]
Environment="HTTP_PROXY=http://proxy-web.micron.com:80/"
Environment="HTTPS_PROXY=http://proxy-web.micron.com:80/"
Environment="NO_PROXY=localhost,127.0.0.1,.micron.com,addmmsi,*.micron.com,.snowflakecomputing.com,*.snowflakecomputing.com,tableau-apac,analytics-apac,tableau-boise,analytics,analytics-boise"
```

6. Start Docker.

```sh
$ sudo systemctl start docker
$ sudo docker run hello-world
```

### Ports

```sh
$ sudo firewall-cmd --list-ports
$ sudo firewall-cmd --zone=public --add-port=80/tcp --permanent
$ sudo firewall-cmd --zone=public --add-port=443/tcp --permanent
$ sudo firewall-cmd --reload
```

### SSL Certificate

https://confluence.micron.com/confluence/display/~LINLINK/How+to+Apply+SSL+Certificate

1. Generate private key.

```sh
$ cd ~
$ hostname
$ openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout privateKey.key
```

```
Country Name (2 letter code) [XX]:SG
State or Province Name (full name) []:SINGAPORE
Locality Name (eg, city) [Default City]:SINGAPORE
Organization Name (eg, company) [Default Company Ltd]:Micron Technology, Inc.
Organizational Unit Name (eg, section) []:PEE
Common Name (eg, your name or your server's hostname) []:tsldf01.wlsg.micron.com
Email Address []:daronphang@micron.com

HelloWorld123!      Challenge password
```

2. Download certificate from https://pkienroll.micron.com/certsrv/

- Request a certificate
- For SSL, date is 2 years but you can get it right away
- Navigate to 'Submit a certificate using base64 encoded'
- Copy the cert from CSR.csr (without BEGIN/END CERTIFICATE REQUEST lines)
- Certificate template should be 'Micron SSL Certificate'
- Additional attributes need to be populated with 'SAN:dns=tsldf01.wlsg.micron.com&dns=tsldf01'
- Download base64 crt and copy to /etc/pki/tls/certs/ssl_cert.cer

## Conf Files

```
/etc/redis.conf
/etc/nginx.conf
```

## HTML Files

```
/usr/share/nginx/html
```

## SELinux

Servers are running with SELinux. Need to perform additional configurations to bypass.

### Nginx

Throws "permission denied while connecting to upstream" error.

```
$ sudo setsebool -P httpd_can_network_connect 1
```

Throws forbidden when accessing contents outside /usr/share/nginx/html.

Change user in /etc/nginx/nginx.conf to your username.

```sh
$ sudo setenforce 0
```

### Docker Containers

Throws "permission denied" error when mounting host FS to container. Need to use z flag.

```
$ docker run -v -d ${pwd}:/var/data:Z some_image
```
