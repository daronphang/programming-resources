## Rest Template

There is alot of boilerplate that goes into interacting with a REST resource, suhc as working with low-level HTTP libraries, creating a client instance and request object, executing the request, intepreting the response, mapping the response to domain objects, and handle any exceptions that may be thrown along the way.

To avoid such boilerplate code, Spring provides Rest Template, a straightforward, synchronous REST client. However, if the API you are consuming includes hyperlinks in its response, you should use Traverson instead.

### Methods

RestTemplate defines 12 unique operations, each of which is overloaded to provide a total of 41 methods.

| Method            | Description                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| delete()          | Performs an HTTP DELETE request on a resource at a specified URL                                                              |
| exchange()        | Executes a specified HTTP method against a URL, returning a ResponseEntity containing an object mapped from the response body |
| execute()         | Executes a specified HTTP method against a URL, returning an object mapped from the response body                             |
| getForEntity()    | Sends an HTTP GET request, returning a ResponseEntity containing an object mapped from the response body                      |
| getForObject()    | Sends an HTTP GET request, returning an object mapped from a response body                                                    |
| headForHeaders()  | Sends an HTTP HEAD request, returning the HTTP headers for the specified resource URL                                         |
| optionsForAllow() | Sends an HTTP OPTIONS request, returning the Allow header for the specified URL                                               |
| patchForObject()  | Sends an HTTP PATCH request, returning the resulting object mapped from the response body                                     |
| postForEntity()   | POSTs data to a URL, returning a ResponseEntity containing an object mapped from the response body                            |
| postForLocation() | POSTs data to a URL, returning the URL of the newly created resource                                                          |
| postForObject()   | POSTs data to a URL, returning an object mapped from the response body                                                        |
| put()             | PUTs resource data to the specified URL                                                                                       |

### Usage

Can either create an instance or declare it as a bean to be injected.

```java
RestTemplate rest = new RestTemplate();

@Bean
public RestTemplate restTemplate() {
    return new RestTemplate();
}
```

Variable parameters are assigned to the placeholders in the order that they are given. You can also use a Map to specify the URL variables.

```java
public Ingredient getIngredientById(String ingredientId) {
    return rest.getForObject(
        "http://localhost:8080/ingredients/{id}",
        Ingredient.class,   // response to be bound to
        ingredientId    // variable parameter
    );
}

public Ingredient getIngredientById(String ingredientId) {
    Map<String,String> urlVariables = new HashMap<>();
    urlVariables.put("id", ingredientId);
    return rest.getForObject(
        "http://localhost:8080/ingredients/{id}",
        Ingredient.class,
        urlVariables
    );
}
```
