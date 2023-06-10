## Dependency Management Solutions

Solutions should avoid conflicting requirements of any form, including diamond dependency version conflicts. We also need to be aware of the impact: all software has bugs, some of those will be security critical.

A stable dependency-management scheme must be flexible with time and scale. We cannot assume indefinite stability of any particular node in the dependency graph, nor can we assume that no new dependencies are added.

When proposing solutions to dependency management, there are four common options that we know of that exhibit at least some of the appropriate properties.

### Nothing Changes (Static Dependency Model)

The simplest way to ensure stable dependencies is to never change them: no API changes, no behavioral changes, etc. Bug fixes are allowed only if no user code could be broken.

However, such scheme is not ideal due to the assumption of indefinite stability. Over a long period, this is not sustainable, and security bugs or other critical issues might force you to upgrade a dependency.

### Semantic Versioning

The **de facto standard for managing dependencies**. SemVer is the nearly ubiquitous practice of representing a version number for some dependency (especially libraries) using three decimal-separated integers representing major, minor and patch.

If we formalize these requirements, we can conceptualize a dependency network as a collection of software components (nodes) and the requirements between them (edges). Edge labels in this network change as a function of the version of the source node, either as dependencies are added/removed. As the whole network is changing asynchronously over time, the process of finding a mutually compatible set of dependencies that satisfy all the transitive requirements can be challenging.

### Bundled Distribution Models

This is what happens with Linux distributions: an organization gathers up a collection of dependencies, finds a mutually compatible set of those, and releases the collection as a single unit.

The higher-level distributors are involved in the process of finding, patching and testing a mutually compatible set of versions to include. Distributors are the engineers responsible for proposing a set of versions to bundle together, testing those to find bugs in the dependency tree, and resolving any issues.

### Live at Head

The model that some engineers at Google have been pushing for that is theoretically sound, but places new and costly burdens on participants in a dependency network. It is viewable as the dependency-management extension of trunk-based development.

Live at Head presupposes that we can unpin dependencies, drop SemVer, and rely on dependency providers to test changes against the entire ecosystem before committing. Live at Head is an explicit attempt to take time and choice out of the issue of dependency management: **always depend on the current version of everything**, and never change anything in a way in which it would be difficult for your dependents to adapt.

However, this philosophical shift in responsibility in the open source ecosystem is difficult to motivate initially: putting the burden on an API provider to test against and change all of its downstream customers is a significant revision to the responsibilities of an API provider.
