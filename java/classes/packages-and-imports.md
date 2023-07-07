## Packages

Java allows you to group classes in a collection called a package. The main reason for using packages is to guarantee the uniqueness of class names i.e. different packages can have the same class names.

From the point of view of the compiler, there is no relationship between nested packages i.e. java.util and java.util.jar have nothing to do with each other.

### Adding Classes into a Package

To place classes inside a package, you must put the name of the package at the top of your source file.

If you don't put a package statement in the source file, then the classes in that source file belong to the default package. The default package has no package name.

Place source files into a subdirectory that matches the full package name i.e. files in com.horstman.corejava should be in a subdirectory `com/horstman/corejava`. However, the compiler does not check the directory structure when it compiles the source files. Hence, it will compile without errors if it does not depend on other packages. Else, the VM won't find the classes if the packages don't match the directories.

```java
package com.horstmann.corejava;

public class Employee {}
```

## Class Importation

A class can use all classes from its own package, and all public classes from other packages. When importing with \*, it has no negative effect on code size. However, if you import classes explicitly, the reader of your code knows exactly which classes to use.

```java
import java.time.*;
import java.time.LocalDate;

LocalDate today = LocalDate.now();
```

For packages that have the same class names, you need to use the full package name.

```java
java.util.Date deadline = new java.util.Date();
java.sql.Date today = new java.sql.Date();
```

## Static Imports

A form of the import statement permits the importing of static methods and fields, not just classes.

```java
import static java.lang.System.*;
import static java.Math.*;

out.println("Hello world!");
exit(0);
sqrt(pow(x,2) + pow(y,2));
```

## Class Path

Classes are stored in subdirectories of the filesystem. The path to the class must match the package name.

Class files can also be stored in a JAR file (Java archive), which contains multiple class files and subdirectories in a compressed format, saving space and improving performance.

The class path is the collection of all locations that can contain class files i.e. `/home/user/classdir:.:/home/user/archives/archive.jar`. It lists all directories and archive files that are **starting points** for locating classes.

### VM

Given a class file of com.horstmann.corejava.Employee class, when the VM searches for the class file:

1. First looks into system class files that are stored in archives in the jre/lib adn jre/lib/ext directories
2. Turns to the class path i.e. `/home/user/classdir/com/horstmann/corejava/Employee.class`, `./horstmann/corejava/Employee.class`, `com/horstmann/corejava/Employee.class` inside `/home/user/archives/archive.jar`

### Compiler

The compiler has a harder time locating files than the VM. If you refer to a class without specifying its package, the compiler first needs to find out the package that contains the class. It consults all import directives as possible sources for the class.

Given the following:

```java
import java.util.*;
import com.horstmann.corejava.*;

Employee e = new Employee();
```

The compiler will find Employee in:

1. java.lang.Employee
2. java.util.Employee
3. com.horstmann.corejava.Employee
4. Current package
5. Recompiles if the source file is newer than the class file

Classes must be unique, and it will throw compile-time error if more than one class is found. Order of import statements doesn't matter.

### Setting the Class Path

It is a good idea to place the command in a shell script. It is not good to set the CLASSPATH environment variable permanently as there is also a global setting, and may result in your classes not loading properly.

```bash
$ java -classpath /home/user/classdir:.:/home/user/archives/archive.jar MyProg
```
