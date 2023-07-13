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
