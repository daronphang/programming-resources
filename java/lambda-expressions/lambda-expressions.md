## Lambda Expressions

A lambda expression is a block of code that you can pass around so it can be executed later, once or multiple times.

### Passing Objects

Taking sorting with a custom comparator as an example: if you want to sort strings differently by length instead of the default dictionary order, you can pass a Comparator object to the sort method.

```java
class LengthComparator implements Comparator<String> {
    public int compare(String first, String second) {
        return first.length() - second.length();
    }
}

Arrays.sort(strings, new LengthComparator());
```

### Expression

You never specify the type of a lambda expression as the type is always inferred from context.

```java
(String first, String second) -> {
    if (first.length() < second.length()) return -1;
    else if (first.length() > second.length()) return 1;
    else return 0;
}
```

### Functional Interfaces

You can supply a lambda expression whenever an object of an interface with a single abstract method is expected. Such an interface is called a functional interface.

```java
Arrays.sort(
    words,
    (first, second) -> first.length() - second.length()
);
```

### Method References

Equivalent of a lambda expression. The :: operator separates the method name from the name of an object or class.

```
object::instanceMethod
Class::staticMethod
Class::instanceMethod
```

```java
Timer t = new Timer(1000, event -> System.out.println(event));
Timer t = new Timer(1000, System.out::println);
```

### Constructor References

Constructor references are like method references, except that the name of the method is new.

Array constructor references are useful to overcome a limitation of Java. It is not possible to construct an array of a generic type T. Instead, pass in a constructor reference to the method.

```java
ArrayList<String> names = ...;
Stream<Person> stream = names.stream().map(Person::new);
List<Person> people = stream.collect(Collectors.toList());
```
