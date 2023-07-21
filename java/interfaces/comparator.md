## Comparator Interface

### Static Methods

The interface has a number of static methods for creating comparators. These methods are intended to be used with lambda expressions or method references. You can also chain methods.

```java
// sort by last name, first name
Arrays.sort(people, Comparator.comparing(Person::getLastName)).thenComparing(Person::getFirstName)
```

```java
// specifying name as key to be used in comparing method
Arrays.sort(
    people,
    Comparator.comparing(
        Person::getName,
        (s,t) => Integer.compare(s.length(), t.length()),
    )
)
```
