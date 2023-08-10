## Gradle

Gradle is a popular option for building JVM projects. Gradle leverages a Domain Specific Language (DSL) to produce a build.gradle build file that is both minimal and flexible.

You are allowed to choose either Groovy or Kotlin programming langauges for a DSL.

## Example

```
plugins {
    id 'org.springframework.boot' version '2.4.0'
    id 'io.spring.dependency-management' version '1.0.10.RELEASE'
    id 'java'
}

group = 'com.example'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

test {
    useJUnitPlatform()
}
```
