## Type Parameters

Generics offer a better solution: type parameters. This makes your code easier to read. Also, no cast is required as the compiler knows the return type is String, not Object.

It is common practice to use uppercase letters for type variables (one letter), and to keep them short. When instantiating, we need to provide a concrete type.

```java
ArrayList<String> files = new ArrayList<String>();
String filename = files.get(0);
```

### Bounds for Type Variables

If you want to place a restriction on type variables, you can restrict T to a class that implements that particular interface.

The extends keyword is used rather than implements. This is because it is a reasonable approximation of the subtype concept.

```java
class ArrayAlg {
    public static <T extends Comparable> T min(T[] a) {
        if (a == null || a.length == 0) return null;
        T smallest = a[0];
        for (int i = 1; i < a.length; i++)
        if (smallest.compareTo(a[i]) > 0) smallest = a[i];
        return smallest;
    }
}
```

A type variable or wildcard can have multiple bounds.

```
T extends Comparable & Serializable
```
