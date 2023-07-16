## Why is Dependency Management Difficult?

The trick isn't just finding a way to manage one dependency, but a network of dependencies and their changes over time. Some subset of this network is directly necessary for your first-party code, and some of it is only pulled in by transitive dependencies.

### Conflicting Requirements

Much of the difficult stems from one problem: what happens when two nodes in the dependency network have conflicting requirements, and your organization depends on both? This can arise for many reasons, including platform considerations, language version, compiler, etc.

### Diamond Dependencies

The diamond dependency problem, and other forms of conflicting requirements, require at least three layers of dependency.

<img src="../../assets/diamond-dependency.png">

In this model, libbase is used by both liba and libb, and liba and libb are both used by a higher-level component libuser. If libbase ever introduces an incompatible change, there is a change that liba and libb, as products of separate organizations, don't update simultaneously. If liba depends on the new libbase version while libb depends on the old, there is no way for libuser to put everything together.

Different programming langauges tolerate the diamond dependency problem to different degrees. For some languages, it is possible to embed multiple (isolated) versions of a dependency within a build. Java provides fairly well-established mechanisms to rename the symbols provided by a dependency. However, C++ has nearly zero tolerance for diamond dependencies, as it is a clear violation of C++'s One definition rule.

If you encounter a conflicting requirement problem, the only easy answer is to skip forward or backward in versions for those dependencies to find something compatible.

### Compatbility Promises

It is better to reuse existing infrastructure than to build it yourself. Reuse is healthy, so long you are not downloading trojaned software. However, just because you avoid a development cost doesn't mean importing a dependency is the correct choice.

In software engineering organizations, we need to be mindful of both development and time costs. Even if we import a dependency with no intent of upgrading it, discovered security vulnerabilities, changing platforms, and evolving dependency networks can conspire to force that upgrade, regardless of our intent.
