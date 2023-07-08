## File Input and Output

When specifying a relative file name, the file is located relative to the directory in which the JVM was started. For IDE, it controls the starting directory.

```java
String dir = System.getProperty("user.dir"); // find the directory
```

### Reading

To read from a file, construct a Scanner object.

```java
String file = "myfile.txt"
String file = "c:\\mydirectory\\myfile.txt"
Scanner in = new Scanner(Paths.get(file), "UTF-8");
```

### Writing

If the file does not exist, it will be created.

```java
PrintWriter out = new PrintWriter("myfile.txt", "UTF-8");
```
