## Build

For project build, you can choose between Maven or Gradle.

Maven has a more rigid declarative approach (opinionated) that keeps things consistent from project to project, environment to envrionment. On the other hand, Gradle can be faster for builds in larger projects, and also offers flexibility for projects with complex build environments.

## JVM

You can choose between Java or Kotlin. Both are first-class citizens in Spring Boot.

Java forms the bedrock-solid foundation of nearly the entire Spring codebase, and hence, it is a great choice to use for building your applications. Nonetheless, Kotlin was created to address perceived gaps in Java's usability.

Kotlin compiles to the same bytecode output that Java does, and Spring projects can be created that include both Java and Kotlin source files.

## Spring Initializr

Project is compressed as zip.

https://start.spring.io/

## CLI

### Installation

Th easiest way to install the CLI as with JDK, Kotlin utilities and more with SDKMAN!.

```bash
$ sdk list
$ sdk list springboot
$ sdk install springboot
```

### Commands

The CLI leverages the Initialzr to provide its project building capabilities and hence, projects created via either mechanism are identical.

```bash
$ spring init   # same as spring initialzr, with defaults
$ spring init -a demo -l java --build maven demo
$ unzip demo.zip -d demo
```

## DevTools

DevTools provides developers with handy development-time tools:

- Automatic application restart when code changes
- Automatic browser refresh when browser-destined resource change (templates, stylsheets, Javascript)
- Automatic disable of template caches
- Built in H2 console if H2 database is in use

When DevTools is in play, the application is loaded into two separate class loaders in the JVM:

- One is loaded with Java code
- Other is loaded with dependency libraries (unlikely to change)

When a change is detected, DevTools reloads only the class loader containing your project code and restarts the Spring application context. However, **changes to dependency will not be available in automatic restarts**. You will need to do a hard restart.
