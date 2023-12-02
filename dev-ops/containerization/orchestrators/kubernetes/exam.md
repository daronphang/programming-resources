## alias

```bash
$ export ns=default
$ export do="--dry-run=client -o yaml"
$ export now="--grace-period 0 --force"

$ alias k='kubectl -n $ns'

```

## vim

```bash
$ vim ~/.vimrc

set sw=2 ts=2 sts=2 et
set expandtab
set tabstop=2
set shiftwidth=2
```

## Creating objects

If unsure what field to pass in the yaml file, create with imperative and use help command.

```bash
$ kubectl create rolebinding -h
```
