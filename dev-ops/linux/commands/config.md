## Distro Version/Architecture

```console
$ cat /etc/os-release
$ lsb_release -a

$ uname -m  # x86_64

$ dpkg --print-architecture     # amd64
```

## Drivers

```console
$ sudo ubuntu-drivers autoinstall

$ sudo lspci -v      View all drivers installed

$sudo dkms status            Get drivers from dynamic kernel module support
```

## Display

Xrandr is a utility for monitor management.

```console
$ xrandr -q
$ xrandr --output DVI-D-0 --mode 1920x1080      # Output targets monitor, mode tells which resolution
$ xrandr --output DVI-D-0 --mode 1920x1080 --rate 60.00
```

## Network

```console
$ ifconfig -a       # private IP address
$ curl ifconfig.me  # public IP address
$ ip address show

$ sudo apt install speedtest-cli
$ speedtest
```

## Checking Disk Space

```console
$ df -h /data     # h is short for human-readable
$ df -h -total    # see total disk space available
```

## Checking Path

```console
$ which python3

$ realpath run_python.sh    # get absolute path
```

## CPU

```console
$ lscpu
```

## Ports

```console
$ sudo lsof -i -P -n | grep LISTEN
$ sudo lsof -i:22   # see a specific port
```
