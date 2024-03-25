## Assertions

Two forms for assertions:

- assert condition
- assert condition : expression

```java
assert x >= 0;
assert x >= 0 : x;
```

### When to Use Assertions

Points for using assertions:

- Assertion failures are intended to be fatal, unrecoverable errors
- Assertion checks are turned on only during development and testing

#### Method Contracts

If the method contract states the a parameter cannot be of a particular value i.e. null, using assertions would be appropriate. This kind of contract is called a **precondition**.

#### Documenting Assumptions

You can also use assertions for documenting assumptions.

```java
public enum Size { SMALL, MEDIUM, LARGE };

public void someFn(Size s) {
    if (s == Size.SMALL) {

    } else if (s == Size.MEDIUM) {

    } else {
        assert s == Size.LARGE;
    }
}
```

### Enabling/Disabling

Assertions are disabled by default.

```sh
$ java -enableassertions MyApp
```
