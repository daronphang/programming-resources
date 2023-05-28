## Monorepo

A version management configuration that stores multiple projects and libraries, along with the tooling for them, in one repository, with well-defined relationships.

To use the same CI/CD pipeline, can consider **language-based monorepo** like Pinterest, where services are grouped into one repository per language.

### Benefits

#### Unified versioning and single source of truth

There is no confusion about which repository hosts the authoritative version of a file. If one team wants to depend on another team's code, it can depend on it directly. Also, there is no need to publish versioned packages and hence, there is no need to worry about incompatibilities of projects depending on conflicting versions.

#### Extensive code sharing, reuse and standardization

Codebase will include a wealth of libraries that can be resued, and duplicated code is mitigated.

#### Simplified dependency management

With a proper build system, it is easy to include code across directories, simplifying dependency management. Changes to dependencies of a project trigger a rebuild of the dependent code. Also, this model avoids "diamond dependencies".

#### Atomic changes

Everything works together at every commit. There is no such thing as breaking change when you fix everything in the same commit. This is a powerful feature as a developer can make a major change to hundreds of files across the repository in a single consistent operation.

#### Collaboration across teams

The availability of all source code in a single repository makes it easier for maintainers to perform testing and performance benchmarking for high-impact changes before they are committed. Also, it is easier to define a clear set of rules for developers to follow.

#### Flexible team boundaries and code ownership

A developer never has to decide where the repository boundaries lie, and there is no need to "fork" the development of a shared library or merge across repositories to update copied versions of code. This environment makes it **easy to do gradual refactoring** and reorganization of the codebase.

#### Code visibility and clear tree structure

There is more accountability as many projects are visible to many people, and monorepos lend themselves to security features. The layout of the codebase is more easily understood, and it is easier to browse the codebase and understand the bigger picture.

### Tradeoffs

- Tooling investments for both development and execution
- Codebase complexity, including unecessary dependencies and difficulties with code discovery
- Effort invested in code health
