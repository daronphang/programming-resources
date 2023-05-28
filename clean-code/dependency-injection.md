## Dependency Injection

Main idea is to separate the construction and usage of objects i.e. building software that is modular and easy to extend. Popular with static languages like Go and Java. However, they are not popular with dynamically typed languages like Python.

DI is a principle that helps to achieve an **inversion of control by decreasing coupling and increasing cohesion**. In DI, objects do not create each other but are injected. Most DI containers won't construct an object until needed.

In the context of dependency management, an object should not take responsibility for instantiating dependencies itself. Instead, it should pass this responsibility to another "authoritative" mechanism, thereby inverting the control.

Injection is the process of providing an instance of a type, to a method that uses that instance.

### Benefits

- Easier to follow SRP (Single Responsibility Principle)
- Flexibility of configurable components
- Testing made easy (inject mocks or test doubles of your dependencies)
- High cohesion with reduced module complexity
- Minimalistic dependencies
- Improve the modularity of your application

### Without DI

```py
import os


class ApiClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")  # <-- dependency
        self.timeout = int(os.getenv("TIMEOUT"))  # <-- dependency


class Service:

    def __init__(self) -> None:
        self.api_client = ApiClient()  # <-- dependency


def main() -> None:
    service = Service()  # <-- dependency
    ...


if __name__ == "__main__":
    main()
```

### With DI

Assembly code might get complicated and become harder to change the application structure. This can resolved by using a Dependency Injector.

```py
import os


class ApiClient:

    def __init__(self, api_key: str, timeout: int) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


class Service:

    def __init__(self, api_client: ApiClient) -> None:
        self.api_client = api_client  # <-- dependency is injected


def main(service: Service) -> None:  # <-- dependency is injected
    ...


if __name__ == "__main__":
    main(
        service=Service(
            api_client=ApiClient(
                api_key=os.getenv("API_KEY"),
                timeout=int(os.getenv("TIMEOUT")),
            ),
        ),
    )
```

## Dependency Injector

With this pattern, objects lose the responsibility of assembling the dependencies. The injector absorbs that responsibility by assembling and injecting dependencies.

If object A depends on object B, object A **must not** create import object B directly. Instead, object A must provide a way for injecting object B.
