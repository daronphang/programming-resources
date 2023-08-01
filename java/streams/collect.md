## Collecting Results

When you are done with a stream, you will often want to look at its elements.

### Iterating

```java
stream.forEach(System.out::println);
stream.forEachOrdered(); // process them in stream order, used for parallel streams
```

### Parsing as Array

The toArray() returns an Object[] array. If you want an array of the correct type, pass the object type in the array constructor.

```java
String[] result = stream.toArray(String[]::new);
```

### Parsing to Collections

For collecting stream elements to another target, there is a convenient collect() that takes an instance of the Collector interface.

```java
List<String> result = stream.collect(Collectors.toList());
Set<String> result = stream.collect(Collectors.toSet());
TreeSet<String> result = stream.collect(Collectors.toCollection(TreeSet::new));
String result = stream.collect(Collectors.joining(", "));
```

```java
Stream<Person> persons = ...;
Map<Integer, String> idToName = people
    .collect(Collectors.toMap(Person::getId, Person::getName));
```
