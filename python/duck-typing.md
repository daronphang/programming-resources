## Duck Typing

If it walks like a duck, and it quacks like a duck, then it must be a duck.

A term commonly related to dynamically typed programming languages and polymorphism. The idea behind this principle is that the code itself does not care about whether an object is a duck, but instead cares about whether it quacks.

Duck typing refers to the principle of not constraining or binding code to **specific data types**.

```py
class Duck:

    def __init__(self, name):
        self.name = name
    def quack(self):
        print('Quack!')
class Car:

    def __init__(self, model):
        self.model = model

    def quack(self):
        print('I can quack, too!')


def quacks(obj):
    obj.quack()
```
