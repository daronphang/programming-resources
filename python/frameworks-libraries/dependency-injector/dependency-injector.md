## Dependency Injector

Python library package. Two main entities are containers and providers.

With the dependency injector, object assembling is consolidated in a container. Dependency injections are defined explicitly.

```console
$ pip install dependency-injector
```

## Entities

### Providers

Provides Factory, Singleton, Callable, Coroutine, Object, List, Dict, Configuration, Resource, Dependency and Selector.

### Containers

A collection of providers. Provides declarative and dynamic containers.

### Wiring

Injects dependencies into functions and methods. Helps integrate with other frameworks including Django, Flask, Aiohttp, FastAPI, etc.

## Implementation

When you need an object, you place a Provide marker as a default value of a function argument. When you call this function, framework assembles and injects the dependency.
