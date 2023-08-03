## Paths

A Path is a sequence of directory names, optionally followed by a file name. The path separator used is based on the OS.

```java
Path absolute = Paths.get("/home", "harry");
Path relative = Paths.get("myprog", "conf", "user.properties");

String baseDir = props.getProperty("base.dir");
// May be a string such as /opt/myprog or c:\Program Files\myprog
Path basePath = Paths.get(baseDir); // OK that baseDir has separators
```

### Combine/Resolve

If you want to combine/resolve paths, you can call p.resolve(q) that returns a path according to these rules:

- If q is absolute, return q
- Else, the result is p then q

```java
// can either take a string or a path
Path workRelative = Paths.get("work");
Path workPath = basePath.resolve(workRelative);
// alternative with a string
Path workPath = basePath.resolve("work");
```

### Normalize

The normalize() removes any redundant components in the path.

```java
normalize("/home/harry/../fred/./input.txt") // yields /home/fred/input.txt
```

### Absolute Path

The toAbsolutePath() yields the absolute path of a given path, starting at a root component.

### Extracting

```java
Path p = Paths.get("/home", "fred", "myprog.properties");
Path parent = p.getParent(); // the path /home/fred
Path file = p.getFileName(); // the path myprog.properties
Path root = p.getRoot(); // the path /
```
