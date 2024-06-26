## alias

```sh
$ export ns=default
$ export do="--dry-run=client -o yaml"
$ export now="--grace-period 0 --force"

$ alias k='kubectl -n $ns'

```

## vim

```sh
$ vim ~/.vimrc

set sw=2 ts=2 sts=2 et
set expandtab
set tabstop=2
set shiftwidth=2
```

## Creating objects

If unsure what field to pass in the yaml file, create with imperative and use help command.

```sh
$ kubectl create rolebinding -h
```

## Copying objects from output

When outputing a running pod in yaml format, need to remove status, volume, volumeMount and nodeName sections, else the new pod won't start.
