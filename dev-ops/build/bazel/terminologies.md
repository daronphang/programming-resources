### Workspace

The workspace is typically a directory where Bazel constructs your project's build files from your source code. It contains various source files in a nested hierarchical fashion.

At your root level, your project might also have a dedicated WORKSPACE file which contains all the references to external dependencies that are needed to build the app.

The workspace is where your inputs are extracted and converted to outputs to generate the desired build file.

### Packages

Packages are directories located below the top-level directory in a workspace. They contain your build files that may be named BUILD or BUILD.bazel, along with other related files and specified dependencies.

### Targets

Everything inside your packages can be considered as targets. It includes source files that developers wrote and added to your project, or generated files that Bazel constructs based on your build configurations. Other than files, targets often involve rules that govern the relationship between your input files and output files.

You may specify your target rules to **chain your inputs and outputs** for consecutive build operations i.e. using a generated file from a previous step as an input file for another step.

### Labels

The nomenclature of a target is known as a label. It is a way to recognize different targets falling under a package and distinguishing them from other targets in the same or different packages.

### Dependencies

When you build your specified targets, one or more target may depend on another for the build process. The latter is the dependency.
