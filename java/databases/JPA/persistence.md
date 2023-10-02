## Data Persistence

When you use JPA, you create a map from the datastore to your application's data model objects. If you are using relational database, much of the actual connection between application code and database will be handled by JDBC.

As a specification, JPA provides metadata annotations, which you use to define the mapping between objects and the database.

```java
Musician georgeHarrison = new Musician(0, "George Harrison");
musicianManager.save(georgeHarrison);
```
