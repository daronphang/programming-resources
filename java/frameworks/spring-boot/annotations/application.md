## @Configuration

The annotation designates a class as a configuration class using Spring's Java-based configuration.

```java
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
```

## @ComponentScan

Spring uses this annotation to gather the Components into its application context. When you have @SpringBootApplication class at the root of your project, Spring will scan every @Component defined by default.

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
