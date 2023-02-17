## Routing

https://docs.celeryq.dev/en/stable/userguide/routing.html

### Automatic

Default setting is to use task_create_missing_queues. If a named queue is not defined in task_queues, a queue named 'celery' will be created automatically.

Celery allows routing each task using named queues.The task routes can either be a dictionary or a list of router objects. If using automatic routing, do not need to define queue when sending tasks to queue using apply_async() or delay().

```py
task_routes = {
    'core.tasks.too_long_task': {'queue': 'too_long_queue'},
    'core.tasks.quick_task': {'queue': 'quick_queue'},
    'feeds.tasks.import_feed': {
        'queue': 'feed_tasks',
        'routing_key': 'feed.import',
        },
}

# specified as a tuple containing a list
task_routes = ([
    ('feed.tasks.*', {'queue': 'feeds'}),
    ('web.tasks.*', {'queue': 'web'}),
    (re.compile(r'(video|image)\.tasks\..*'), {'queue': 'media'}),
],)
```

```console
$ celery --app=proj_name worker -Q too_long_queue -c 2
$ celery --app=proj_name worker -Q quick_queue -c 2
```

### Manual

```py
process_link.apply_async(args=[link1], queue=queue1)
process_link.apply_async(args=[link2], queue=queue2)
```

```console
$ celery -A tasks.app worker --loglevel=info -P solo -Q queue1
```

## Creating Queues

```
CELERY_CREATE_MISSING_QUEUES = True
```

```console
$ celery -A proj worker -l info -Q queue1,queue2
```

## Consuming New Queues

Can be done via command prompt or within Python.

```console
$ celery control add_consumer content.0c3a92a4-3472-47b8-8258-2d6c8a71e3ba
```

```py
app.control.add_consumer('content.0c3a92a4-3472-47b8-8258-2d6c8a71e3ba', reply=True)
```
