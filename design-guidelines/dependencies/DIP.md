## Dependency Inversion Principle (DIP)

**The more detailed something is, the more likely it will change**. If high-level ideas are dependent on it, it will be extremely sensitive to changes which creates a problem. We want to invert dependencies relative to that kind of decomposition.

DIP is about the level of abstraction in the messages sent from your code to the thing it is calling. DIP is about raising the abstraction level of a dependency to be closer to the domain, as limited by the needs of the system i.e. from top-down to bottom-up approach.

In simple terms:

- we should not depend on low-level implementations, but rely on high-level abstractions
- Abstractions should not depend on details, but details should depend on abstractions

### Abstractions

Many people confuse abstraction with:

- An interface
- An abstract base class
- Something given as a constraint e.g. external system architecture
- Something called a requirement, which is stated as a solution

Any of them can be misleading.

In the context of interface and abstract base class, an example would be java.sql.Connection. If the methods make sense to your domain e.g. getAutoCommit(), createStatement(), it might be okay, but not if the methods make sense to a software library. As soon as you given in and **allow clients to see unnecessary methods**, you probably **violate both DIP and Liskov Substitution Principle**. Instead, the abstraction should be at a level that is **appropriate for your domain**.

## Example

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
