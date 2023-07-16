## Shared Libraries

Useful for sharing parts of Pipelines between various projects to reduce redundancies and keeping code DRY. A shared library is a collection of independent Groovy scripts which you pull into your Jenkinsfile at runtime. A shared Library is defined with a name, a source code retrival method such as by SCM, and optionally a default version.

To access them, the Jenkinsfile needs to use the @library annotation. If the line immediate after @Library annotation is not an import statement, need to add an underscore.

```groovy
@Library('my-shared-library') _

/* Using a version specifier, such as branch, tag, etc */
@Library('my-shared-library@1.0') _

/* Accessing multiple libraries with one statement */
@Library(['my-shared-library', 'otherlib@abc1234']) _

/* accessing class libraries with src/ directories requires import statement */
@Library('somelib')
import com.mycorp.pipeline.somelib.UsefulClass
```

### Structure

```
(root)
+- src                     # Groovy source files
|   +- org
|       +- foo
|           +- Bar.groovy  # for org.foo.Bar class
+- vars
|   +- foo.groovy          # for global 'foo' variable
|   +- foo.txt             # help for 'foo' variable
+- resources               # resource files (external libraries only)
|   +- org
|       +- foo
|           +- bar.json    # static helper data for org.foo.Bar
```

The src directory is added to the classpath when executing Pipelines.

The vars directory hosts script files that are exposed as global variables in Pipelines. The name of the file is the name of the variable in the Pipeline i.e. fooBar.groovy creates a variable named fooBar (camelcase required). You can put as many functions as you like inside this file.

https://github.com/darinpope/github-api-global-lib

### Defining Global Variables

Internally, scripts in the vars directory are instantiated on-demand as singletons. This allows multiple methods to be defined in a single .groovy file for convenience.

```groovy
/* vars/log.groovy */
def info(message) {
    echo "INFO: ${message}"
}

def warning(message) {
    echo "WARNING: ${message}"
}
```

```groovy
/* jenksfile */
@Library('utils') _

log.info 'Starting'
log.warning 'Nothing to do!'
```

### Other Common Code

This includes helper classes, or common code that you might want to include inside pipeline steps themselves. You can also use it as a place to store static constants which you want to use throughout your pipelines.
