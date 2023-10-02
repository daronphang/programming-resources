## Exceptions Handling

An exception object is always an instance of a class derived from Throwable. Hierarchy as follows:

- Throwable as root
- Error and Exception as branches
- Under Exception, splits into IOException and Runtime Exception

The error hierarchy describes internal errors and resource exhaustion situations inside the Java runtime system. You should not throw an object of this type. Instead, focus on the Exception hierarchy.

For exception hierarchy, the general rule is that a Runtime Exception occurs because you made a programming error (i.e. a bad cast, out-of-bounds array access, null pointer access) that should not have been allowed in the first place. Any other exception occurs because of a bad thing (i.e. I/O error).

### Advertising Thrown Exceptions

When you write your own methods, you don't have to advertise every possible throwable object that your method might actually throw. An exception is thrown in any of the following situations:

- You call a method that throws a checked exception
- You detect an error and throw a checked exception with the throw statement
- you make a programming error (unchecked exception)
- An internal error occurs in the VM or runtime library (unchecked exception)

If either of the first two scenarios occurs, you must tell programmers who will use your method about the possibility of an exception which is a potential death trap. **If no handler catches the exception, the current thread of execution terminates**.

You do not need to advertise Java errors as they are beyond your control i.e. inheriting from Error. Similarly, you should not advertise unchecked exceptions inheriting from Runtime Exception as they are completely under your control i.e. ArrayIndexOutOfBoundsException.

In summary, **a method must declare all the checked exceptions it might throw**. If it fails to faithfully declare all checked exceptions, the compiler will issue an error message.

### Superclass Methods

If you override a method from a superclass, the checked exceptions that the subclass method declares cannot be more general than those of the superclass method. If the superclass method throws no checked exception, neither can the subclass.
