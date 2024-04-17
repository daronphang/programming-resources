## Linux capabilities

Linux capabilities provide a subset of the available root privileges to a process. This effectively breaks up root privileges into smaller and distinctive units. Each of the units can then be independently be granted to processes.

Linux kernel capabilities are supported not only for processes, but for all threads in a process as well.

```
CHOWN
DAC
KILL
SETFCAP
SETPCAP
SETUID
GETGID
NET_BIND
NET_ADMIN
SYS_ADMIN
SYS_CHROOT
```

```sh
$ cat /proc/<PID>/status | grep Cap
$ capsh --decode=<hex number>
$ getpcaps <PID>
```

```sh
$ sudo getcap /path/to/the/file
$ sudo setcap cap_net_bind_service+ep /path/to/the/file
$ sudo setcap cap_net_raw=ep ping
```
