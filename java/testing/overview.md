## Writing Tests

```java
@Test
@DisplayName("First number is less than the second")
public void compare2() {
    Basics basicTests = new Basics();
    int value = basicTests.compare(2, 3);
    Assertions.assertEquals(-1, value);
}
```
