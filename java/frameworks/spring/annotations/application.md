## @Configuration, @Bean

The annotation designates a class as a configuration class that will provide beans to the Spring application context.

The **class methods are annotated with @Bean**, indicating that the objects they return should be added as beans in the application context. A bean is an object that the Spring container instantiates, assembles and manages.

As best practice, we should only define beans for service layer objects, data access objects, presentation objects, and infrastructure objects (HibernateSessionFactories, JMS Queues). We shouldn't configure fine-grained objects in the container.

```java
@Configuration
public class AccountConfig {
    @Bean
    public AccountService accountService() {
        return new AccountService(accountRepository());
    }

    @Bean
    public AccountRepository accountRepository() {
        return new AccountRepository();
    }

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource dataSource = new DriverManagerDataSource();

        dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        dataSource.setUsername("mysqluser");
        dataSource.setPassword("mysqlpass");
        dataSource.setUrl(
        "jdbc:mysql://localhost:3306/myDb?createDatabaseIfNotExist=true");

        return dataSource;
    }
}
```

## @Component, @ComponentScan

The component is a class-level annotation that allows Spring to detect our custom beans automatically. **Its primary purpose is to identify the class as a component for component scanning**. This means that Spring will:

- Scan our application for classes annotated with @Component
- Instantiate them and inject any specified dependencies into them
- Inject them wherever needed

However, the component must be able to be detected by @ComponentScan, else it will not do anything i.e. outside of source. Nonetheless, most developers prefer to use more specialized stereotype annotations such as @Controller, @Service, and @Repository.

The @ComponentScan annnotation is used by Spring to gather the Components into its application context. When you have @SpringBootApplication class at the root of your project, Spring will scan every @Component defined by default.

However, if you need to scan outside sources, or if the root of the project is not Spring application, we can configure @ComponentScan explicitly to look in whatever package we specify, as long as it exists on the classpath.

```java
package com.baeldung.component.scannedscope;

@Component
public class ScannedScopeExample {}
```

```java
package com.baeldung.component.inscope;

@SpringBootApplication
@ComponentScan({
    "com.baeldung.component.inscope",
    "com.baeldung.component.scannedscope"
})
public class ComponentApplication {
    //public static void main(String[] args) {...}
}
```

## @EnableAutoConfiguration

The one line configuration that enables the magic of Spring Boot autoconfiguration.

## @SpringBootApplication

The annotation combines three other annotations: @Configuration, @ComponentScan, @EnableAutoConfiguration.

## @Value

The annotation is the most straightforward approach to ingesting configuration settings into your code. It is built around pattern-matching and the Spring Expression Language (SpEL).

```env
greeting-name=Dakota
greeting-coffee=${greeting-name} is drinking coffee
```

```java
@RestController
@RequestMapping("/greeting")
class GreetingController {
    @Value("${greeting-name: Mirage}") // allows for default value
    private String name;

    @GetMapping
    String getGreeting(){
        return name;
    }
}
```

## @ConfigurationProperties

Using this annotation, a developer can define properties, group related properties, and reference/use the in a tool-verifiable and typesafe way. In order to register a class to manage configuration properties, you need to add @ConfigurationProperties annotation and specify the prefix.

To instruct the application to process @ConfigurationProperties classes and add their properties to the app's environment, you need to add the @ConfigurationPropertiesScan annotation to the main app.

```java
@ConfigurationProperties(prefix = "greeting")
class Greeting {
    private String name;
    private String coffee;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCoffee() {
        return coffee;
    }
    public void setCoffee(String coffee) {
        this.coffee = coffee;
    }
}
```

```java
@SpringBootApplication
@ConfigurationPropertiesScan
public class SburRestDemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(SburRestDemoApplication.class, args);
    }
}
```

## @Autowired

Usually we provide bean configuration details in the Spring bean configuration file, and we specify the beans that will be injected into other beans using **ref attribute**. Nonetheless, Spring provides autowiring features where we **don't need to specify bean injection details explicitly**.

The annotation allows Spring to resolve and inject collaborating beans into the bean i.e. autowire relationships between collaborating beans. **We can use autowiring on properties/variables, setters and constructors**.

```java
@Component("fooFormatter")
public class FooFormatter {
    public String format() {
        return "foo";
    }
}

@Component
public class FooService {
    // FooFormatter bean is injected into the service
    @Autowired
    private FooFormatter fooFormatter;
}
```

## @PostConstruct, @Predestroy

Spring calls the methods only once, just after the initialization of bean properties or before it removes the bean from the application context. The methods can have any access level, but it can't be static.

One possible use is populating a database, and closing a db connection.

```java
@Component
public class DbInit {

    @Autowired
    private UserRepository userRepository;

    @PostConstruct
    private void postConstruct() {
        User admin = new User("admin", "admin password");
        User normalUser = new User("user", "user password");
        userRepository.save(admin, normalUser);
    }

    @PreDestroy
    public void preDestroy() {
        dbConnection.close();
    }
}
```
