## Classes

Considered as a blueprint of objects. An object is an instance of a class. Constructor function **init**() is called whenever a new object of that class is instantiated.

## Attributes

### Get Attributes

```py
hasattr(class_name, 'attr')   # true/false
getattr(class_name, 'attr')   # returns value, else None
```

### Self Attributes

```py
self.__class__  # Get class of current instance
self.__class__.__base__ #Get parent class
self.__class__.__name__
self.__dict__  # Get instance attributes and values in dict format
```

### Class vs instance attribute

An instance attribute is a Python variable belonging to one object. Variable is only accessible in scope of object and defined inside constructor.

Class attribute belongs to class rather than an instance of an object. Shared between all objects of class and defined outside of constructor. Useful for storing constants Class-wide or defining default values.

```py
class ExampleClass(object):
  class_attr = 0

  def __init__(self, instance_attr):
    self.instance_attr = instance_attr
```

## Comparing classes

```py
class Test:
    foo = 'hello'
    bar = 'world'

    def __eq__(self, other):
        if not isinstance(other, Test):
            return NotImplemented
        return self.foo == other.foo and self.bar == other.bar
```

## Super

Primary use case is to extend the functionality of the inherited method.

Returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class through inheritance. Python super() allows us to refer the superclass implicitly.

```py
super().__init__()  # python 3

class Person(object):
    super(Person, self).__init__() # python 2, calls its parent class __init__
```

```python
class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')

class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')

d1 = Dog()
# dog has four legs
# dog is a warm-blooded animal
```

### MRO (Method Resolution Order)

For multiple inheritance, when classes have the same method name, **Method Resolution Order (MRO)** algorithm comes into play which decides where Python will look for a given method, and which method will be called when there's a conflict.

First, the current class is searched. If not found, the search moves to parent classes. This is left-to-right, depth-first.

```py
class First:
    def __init__(self):
        print('first')

class Second:
    def __init__(self):
        print('second')

class Third(Second,First):
    def __init__(self):
        # MRO looks for __init__ in Second(), then First()
        # if found, it will only be called once
        super().__init__()
        print('third')

print(Third())
# second
# third
```

```py
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)
'''
Initializing: class C
Initializing: class B
Initializing: class A
Printing from class C: 1
Printing from class B: 2
Printing from class A: 3
'''
```

## Abstract classes

A class is an Abstract class if it contains one or more abstract methods (declared but no implementation). A subclass that doesn't implement the abstract methods will throw an error.

```py
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def feed(self, action):
        pass

    def concrete_method(self):
        # some logic
        return 'hello world!'
```

## Getters and setters

Pythonic way to use getters and setters in OOP. Without property, all programs that make use of class have to be refactored if properties of class change i.e. making attributes private/public.

```py
# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)
```

```py
# Can use getter, setter and deleter

class House:
	def __init__(self, price):
		self._price = price

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, new_price):
		if new_price > 0 and isinstance(new_price, float):
			self._price = new_price
		else:
			print("Please enter a valid price")

	@price.deleter
	def price(self):
		del self._price
```
