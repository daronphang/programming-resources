## Cloneable Interface

The clone method is a protected method of Object. If the fields in the original and shallow clone are immutable, then sharing is safe. However, if subojects are mutable, you must redefine the clone method to make a deep copy that clones the subobjects as well. **The default implementation of clone is shallow copy**.

If you choose to use clone method, the class must:

- Implement the Cloneable interface
- Redefine the clone method with the public access modifier

```java
// shallow copy
class Employee implements Cloneable {
    public Employee clone() throws CloneNotSupportedException {
        return (Employee) super.clone();
    }
}
```

```java
// deep copy
class Employee implements Cloneable {
    public Employee clone() throws CloneNotSupportedException {
        Employee cloned = (Employee) super.clone();
        // clone mutable fields
        cloned.hireDay = (Date) this.hireDay.clone();
        return cloned;
    }
}
```
