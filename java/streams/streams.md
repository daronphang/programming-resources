## Stream Library

Streams provide a view of data that lets you specify computations at a higher conceptual level than with collections. With a stream, **you specify what you want to have done, not how to do it** i.e. follows "what, not how" principle. You leave the scheduling of operations to the implementation and hence, can be used for **optimization**.

For instance, if you want to compute the average of a certain property, you specify the source of data and property, and the stream library can then optimize the computation by using multiple threads.

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

It is important that **you don't modify the collection that is backing a stream while carrying out a stream operation** (even if the modification is threadsafe). This is because streams don't collect their data i.e. their data is always in a separate collection. If you were to modify that collection, the outcome of the stream operations would be undefined. This requirement is known as **noninterference**. Nonetheless, since stream operations are lazy, it is possible to mutate up to the point when the terminal operation executes, but it is not recommended.

```java
// works but not recommended
List<String> wordList = . . .;
Stream<String> words = wordList.stream();
wordList.add("END");
long n = words.distinct().count();
```

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

### Primitive Types

```
IntStream
LongStream
DoubleStream
```

```java
IntStream stream = IntStream.of(1, 1, 2, 3, 5);
stream = Arrays.stream(values, from, to); // values is an int[] array
```

### Parallel Streams

Streams make it easy to parallelize bulk operations. When stream operations run in parallel, the intent is that the same result is returned as if they had run serially. For parallel streams to work well:

- **Operations can be executed in an arbitrary order**
- Data should be in memory and it would be inefficient to wait for the data to arrive
- Stream operations should not block
- Stream operations should do a substantial amount of work; else, it does not make sense to pay for the cost of setting up the parallel computation

```java
long count = words.parallelStream()
    .filter(w -> w.length() > 12)
    .count();

Map<Integer, Long> shortWordCounts = words
    .parallelStream()
    .filter(s -> s.length() < 10)
    .collect(groupingBy(String::length, counting())
);
```

By default, streams that arise from ordered collections (arrays, lists), or from calling Stream.sorted, are ordered. Results are accumulated in the order of the original elements, and are entirely predictable.

Some operations can be more effectively parallelized when the ordering requirement is dropped, by calling unordered() on a stream.

```java
Stream<String> sample = words.parallelStream().unordered().limit(n);
```

## Streams vs Collections

1. A stream does not store its elements; they may be stored in an underlying collection or generated on demand
2. Stream operations don't mutate their source
3. Stream operations are lazy when possible i.e. filtering first 5 matches
