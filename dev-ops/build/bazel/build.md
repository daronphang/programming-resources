## Usage

1. Download and install Bazel
2. Set up a project workspace, which is a directory where Bazel looks for build inputs and BUILD files, and where it stores build outputs
3. Write a BUILD file, which tells Bazel what to build and how to build it
4. Run Bazel from the command line; Bazel places your outputs within the workspace

## BUILD

You write your BUILD file by declaring build targets using Starlark, a domain-specific language.

A build target specifies a set of input artifacts that Bazel will build plus their dependencies, the build rule Bazel will use to build it, and options that configure the build rule.

A build rule specifies the build tools Bazel will use, such as compilers and linkers, and their configurations. Bazel ships with a number of build rules covering the most common artifact types in the supported languages on supported platforms.
