## Process status

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

```sh
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

### Kill

```sh
$ kill <pid>
$ pkill <process name>
$ killall <process name>
```

## Checking assigned CPU to process

```sh
$ top -p <PID> -p <PID>  # add Last Used CPU by pressing f followed by space
```
