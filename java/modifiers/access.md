## public

Any method in any class can call the method. Although you can use the public keyword with your instance fields, it would allow any part of the program to read and modify the instance fields, **completely ruining encapsulation**.

## private

Methods that can access the instance fields are the methods of the class itself. No outside method can read or write to these fields.

## protected

When you want to restrict a method to subclasses only i.e. allow subclass methods to access a superclass field.

# Non-Access Modifiers
