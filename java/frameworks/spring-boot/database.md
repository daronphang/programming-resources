## Spring Data

Spring Data's mission is to provide a familiar and consistent programming model for data access while still retaining the special traits of the underlying data store. Regardless of database engine or platform, its goal is to make developer's access to data as simple and powerful as possible.

## Repository

Configuring and establishing a database connection in the Java ecosystem is a cumbersome affair, with lots of repetitive ceremony. To resolve this, Spring Data introduces the concept of repositories.

A repository is an interface as a useful abstraction above various databases. The repository itself is a mere placeholder for the following types:

- The object stored in the database
- The object's unique ID/primary key field

The preferred practice of writing code is to use the highest level interface. Between **JpaRepository and CrudRepository**, while the former extends a handful of interfaces and incorporates a broader functionality, the latter covers all of the key CRUD capabilities.

```java
// first arg is the object type, second is the unique ID
interface CoffeeRepository extends CrudRepository<Coffee, String> {}

@RestController
@RequestMapping("/coffees")
class RestApiDemoController {
    private final CoffeeRepository coffeeRepository;
    public RestApiDemoController() {
        this.coffeeRepository.saveAll(List.of(
        new Coffee("Café Cereza"),
        new Coffee("Café Ganador"),
        new Coffee("Café Lareño"),
        new Coffee("Café Três Pontas")
        ));
    }

    @GetMapping
    Iterable<Coffee> getCoffees() {
        return coffeeRepository.findAll();
    }

    @GetMapping("/{id}")
    Optional<Coffee> getCoffeeById(@PathVariable String id) {
        return coffeeRepository.findById(id);
    }

    @PostMapping
    Coffee postCoffee(@RequestBody Coffee coffee) {
        return coffeeRepository.save(coffee);
    }
}
```
