## Spring Bean

A bean is an object that the Spring container instantiates, assembles and manages.

As best practice, we should only define beans for service layer objects, data access objects, presentation objects, and infrastructureo objects (HibernateSessionFactories, JMS Queues). We shouldn't configure fine-grained objects in the container.

### Configuration

The @Bean annotation on a method indicates that the method creates a Spring Bean. A class annotated with @Configuration indicates that it contains Spring Bean configurations.

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
}
```
