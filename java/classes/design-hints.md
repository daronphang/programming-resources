## Class Design Hints

1. Always keep data private
2. Always initialize data
3. Separate related members into another class i.e. Customer, Address
4. Not all fields need individual accessors and mutators
5. Break up classes that have too many responsibilities
6. Make the name of your classes and methods reflect their responsibilities
7. Prefer immutable classes i.e. instead of mutating objects, methods return new objects with the modified state

The problem with mutation is that it can happen concurrently when multiple threads try to update an object at the same time. The results are unpredictable. When classes are immutable, it is safe to share their objects among multiple threads. Nonetheless, not all classes should be immutable i.e. depends on their implementation and usage.

## Inheritance Design Hints

1. Place common operations and fields in the superclass
2. Don't use protected fields as the subclasses are unbounded and anyone can form a subclass of your classes and directly access protected instances; instead, use them to indicate methods that are not ready for general use and should be redefined
3. Use inheritance to model the 'is-a' relationship
4. Don't use inheritance unless all inherited methods make sense
5. Don't change the expected behavior when you override a method
6. Use polymorphism, not type information
7. Don't overuse reflection as it can be fragile
