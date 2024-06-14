## Shared library

### Dependency management and change control

One of the most common techniques for sharing code is to use a shared library i.e. JAR file, DLL. Common code is consolidated and shared at compile time. However, the trade-offs associated with the granularity of a shared library are **dependency management** and **change control**.

If a change occurs to any of the class files in the coarse-grained shared library, every service, whether it cares about the change or not, **must eventually adopt the change** because of a version deprecation of the shared library. This forces unnecessary retesting and redeployment of all the services using that library, therefore significantly increasing the overall testing scope of a shared library change.

Breaking shared code into smaller functionality-based shared libraries is better for change control and overall maintainability, but unfortunately creates a big ball of mud in terms of dependency management.

Advice is to generally avoid large, coarse-grained shared libraries and **strive for smaller, functionally partitioned libraries** whenever possible, thus favoring change control over dependency management.

### Versioning

Always use versioning for shared libraries. However, there are trade-offs and hidden complexity in versioning:

- Communicating a version change to multiple teams
- Depreciation of older versions
- Avoid the use of LATEST version

<table>
<tr>
<th>Advantages</th>
<th>Disadvantages</th>
</tr>
<tr>
<td>
• Ability to version changes </br>
• Shared code is compiled, reducing runtime errors </br>
• Good agility for code shared code changes
</td>
<td>
• Dependencies can be difficult to manage </br>
• Code duplication in heterogenous codebases </br>
• Version deprecation can be difficult </br>
• Version communication can be difficult
</td>
</tr>
</table>
