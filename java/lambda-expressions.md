## Lambda Expressions

A lambda expression is a block of code that you can pass around so it can be executed later, once or multiple times i.e. deferred execution. There are many reasons for this:

- Running the code in a separate thread
- Running the code multiple times
- Running the code at the right point in an algorithm
- Running the code when something happens i.e. callback
- Running the code only when necessary

To accept a lambda, we need to pick a functional interface that is scoped to your use case.

| Functional Inteface | Parameter Types | Return Type  | Abstract Method Name | Description                                      |
| ------------------- | --------------- | ------------ | -------------------- | ------------------------------------------------ |
| Runnable            | none            | void         | run                  | Runs an action without arguments or return value |
| Supplier<T>         | none            | T            | get                  | Supplies a value of type T                       |
| Consumer<T>         | T               | void         | accept               | Consumes a value of type T                       |
| BiConsumer<T,U>     | T,U             | void         | accept               | Consumes values of types T and U                 |
| Function<T,R>       | T               | R            | apply                | A function with argument of type T               |
| BiFunction<T,U,R)   | T,U             | R            | apply                | A function with arguments of type T and U        |
| UnaryOperator<T>    | T               | T            | apply                |                                                  |
| BinaryOperator<T>   | T,T             | T            | apply                |                                                  |
| Predicate<T>        | T               | boolean      | test                 | A boolean-valued function                        |
| BiPredicate<T,U>    | T,U             | boolean test | test                 | A boolean-valued function with two arguments     |

```java
// Runs an action without arguments or return value
public static void repeat(int n, Runnable action) {
    for (int i = 0; i < n; i++>) {
        action.run();
    }
}
// runs an action with integer as an argument and without return value
public static void repeat(int n, IntConsumer action) {
    for (int i = 0; i < n; i++>) {
        action.accept(i);
    }
}
```

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

### Closures

Lambda expressions form closures. They can access variables from an enclosing method or class. However, **you can only reference variables whose value doesn't change (final variable)** as mutating variables in lambda expressions is not safe when multiple actions are executed concurrently. You also cannot reference variables that are mutated in the enclosing scope.

```java
public static voide countDown(int start, int delay) {
    ActionListener listener = event -> {
        start--;    // this is illegal
        System.out.println(start);
    }
    new Timer(delay, listener).start();
}
```
