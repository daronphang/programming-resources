## Stereotypes Annotations

Stereotype annotations are a set of specialized annotations that are used to indicate the role or purpose of a particular component within the application. When declared with a stereotype annotation, you declare that the class should be automatically discovered by Spring component scanning and instantiated as a bean in the Spring application context.

Spring defines a handful of stereotype annotations:

- @Component
- @Controller
- @Repository
- @Service

### @Component

The most general-purpose annotation and is used to mark any class as a component that can be managed by the Spring framework. It is often used as a catch-all for classes that don't it into any other stereotype.

### @Service

Used to mark a class as a service component, which typically performs business logic or other logic-related tasks within the application.

### @Repository

Component that is responsible for managing the persistence of data within the application i.e. dealing with CRUD operations. It is used with DAO (Data Access Object) or Repository implementations that deal with database tables.

### @Controller

Component that is responsible for handling incoming requests and returning appropriate responses.
