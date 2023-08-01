## Stream Library

Streams provide a view of data that lets you specify computations at a higher conceptual level than with collections. With a stream, **you specify what you want to have done, not how to do it** i.e. follows "what, not how" principle. You leave the scheduling of operations to the implementation and hence, can be used for **optimization**.

For instance, if you want to compute the average of a certain property, you specify the source of data and property, and the stream library can then optimize the computation by using multiple threads.

### Workflow

You set up a pipeline of operations in three stages:

1. Create a stream
2. Specify intermediate operations for transforming the initial stream into others, possibly in multiple steps
3. Apply a terminal operation to produce a result; this operation forces the execution of the lazy operations that precede it
4. After terminal step, the stream can no longer be used

### Creating

You can turn any collection into a stream with stream(). If you have an array, use the static stream.of().

```java
// Stream.of has varargs parameter
Stream<String> words = Stream.of(contents.split("\\PL+"));
Stream<String> words = Stream.of("hello", "world");
Stream<String> words = Arrays.stream(array, from, to);
Stream<String> silence = Stream.empty(); // empty stream
```

#### Infinite

The Stream interface has two static methods for making infinite streams.

The generate() takes a function with no arguments. Whenever a stream value is needed, that function (`Supplier<T>`) is called to produce a value.

The iterate() is used to produce infinite sequences. It takes a seed value and a function, and repeatedly applies the function (`UnaryOperator<T>`)to the previous result.

```java
Stream<String> echoes = Stream.generate(() -> "Echo");
Stream<Double> randoms = Stream.generate(Math::random);

Stream<BigInteger> integers = Stream.iterate(BigInteger.ZERO, n -> n.add(BigInteger.ONE));
```

### Example

```java
// read file into a string
String contents = new String(
    Files.readAllBytes(Paths.get("hello.txt")),
    StandardCharsets.UTF_8
);
// split into words, nonletters are delimiters
List<String> words = Arrays.asList(contents.split("\\PL+"));

// iterate with collections
long count = 0;
for (String w : words) {
    if (w.length() > 12) count++;
}

// with streams
long count = words.stream()
    .filter(w -> w.length() > 12)
    .count();
```

### Parallel

```java
long count = words.parallelStream()
    .filter(w -> w.length() > 12)
    .count();
```

## Streams vs Collections

1. A stream does not store its elements; they may be stored in an underlying collection or generated on demand
2. Stream operations don't mutate their source
3. Stream operations are lazy when possible i.e. filtering first 5 matches
