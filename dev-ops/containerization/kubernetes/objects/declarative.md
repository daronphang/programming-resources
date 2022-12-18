## Kompose

Tool to convert Docker Compose to Kubernetes objects.

## Commands

Multiple yaml files can be applied.

```
$ kubectl create -f your_yaml_file.yaml --dry-run --validate=true

$ kubectl apply -f filename.yml           # Create/update resources in a file
$ kubectl apply -f myyaml/                # Create/update whole directory of yaml
$ kubectl -f app.yml --dry-run
$ kubectl diff -f app.yml                 # Compares your yml with server's yml

$ kubectl api-resources
$ kubectl api-versions
$ kubectl explain services --recursive    # Get keys each API version supports
$ kubectl explain services.spec           # Get subkeys of spec
$ kubectl explain services.spec.type
```

## Pods

Rarely create individual Pods directly as they are designed as relatively ephemeral, disposable entities.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:1.14.2
      ports:
        - containerPort: 80
```

## Deployments

Creates a ReplicaSet to bring up three nginx Pods.

```yaml
# deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  spec:
    selector:
      matchLabels: # Glue telling the kind which pods are theirs
        app: nginx
    replicas: 3
    template:
      metadata: # kubectl explain deployment.spec.template.metadata
        labels:
          app: nginx:
      spec:
        containers:
          name: nginx
          image: nginx:1.17.3
          ports:
            containerPort: 80
---  # separation between manifests
apiVersion: apps/v2
```

```yaml
-- Postgres Database
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgresql
  namespace: Database
spec:
  selector:
    matchLabels:
      app: postgresql
  replicas: 1
  template:
    metadata:
      labels:
        app: postgresql
    spec:
      containers:
        - name: postgresql
          image: postgresql:latest
          ports:
            - name: tcp
              containerPort: 5432
          env:
            - name: POSTGRES_USER
              value: postgres
            - name: POSTGRES_PASSWORD
              value: postgres
            - name: POSTGRES_DB
              value: postgres
          volumeMounts:
        - mountPath: /var/lib/postgresql/data
          name: postgredb
      volumes:
        - name: postgredb
          persistentVolumeClaim:
            claimName: postgres-data

-- My Api
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-api
  namespace: Api
spec:
  selector:
    matchLabels:
      app: my-api
  replicas: 1
  template:
    metadata:
      labels:
        app: my-api
    spec:
      containers:
        - name: my-api
          image: my-api:latest
          ports:
            - containerPort: 8080
              name: "http"
          volumeMounts:
            - mountPath: "/app"
              name: my-app-storage
          env:
            - name: POSTGRES_DB
              value: postgres
            - name: POSTGRES_USER
              value: postgres
            - name: POSTGRES_PASSWORD
              value: password
          resources:
            limits:
              memory: 2Gi
              cpu: "1"
      volumes:
        - name: my-app-storage
          persistentVolumeClaim:
            claimName: my-app-data
```
