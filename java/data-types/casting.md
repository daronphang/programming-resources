## Casting

The process of forcing a conversion from one type to another. Allows converting an object reference from one class to another, if its actual type has been temporarily forgotten i.e. assigning a superclass reference to a subclass variable (promising more).

```java
double x = 3.405;
int nx = (int) x;

Manager boss = (Manager) staff[0];
```

## Instance of

If you cast down an inheritance chain but lie about what the object contains, Java will notice the broken promise and generate a ClassCastException.

```java
if (staff[1] instanceof Manager) {
    boss = (Manager) staff[1];
}
```
