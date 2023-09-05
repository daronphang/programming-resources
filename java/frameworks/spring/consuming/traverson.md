## Traverson

A hyperlink-aware, synchronous REST client provided by Spring HATEOAS.

### Usage

```java
Traverson traverson = new Traverson(
    URI.create("http://localhost:8080/api"),
    MediaTypes.HAL_JSON
);
```
