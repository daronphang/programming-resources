## Metaclass

Classes are objects in Python. This object is itself capable of creating objects (instances). Hence, you can assign it to a variable, attach attributes, or pass it as a function parameter.

A Metaclass is the class of a class. A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves. **A class is an instance of a metaclass**.

### type

The type of any class is type. **Type is a metaclass**, of which classes are instances of i.e. type is the metaclass from which all classes are derived.

```py
class Foo:
    pass

x = Foo()
print(x)    # class '__main__.Foo'
print(Foo)  # class 'type'

# x is an instance of type Foo
# Foo is an instance of type metaclass
# type is also an instance of type metaclass, so it is an instance of itself

print(type(int))    # class 'type'
print(type(float))  # class 'type'
print(type(dict))   # class 'type'
print(type(type))   # class 'type'
```

### Why would you use metaclasses?

Metaclasses are deeper magic that 99% of users should never worry about it. If you wonder whether you need them, you don't (the people who actually need them know with certainty that they need them, and don't need an explanation about why).

A metaclass is most commonly used as a class-factory. When you create an object by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass. Combined with the normal **init** and **new** methods, metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry or replace the class with something else entirely.

## Custom metaclasses

When a class is instantiated i.e. Foo(), the following occurs:

1. the **call**() of Foo's parent class (type metaclass) is invoked
2. Foo.**new**() is called to create
3. Foo.**init**() is called to instantiate

If Foo does not define **new**() and **init**(), the default methods are inherited from type metaclass. If defined, they override, which allows for customized behavior when instantiating Foo.

```py
class Foo:
    def __new__(cls):
        x = object.__new__(cls)
        x.attr = 100
        return x

f = Foo()
print(f.attr)   # 100

g = Foo()
print(g.attr)   # 100
```

Can create custom metaclasses that inherit from type.

```py
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dict)
        x.attr = 100
        return x


class Foo(metaclass=Meta):
    pass

print(Foo.attr) # 100
```

### Singleton

```py
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
```

```py
import threading


class Singleton(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance
```
