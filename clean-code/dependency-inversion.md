## Dependency Inversion (IoC)

A fundamental design principle used by frameworks to invert the responsibilities of flow control in an application. In simple terms:

- we should not depend on low-level implementations, but rely on high-level abstractions
- Abstractions should not depend on details, but details should depend on abstractions

For Python, this can be implemented easily with duck-typing.

### Mistake

```py
def cook():
    bread = Bread()
    bread.bake()

# for multiple food
def cook(food: str):
    if food == 'bread':
        bread = Bread()
        bread.bake()
    elif food == 'cookies':
        cookie = Cookie()
        cookie.bake()

cook('bread')
```

### Solution

```py
from abc import ABC, abstractmethod


class Bakable(ABC):
    @abstractmethod
    def bake(self):
        pass


class Bread(Bakable):
    def bake(self):
        print('Smells like bread')


class Cookies(Bakable):
    def bake(self):
        print('Cookie smell all over the place')


def cook(bakable: Bakable):
    bakable.bake()


cookies = Cookies()
bread = Bread()
cook(cookies)
cook(bread)
```
