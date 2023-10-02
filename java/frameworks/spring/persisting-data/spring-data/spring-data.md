## Spring Data

Spring Data's mission is to provide a familiar and consistent programming model for data access while still retaining the special traits of the underlying data store. Regardless of database engine or platform, its goal is to make developer's access to data as simple and powerful as possible.

A few of the most popular Spring Data projects include:

- Spring Data JPA (JPA persistence against a relational database)
- Spring Data MongoDB (document)
- Spring Data Neo4j (graph)
- Spring Data Redis
- Spring Data Cassandra
- Spring Data REST
- Spring Data HATEOS

One of the most useful features provided by Spring Data for all those projects is the ability to automatically create repositories, based on a repository specification interface.

## Spring Data REST

A member of the Spring Data family that automatically creates REST APIs for repositories created by Spring Data. You get an API with operations for each repository interface you have defined.

Spring Data REST builds on top of Spring Data repositories, analyzes your application's domain model and expoes HATEOS resources for aggregates contained in the model.

```
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-rest</artifactId>
</dependency>
```

### Custom Links

By declaring a resource processor bean, you can add links to the list of links that Spring Data REST automatically includes. Spring Data HATEOAS offers ResourceProcessor, an interface for manipulating resources before they are returned through the API.

```java
@Bean
public ResourceProcessor<PagedResources<Resource<Taco>>>
tacoProcessor(EntityLinks links) {
    return new ResourceProcessor<PagedResources<Resource<Taco>>>() {
        @Override
        public PagedResources<Resource<Taco>> process(PagedResources<Resource<Taco>> resource) {
            resource.add(
            links.linkFor(Taco.class)
            .slash("recent")
            .withRel("recents"));
            return resource;
        }
    };
}
```
