## Build System

All build systems have a straightforward purpose: they transform source code into executable binaries that can be read by machines. A good build system will try to optimize for two properties: fast and correct.

Build systems are not just for humans; they also allow machines to create builds automatically, whether for testing or for releases to production.

### Workflows

- Code is automatically build, tested and pushed to production without human intervention
- Developer changes are automatically tested when they are sent for code review
- Changes are tested again immediately before merging into the trunk

### Managing Dependencies

Managing your own code is fairly straightforward, but managing its dependencies (internal, external) is much more difficult. This problem recurs repeatedly in the design of build systems, and managing dependencies is perhaps the most fundamental job of a build system.
