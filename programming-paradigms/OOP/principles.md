## Inheritance

Inheritance is a way of creating a derived/child class using details of an existing/base/parent class without modifying it. Functions of the parent class are extended to the child class.

```py
class Bird:
    def __init__(self, name):
        self.name = name


class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name)
```

## Encapsulation

Encapsulation refers to hiding the internal state of the object from the outside i.e. making them private. This puts restrictions on accessing variables and properties directly, and prevents accidental modification of data. An object's variable can only be changed by an object's method. Hides data at implementation level.

Encapsulation is simply combining data and behavior into one package and hiding the implementation details from the users of the object.

The key to making encapsulation work is to have methods never directly access instance fields in a class other than their own. **Programs should interact with object data only through the object's methods**.

```py
# python does not have a concept of private attributes
# by convention, can define a private attribute by prefixing it with _

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0
```

## Polymorphism

An ability in OOP to use a common interface for multiple forms i.e. having the same function name but different signatures. Can be implemented with Inheritance.

```py
class Bird:
  def intro(self):
    print("There are many types of birds.")

  def flight(self):
    print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")


class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
```

## Abstraction

Process of handling complexity by hiding unnecessary information from the user. This enables the user to implement more complex logic on top of the provided abstraction without understanding and even thinking about all the hidden background complexity. Users only interact with the basic implementation of the function. Hides data at design level.
