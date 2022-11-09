## Process Status

Used to get more detailed information about a specific process/processes i.e. check if a process is running or not.

"ps aux" is most frequently used command by Linux admin. Prints all running processes in system regardless from where they have been executed. A process is associated with any program running on your system, and is used to manage and monitor a program's memory usage, processor time, and I/O resources.

```
USER        User account under which this process is running
PID         Process ID
%CPU        CPU time used by this process
%MEM        Physical memory used by this process
VSZ         Virtual memory
RSS         Resident set size i.e. non-swappable physical memory
TTY         Terminal from which this process is started
STAT        Process state
START       Starting time
TIME        Total CPU time used by this process
```

```console
$ ps        # Displays info about processes that are bound by the controlling terminal
$ ps aux    # Displays the most amount of info a user usually needs to understand current state
$ ps -A     # Prints all running processes (summarized)
$ ps -AF    # Prints full format
$ ps x
$ ps -He

$ sudo kill <pid>

$ ps aux --sort -%mem
$ ps aux --sort=-%mem
$ ps aux | sort -nk +4 | tail -n 10      Sort by 4th field (%MEM), show last 10 lines
$ ps aux --sort -rss | head
```

### kill

```console
$ kill <pid>
$ pkill <process name>
$ killall <process name>
```


## Installing Packages

```console
$ # update fetches latest versions for packages installed on system
$ # upgrade performs the updates
$ sudo apt update && apt upgrade
```

## Substitute User

Elevate privileges assigned to the current user. Both su and sudo are used to run commands with root permissions. Root user is equivalent to administrator user on Windows.

For su, it switches you to the root user account and prompts for the root account's password. On the other hand, sudo runs a single command with root privileges and prompts for current user's password before running command as the root user.

```console
$ whoami
$ sudo
$ su <user>                   ctrl+D to logout of su or type 'exit'
$ sudo apt update             Updates packages but does not install them
$ sudo apt upgrade
```

## History

View previously used commands.

```console
$ history
```

## Ping

```console
$ ping [option] [hostname/IP address]
$ ping google.com
```

## Extracting/Compressing Files

tar.gz (gzip) file contains compressed files to save storage space and bandwidth during downloading process. It is a combination of .tar file and .gz file.

```
x   instructs tar to extract the files from zipped file
v   verbose
z   instructs tar to decompress files
f   filename to work on
```

```console
$ gzip test.txt     # compress file, outputs test.txt.gz
```

```console
$ tar -xvzf documents.tar.gz
tar –xvzf documents.tar.gz –C /home/user/destination    # put files to specific directory
```

## Installing Files

dpkg is a tool to install, build, remove and manage Debian packages.

```console
$ sudo dpkg -i package_file.deb     # for ubuntu debian, to install dependencies automatically
$ sudo dpkg -r package.deb  # remove program
$ sudo dpkg --update-avail  # updating repositories
```
