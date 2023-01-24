## Wiring

Wiring feature provides a way to inject container providers into the functions and methods.

To use wiring, need to perform the following:

- Place @inject decorator to inject the dependencies
- Place markers to help container find the injections i.e. Provide[Container.bar]
- Wire the container with the markers in the code
- Use functions and classes normally

```py
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject


class Service:
    ...


class Container(containers.DeclarativeContainer):

    service = providers.Factory(Service)


@inject
def main(service: Service = Provide[Container.service]) -> None:
    ...


if __name__ == "__main__":
    container = Container()
    container.wire(modules=[__name__])

    main()
```
