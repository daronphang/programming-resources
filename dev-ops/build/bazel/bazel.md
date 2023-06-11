## Bazel

Bazel is an open-source build and test tool similar to Make, Maven and Gradle. It uses a human-readable, high-level build language. Bazel supports projects in multiple languages and builds outputs for multiple platforms. It also supports large codebases across multiple repositories, and large numbers of users.

Incremental builds are vital for better build performance. In an incremental build, code changes in small increments and hence, it does not make sense to rebuild the entire application everytime something changes.

Bazel divides the codebase into different build units, and the scope of a build can be very granular i.e. only the part that has been changed and affected parts are rebuilt.

### Benefits

#### High-level build language (declarative)

Bazel uses an abstract, human-readable language (Starlark) to describe the build properties of your project at a high semantical level. Unlike other tools, Bazel operates on the concepts of libraries, binaries, scripts, and data sets, shielding you from the complexity of writing individual calls to tools such as compilers and linkers.

#### Reproducibility

Bazel produces pure functional builds where your output files are strictly dependent on your inputs. This gives two important characteristics to your builds: hermetic and idempotent. Hermetic build means the inputs that you explictly mention are readable by your build steps.

#### Fast and reliable

Bazel caches all previously done work and tracks changes to both file content and build commands. This way, Bazel knows when something needs to be rebuilt, and rebuilds only that. To further speed up your builds, you can set up your project to build in a highly parallel and incremental fashion.

#### Multi-platform

Bazel runs on Linux, macOS, and Windows. Bazel can build binaries and deployable packages for multiple platforms, including desktop, server, and mobile, from the same project.

#### Scaling

Bazel scales. Bazel maintains agility while handling builds with 100k+ source files. It works with multiple repositories and user bases in the tens of thousands.

#### Extensible

Bazel is extensible. Many languages are supported, and you can extend Bazel to support any other language or framework.

#### Integration

Bazel complements modern platforms like Docker and Kubernetes. For instance, you can have a handy Docker container for your monorepo containing a web client a bunch of microservices to kickstart a testing environment that resembles your production environment.

#### Parallelism and caching

Bazel speeds up your builds using a caching mechanism. It intelligently compares your subsequent builds with your previous cached builds, and only builds those files which the developers updated. This ensures that Bazel only spends your CPU resources on building those pieces of your project that need to be re-built.

Bazel allows you to generate concurrenet builds in a parallel fashion to save time across your distributed codebase. You can generate builds on both a single machine as well as across multiple machines remotely.
