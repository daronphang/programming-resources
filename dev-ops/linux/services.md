## init

The 'init' daemon is the first process executed by the Linux kernel ad its PID is always 1. If unable to start, system will 'Kernel Panic'. Created in the 1980s. Its purpose is to initialize, manage and track system services and daemons. Starts serially and results in delayed and longer booting time.

To create a service, you will need to write a script and store it in /etc/init.d directory.

```console
$ sudo sservice <command> <service-name>
$ sudo /etc/init.d/<service-name> <command>     # same
```

```sh
#!/bin/bash
# chkconfig: 2345 20 80
# description: Description comes here....

# Source function library.
. /etc/init.d/functions

start() {
    # TODO: code to start app comes here
}

stop() {
    # TODO: code to stop app comes here
}

case "$1" in
    start)
       start
       ;;
    stop)
       stop
       ;;
    restart)
       stop
       start
       ;;
    status)
       # TODO: code to check status of app comes here
       ;;
    *)
       echo "Usage: $0 {start|stop|restart|status}"
esac

exit 0
```

## systemd (system daemon)

Systemd is an init daemon used by modern systems and starts system services in parallel which removes unnecessary delays and speeds up the initialization process.

To create a service, you need to write .service file and store it in /etc/systemd/system directory.

```console
$ sudo systemctl <command> <service-name>

$ sudo systemctl start nginx
```

### edit

The edit command opens up a blank drop-in snippet file.

```sh
$ sudo systemctl edit ssh
```

When the file is saved, systemctl will create a file called override.conf under a directory at /etc/systemd/system/yourservice.service.d, where yourservice is the name of the service you chose to edit. This command is useful for changing a few properties of the unit file.

Second way is to use the edit command with the --full flag.

```sh
$ sudo systemctl edit ssh --full
```

This command opens a full copy of whatever unit file you chose to edit in a text editor. When the file is saved, systemctl will create a file at /etc/systemd/system/yourservice.service. This is useful if you need to make many changes to an existing unit file.

In general, any unit file in /etc/systemd/system will override the corresponding file in /lib/systemd/system.

## Service Commands

killall will look for the exact match of the process name whereas pkill will allow terminating the process either by full name or by partial process name.

```sh
$ kill {PID}
$ killall {ProcessName}
$ pkill python
```
