## Transformation (filter, map, flatMap)

A stream transformation produces a stream whose elements are derived from those of another stream.

```java
// takes a predicate i.e. T -> boolean
Stream<String> words = words.stream().filter(w -> w.length() > 12);
Stream<String> words = words.stream().map(String::toLowerCase);
```

### Extracting Substreams

Can use limit() or skip().

```java
Stream<Double> randoms = Stream.generate(Math::random).limit(100);
Stream<String> words = Stream.of(contents.split("\\PL+")).skip(1);
```

### Concatenating Streams

Can use concat(). First stream should not be infinite.

```java
public static Stream<String> letters(String s) {
    List<String> result = new ArrayList<>();
    for (int i = 0; i < s.length(); i++) {
        result.add(s.substring(i, i + 1));
    }
    return result.stream();
}

Stream<String> combined = Stream.concat(
    letters("hello"),
    letters("world")
);
// yields ["H", "e", "l", "l', "o", ... "l", "d"]
```

### Others

Include distinct(), sorted() and peek(). With peek(), it yields another stream with the same elements as the original, but a function is invoked every time an element is retrieved.

```java
Stream<String> uniqueWords = Stream.of("hello", "world", "hello").distinct();
Stream<String> longestFirst = words
    .stream()
    .sorted(Comparator.comparing(String::length))
    .reversed();
Object[] powers = Stream
    .iterate(1.0, p -> p * 2)
    .peek(e -> System.out.println("Fetching " + e))
    .limit(20)
    .toArray();
```
