## Adapter pattern

In the adapter pattern, the adapter container is used to modify the interface of the application container so that it conforms to some predefined interface that is expected of all applications. For example, an adapter might ensure that an application implements a consistent monitoring interface.

Real-world application development is a heterogeneous, hybrid exercise. Some parts of your application might be written from scratch by your team, some supplied by vendors, and some might consist entirely of off-the-shelf open source or proprietary software that you consume as precompiled binary. The net effect of this heterogeneity is that any real-world application you deploy will have been written in a variety of languages, with a variety of conventions for logging, monitoring, and other common services.

Yet, to effectively monitor and operate your application, you need common interfaces. When each application provides metrics using a different format and interface, it is very difficult to collect all of those metrics in a single place for visualization and alerting. This is where the adapter pattern is relevant.

### Monitoring

When monitoring your software, you want a single solution that can automatically discover and monitor any application that is deployed into your environment. To make this feasible, every application has to implement the same monitoring interface.

Fortunately, most monitoring solutions understand that they need to be widely applicable, and thus they have implemented a variety of plugins that can adapt one monitoring format to a common interface.

### Logging

There is a wide variety of heterogeneity in how systems log data to an output stream. Systems might divide their logs into different levels (such as debug, info, warning, and error) with each level going into a different file. Some might simply log to stdout and stderr. This is especially problematic in the world of containerized applications where there is a general expectation that your containers will log to stdout.

Fortunately, as with monitoring, the adapter pattern can help provide a modular, re-usable design for both of these situations:

- While the application container may log to a file, the adapter container can redirect that file to stdout
- Different application containers can log information in different formats, but the adapter container can transform that data into a single structured representation that can be consumed by your log aggregator

### Health monitor

Though a container orchestrator allows us to add simple health checks to ensure a process is running and listening to a particular port, the adapter pattern can help if we want to add richer health checks i.e. running queries against a database.
