## JPA (Java Persistence API)

JPA is concerned with persistence, which means any mechanism by which Java objects outlive the application process that created them. The JPA specification lets you define which objects should be persisted, and how they are persisted in your Java applications.

JPA is not a tool or framework; instead, it defines a set of concepts that guide implementers. JPA was originally intended for use with relational databases, but it has since evolved and extended for use with NoSQL. A popular framework that supports JPA with NoSQL is **EclipseLink**.

### JPA vs JDBC

JPA lets you avoid the need to think 'relationally'. In JPA, you define your persistence rules in the realm of Java code and objects, whereas JDBC requires you to manually translate from code to relational tables and back again.

### Implementations

Popular JPA implementations include Hibernate and EclipseLink. Every JPA implementation provides some kind of ORM layer.
