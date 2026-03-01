## Distro version/architecture

```sh
$ cat /etc/os-release
$ lsb_release -a

$ uname -m  # x86_64
$ uname -a

$ cat /etc/issue # Debian GNU/Linux 10

$ dpkg --print-architecture     # amd64
```

## Drivers

```sh
$ sudo ubuntu-drivers autoinstall

$ sudo lspci -v      View all drivers installed

$sudo dkms status            Get drivers from dynamic kernel module support
```

## Display

Xrandr is a utility for monitor management.

```sh
$ xrandr -q
$ xrandr --output DVI-D-0 --mode 1920x1080      # Output targets monitor, mode tells which resolution
$ xrandr --output DVI-D-0 --mode 1920x1080 --rate 60.00
```

## Checking disk space

df and du commands are used to monitor disk space but serve different purposes:

- df (disk free) reports space at the filesystem level. Defaults to showing all mounted filesystems
- du (disk usage) reports space at the directory/file level. It calculates the size of each file one at a time, giving a more accurate snapshot of a given directory/subdirectory. du doesn't follow symlinks (a running process can keep a deleted file open, du doesn't see this so it will report a lower number than df)

```sh
$ df -h /data     # h is short for human-readable
$ df -h -total    # see total disk space available

$ sudo du -h --max-depth=1 /var
```

## Checking path

```sh
$ which python3

$ realpath run_python.sh    # get absolute path
```

## CPU

```sh
$ lscpu
```

## Ports

```sh
$ sudo lsof -i -P -n | grep LISTEN
$ sudo lsof -i:22   # see a specific port
```

## Mounting directory

UID and GID only work for filesystems that don't support Linux permission schema i.e. FAT, NTFS.

```bash
$ sudo mount -t cifs -o username=daronphang,password=password //10.195.111.11/F10_PEE_UIPATH/daronphang /mnt/uipath
```

```bash
$ sudo mount -t cifs -o credentials=abs/path/to/.cifs //10.195.111.11/F10_PEE_UIPATH/daronphang /mnt/uipath
```

## Checking directory size

```bash
$ df -h
$ sudo du -h --max-depth=1 /var
```
