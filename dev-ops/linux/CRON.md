## CRON

Built-in Linux utility that runs processes on your system at a scheduled time. Reads crontab (cron tables) for predefined commands and scripts.

https://crontab.guru/#____\*__\__

### Service

```bash
$ sudo systemctl status crond.service
```

### Crontab

```bash
$ crontab -e    # for user
$ crontab –u other_username –e
$ sudo vim /etc/crontab # for root
```

## Syntax

```
a b c d e /directory/command output
* 2 0 * 4 /root/backup.sh # runs 2am on first day of month on Wed
* * * * * /root/backup.sh # runs job every minute
```

### Troubleshooting

Add bash/sh path in crontab.

```
* * * * * touch /tmp/testing.txt
* * * * * /bin/bash /root/backup.sh
```

### Time Format

```
a   Minute, 0-59
b   Hour, 0-23
c   Day, 0-31
d   Month, 0=None, 12=December
e   Day of week, 0=Sunday, 7=Sunday
```

### Command

Represents the exact directory and filename to execute.

```
/root/backup.sh
```

### Output (Optional)

CRON sends an email to the owner of the crontab by default. To disable, add >/dev/null 2>&1, after the timing and command fields.

```
a b c d e /directory/command /dev/null 2>&1
```

### Operators (Optional)

```
*   Stands for all values; use it to keep running everyday
,   separate individual values
-   Range of values
/   Divide a value into steps
```
