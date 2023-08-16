## @ResponseBody

Instructs a Controller class to return a formatted response as JSON by default, or another format if specified.

## @Controller

Spring MVC was created to separate concerns between data, delivery and presentation, assuming the views would be provided through SSR. The @Controller annotation helps to tie the various pieces together.

The @Controller is a sterotype/alias for the @Component annotation, meaning that upon application startup, a Spring Bean is created from that class. A Spring Bean is an object created and managed by the Spring IoC container.

## @RestController

The @RestController annotation is a convenience notation that combines @Controller with @ResponseBody into a single annotation.

```java
@RestController
class RestApiDemoController {
    private List<Coffee> coffees = new ArrayList<>();
}
```

## @RequestMapping

To map a function to a request. Spring Boot performs marshalling/demarshalling (JSON by default) automatically. There are also specialized convenience annotations for streamlining:

- @GetMapping
- @PostMapping
- @PutMapping
- @PatchMapping
- @DeleteMapping

```java
@PostMapping("/coffees")
Coffee postCoffee(@RequestBody Coffee coffee) {
    coffees.add(coffee);
    return coffee;
}
```

### Query Parameters

```java
@GetMapping("/coffees/{id}")
Optional<Coffee> getCoffeeById(@PathVariable String id) {
    for (Coffee c: coffees) {
        if (c.getId().equals(id)) {
            return Optional.of(c);
    }
    }
    return Optional.empty();
}

@PutMapping("/coffees/{id}")
Coffee putCoffee(@PathVariable String id, @RequestBody Coffee coffee) {
    int coffeeIndex = -1;
    for (Coffee c: coffees) {
        if (c.getId().equals(id)) {
            coffeeIndex = coffees.indexOf(c);
            coffees.set(coffeeIndex, coffee);
        }
    }
    return (coffeeIndex == -1) ? postCoffee(coffee) : coffee;
}
```

### Reducing Reptition

You can elevate the portion fo the URI mapping that is common to all methods of a class to the class-level annotation.

```java
@RestController
@RequestMapping("/coffees")
class RestApiDemoController {
    private List<Coffee> coffees = new ArrayList<>();
    public RestApiDemoController() {
        coffees.addAll(List.of(
        new Coffee("Café Cereza"),
        new Coffee("Café Ganador"),
        new Coffee("Café Lareño"),
        new Coffee("Café Três Pontas")
        ));
    }
    @GetMapping
    Iterable<Coffee> getCoffees() {
        return coffees;
    }

    @GetMapping("/{id}")
    Optional<Coffee> getCoffeeById(@PathVariable String id) {
        for (Coffee c: coffees) {
            if (c.getId().equals(id)) {
                return Optional.of(c);
            }
        }
        return Optional.empty();
    }
}
```
