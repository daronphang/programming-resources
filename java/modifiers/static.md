## static

The static keyword is mainly used for memory management. If you define a field as static, there is only one such field per class i.e. class attribute and not instance attribute. All objects of the class will share that field.

If static has been omitted, the variable would then be an instance field and requires an object of that class to access the field.

The static keyword is applicable to blocks, variables, methods and classes.

```java
public class Math {
    public static final double PI = 3.1415;
}
```

Use static methods in the following situations:

- When a method does not need to access the object state
- When a method only needs to access static fields of the class
- When using static factory methods to construct objects i.e. LocalDate.now, LocalDate.of
