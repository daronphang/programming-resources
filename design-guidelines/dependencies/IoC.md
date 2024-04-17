## Inversion of Control (IoC)

IoC is a programming design principle that inverts the flow of control in an application. Instead of having main() instantiating objects and calling methods, IoC can remove the responsibilities from main() by performing the instantiation, method calls and triggering user actions.

IoC is about who initiates the call. Does your code call into a framework, or does it plug something into a framework, and then the framework calls back?

IoC is used by containers/systems/libraries/frameworks that allow them to regain some control from the application and invoking the appropriate methods when needed i.e. **don't call us, we will call you**.

IoC is simply providing a callback (reaction) to an event that might happen in a system. Instead of executing some logic directly, we invert the control to that callback whenever a specific event occurs. This pattern allows us to **separate what we want to do from when we want to do it** with each part knowing as little as possible about the other.

IoC offers us the ability to **separate the concern** of writing the code to take action from the concern of declaring when to take that action. This comes in handy when we are developing a complex system and we want to keep it clean and maintainable.

## Example

### Frameworks

```java
@SpringBootApplication
public class MyApplication {
   public static void main(String[] args) {
      SpringApplication.run(MyApplication.class, args);
  }
}

@GetMapping("/hello")
public void createPost() {
    // handle request
}
```

### Message handling

Messaging systems are a good example of IoC. We invert the control of fetching the messages to the messaging system and ask it to handle the message.

```java
@KafkaListener(topics = "myTopic", groupId = "myGroup")
public void consumeMessage(String message) {
   System.out.println("Received Message in myGroup : " + message);
}
```
