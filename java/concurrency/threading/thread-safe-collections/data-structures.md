## Thread-Safe collections

The java.util.concurrent package supplies efficient implementations for maps, sorted sets, and queues. These collections use sophisticated algorithms that minimize contention by allowing concurrent access to different parts of the data structure.

The collections return **weakly consistent iterators**. That means that the iterators may or may not reflect all modifications that are made after they were constructed. In constrast, an iterator of a collection will throw a ConcurrentModificaitonException when the collection has been modified after construction.

```
ConcurrentHashMap()
ConcurrentSkipListMap()
ConcurrentSkipListSet()
ConcurrentLinkedQueue()
```

### Atomic Update of Map Entries

If there is a sequence of operations on a hashmap, the results may be unpredictable as the sequence is not atomic.

**You cannot have null values in a ConcurrentHashMap**.

```java
Long oldValue = map.get(word);
Long newValue = oldValue == null ? 1 : oldValue + 1;
map.put(word, newValue);    // might not replace oldValue
```

#### replace

Replaces an old value with a new one, provided that no other thread has come before and replaced the old value with something else.

```java
do {
    Long oldValue = map.get(word);
    Long newValue = oldValue == null ? 1 : oldValue + 1;
} while (!map.replace(word, oldValue, newValue));
```

#### putIfAbsent (Java SE8)

```java
map.putIfAbsent(word, new LongAdder());
map.get(word).increment();

// short form
map.putIfAbsent(word, new LongAdder()).increment();
```

#### compute (Java SE8)

If the function returns null, the existing entry is removed from the map.

```java
map.compute(word, (k,v) -> v == null ? 1 : v + 1);
map.computeIfAbsent(word, k -> new LongAdder()).increment();
```

#### merge

The merge() has a parameter for the initial value that is used when the key is not present. Otherwise, the function you supplied is called. If the function returns null, the existing entry is removed from the map.

```java
map.merge(word, 1L, (existingValue, newValue) -> existingValue + newValue);
map.merge(word, 1L, Long::sum);
```

### Bulk Operations on Concurrent Hash Maps

Java SE8 provides bulk operations on concurrent hash maps that can safely execute even while other threads operate on the map. They traverse the map and operate on the elements they find as they go along. No effort is made to freeze a snapshot of the map in time.

There are three kinds of operations:

- search: applies a function to each key and/or value, until the function yields a non-null result
- reduce: combines all keys and/or values, using a provided accumulation function
- forEach: applies a function to all keys and/or values
