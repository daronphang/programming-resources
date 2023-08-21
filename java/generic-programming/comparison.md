## Wildcards vs Type Parameters

There are certain places where wildcards and type parameters do the same thing.

When deciding if you need a type variable, ask yourself if that type variable is used to relate two or more parameters, or to relate a parameter type with the return type. If the answer is no, then a wildcard should suffice.

Type parameter is more strict than wildcards. If you need to enforce type safety, use type parameters.

### Variable declaration

You cannot use wildcards as types when declaring parameters.

```java
? t = p.getFirst(); // Error
T t = p.getFirst(); // okay
```

### Method parameters

We can't use wildcards directly to specify the type of a parameter in a method. However, we can use wildcards as part of a generic code enclosed on angle brackets.

```java
public static <T> void print(T item) {
    System.out.println(item);
}

public static <T extends Number> void copy(List<T> dest, List<T> src);
public static <T> void copy(List<T> dest, List<? extends T> src); // avoid
```

### Bounded and unbounded types

Whenever we have an **unbounded generic type, we should prefer using wildcards over type parameters**. This is because wildcards make code simpler and more flexible.

If a type parameter appears only once in the method declaration, we should consider replacing it with a wildcard.

```java
public static <E> void swap(List<E> list, int src, int des);
public static void swap(List<?> list, int src, int des);    // preferred
```

We can't use type parameters with the lower bound (super); however, they can have multiple bounds, while wildcards can't.

### Return types

When a generic method returns a generic type, we should use a type parameter instead of a wildcard. This is because clients are forced to deal with the types themselves.

```java
public static List<E> merge(
    List<? extends E> listOne,
    List<? extends E> listTwo
) {
    return Stream.concat(
        listOne.stream(),
        listTwo.stream()
    ).collect(Collectors.toList());
}
```
