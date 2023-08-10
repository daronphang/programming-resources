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
