## Classes

Classes are the building blocks with which all Java applications and applets are built. Everything in a Java program must be inside a class.

You need to make the filename for the source code the same as the name of the public class i.e. with class FirstSample, use FirstSample.java.

All objects in Java live on the heap. When an object contains another object variable, it contains just a pointer to yet another heap object.

For the source file, you need to provide it with the public access specifier. You can only have one public class in a source file, but any number of nonpublic classes. Many programers prefer to put each class into its own source file.

When using multiple source files, you can provide either of the following for compilation:

- javac Employee\*.java (build all files matching the wildcard)
- javac Employee.java (any classes referenced by Employee will also be built)

```java
class Employee {
    private String name;
    private double salary;
    private LocalDate hireDay;

    // constructor
    public Employee(String n, double s, int year, int month, int day) {
        name = n;
        salary = s;
        hireDay = LocalDate.of(year, month, day);
    }

    public String getName() {
        return name;
    }
}
```

### Implicit and Explicit Parameters

Methods operate on objects and access their instance fields. The first parameter is called the implicit parameter, and it is the object of the class' type that appears before the method name i.e. this keyword.

```java
public void raiseSalary(double byPercent) {
    double raise = salary * byPercent / 100;
    this.salary += raise;
}
```

### Defining Methods

Method declarations have six components:

- Modifiers
- Return type
- Method name
- Parameter list in parenthesis
- An exception list
- The method body, enclosed between braces

### Methods with Variable Number of Parameters

You can pass in an ellipsis to denote an arbitrary number of objects.

```java
public class PrintStream {
    public PrintStream printf(String fmt, Object... args) {
        return format(fmt, args);
    }
}
```

### Encapsulation

If you want to get and set the value of an instance field, you need to supply three items:

- A private data field
- A public field accessor method
- A public field mutator method

**Be careful not to write accessor methods that return references to mutable objects**. This is very subtle and you can break encapsulation as they will return the same object and automatically changes the private state of the class member.

If you need to return a reference to a mutable object, you should clone it first.

```java
public Date getHireDay() {
    return (Date) self.hireDay.clone();
}
```

### Class-Based Acess Privileges

A method can access the private data of the object, and also the private data of all objects of its class.

```java
class Employee {
    public boolean equals(Employee other) {
        return self.name.equals(other.name);
    }
}
```

### Main Method

The main method does not operate on any objects. When the program starts, there aren't any objects yet; the main method executes and construct the objects the program needs.

Every class can have a main method. This is a handy trick for unit testing of classes.

```java
class Employee {
    public static void main(String[] args) {
        // fill the staff array with three Employee objects
        Employee[] staff = new Employee[3];
        staff[0] = new Employee();
        staff[1] = new Employee();

        for (Employee e: staff) {
            e.raiseSalary();
        }
    }
}
```

### Method Parameters

Parameters can be passed to a method in two ways: 'call by value' or 'call by reference'. 'Call by value' means the method gets just the value that the caller provides. In constrast, 'call by reference' means that the method gets the location of the variable that the caller provides.

Java always uses call by value i.e. makes a copy of the parameters. The method cannot modify the contents of any parameter variables passed to it. However, this is **only applicable for primitive values**. When an object is passed to a function, the object reference gets copied, and both the copy and original refer to the same object.

A method can change the state of an object parameter. Nonetheless, Java does not use call by reference for objects, which is a common misunderstanding.

```java
public static void swap(Employee x, Employee y) {
    // x and y references are copied
    Employee temp = x;
    x = y;
    y = temp;
}
Employee a = new Employee();
Employee b = new Employee();
swap(a,b);
// original values a and b still refer to the same objects
```

### Default Field Initialization

If you don't set a field explicitly in the constructor, it is automatically set to a default value. It can be considered poor programming practice to rely on the defaults.

```
numbers: 0
boolean: false
object references: null
```

## Documentation Comments

the JDK contains a useful tool called javadoc, that generates HTML documentation from your source files. You should put comments in the same class file. The javadoc utility extracts information for the following:

- Packages
- Public classes and interfaces
- Public and protected fields
- Public and protected constructors and methods

### Class Comments

Comments must be placed after import statements, and directly before the class definition.

```java
/**
Some documentation
*/
public class HelloWorld {}
```

### Method Comments

Each method comment use immediately precede the method. You can also use the following tags:

- @param variable description
- @return description
- @throws class description

```java
/**
Raises the salary of an employee.
@param byPercent the percentage to raise
@return the amount of the raise
*/
public double raiseSalary(double byPercent) {}
```
