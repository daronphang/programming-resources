## Breaking dependencies

Dependencies can be problematic in legacy code, but fortunately, we can break them. Nearly every problem that you run into will be the result of some dependency that you should break.

In OOP, often the first step is to attempt to instantiate the classes that we need in a test harness. In the easiest cases, we can do this just by importing or including the declaration of the classes we depend upon.

## Building dependencies

### Extract interfaces

If you have a cluster of classes that you want to build more quickly, there may be dependencies that can affect compile time. To minimize this, we can extract interfaces for the classes in your cluster that are used by classes outside the cluster.
