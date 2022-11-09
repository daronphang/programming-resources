## Supervisor

A client/server system that allows its users to monitor and control a number of processes on linux. Processes can be stopped and restarted as a unit. Starts its sub-processes via fork/exec.

### Benefits

In many VPS environments, it is often the case that you will have a number of small programs that you want to run persistently i.e. shell scripts, node.js apps, or any large-sized packages.

Usually, external packages are supplied with a unit file that allows them to be managed by an init system such as systemd, or packaged as docker images. However, for software that isn't well-packaged, or for users who prefer not to interact with low-level init system on the server, it is helpful to have a lightweight alternative.

Supervisor is a process manager which provides a singular interface for managing and monitoring a number of long-running programs. Supervisord's primary purpose is to create and manage processes based on data in its configuration file. It does this by creating subprocesses. Each subprocess spawned by supervisor is managed for the entirety of its lifetime by supervisord (parent process). When a child dies, supervisor is notified of its death via SIGCHILD signal, and it performs the appropriate operation.

## Configuration

```console
$ # for all conf is /etc/supervisor/conf.d/

$ sudo nano /etc/supervisor/conf.d/idle.conf
$ sudo tail /var/log/idle.out.log
```

```conf
[supervisord]
logfile = /tmp/supervisord.log
logfile_maxbytes = 50MB
logfile_backups=10
loglevel = info
pidfile = /tmp/supervisord.pid
nodaemon = false
minfds = 1024
minprocs = 200
umask = 022
user = chrism
identifier = supervisor
directory = /tmp
nocleanup = true
childlogdir = /tmp
strip_ansi = false
environment = KEY1="value1",KEY2="value2"
```

## Adding Subprocess

Create config file in /etc/supervisor/conf.d/myapp.conf.

No shell is executed by supervisord when it runs a subprocess, so environment variables such as USER, PATH, HOME, SHELL, LOGNAME, etc. are not changed from their defaults or otherwise reassigned. If need to set environment variables for a particular program that might be otherwise set by a shell invocation for a particular user, need to do it explicitly within the environment= program config.

For command, should put full path as Supervisor may not be able to find relative path.

https://medium.com/@monirz/deploy-golang-app-in-5-minutes-ff354954fa8e

```
autostart         Tells supervisor that this program should be started when system boots
autorestart       Always restart after exists if TRUE
stderr_logfile    Location of log files; specified directories MUST exist
command           Path should be binary or executable
directory         Path of directory
```

```conf
[program:apache2]
command=/home/chrism/bin/httpd -c "ErrorLog /dev/stdout" -DFOREGROUND
user=chrism
environment=HOME="/home/chrism",USER="chrism"

[program:portfolio-backend-api]
user=daronphang
directory=/home/daronphang/portfolio-backend-api/src
command=/usr/local/go/bin/go run main.go
autostart=true
autorestart=true
stderr_logfile=/home/daronphang/log/portfolio-backend-api/supervisor.err.log
stdout_logfile=/home/daronphang/log/portfolio-backend-api/supervisor.out.log
environment=GOPATH=/usr/local/go/bin,HOME=/home/daronphang,USER=daronphang
```

### Example

```conf
[program:MDE]
directory=/home/myassistant/myassistant-data-extrator/src/MDE
command=go run main.go
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/home/myassistant/log/MDE/mde.err.log
stdout_logfile=/home/myassistant/log/MDE/mde.out.log

[program:MLLA]
directory=/home/myassistant/myassistant-low-level-api/src
command=/home/myassistant/myassistant-low-level-api/mlla/bin/gunicorn -w 8 -b 127.0.0.1:8081 myassistant.ma:app
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
stderr_logfile=/home/myassistant/log/MLLA/MLLA.err.log
stdout_logfile=/home/myassistant/log/MLLA/MLLA.out.log

[program:nginx]
command=/usr/sbin/nginx -g "daemon off;"
autostart=true
autorestart=true
startretries=5
numprocs=1
startsecs=0
process_name=%(program_name)s_%(process_num)02d
stderr_logfile=/var/log/supervisor/%(program_name)s_stderr.log
stderr_logfile_maxbytes=10MB
stdout_logfile=/var/log/supervisor/%(program_name)s_stdout.log
stdout_logfile_maxbytes=10MB

[supervisord]
logfile = /home/myassistant/log/supervisord.log ; main log file; default $CWD/supervisord.log
pidfile = /home/myassistant/log/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false               ; start in foreground if true; default false

[inet_http_server]
port = 127.0.0.1:9001

[supervisorctl]
serverurl = http://127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
```

### Services

After updating configuration, need to restart.

```console
$ sudo supervisorctl reread     # should show output
$ sudo supervisorctl update
$ sudo supervisorctl    # enter interactive shell, view running processes
supervisor> stop <process_name>
supervisor> start <process_name>
```

### Environment Variables

```conf
[program:example]
command=/usr/bin/example --loglevel=%(ENV_LOGLEVEL)s
```

### Web Interface

To restart after editing. Can be configured together with Nginx (needs to be disabled first).

```console
$ sudo systemctl stop nginx
$ sudo systemctl disable nginx
$ supervisorctl reread
$ sudo supervisorctl update
```

```conf
[inet_http_server]
port=*:6000
username=admin #username to access the web interface
password=admin # password to access the web interface

[program:nginx]
command=/usr/sbin/nginx -g "daemon off;"
autostart=true
autorestart=true
startretries=5
numprocs=1
startsecs=0
process_name=%(program_name)s_%(process_num)02d
stderr_logfile=/var/log/supervisor/%(program_name)s_stderr.log
stderr_logfile_maxbytes=10MB
stdout_logfile=/var/log/supervisor/%(program_name)s_stdout.log
stdout_logfile_maxbytes=10MB
```
