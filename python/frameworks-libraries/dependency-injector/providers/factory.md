## Factory Provider

Factory provider creates new objects. The first argument is a class, a factory function or method that creates an object. The rest of the Factory positional and keyword arguments are the dependencies.

```py
from dependency_injector import containers, providers


class User:
    ...


class Container(containers.DeclarativeContainer):

    user_factory = providers.Factory(User)


if __name__ == "__main__":
    container = Container()

    user1 = container.user_factory()
    user2 = container.user_factory()
```

### Adding Attributes

```py
from dependency_injector import containers, providers


class Client:
    ...


class Service:
    def __init__(self) -> None:
        self.client = None


class Container(containers.DeclarativeContainer):

    client = providers.Factory(Client)

    service = providers.Factory(Service)
    service.add_attributes(client=client)


if __name__ == "__main__":
    container = Container()

    service = container.service()

    assert isinstance(service.client, Client)
```

### Nested Dependencies

Need to create factories for all the classes, and use \_\_ syntax for passing the argument.

```py
from dependency_injector import containers, providers


class Regularizer:
    def __init__(self, alpha: float) -> None:
        self.alpha = alpha


class Loss:
    def __init__(self, regularizer: Regularizer) -> None:
        self.regularizer = regularizer


class ClassificationTask:
    def __init__(self, loss: Loss) -> None:
        self.loss = loss


class Algorithm:
    def __init__(self, task: ClassificationTask) -> None:
        self.task = task


class Container(containers.DeclarativeContainer):

    algorithm_factory = providers.Factory(
        Algorithm,
        task=providers.Factory(
            ClassificationTask,
            loss=providers.Factory(
                Loss,
                regularizer=providers.Factory(
                    Regularizer,
                ),
            ),
        ),
    )


if __name__ == "__main__":
    container = Container()

    algorithm_1 = container.algorithm_factory(
        task__loss__regularizer__alpha=0.5,
    )
    assert algorithm_1.task.loss.regularizer.alpha == 0.5

    algorithm_2 = container.algorithm_factory(
        task__loss__regularizer__alpha=0.7,
    )
    assert algorithm_2.task.loss.regularizer.alpha == 0.7
```

### String Imports

```py
class Container(containers.DeclarativeContainer):

    service = providers.Factory("myapp.mypackage.mymodule.Service")
    service = providers.Factory(".mypackage.mymodule.Service")  # relative
```
