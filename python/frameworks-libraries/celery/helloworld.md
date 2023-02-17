## Helloworld

```py
# tasks.py
from celery import Celery


class CeleryConfig:
    broker = 'redis://localhost:6379/0'
    backend = 'redis://localhost:6379/0'
    task_routes = {
        'tasks.hello': {
            'queue': 'test1_queue',
            'routing_key': 'test1_routing_key'
            }}

# provide broker and backend at point of creation rather than defer it
app = Celery(
    __name__,
    broker=CeleryConfig.broker,
    backend=CeleryConfig.backend
    )
app.config_from_object(CeleryConfig)


@app.task(bind=True)
def hello(self, payload):
    print(f'hello world, {payload}')
    return
```

```console
$ cd path/to/parent # for celery to register PATH
$ celery -A tasks.app worker --loglevel=info -P solo -Q test1_queue
```

### Check Registered Tasks

When you start celery, should be able to see the name of the tasks. If unregistered, means celery worker is unable to discover the path.

```console
$ celery -A src.tasks.app worker --loglevel=info -P solo -Q test1_queue     # does not work! registers tasks as src.tasks.hello
$ celery -A tasks.app worker --loglevel=info -P solo -Q test1_queue
```

```
[tasks]
    . tasks.hello
```

### Main Name

When creating an instance of Celery, need to provide name. This is because when you send a task message, the message doesn't contain any source code, but only the name of the task you want to execute. If Celery is not able to detect what module the function belongs to, it uses the main module name (**main**) to generate the beginning of the task name.

```py
# tasks.py
from celery import Celery
app = Celery()

@app.task
def add(x, y): return x + y

if __name__ == '__main__':
    app.worker_main()   # when module is executed, tasks will be named starting with __main__
```

```py
# test.py
from tasks import add

# when imported, tasks will be named by the real name of module (tasks)
add.name
# tasks.add
```
