## Application Configuration

Spring Boot applications supply a variety of powerful mechanisms for developers to dynamically configure and reconfigure their applications, even while the app is running. These mechanisms leverage the Spring environment to manage configuration properties from all sources, including:

- devtools global setting properties
- command line arguments
- OS environment variables
- Application properties packaged inside the jar
- Default properties specified by setting SpringApplication.setDefaultProperties

## Autoconfiguration Report

Spring Boot sets up the application with the beans it needs to fulfill the functionalities that are part and parcel to chosen capabilities, dependencies, and code. To see what beans are created/not created, you can produce the autoconfiguration report.

```bash
$ java -jar bootapplication.jar --debug
$ java -Ddebug=true -jar bootapplication.jar
```
