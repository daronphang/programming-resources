## Text Input and Output

When saving data, you have the choice between binary and text formats. For the latter, you need to consider the character encoding.

### Binary

For binary, you can use OutputStreamWriter and InputStreamReader classes.

```java
Reader in = new InputStreamReader(System.in);
Reader in = new InputStreamReader(
    new FileInputStream("data.txt"),
    StandardCharsets.UTF_8
);
```

### Text

To process text, the easiest way is to use Scanner class. Alternatively, you can read a text file into a string directly by creating an instance of String class.

```java
String file = "myfile.txt"
String file = "c:\\mydirectory\\myfile.txt"
Scanner in = new Scanner(Paths.get(file), "UTF-8");
```

```java
String content = new String(Files.readAllBytes(path), charset);
```

To write to a print writer, use the same print() that you use with System.out. If the wrtier is set to autoflush mode, all characters in the buffer are sent to their destination whenever println is called (print writers are always buffered).

```java
PrintWriter out = new PrintWriter("employee.txt", "UTF-8");
// equivalent
PrintWriter out = new PrintWriter(
    new FileOutputStream("employee.txt"),
    "UTF-8"
);

String name = "Harry Hacker";
double salary = 75000;
out.print(name);
out.print(' ');
out.println(salary);
```

## Example

```java
private static Employee[] readData(Scanner in) {
    int n = in.nextInt(); // retrieve the array size
    in.nextLine(); // consume newline

    Employee[] employees = new Employee[n];
    for (int i = 0; i < n; i++) {
        employees[i] = readEmployee(in);
    }
    return employees;
}

public static Employee readEmployee(Scanner in) {
    String line = in.nextLine();
    String[] tokens = line.split("\\|");
    String name = tokens[0];
    double salary = Double.parseDouble(tokens[1]);
    LocalDate hireDate = LocalDate.parse(tokens[2]);
    int year = hireDate.getYear();
    int month = hireDate.getMonthValue();
    int day = hireDate.getDayOfMonth();
    return new Employee(name, salary, year, month, day);
}
```
