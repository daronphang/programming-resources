## Java

Java was never just a language but a whole platform with a huge library containing lots of reusable code, and an execution environment that provides services usch as security, portability across OS, and automatic garbage collection.

### Buzzwords

#### Secure

Java is intended to be used in networked/distributed environments, and a lot of emphasis has been placed on security. Java enables the construction of virus-free, tamper-free systems.

#### Architecture-Neutral

The compiler generates an architecture-neutral object file format that is executable on many processors. The Java compiler generates bytecode instructions which have nothing to do with a particular computer architecture.

#### High-Performance

Just-in-time compilers have become competitive with traditional compilers and in some cases, even outperform them as they have more information available i.e. JIT compiler can monitor which code is executed frequently and optimize just that code for speed.

### Garbage Collection

Java does automatic garbage colelction. If a block of memory is no longer needed, it will eventually be recycled.

## Jargons

| Name                     | Acronym | Explanation                                                                                                                                      |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Java Development Kit     | JDK     | The software for programmers who want to write Java programs. Consists of a Java VM and a Java-bytecode compiler. Licensed under Oracle          |
| Java Runtime Environment | JRE     | The software for consumers who want to run Java programs                                                                                         |
| Server JRE               | -       | The software for running Java programs on servers                                                                                                |
| Standard Edition         | SE      | The Java platform for use on desktops and simple server applications                                                                             |
| Enterprise Edition       | EE      | The Java platform for complex server applications                                                                                                |
| Micro Edition            | ME      | The Java platform for use on cell phones and other small devices                                                                                 |
| Java FX                  | -       | An alternate toolkit for GUI that is included in Oracle's Java SE distribution                                                                   |
| OpenJDK                  | -       | A free and open source implementation of Java SE. It does not include browser integration or JavaFX. Licensed under General Public License (GNU) |
| Software Development Kit | SDK     | An outdated term that described JDK from 1998 until 2006                                                                                         |

## Installation

### OpenJDK vs OracleJDK

There is no technical difference between the two, since the build process for OracleJDK is based on OpenJDK. When it comes to performance, Oracle's is much better regarding responsiveness and JVM performance. It puts more focus on stability because of the importance it gives to its enterprise customers. However, openJDK has more releases and is continually improving and becoming more stable with the contributions from the community.

### Managing Multiple JDKs

The easier way to manage one or more JDKs on your machine is by usign SDKMAN!. This package manager also facilitiates the installation of the Spring Boot CLI. It is recommended to choose the current LTS version packaged by AdoptOpenJDK.

https://sdkman.io/install

```sh
$ sdk list java
$ sdk install java <version>
```

### Manual

1. Download OpenJDK i.e. Microsoft OpenJDK 17
2. Uncompress the file

```sh
$ tar xvf microsoft-jdk-17.0.7-linux-x64.tar.gz -C /usr/local/jdk-17.0.7+7/
```

3. Export to PATH under ~/.profile

## Running via CLI

For compiling and launching a Java program. You must have a main method (declared public) in the source file for your class for your code to execute.

```java
public class Welcome {
    public static void main(String[] args) {
        String greeting = "Welcome to Java!";
        System.out.println(greeting);
    }
}
```

```sh
$ javac Welcome.java # compiles the file into the file Welcome.class
$ java Welcome  # launches JVM
```

## Applets

Most of the early hype about Java came from its ability to run applets inside a web browser. Applets are meant to be viewed in a browser; however, many browsers do not have Java support or make it difficult to enable it (best bet is Firefox).

## jconsole

The Java VM has support for monitoring and management of Java applications, allowing the installation of agents in the VM to track memory consumption, thread usage, class loading, etc.

This feature is important for large and long-running Java programs, such as application servers.

```sh
$ ps aux | grep java
$ jconsole processID
```

## jmap

The jmap utility is used to get a heap dump that shows you every object on the heap. Point your browser to localhost:7000.

```sh
$ jmap -dump:format=b,file=dumpFileName processID
$ jhat dumpFileName
```
