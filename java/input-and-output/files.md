## Files

To read a file, you can construct a Scanner from a Path object.

```java
Scanner in = new Scanner(Paths.get("/home/fred/input.txt"));
int lineNumber = 1;
while(in.hasNextLine()){
    String line = in.nextLine();
    System.out.println("line " + lineNumber + " :" + line);
    lineNumber++;
}
```

Alternatively, you can use Files class that provides common file operations. The class discussed here is concerned with the storage of files on a disk.

### Reading

```java
byte[] bytes = Files.readAllBytes(path);
String content = new String(bytes, charset);
List<String> lines = Files.readAllLines(path, charset);
```

### Writing

```java
Files.write(path, content.getBytes(charset));
Files.write(path, content.getBytes(charset), StandardOpenOption.APPEND);
Files.write(path, lines);
```

### Larger Files or Binary

If your files are large or binary, you can use the input/output streams or readers/writers. The methods from Files class save you from dealing with FileInputStream, FileOutputStream, BufferedReader, or BufferedWriter.

```java
InputStream in = Files.newInputStream(path);
OutputStream out = Files.newOutputStream(path);
Reader in = Files.newBufferedReader(path, charset);
Writer out = Files.newBufferedWriter(path, charset);
```

### Creating

```java
Files.createFile(path); // throws exception if exists
// all but the last component in the path must already exist
Files.createDirectory(path);
Files.createDirectories(path);  // create intermediate directories
```

### Modifying

The copy or move methods will fail if the target exists. To avoid this, you can specify options. You can also copy an input stream to a Path i.e. saving the input stream to disk.

```
REPLACE_EXISTING    Override an existing target
COPY_ATTRIBUTES     Copy all file attributes
ATOMIC_MOVE         Provides guarantee for concurrency, blocking
```

```java
Files.copy(fromPath, toPath);
Files.move(fromPath, toPath);
Files.copy(
    fromPath,
    toPath,
    StandardCopyOption.REPLACE_EXISTING,
    StandardCopyOption.COPY_ATTRIBUTES
);
Files.move(fromPath, toPath, StandardCopyOption.ATOMIC_MOVE);
Files.copy(inputStream, toPath);
Files.copy(fromPath, outputStream);
Files.delete(path); // throws exception if it doesn't exist
boolean deleted = Files.deleteIfExists(path);
```

### File Information

```java
static boolean exists(Path path)
static boolean isHidden(Path path)
static boolean isReadable(Path path)
static boolean isWritable(Path path)
static boolean isExecutable(Path path)
static boolean isRegularFile(Path path)
static boolean isDirectory(Path path)
static boolean isSymbolicLink(Path path)
```

## Visiting Directory Entries

If you want to have a filter criterion involving the file attributes, you can call find() with a predicate function that accepts a path and a BasicFileAttributes object.

```java
// directory is read lazily, does not enter subdirectories
try (Stream<Path> entries = Files.list(pathToDirectory)) {
    ...
}

// to process all descedants, DFS order
try (Stream<Path> entries = Files.walk(pathToRoot)) {
    // Contains all descendants, visited in depth-first order
}
```

### Copying Files to Another Directory

Unfortunately, you cannot easily use the Files.walk() to delete a tree of direc-
tories since you need to first delete the children before deleting the parent. Instead, you can use directory streams.

```java
Files.walk(source).forEach(p -> {
    try {
        Path q = target.resolve(source.relativize(p));
        if (Files.isDirectory(p)) Files.createDirectory(q);
        else Files.copy(p, q);
    }
    catch (IOException ex) {
        throw new UncheckedIOException(ex);
    }
});
```

### Directory Streams

If you need more fine-grained control over the traversal process, instead of using Files.walk(), you can use Files.newDirectoryStream object instead. You can filter the files with a glob pattern.

```java
try (DirectoryStream<Path> entries = Files.newDirectoryStream(dir)) {
    for (Path entry : entries) {
        // Process entries
    }
}

try (DirectoryStream<Path> entries = Files.newDirectoryStream(dir, "*.java"))
```

If you want to visit all descendants of a directory, call walkFileTree() instead and supply an object of type FileVisitor. The object gets notified:

- When a file is encountered with visitFile()
- Before a directory is processed with preVisitDirectory()
- After a directory is processed with postVisitDirectory()
- When an error occurred with visitFileFailed()

In each case, you can specify whether you want to:

- Continue visiting the next file with FileVisitResult.CONTINUE
- Continue the walk but skip the current directory with FileVisitResult.SKIP_SUBTREE
- Continue the walk but without visiting siblings with FileSkipResult.SKIP_SIBLINGS
- Terminate the walk with FileVisitResult.TERMINATE

```java
Files.walkFileTree(
    Paths.get("/"),
    new SimpleFileVisitor<Path>() {
        public FileVisitResult preVisitDirectory(Path path, BasicFileAttributes attrs) throws IOException {
            System.out.println(path);
            return FileVisitResult.CONTINUE;
        }

        public FileVisitResult postVisitDirectory(Path dir, IOException exc) {
            return FileVisitResult.CONTINUE;
        }

        public FileVisitResult visitFileFailed(Path path, IOException exc) throws IOException {
            return FileVisitResult.SKIP_SUBTREE;
        }
    }
);
```
