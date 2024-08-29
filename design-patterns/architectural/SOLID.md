## SOLID

A set of five design principles to help developers design robust, testable, extensible and maintainable object-oriented software systems.

## Single Responsibility Principle (SRP)

SRP states that a class, module or function should have only reason to change i.e. it should only have one responsibility.

Separating responsibilities is important because **each responsibility is an axis of change (only if the changes occur)**. When requirements change, that change will be manifested through a change in responsibility.

## Open-Closed Principle (OCP)

OCP states that classes, modules, and functions should be open for extension but closed for modification. It means you should be able to extend the functionality of a class without modifying the existing code and avoiding potential new bugs. The key to this is using **abstractions**.

```py
class Square:
    def __init__(self):
        self.width = 5

    def area():
        return self.width * self.width


def calculate_area(shapes):
    ans = 0
    for shape in shapes:
        ans += shape.area()
    return ans
```

## Liskov Substitution Principle (LSP)

LSP states that child classes or subclasses must be substitutable for their parent classes or super classes. In other words, the child class must be able to replace the parent class.

## Interface Segregation Principle (ISP)

ISP states that clients should not be forced to implement interfaces or methods they do not use. Developers should break down large interfaces into smaller, more specific ones, so that clients only need to depend on interfaces that are relevant to them. Classes that have “fat” interfaces are classes whose interfaces are not cohesive.

The ISP acknowledges that there are objects that require noncohesive interfaces; however, it suggests that clients should not know about them as a single class. Instead, clients should know about abstract base classes that have cohesive interfaces.

When clients are forced to depend on methods that they don’t use, then those clients are subject to changes to those methods. This results in an inadvertent coupling between all the clients.

## Dependency Inversion Principle (DIP)

DIP states that high-level modules should not depend on low-level modules. Instead, they should depend on abstractions. Additionally, abstractions should not depend on details, but details should depend on abstractions.

Instead of writing code that relies on specific details of how lower-level code works, you should write code that depends on more general abstractions that can be implemented in different ways. The lower-level modules provide the implementation for interfaces that are declared within, and called by, the upper-level modules.
