## Wildcards

Wildcards distinguish between the safe accessor methods and unsafe mutator methods. This is the key behind bounded wildcards. As the compiler only knows it needs some subtype but doesn't know which type, it refuses to pass any specific type. The sole exception is passing in null.

```java
? extends Employee getFirst() // safe
// impossible to call setFirst()
void setFirst(? extends Employee) // unsafe
```

## Bounded Wildcards

### Extends (Upper Bound)

In a wildcard type, a type parameter is allowed to vary.

```java
public static void printBuddies(Pair<? extends Employee> p) {
    Employee first = p.getFirst();
    Employee second = p.getSecond();
    System.out.println(first.getName() + " and " + second.getName() + " are buddies.");
}
```

### Supertype (Lower Bound)

You can specify a supertype bound. Intuitively speaking, wildcards with supertype bounds let you write to a generic object, while wildcards with subtype bounds let you read from a generic object.

A wildcard with a supertype bound gives you a behavior that is opposite to that of above. Another common use for supertype bounds is an argument type of a functional interface.

```java
void setFirst(? super Manager) {}
? super Manager getFirst()
```

```java
default boolean removeIf(Predicate<? super E> filter) {}

// you want to be able to pass a Predicate<Object>,
// not just Predicate<Employee>
ArrayList<Employee> staff = . . .;
Predicate<Object> oddHashCode = obj -> obj.hashCode() %2 != 0;
staff.removeIf(oddHashCode);
```

## Unbounded Wildcards

```java
public static boolean hasNulls(Pair<?> p) {
    return p.getFirst() == null || p.getSecond() == null;
}
```

## Wildcards vs Type Parameters

- A wildcard is not a type variable and you cannot write code that uses wildcard as a type
- If you have only one parameterized type argument, you can use wildcard
- Type parameters support multiple bounds, wildcards don't
- Wildcards support both upper and lower bounds (super, extends), type parameters just support upper bounds

```java
? t = p.getFirst(); // Error
T t = p.getFirst(); // okay
```
