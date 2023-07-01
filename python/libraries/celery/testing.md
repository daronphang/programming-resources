## Celery Testing

https://distributedpython.com/posts/unit-testing-celery-tasks/

```py
@app.task(bind=True)
def heartbeat(self, name):
    print(name)
    return name
```

```py
import pytest
import unittest.mock as mock

from main import heartbeat


@mock.patch('src.main.BaseTask.on_success')
def test_heartbeat(mock_success):
    task = heartbeat.apply(args=('john'), kwargs={})
    assert task.results == 'john'
```
