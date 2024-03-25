## Managing Resources

By default, a container has no resource constraints and can use as much of a given resource as the host's kernel scheduler allows.

```sh
$ docker run --cpus=2 nginx
$ docker run -m 512m nginx
```
