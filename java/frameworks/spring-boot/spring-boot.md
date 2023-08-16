## Spring Boot

Spring Boot is an extension of the Spring framework, which eliminates boilerplate configurations required for setting up a Spring application. It takes an **opinionated view of the Spring platform**, which paves the way for a faster and more efficient development ecosystem.

Spring boot aims to simplify to the maximum extend possible; the patterns of code and process that developers do over and over again. Once patterns are identified, Boot springs into action to initialize the required beans automatically, with sensible default configurations.

The three core features of Spring Boot upon which everything else builds are simplified dependency management, simplified deployment, and autoconfiguration.

## Simplified Dependency Management

In providing a RESTful API, we might expect to see a collection of dependencies that includes code to supply responses in a particular format, including JSON, XML, marshalling/unmarshalling, listening for requests and returning responses, decoding complex URIs, etc.

For versioning, it might lead to diamond dependencies whereby a library has conflicting requirements with another.

### Spring Boot Starters

Spring Boot starters are Bills of Materials (BOMs) built around the proven premise that the vast majority of times you provide a particular capability, and you do it nearly the same way, every time.

When building an API, we expose endpoints, listen for requests, process requests, deserialize objects, exchange information in standard formats, etc. The design/development/usage pattern don't vary much; it is adopted industry-wise, with few variations. Like other similar patterns, they are captured in a Spring Boot starter.

Adding a single starter, i.e. spring-boot-starter-web, provides all of those related functionalities in a **single appliation dependency**. All dependencies encompassed by it are **version-synchronized** too.

In rare cases when you must incorporate functionality provided by a different version, you can simply override the tested version.

The versions of starter dependencies themselves are determined by the version of Spring Boot you are using. Nonetheless, rest assured that all the dependencies pulled are compatible with each other as they have been tested.

```
// gradle
dependencies {
    compile "org.springframework.boot:spring-boot-starter-web"
    compile "org.springframework.boot:spring-boot-starter-thymeleaf"
    compile "org.springframework.boot:spring-boot-starter-data-jpa"
    compile("org.springframework.boot:spring-boot-starter-security")
    compile "com.h2database:h2"
    testCompile("org.springframework.boot:spring-boot-starter-test")
}
```

```bash
$ gradle dependencies
$ mvn dependency:tree
```

## Executable JARs for Simplified Deployment

Deployment of Java applications were a complex affair. For instance, for deploying a web application, you need to install database drivers, create connection pool, build and test your application, etc. **You need to verify that all dependencies are deployed independently**. Spring Boot collapsed much of the cumbersome deployment process into **one step**.

Rather than teasing out every file from the application JAR and all dependent JARs, then combining them into a single destination JAR (sharding), the designers of Spring Boot approached things from a novel perspective, by nesting JARs.

Nesting JARs instead of sharding them alleviates many potential problems:

- No conflicts arising when different dependencies require the same dependency but different versions
- Removes legal issues due to repackaging software and combining it with others using a different license

The Spring Boot plugin ensures that all JARs are zipped into the output JAR.

```bash
$ java -jar <Application.jar>
$ Application.jar   # file is also executable
```

## Autoconfiguration (Convention over Configuration)

Spring Boot gives you productivity by bringing opinions to widely used and repeated cases i.e. focsuses on 'developer-first' environment configuration. When it comes to writing code to complete a particular task, activities that are repeated are ripe for streamlining.

For instance, when assessing a database, we need to open a connection pool and close it when the application completes. These steps can be streamlined automatically by following a simple and expected convention.

Another instance would be when connecting to a messaging platform like RabbitMQ or Kafka, we need to specify certain settings i.e. hostname, credentials, ports, etc. Defaults are then specified if none are provided i.e. localhost, default port, etc. **This makes sense as an opinion as it is nearly 100% consistent for development environments**.

Moreover, if you need to provide your own configuration, the autoconfiguration can be selectively overriden, or disabled entirely.
