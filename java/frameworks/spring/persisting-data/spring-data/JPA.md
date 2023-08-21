## Spring Data JPA

### Adding Dependency

Spring Boot configures Hibernate as the default JPA provider.

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

### Annotating Domain

To declare class as a JPA entity, it needs to be annotated with @Entity. JPA also requires that entities have a noarguments constructor.

However, when using @Data from Lombok, it implictly adds a required arguments constructor but it gets removed by @NoArgsConstructor. An explicit @RequiredArgsConstructor ensures that you still have a required arguments constructor.

```java
package tacos;
import javax.persistence.Entity;
import javax.persistence.Id;
import lombok.AccessLevel;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.RequiredArgsConstructor;

@Data
@RequiredArgsConstructor
@NoArgsConstructor(access=AccessLevel.PRIVATE, force=true)
@Entity
public class Ingredient {
    @Id
    private final String id;
    private final String name;
    private final Type type;

    public static enum Type {
        WRAP, PROTEIN, VEGGIES, CHEESE, SAUCE
    }
}
```

```java
package tacos;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.OneToMany;
import javax.persistence.PrePersist;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import lombok.Data;

@Data
@Entity
public class Taco {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Long id;

    @NotNull
    @Size(min=5, message="Name must be at least 5 characters long")
    private String name;

    private Date createdAt;

    @ManyToMany(targetEntity=Ingredient.class)
    @Size(min=1, message="You must choose at least 1 ingredient")
    private List<Ingredient> ingredients;

    @PrePersist
    void createdAt() {
        this.createdAt = new Date();
    }
}
```

### Repository

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

#### Customizing JPA Repositories

When generating the repository implementation, Spring Data examines any methods in the repository interface, parses the method name, and attempts to understand the method's purpose in the context of the persisted object. In essence, **Spring Data defines a sort of miniature domain-specific language (DSL) where persistence details are expressed in the repository method signatures**.

Repository methods are composed of:

- A verb
- An optional subject (class would be parameterized by subject already)
- The word By
- A predicate (true/false)

Spring data method signatures include:

- IsAfter, After, IsGreaterThan, GreaterThan
- IsGreaterThanEqual, GreaterThanEqual
- IsBefore, Before, IsLessThan, LessThan
- IsLessThanEqual, LessThanEqual
- IsBetween, Between
- IsNull, Null
- IsNotNull, NotNull
- IsIn, In
- IsNotIn, NotIn
- IsStartingWith, StartingWith, StartsWith
- IsEndingWith, EndingWith, EndsWith
- IsContaining, Containing, Contains
- IsLike, Like
- IsNotLike, NotLike
- IsTrue, True
- IsFalse, False
- Is, Equals
- IsNot, Not
- IgnoringCase, IgnoresCase

```java
List<Order> findByDeliveryZip(String deliveryZip);
List<Order> readOrdersByDeliveryZipAndPlacedAtBetween(
    String deliveryZip,
    Date startDate,
    Date endDate
);
```
