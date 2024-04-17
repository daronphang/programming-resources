## Installing packages

```sh
$ # update fetches latest versions for packages installed on system
$ # upgrade performs the updates
$ sudo apt update && apt upgrade
```

### Setting proxy

To setup proxy for apt/yum, need to modify /etc/apt.conf or /etc/yum.conf.

```
proxy=http://micron.com:80
```

## Substitute user

Elevate privileges assigned to the current user. Both su and sudo are used to run commands with root permissions. Root user is equivalent to administrator user on Windows.

For su, it switches you to the root user account and prompts for the root account's password. On the other hand, sudo runs a single command with root privileges and prompts for current user's password before running command as the root user.

```sh
$ whoami
$ sudo
$ su <user>                   ctrl+D to logout of su or type 'exit'
$ sudo apt update             Updates packages but does not install them
$ sudo apt upgrade
```

## History

View previously used commands.

```sh
$ history
```
