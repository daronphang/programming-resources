## JAR Files

When you package your application, you want to give your users a single file, not a directory structure filled with class files. JAR files were designed for this purpose. Moreover, JAR files are compressed.

```bash
$ jar cvf JARFileName File1 File2
$ jar cvfe MyProgram.jar com.mycompany.mypkg.MainAppClass File1 File2
```

### Manifest

In addition to class files, images, and other resources, each JAR file contains a manifest file that describes special features of the archive (MANIFEST.MF located in META-INF subdirectory of the JAR file).

The manifest entries are grouped into sections. The first section is called the main section and applies to the whole JAR file. Subsequent entries can specify properties of named entities such as individual files, packages, or URLs. Those entries must begin with a Name entry.

```
Manifest-Version: 1.0
Name: Woozle.class
```

```bash
$ jar cfm JARFileName ManifestFileName
$ jar cfm MyArchive.jar manifest.mf com/mycompany/mypkg/*.class
$ java -jar MyProgram.jar
```