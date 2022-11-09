## Object Oriented Programming (OOP)

Programming paradigm that relies on concept of classes and objects, structuring reusuable pieces of code blueprints (classes) which are used to create individual instances of objects. A means of structuring programs so that properties and behaviors are bundled into individual objects. Classes can share methods and attributes. An object has two characteristics: attributes (fields) and behavior (methods).

A purely OOP language has everything inside the program as objects i.e. it doesn't support primitive data types. The seven qualities to be satisfied for an OOP language are:

1. Abstraction
2. Polymorphism
3. Encapsulation
4. Inheritance
5. All predefined types must be objects
6. All user-defined types must be objects
7. Every operation on objects must be done with the help of methods

### Class

A class is a blueprint for the object and is used to construct instances. An object's class defines how the object is implemented by defining its internal state and the implementation of its operations. In contrast, an object's type refers to its interface.

### Object

An object is an instantiation of a class.

### Methods

Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

### Interfaces

Every operation declared by an object specifies the operation's name, the objects it takes as parameters, and the operation's return value; this is known as the operation's signature. The set of all signatures defined by an object's operations is called the interface. An object's interface characterizes the complete set of requests that can be sent to the object. A type is a name used to denote an interface. An object may have many types, and many objects can share a type.

Objects are known only through their interfaces; there is no way to know anything about an object or to ask it to do anything without going through its interface. Different objects are free to implement requests differently i.e. two objects can have different implementations of identitcal interfaces.

Run-time association of a request to an object and one of its operations is known as **dynamic binding** i.e. issuing a request doesn't commit to a particular implementation until run-time. Also allows to substitute objects that have identical interfaces for each other at run-time; substitutability is known as **polymorphism**. It lets a client object make few assumptions about other objects beyond supporting a particular interface.

### Specifying Object Implementations

Objects are created by instantiating a class. Object created is an instance of the class. New classes can be defined by existing classes using **inheritance**.

An abstract class is one whose main purpose is to define a common interface for its subclasses. An abstract class cannot be instantiated. Classes that aren't abstract are **concrete classes**.

A **mixin** class is a class that's intended to provide an optional interface or functionality to other classes. Similar to abstract class whereby it is not intended to be instantiated. Mixin classes require multiple inheritance i.e. existing class, mixin class, and augmented class (consisting of methods from both existing and mixin).

### Programming to an Interface, not an Implementation

Should manipulate objects solely in terms of interface defined by abstract classes as it reduces implementation dependencies between subsystems. Don't declare variables to be instances of a particular concrete class but instead, commit to an interface defined by an abstract class.
