## Singleton Provider

Memorizes the first created object and returns it on the rest of the calls. When an object is created and memorized, Singleton provider just returns it without applying injections.

```py
from dependency_injector import containers, providers


class UserService:
    ...


class Container(containers.DeclarativeContainer):

    user_service_provider = providers.Singleton(UserService)


if __name__ == "__main__":
    container = Container()

    user_service1 = container.user_service_provider()
    user_service2 = container.user_service_provider()
    assert user_service1 is user_service2
```

## Scope

Scope is tied to the container.

```py
if __name__ == "__main__":
    container1 = Container()
    user_service1 = container1.user_service_provider()
    assert user_service1 is container1.user_service_provider()

    container2 = Container()
    user_service2 = container2.user_service_provider()
    assert user_service2 is container2.user_service_provider()

    assert user_service1 is not user_service2
```

## Reset

Can be used with a context manager. Memorized instance will be reset when entering and exiting a context.

```py
if __name__ == "__main__":
    container = Container()

    user_service1 = container.user_service()
    container.user_service.reset()
    user_service2 = container.user_service()
    assert user_service2 is not user_service1

    with container.user_service.reset():
        user_service2 = container.user_service()
```

## Threading

Singleton provider is NOT thread-safe. Need to explicitly establish a synchronization for using the provider in multi-threading application. Otherwise, could trap into the race condition problem: Singleton will create multiple objects.

Two thread-safe implementations:

- ThreadSafeSingleton: Can use in multi-threading operations without additional synchronization
- ThreadLocalSingleton: Uses thread-locals as a storage. This type of singleton will manage multiple objects - one object for each thread

```py
import threading
import queue

from dependency_injector import containers, providers


def put_in_queue(example_object, queue_object):
    queue_object.put(example_object)


class Container(containers.DeclarativeContainer):

    # Queue contains same number of objects as number of threads where
    # thread-local singleton provider was used

    thread_local_object = providers.ThreadLocalSingleton(object)

    queue_provider = providers.ThreadSafeSingleton(queue.Queue)

    put_in_queue = providers.Callable(
        put_in_queue,
        example_object=thread_local_object,
        queue_object=queue_provider,
    )

    thread_factory = providers.Factory(
        threading.Thread,
        target=put_in_queue.provider,
    )


if __name__ == "__main__":
    container = Container()

    n = 10
    threads = []
    for thread_number in range(n):
        threads.append(
            container.thread_factory(name="Thread{0}".format(thread_number)),
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    all_objects = set()
    while not container.queue_provider().empty():
        all_objects.add(container.queue_provider().get())

    assert len(all_objects) == len(threads) == n
```

### Scopes

Each request will have a different object.

```py
from dependency_injector import containers, providers
from flask import Flask, current_app


class Service:
    ...


class Container(containers.DeclarativeContainer):

    service_provider = providers.ThreadLocalSingleton(Service)


def index_view():
    service_1 = current_app.container.service_provider()
    service_2 = current_app.container.service_provider()
    assert service_1 is service_2
    print(service_1)
    return "Hello  World!"


def teardown_context(request):
    current_app.container.service_provider.reset()
    return request


container = Container()

app = Flask(__name__)
app.container = container
app.add_url_rule("/", "index", view_func=index_view)
app.after_request(teardown_context)


if __name__ == "__main__":
    app.run()
```
