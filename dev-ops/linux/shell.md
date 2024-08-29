## Shell

The shell is a command line interpreter in Linux. It is a program that receives commands from the user and gives them to the OS to execute. Bash is the default login shell for most Linux distributions, but there are other types including Korn shell (ksh), Z shell (zsh) and C shell (csh).

### Interactive Login Shell

An interactive shell receives commands from the user and displays output to the user. Moreover, users get a login shell when they login to their account. Starts when you log in on a text console, through SSH or with su.

Bash loads the configuration files in the following:

1. Login shell invokes /etc/profile
2. /etc/profile invokes scripts in /etc/profile.d/\*.sh
3. Then executes users ~/.bash_profile
4. ~/.bash_profile invokes users ~/.bashrc
5. ~/.bashrc invokes /etc/bashrc

If ~/.bash_profile cannot be found, it will look for the following in the order:

- ~/.bash_login
- ~/.profile

```sh
$ sudo vi ~/.bashrc
$ export [VARIABLE_NAME]=[variable_value]
$ source ~/.bashrc
```

### Interactive Non-login Shell

A non-login shell is started by a login shell without the interference of the login process i.e. a shell that is started from another shell.

Bash loads configuration from the following:

- ~/.bashrc

### Non-interactive Login Shell

This is extremely rare, and unlikely to encounter it.

```sh
$ echo 'echo $-; shopt login_shell' | ssh localhost
Pseudo-terminal will not be allocated because stdin is not a terminal.
hBs
login_shell    	on
```

```sh
$ if tty -s; then echo 'This is interactive shell.'; else echo 'This is non-interactive shell.'; fi
```

### Non-interactive Non-login Shell

Started when we run scripts on our machine as they run in their new shell that is non-interactive. It only opens to execute the script and closes immediately once it is finished.

Loads configuration in the following:

- $BASH_ENV

```sh
$ bash script.sh
```

## Shell Check

To check if you are on the login shell, it has a hyphen as a prefix.

```sh
$ echo $0   # -bash
$ shopt login_shell
```

To check if shell is interactive, check the contents of $- variable (will include 'i').

```sh
$ echo $-   # himBHs
```
