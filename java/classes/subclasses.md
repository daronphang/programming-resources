## Subclasses

For inheritance, use the extends keyword for create subclasses from an existing class (also called superclass, base class, or parent class). Subclasses have more functionality than their superclasses.

```java
public class Manager extends Employee {
    private double bonus;

    public Manager(String name, double salary, int year, int month, int day) {
        super(name, salary, year, month, day);
        bonus = 0;
    }

    public void setBonus(double bonus) {
        this.bonus = bonus;
    }
    }
```

### Overriding Methods

Only the superclass has access to its own private fields, and not the subclass. To access those private fields, need to use the public interface i.e. getters.

When overriding a method, the subclass method must be at least as visible as the superclass method i.e. if superclass method is declared public, sublcass must also be declared public.

```java
public double getSalary() {
    double baseSalary = super.getSalary();
    return baseSalary + bonus;
}
```

### Multiple Inheritance

Java does not support multiple inheritance. For ways to recover much of the functionality of multiple inheritance, need to use interfaces.

## Abstract Classes

Classes with one or more abstract methods must itself be declared abstract. It can also have fields and concrete methods. Abstract classes cannot be instantiated.

```java
public abstract class Person {
    public abstract String getDescription();
    // no implementation required
}
```

```java
public class Student extends Person {
    private String major;

    public Student(String name, String major) {
        super(name);
        this.major = major;
    }

    public String getDescription() {
        return "a student majoring in " + major;
    }
}
```

## Object Superclass

The Object class is the ultimate ancestor: every class in Java extends Object. It is useful as a generic holder for arbitrary values.

```java
Object obj = new Employee('john', 35000);
Employee e = (Employee) obj;
```

### override

To explicitly declare a method as override, can define with @override. If you make a mistake and the method does not override any methods from superclass, the compiler will throw an error.

```java
@Override public boolean equals(Object other) {}
```

### equals

To guard against the possibility that class attributes are null, use the Objects.equals method.

If the implicit and explicit parameters don't belong to the same class i.e. inheritance, but you still want to test for equality, you can use instanceof. However, this has been an area of controversy, and leaves open the possibility that otherObject can belong to a subclass.

Java specification requires that the equals method has the following properties:

1. Reflexive: for any non-null reference, x.equals(x) should return true
2. Symmetric: for any references x and y, x.equals(y) should return true if and only y.equals(x) returns true
3. Transitive: for any references x,y,z, if x.equals(y) and y.equals(z), then x.equals(z) should return true
4. Consistent: if the objects to x and y refer haven't changed, repeated calls x.equals(y) should return the same value
5. For any non-null reference, x.equals(null) should return false

```java
public class Employee {

    // make sure to cast otherObject as Object and not Employee
    // common mistake that will define another method and not override
    // Object.equals method
    public boolean equals(Object otherObject) {
        // a quick test to see if the objects are identical i.e. identity by pointer
        if (this == otherObject) return true;

        // must return false if the explicit parameter is null
        if (otherObject == null) return false;

        // testing for inheritance subclass
        if (!otherObject instanceof Employee) return false;

        // if the classes don't match, they can't be equal
        if (getClass() != otherObject.getClass()) return false;

        // now we know otherObject is a non-null Employee
        Employee other = (Employee) otherObject;

        // test whether the fields have identical values
        return Objects.equals(name, other.name)
            && salary == other.salary
            && Objects.equals(hireDay, other.hireDay);
    }
}
```
