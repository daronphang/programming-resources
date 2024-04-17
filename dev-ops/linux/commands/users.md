## User permissions

For 'umask', need to subtract the value from 0777 for default directory creation permission, and 0666 for default file creation permission.

```sh
$ id            # check user and group IDs
$ sudo -l       # check commands current user can run
$ umask         # default permission you have to create files and directories
$ groups
```

### Add user to sudo/group

To create a new user with sudo access, need log into the system with a root user or an account with sudo privileges.

Most Linux distro have a user group for sudo users. To grant the new user elevated privileges, add them to the sudo group. The '-aG' option tells the system to append the user to the specified group.

```sh
$ sudo adduser newuser              # creates a new user, group and home directory
$ sudo usermod -aG sudo newuser
$ groups newuser
$ grep /etc/group -e "docker"       # check to see who were successfully added to the group
```

### Remove user

```sh
$ sudo killall -u username      # if user is logged in
$ userdel -r username   # r flag force remove user's home directory and mail spool
$ userdel -f username
```

## Create group

```sh
$ groupadd mygroup
$ groupadd -g 1010 mygroup

$ groupadd -r mysystemgroup     # create system group
```

## Root

### Enabling

```sh
$ sudo passwd -u root        # enter a new password for root, -u flag to unlock root user
$ su root
$ whoami
```

### Disabling

Before you block access to root account, need ensure you have created an administrative account capable of using 'sudo' command to gain root user privileges.

The -m flag means create user's home directory and -c flag allows to specify a comment.

```sh
$ useradd -m -c "Some comment" daronphang
$ passwd 123password
```

```sh
$ sudo passwd -l root       # -l flag to lock password for the root user
$ sudo usermod -L root
$ sudo nano /etc/passwd     # change root shell from /bin/bash to /usr/sbin/nologin
$ sudo usermod -s /usr/sbin/nologin root    # same as above

$ cat /etc/passwd           # verify shell set for root
```
