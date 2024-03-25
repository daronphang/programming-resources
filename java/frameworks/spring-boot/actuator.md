## Actuator

Actuator brings production-ready features to our application. **Monitoring of application, gathering metrics, understanding traffic, or the state of database becomes trivial with this dependency**. It is mainly used to expose operational information about the running application. It uses HTTP endpoints or JMX beans to enable us to interact with it.

With the Actuator, you can inspect the inner workings of your application including:

- What beans have been configured in the Spring application context
- What decisions were made by Spring Boot's autoconfiguration
- What env variables, system properties, configuration properties, and command-line arguments are available to your application
- Current state of threads in and supporting your application
- Trace of recent HTTP requests handled by your application
- Various metrics pertaining to memory usage, garbage collection, web requests, and data source usage

### Getting Started

To enable Spring Boot Actuator, we need to add it to the package manager i.e. Maven, Gradle.

```xml
<dependencies>
    ... (other dependencies omitted for brevity)
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

### Endpoints

Actuator comes with most endpoints disabled by default. They are also placed under the /actuator path. We can also curl /actuator that acts as a discovery endpoint and returns hypermedia i.e. links for exposed endpoints.

The Actuator can be configured via application.properties.

```properties
management.endpoints.web.exposure.include=*
management.endpoints.web.base-path
management.endpoint.health.show-details=always
```

```
/auditevents
/beans
/conditions
/configprops
/env
/flyway
/health
/heapdump
/info
/liquibase
/logfile
/loggers
/metrics
/prometheus
/scheduledtasks
/sessions
/shutdown
/threaddump
```

### Logging

Actuator allows developers to set a typical logging level for most or all components, and **change that level temporarily when a critical issue arises** in live, production Spring Boot applications. This can be done by sending a POST request with JSON value for configured level.

```sh
$ echo '{"configuredLevel": "TRACE"}' | http :8080/actuator/loggers/org.springframework.data.web
```
