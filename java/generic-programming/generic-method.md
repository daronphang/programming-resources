## Generic Method

You can define generic methods both inside ordinary classes and generic classes.

```java
class ArrayAlg {
    public static <T> T getMiddle(T... a) {
        return a[a.length / 2];
    }
}

String middle = ArrayAlg.<String>getMiddle("John", "Q.", "Public");
```
