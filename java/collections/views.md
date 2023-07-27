## Views

By using views, you can obtain other objects that implement the Collection or Map interfaces i.e. it returns an object of a class that implements the desired interface and whose methods manipulate the original collection.


### Lightweight Wrappers

The returned object is not an ArrayList, but a view object with get() and set() that access the underlying array. All methods that change the size of the array (add, remove) would throw an UnsupportedOperationException.

```java
Card[] cardDeck = new Card[52];
List<Card> cardList = Arrays.asList(cardDeck);
```

### Subranges

You can use the sublist method to obtain a view into the subrange of the list.

```java
List<Employee> group2 = staff.subList(10,20);
```

### Unmodifiable Views

The Collections class has methods that produce unmodifiable views of collections. These views add a runtime check to an existing collection. If an attempt to modify the collection is detected, an exception is thrown and the collection remains untouched.

Each method is designed to work with an interface.

```
Collections.unmodifiableCollection
Collections.unmodifiableList
Collections.unmodifiableSet
Collections.unmodifiableSortedSet
Collections.unmodifiableNavigableSet
Collections.unmodifiableMap
Collections.unmodifiableSortedMap
Collections.unmodifiableNavigableMap
```

```java
List<String> staff = new LinkedList<>();
lookAt(Collections.unmodifiableList(staff));
```

### Synchronized Views

If you access a collection from multiple threads, you need to ensure that the collection is not accidentally damaged. Instead of implementing thread-safe collection classes, the library designers used the view mechanism to make regular collections thread safe.

```java
Map<String, Employee> map = Collections.synchronizedMap(new HashMap<String, Employee>());
```

### Checked Views

Checked views are intended as debugging support for a problem that can occur with generic types. 

However, the checked views are limited by the runtime checks that the VM can carry out. If you have a generic class, the VM will convert it into a single raw class i.e. `Pair<String>` cannot be protected from `Pair<Date>`.

```java
ArrayList<String> strings = new ArrayList<>();
ArrayList rawList = strings; // warning only for compatibility with legacy code
rawList.add(new Date());
```
```java
List<String> safeStrings = Collections.checkedList(strings, String.class);
ArrayList rawList = safeStrings;
rawList.add(new Date()) // checked list throws a ClassCastException
```

