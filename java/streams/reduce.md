## Reductions

Reductions are terminal operations i.e. reduce the stream to a non-stream value that can be used in your program. It take a binary function and keeps applying it, starting with the first two elements.

You can also supply an identity/starting value; if the stream is empty, the identity will be returned. Hence, you do not have to deal with the Optional class.

```java
List<Integer> values = . . .;
Optional<Integer> sum = values.stream().reduce((x, y) -> x + y);
Optional<Integer> sum = values.stream().reduce(Integer::sum);
Integer sum = values.stream().reduce(0, (x, y) -> x + y)
```

For simple reductions i.e. min, max, the methods return an `Optional<T>` value that either wraps the answer or indicates that there is none. Previously, null was returned, but that can lead to null pointer exceptions when it happens in an incompletely tested program.

```java
Optional<String> largest = words.max(String::comapreToIgnoreCase);
System.out.println("largest: " + largest.orElse(""));
```

| Method                                            | Description                      |
| ------------------------------------------------- | -------------------------------- |
| Optional<T> max(Comparator<? super T> comparator) |                                  |
| Optional<T> min(Comparator<? super T> comparator) |                                  |
| Optional<T> findFirst()                           |                                  |
| Optional<T> findAny()                             | Useful for parallelizing streams |
| boolean anyMatch(Predicate<? super T> predicate)  |                                  |
| boolean allMatch(Predicate<? super T> predicate)  |                                  |
| boolean noneMatch(Predicate<? super T> predicate) |                                  |

### Accumulating

The simple form of reduce function requires `(T,T) -> T`, with the same types for the arguments and result. If you want to perform more complex operations, you can supply an accumulator function.

You need to supply the second function as the computations are parallelized, and you need to combine their results.

In practice, this method won't be used as often as it is easier to map and use simple reduce methods.

```java
int result = words.reduce(
    0,
    (total, word) -> total + word.length(),
    (total1, total2) -> total1 + total2
);

// simpler
words.mapToInt(String::length).sum();
```

## Optional Type

The type is intended as a safer alternative for a reference that refers to an object or is null.

If you don't use Optional values correctly, you don't get any benefit over the "something or null" approach of the past.

```java
Optional<T> optionalValue = . . .;
optionalValue.get().someMethod();

// no safer than this
T value = . . .;
value.someMethod();
```

```java
if (optionalValue.isPresent()) optionalValue.get().someMethod();
// no easier than
if (value != null) value.someMethod();
```

| Method                                                                       | Description                                                                 |
| ---------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| T orElse(T other)                                                            | Yields the value of this Optional, or other if empty                        |
| T orElseGet(Supplier<? extends T> other)                                     | Yields the value of this Optional, or the result of invoking other if empty |
| <X extends Throwable> T orElseThrow(Supplier<? extends X> exceptionSupplier) |                                                                             |
| void ifPresent(Consumer<? super T> consumer)                                 |                                                                             |
| <U> Optional<U> map(Function<? super T, ? extends U> wrapper)                |                                                                             |
| T get()                                                                      | Yields the value, else throws NoSuchElementException if empty               |

### Creating

```java
Optional<Integer> v = Optional.of(1 / x);
```
