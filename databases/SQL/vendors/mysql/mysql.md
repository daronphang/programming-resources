## Installation (Linux)

```console
$ sudo dpkg -i mysql-apt-config_w.x.y-z_all.deb
$ sudo apt update
$ sudo apt install mysql-server
$ mysql_secure_installation
```

### Changing Ownership

```console
$ # folders are under mysql as user
$ sudo chown -R daronphang /var/log/mysql
$ sudo chown -R daronphang /var/lib/mysql
```

### Adding New User

For debian, the 'auth_socket_plugin' is called 'unix_socket'.

```console
mysql> SELECT User, Host, plugin FROM mysql.user;

mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED WITH mysql_native_password BY 'YOUR_PASSWD';

mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION; # alternative

mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYTEM_USER';
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='YOUR_SYTEM_USER'; # alternative

mysql> FLUSH PRIVILEGES;
mysql> exit;

$ sudo service mysql restart
$ mysql -u YOUR_SYSTEM_USER     # no sudo required
```

```console
mysql> ALTER USER 'userName'@'localhost' IDENTIFIED BY 'New-Password-Here'; # change password
```

## Services

### Starting

```console
$ sudo service mysql start --skip-grant-tables  # for connecting without privileges
$ sudo systemctl start mysqld

$ sudo mysqld_safe --skip-grant-tables &
```

### Stopping

```console
$ sudo systemctl stop mysql
$ sudo systemctl restart mysql
```

### Status

```console
$ systemctl status mysql
```

### Resetting Root

```console
$ systemctl stop mysql
$ ps aux | grep mysql # kill all pids
$ sudo mysqld_safe --skip-grant-tables &
mysql> FLUSH PRIVILEGES;
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass';
```

## Connecting to Server

Some systems like ubuntu uses auth_socket_plugin by default and is authenticated by the system's user credentials.

```console
$ mysql -h 127.0.0.1 -P 3306 -u daronphang  # using TCP/IP
$ mysql -h localhost -u daronphang  # using socket pipe
$ mysql -u daronphang_remote -h 139.234.111.5 -P 3306 -p
```

### Auth Sockets

Authenticates clients from the local host through the Unix socket file. The auth_socket plugin checks whether the socket user name matches the MySQL username specified by the client program to the server. If mismatch, server will refuse the connection.

**If using supervisor to start, need to ensure user is specified in conf**.

```console
valerie@localhost> mysql -u stefanie   # user option value differs from client, rejects
stefanie@localhost> mysql -u stefanie    # accespts
```

### Remote Connections

1. Configure MySQL server. MySQL server listens for connections only from localhost by default. Need to edit bind-address in conf.
2. Configure server's firewall and open port 3306 via ufw.
3. Grant access to user in MySQL server with remote IP address as host with all privileges.

Ensure that the user's plugin is mysql_native_password for TCP/IP.

https://linuxize.com/post/mysql-remote-access/

```console
$ sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
$ sudo systemctl restart mysql
```

```conf
bind-address           = 0.0.0.0
```

```console
$ need to do it through root access
mysql>CREATE USER 'daronphang_remote'@'119.75.213.455' IDENTIFIED BY 'YOUR_PASSWORD';
mysql>GRANT ALL PRIVILEGES ON *.* TO 'daronphang_remote'@'119.75.213.455';
mysql>UPDATE mysql.user SET plugin='mysql_native_password' WHERE User='daronphang_remote';
mysql> FLUSH PRIVILEGES;
```

### TCP/IP via SSH

When using this option, the connection to MySQL from SSH is via localhost. Hence, do not need to add users to database for remote connections.

If using SSH keys, need to set **OPEN_SSH**.

```
SSH Hostname: 139.177.190.9:22
SSH Username: daronphang
SSH password:
SSH Key File: path/to/private_key_rsa
MySQL Hostname: localhost/127.0.0.1
username: root
password:
Default Schema:
```

### SSH Key

Need to use RSA private key instead of OpenSSH.

https://stackoverflow.com/questions/65145221/mysql-could-not-connect-the-ssh-tunnel-access-denied-for-none

```console
$ ssh-keygen -b 4096 -t rsa -m PEM      # rsa private key
$ ssh-keygen -p -m PEM -f ~/.ssh/id_rsa     # downgrade from OpenSSH to RSA private key
```

### MySQL Workbench

If using auth_socket, need to change connection type from 'TCP/IP' to 'Local Socket/Pipe'. By default, the path should be /var/run/mysqld/mysqld.sock.
