## Creating Volumes

### CIFS

```sh
$ docker volume create \
--driver local \
--opt type=cifs \
--opt o=username=daronphang,password=123,vers=3.0,rw \
--opt device=//10.195.168.10/F10_PEE_UIPATH/daronphang \
--name uipath
```

### Bind Mount

```sh
$ docker volume create \
--driver local \
--opt type=none \
--opt o=bind \
--opt device=/home/daronphang/df_microservices \
--name df_microservices
```
