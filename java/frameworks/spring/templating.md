## Template Engines

Template engines provide a way for server-side applications to generate final pages that will be displayed and executed in the user's browser. These view technologies differ in approaches but generally provide the following:

- A template language and/or collection of tags that define inputs used by the template engine to produce the expected outcome
- A view resolver that determines the view/template to use to fulfill a requested resource

Spring Boot supports view technologies including ThymeLeaf, JSP, FreeMarker, Groovy Markup, and Mustache. **ThymeLeaf** is the most widely used and provides excellent support for both Spring MVC and Spring WebFlux applications.

```
FreeMarker                  spring-boot-starter-freemarker
Groovy                      spring-boot-starter-groovy-templates
JavaServer Pages (JSP)      Provided by Tomcat/Jetty
Mustache                    spring-boot-starter-mustache
ThymeLeaf                   spring-boot-starter-thymeleaf
```

### Caching

By default, templates are parsed only once, and the results of that parse are cached for subsequent use. This is a great feature for production, as it prevents redundant template parsing on each request and improves performance.

For development purposes, you can disable caching.

```
spring.freemarker.cache=false
spring.groovy.template.cache=false
spring.mustache.cache=false
spring.thymeleaf.cache=false
```
