## Interfaces

An interface is a way of describing what classes should do, without specifying how they should do it. A class can implement one or more interfaces. An interface is not a class but a set of requirements for the class that wants to conform to the interface.

The reason for interfaces is that Java is strongly typed. When making a method call, the compiler needs to be able to check that the method actually exists.

Although interfaces can be introduced as an abstract class, a major problem is that a class can only extend a single class as Java does not support multiple inheritance. **With interfaces, a class can implement as many interfaces as it likes**.

All methods of an interface are automatically public. Interfaces can define constants, but never have instance fields. Supplying instance fields and methods that operate on them is the job of the classes that implement the interface.

```java
// the sort method of Arrays class promises to sort under a condition
// that the object belongs to classes that implement the Comparable interface
public interface Comparable {
    int compareTo(Object other);
}

class ArrayList implements Comparable {
    public int compareTo(Object, otherObject) {
        // x < y returns -1, x == y returns 0, x > y returns 1
        if (((Comparable) a[i]).compareTo(a[j]) > 0) {
            // rearrange a[i] and a[j]
            ...
        }
    }
}
```

```java
class Employee implements Comparable {
    public int compareTo(Object otherObject) {
        Employee other = (Employee) otherObject;
        return Double.compare(this.salary, other.salary);
    }
}

Employee[] staff = new Employee[3];
staff[0] = new Employee("Harry Hacker", 35000);
staff[1] = new Employee("Carl Cracker", 75000);
staff[2] = new Employee("Tony Tester", 38000);
Arrays.sort(staff);
```

### Properties

- You cannot use new operator to instantiate an interface
- You can declare interface variables
- An interface variable must refer to an object of a class that implements the interface
- You can use instanceof to check whether an object implements an interface
- You can extend interfaces
- Constant fields are always public static final

```java
Comparable x;

x = new Employee();

if (x instanceof Comparable) {
    // do something
}

public interface Powered extends Movable {
    double SPEED_LIMIT = 95; // a public static final constant
}
```

### Static Methods

As of Java SE8, you are allowed to add static methods.

```java
public interface Path {
    public static Path get(String first, String... more) {
        return FileSystems.getDefault().getPath(first, more);
    }
    ...
}
```

### Default Methods

You can supply a default implementation for any interface method.

An important use for default methods is interface evolution. If you add a new method to the interface, the class that extends it can no longer compile as it does not implement the new method. Making the method as default solves this problem.

```java
public interface Comparable<T> {
    default int compareTo(T other) { return 0; }
    // By default, all elements are the same
}
```

### Resolving Default Method Conflicts

If the same method is defined as default in one interface and again in the superclass, superclasses by default will win and override the method.

If two interfaces clash with the same methods, you must resolve the conflict as Java compiler will throw an error by overriding that method in the class.

```java
interface Person {
    default String getName() { return ""; }
}

interface Named {
    default String getName() { return "Hello"; }
}

class Student implements Person, Named {
    public String getName() {return "hello world"; }
}
```
