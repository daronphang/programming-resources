## @Entity, @Id

The annotation is from javax.persistence that indicates the class is a persistable entity, while the id annotation is to mark the field as tha database table's ID field.

## @Component

The component is a class-level annotation that allows Spring to detect our custom beans automatically. This means that Spring will:

- Scan our application for classes annotated with @Component
- Instantiate them and inject any specified dependencies into them
- Inject them wherever needed

However, the component must be able to be detected by @ComponentScan, else it will not do anything i.e. outside of source. Nonetheless, most developers prefer to use more specialized stereotype annotations such as @Controller, @Service, and @Repository.

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
