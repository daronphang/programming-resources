## Translation of Generics in VM

- There are no generics in VM, only ordinary classes and methods
- All type parameters are replaced by their bounds
- Bridge methods are synthesized to preserve polymorphism
- Casts are inserted as necessary to preserve type safety

## Type Erasure

Whenever you define a generic type, a corresponding raw type is automatically provided. The name of the raw type is simply the name of the generic type, with the type parameters removed.

The raw type replaces type variables with the first bound, or Object if no bounds
are given.

```java
// Since T is an unbounded type variable, it is simply replaced by Object.
public class Pair {
    private Object first;
    private Object second;
    public Pair(Object first, Object second) {
        this.first = first;
        this.second = second;
    }
    public Object getFirst() { return first; }
    public Object getSecond() { return second; }
    public void setFirst(Object newValue) { first = newValue; }
    public void setSecond(Object newValue) { second = newValue; }
}
```

### Beware of Clashes after Erasure

It is illegal to create conditions that cause clashes when generic types are used. The solution is to rename the offending method.

To support translation by erasure, there is another restriction that a class or variable type may not at the same time be a subtype of two interface types which are different parameterizations of the same interface.

```java
// conceptually, it has two equals()
// boolean equals(String)
// boolean equals(Object)
// clashes with Object.equals()
public class Pair<T> {
    public boolean equals(T value) {
        return first.equals(value) && second.equals(value);
    }
...
}
```

```java
// Manager implements Comparable<Employee> and Comparable<Manager>
// different parameterizations of the same interface
class Employee implements Comparable<Employee> { . . . }
class Manager extends Employee implements Comparable<Manager>
{ . . . } // Error
```

## Restrictions

Most of the restrictions are a consequence of type erasure.

### Type parameters cannot be instantiated with primitive types

You cannot substitute a primitive type for a type parameter. Afte erasure, the generic class has fields of type Object, and you can't use them to store primitive values.

### Runtime type inquiry only works with raw types

Objects in the virtual machine always have a specific nongeneric type. Therefore,
all type inquiries yield only the raw type.

```java
if (a instanceof Pair<String>) // Error
```

### You cannot create arrays of parameterized types

An array remembers its component type and throws an ArrayStoreException if you
try to store an element of the wrong type. However, erasure renders this mechanism ineffective for generic types.

```java
Pair<String>[] table = new Pair<String>[10]; // Error
```

### Type variables are not valid in static contexts

You cannot reference type variables in static fields or methods.

### You cannot throw or catch instances of a generic class

it is not legal for a generic class to extend Throwable.

### You can defeat checked exception checking

A bedrock principle of Java exception handling is that you must provide a handler
for all checked exceptions. You can use the following to defeat this scheme by tricking the compiler into believing that it is not a checked exception i.e. unchecked:

- Generic classes
- Erasure
- @SuprressWarnings annotation

```java
public abstract class Block {
    public abstract void body() throws Exception;
    public Thread toThread() {
        return new Thread() {
            public void run() {
                try {
                    body();
                }
                catch (Throwable t) {
                    // turns all exceptions into those that the compiler
                    // believes to be unchecked
                    Block.<RuntimeException>throwAs(t);
                }
            }
        };
    }

    @SuppressWarnings("unchecked")
    public static <T extends Throwable> void throwAs(Throwable e) throws T {
        throw (T) e;
    }
}
```

```java
// program runs a thread that will throw a checked exception
// however, the Thread object's run() does not mind checked exceptions
// as it turns into unchecked
public class Test {
    public static void main(String[] args) {
        new Block() {
            public void body() throws Exception {
                Scanner in = new Scanner(new File("ququx"), "UTF-8");
                while (in.hasNext())
                System.out.println(in.next());
            }
        }
        .toThread().start();
    }
}
```
