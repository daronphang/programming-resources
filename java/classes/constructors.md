## Constructors

- Has the same name of the class
- Runs when you construct objects of the class
- Can only be called in conjuction with the new operator
- A class can have more than one constructor
- Has no return value
- Variables declared in the constructor are only accessible inside the constructor (caution)

### Overloading

Overloading occurs if several methods have the same name but different parameters. The compiler must sort out which method to call. It picks the correct method by matching the parameter types in the headers of the various methods with the types of values passed in the call (known as overloading resolution).

If the compiler cannot match the parameters, or if there are multiple methods that match the call, it will raise a compile-time error.

Some classes have more than one constructor. Nonetheless, Java allows you to overload any method.

```java
// can either construct an empty object or pass an initial string
StringBuilder messages = new StringBuilder();
StringBuilder toDoList = new StringBuilder("To do:\n");
```

```java
// String class has four public methods called indexOf
indexOf(int)
indexOf(int, int)
indexOf(String)
indexOf(String, int)
```

### Parameter Names

When you write very trivial constructors, it can be frustrating to come up with parameter names. For general practice, you can opt for single-letter parameter names, or prefix with an 'a', or use this keyword.

```java
public Employee(String n, double s) {
    name = n;
    salary = s;
}

public Employee(String aName, double aSalary) {
    name = aName;
    salary = aSalary;
}

public Employee(String name, double salary) {
    this.name = name;
    this.salary = salary;
}
```

### Calling Another Constructor

If the first statement of a constructor has the form this(), then the constructor calls another constructor of the same class.

```java
class Employee {
    private String name;
    private double salary;
    private static double nextId = 1;

    public Employee(String n, double s) {
        this.name = n;
        this.salary = s;
    }

    public Employee(double s) {
        // calls Employee(String, double)
        this("Employee #" + nextId, s);
        nextId++;
    }
}

// calls two constructors
Employee e = new Employee(6000);
```

### Initialization Blocks

```java
class Employee {
    private static int nextId;
    private int id;

    {
        id = nextId;
        nextId++;
    }
}
```

### Calling Constructors

It is always a good idea to organize your initialization code. If your class requires complex initialization code, use a static initialization block. When a constructor is called:

1. If the constructor calls a second constructor, the second constructor runs first before the body of this constructor
2. All data fields are initialied to their default values if not specified
3. All field initializers and initialization blocks are executed, in the order in which they occur in the class declaration
4. The body of the constructor is executed

### Object Destruction and finalize Method

The most common activity in a destructor is reclaiming the memory set aside for objects. Since Java does automatic garbage collection, manual memory reclamation is not needed and hence, Java does not support destructors.

For objects that utilize a resource i.e. file, it is important that the resource be reclaimed and recycled when it is no longer needed.

You can add a finalize method to any class. It will be called before the garbage collector sweeps away the object. However, in practice, **do not rely on the finalize method for recycling resources** that are short in supply as you simply cnanot know when the method will be called.
