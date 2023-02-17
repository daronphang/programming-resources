## Configuration

Can be set on the app directly or by using a configuration module.

https://docs.celeryq.dev/en/stable/userguide/configuration.html#example-configuration-file

### App Setting

```py
app.conf.task_serializer = 'json'

# configuring many settings at once
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
```

### Module

```py
app.config_from_object('celeryconfig')
```

```py
# celeryconfig.py

broker_url = 'pyamqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Oslo'
enable_utc = True
```
