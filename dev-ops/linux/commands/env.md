## Environment Variables

```console
$ printenv | less
$ printenv HOME
$ set | grep [VARIABLE_NAME]  # includes local and shell variables
```

### Shell

```console
$ export [VARIABLE_NAME]=[variable_value]

$ unset [VARIABLE_NAME]
```

### Permanent

```console
$ sudo vi ~/.bashrc
$ export [VARIABLE_NAME]=[variable_value]
$ source ~/.bashrc
```
