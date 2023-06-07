## Artifact-Based Build System

Instead of letting engineers define tasks, we can have a small number of tasks defined by the system that engineers can configure in a limited way. Engineers would still need to tell the system what to build, but how of doing the build would be left to the system.

This is the approach taken by Blaze, Bazel, Pants and Buck. Rather than being an imperative set of commands describing how to produce an output, buildfiles are declarative manifest describing a set of artifacts to build, their dependencies, and a limited set of options that affect how they are built.

### Functional perspective

Artifact-based build systems can be made an analogy with functional programming. In functional languages, the programmer describes a computation to perform, but leaves the details of when and how that computation is executed to the compiler.

The langauge is often able to trivially **parallelize such programs and make strong guarantees about their correctness** that would be impossible in an imperative language. With the build system, it is taking source files as inputs and produces binaries as outputs.

### Stale builds

Relating to the functional programming paradigm, if the build system knows that the output from the compiler depends on its inputs, and its inputs did not change, the output can be reused. This guarantees that it won't produce stale builds.

### Tools as dependencies

For builds that depend on the tools installed on a machine, reproducing builds across systems can be difficult due to different tool versions or locations. This problem becomes even more difficult when your project uses languages that require different tools based on the platform they are being built on.

Bazel solves this problem by treating tools as dependencies to each target. Before building, it checks if the specified compiler is available at a known location, and downloads if it is not.

For platform independence, Bazel solves this problem by using toolchains. Rather than having targets depend directly on their tools, they actually depend on types of toolchains. A toolchain contains a set of tools defining how a type of target is built on a particular platform.

### Isolating the environment

For tasks that write actions on the same resource, Bazel makes these conflicts impossible by using **sandboxing**. On supported systems, every action is isolated from every other action via a filesystem sandbox. This is enforced by systems such as LXC on Linux, which is the same technology behind Docker.

### Making external dependencies deterministic

Build systems often need to download dependencies from external sources. However, depending on files outside of the current workspace is risky, as the files can change anytime and can lead to unreproducible builds. It can also introduce a huge security risk when it is owned by a third party.

The fundamental problem is that we want the build system to be aware of these files without having to check them into source control. Updating a dependency should be a conscious choice, but it should be made once in a central place, rather than managed by individual engineers.

Bazel and other build systems address this problem by requiring a workspace wide manifest file that lists a cryptographic hash for every external dependency in the workspace. When Bazel runs a build, it checks the actual hash of its cached dependency against the expected hash defined in the manifest, and redownloads the file only if the hash differs.
