## Bulk Operations on Concurrent Hash Maps

Java SE8 provides bulk operations on concurrent hash maps that can safely execute even while other threads operate on the map. They traverse the map and operate on the elements they find as they go along. No effort is made to freeze a snapshot of the map in time.

There are three kinds of operations that operate on keys, values, keys/values and entry objects:

- search: applies a function to each key and/or value, until the function yields a non-null result
- reduce: combines all keys and/or values, using a provided accumulation function
- forEach: applies a function to all keys and/or values

With each of the operation, you need to specify a **parallelism threshold**:

- To run in a single thread, set it to Long.MAX_VALUE
- To run in multiple threads, the map must contain more elements than the threshold
- To run in all threads, set it to 1

```java
U searchKeys(long threshold, BiFunction<? super K, ? extends U> f)
U searchValues(long threshold, BiFunction<? super V, ? extends U> f)
U search(long threshold, BiFunction<? super K, ? super V, ? extends U> f)
U searchEntries(long threshold, BiFunction<Map.Entry<K, V>, ? extends U> f)
```

## Bulk Operations on Concurrent Set Views

There is no ConcurrentHashSet class in collections. Instead, you can use newKeySet() that yields a `Set<K>` that is actually a wrapper around a `ConcurrentHashMap<K, Boolean>`.

```java
Set <String> words = ConcurrentHashMap.<String>newKeySet();
```

## Parallel Array Algorithms

The Arrays class has a number of parallelized operations.

```java
Arrays.parallelSort();
Arrays.parallelSort(words, Comparator.comparing(String::length));
Arrays.parallelSetAll(values, i -> i % 10);
```
