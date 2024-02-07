## Helm

Helm is a tool that streamlines installing and managing Kubernetes applications i.e. lets us treat our Kubernetes apps as apps instead of just a collection of objects.

```bash
$ helm --debug # verbose
```

### add, search

The add command is used to add a new chart repository to Helm and this allows us to browse and install charts from the new repository.

```bash
$ helm repo add polar https://charts.bitnami.com/bitnami
$ helm repo ls
$ helm repo update
$ helm search repo polar | grep nginx
$ helm search repo nginx # find latest version
```

### install

```bash
$ helm install bravo bitnami/drupal # release name is bravo

$ helm show values bitnami/apache
$ helm show values bitnami/apache | yq e # parse yaml and show with colors
$ helm install bravo bitnami/apache --set rpelicaCount=2 --set image.debug=true # adding values
```

### list

```bash
$ helm list -n mercury -a # will not show pending status, need list all
```

### pull

Retrieves a package from a package repository, and download it locally.

```bash
$ helm pull bitnami/apache
```

## Values file

One of the built-in objects is Values. This object provides access to values passed into the chart. This object provides access to values passed into the chart. Its contents come from multiple sources (lowest priority first):

- The values.yaml file in the chart
- If this is a subchart, the values.yaml file of a parent chart
- A values file if passed into helm install or helm upgrade with the -f flag i.e. `helm install -f myvals.yaml ./mychart`
- Individual parameters passed with --set i.e. `helm install --set foo=bar ./mychart`

YAML is a flexible format, and values may be nested deeply or flattened.

```yaml
# values.yaml
favorite:
  drink: coffee
  food: pizza
```

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
data:
  myvalue: "Hello World"
  drink: {{ .Values.favorite.drink }}
  food: {{ .Values.favorite.food }}
```

### Set flag

The flag --set has a higher precedence than the default values.yaml.

```bash
$ helm install -f values.yaml mywebapp /root/apache-10.2.3.tgz

$ helm install solid-vulture ./mychart --dry-run --debug --set favoriteDrink=slurm --set aws.subnets={subnet-123456,subnet-654321}
```
