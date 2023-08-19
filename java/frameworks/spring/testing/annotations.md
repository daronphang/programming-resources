## @WebMvcTest

This is a special test annotation provided by Spring Boot that arranges for the test to run in the context of a Spring MVC application i.e. registers the controller in Spring MVC so that you can throw requests against it.

It also sets up Spring support for testing Spring MVC. Although it could be made to start a server, mocking the mechanics of Spring MVC is sufficient.
