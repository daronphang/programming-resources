## Type and Class

Classes are objects in Python, and hence, a class also has a type. 

The type of any new-style class is type. Type is a metaclass, of which classes are instances of i.e. type is the metaclass from which all new-style classes are derived.

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

## Custom Metaclasses

When a class is instantianted i.e. Foo(), the following occurs:
1. the __call__() of Foo's parent class (type metaclass) is invoked
2. Foo.__new__() is called to create
3. Foo.__init__() is called to instantiate 

If Foo does not define __new__() and __init__(), the default methods are inherited from type metaclass. If defined, they override, which allows for customized behavior when instantiating Foo.

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