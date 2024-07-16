## Environment variables

```sh
$ printenv
$ printenv | less
$ printenv HOME
$ set | grep [VARIABLE_NAME]  # includes local and shell variables
```

## Shell

```sh
$ export [VARIABLE_NAME]=[variable_value]

$ unset [VARIABLE_NAME]
```

## Permanent

Need to consider the following situations:

- Login shell
- Non-login shell
- Interactive shell
- Non-interactive shell

### Global

```
/etc/profile.d      if available
/etc/profile
/etc/environment
```

Creates a .sh file in one of the folders above. Syntax to add is the same for both global or user.

## Proxies

When running apt/yum, it uses root and hence, setting proxies in ~/.shrc will not reflect. Need to modify yum/apt.conf file.

```
/etc/yum.conf                     # modify proxy globally
/etc/yum.repos.d/some.repo        # modify proxy for specific repositories
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
