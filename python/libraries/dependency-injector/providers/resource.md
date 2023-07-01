## Resource Provider

Resource provider provides a component with initialization and shutdown. Similar to Singleton as resource initialization happens only once. Helps to initialize and configure logging, event loop, thread or process pool, etc.

Container provides an interface to initialize and shutdown resources.

```py
# init and shutdown all resources
container = Container()
container.init_resources()
container.shutdown_resources()

# init and shutdown resources one-by-one
container = Container()
container.thread_pool.init()
container.thread_pool.shutdown()
```

```py
import sys
import logging
from concurrent.futures import ThreadPoolExecutor

from dependency_injector import containers, providers


def init_thread_pool(max_workers: int):
    thread_pool = ThreadPoolExecutor(max_workers=max_workers)
    yield thread_pool
    thread_pool.shutdown(wait=True)


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    thread_pool = providers.Resource(
        init_thread_pool,
        max_workers=config.max_workers,
    )

    logging = providers.Resource(
        logging.basicConfig,
        level=logging.INFO,
        stream=sys.stdout,
    )


if __name__ == "__main__":
    container = Container(config={"max_workers": 4})

    container.init_resources()

    logging.info("Resources are initialized")
    thread_pool = container.thread_pool()
    thread_pool.map(print, range(10))

    container.shutdown_resources()
```

## Initializer Types

### Function

```py
def init_resource(argument1=..., argument2=...):
    return SomeResource()


class Container(containers.DeclarativeContainer):

    resource = providers.Resource(
        init_resource,
        argument1=...,
        argument2=...,
    )
```

### Generator

```py
def init_resource(argument1=..., argument2=...):
    resource = SomeResource()  # initialization

    yield resource

    # shutdown
    ...


class Container(containers.DeclarativeContainer):

    resource = providers.Resource(
        init_resource,
        argument1=...,
        argument2=...,
    )
```

### Subclass

```py
from dependency_injector import resources


class MyResource(resources.Resource):

    def init(self, argument1=..., argument2=...) -> SomeResource:
        return SomeResource()

    def shutdown(self, resource: SomeResource) -> None:
        # shutdown
        ...


class Container(containers.DeclarativeContainer):

    resource = providers.Resource(
        MyResource,
        argument1=...,
        argument2=...,
    )
```
