## @Controller

Spring MVC was created to separate concerns between data, delivery and presentation, assuming the views would be provided through SSR. The @Controller annotation helps to tie the various pieces together.

The @Controller is a sterotype/alias for the @Component annotation. This means that upon application startup, a Spring Bean is created from that class. A Spring Bean is an object created and managed by the Spring IoC container.

The controller's job is to handle HTTP requests and either hand a request off to a view to render HTML or write data directly to the body of a response.

```java
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

## @ResponseBody

Instructs a Controller class to return a formatted response as JSON by default, or another format if specified.

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

## @ModelAttribute

An annotation that binds a method parameter or method to a named model attribute, and then exposes it to a web view.

In general, Spring MVC will always make a call to that method first, before it calls any request handler methods i.e. **@ModelAttribute methods are invoked before the controller methods annotated with @RequestMapping**. The model has to be created before any processing starts inside the controller methods.

### At Method Level

Annotation is used to define objects which should be part of a Model i.e. equivalent to @Bean and @Before. We can also add values in the Model that will be identified as global. This means for every request, a default value exists for every method in the response.

```java
@ModelAttribute("person")
public Person getPerson(){
    return new Person();
}

@ModelAttribute
public void addAttributes(Model model) {
    model.addAttribute("msg", "Welcome to the Netherlands!");
}
```

### As Method Argument

Indicates the argument should be retrieved from the model i.e. equivalent to @Autowired and @Qualifier. It tries to retrieve a bean with the given name and if not found, instead of throwing an error or returning null, it creates a new instance using the default constructor.

```java
@RequestMapping(value = "/addEmployee", method = RequestMethod.POST)
public String submit(@ModelAttribute("employee") Employee employee) {
    // Code that uses the employee object
    return "employeeView";
}
```

## @SessionAttributes

When developing web applications, we often need to refer to the same attributes in several views i.e. shopping cart contents displayed on multiple pages.

A good location to store those attributes is in the user's session. @sessionAttributes annotation is used to store model attributes in the HTTP Servlet session between requests.

```java
@Controller
@SessionAttributes("pet")
public class EditPetForm {
	// ...
}
```
