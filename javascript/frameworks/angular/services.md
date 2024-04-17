## providedIn scopes

Services scopes can be declared in the following: root, platform, or any.

### root

When declared with 'root', benefits include:

- Services are tree-shakable
- Services are singleton for the whole application and for lazy-loaded modules
- There is no need to explicitly register the service with NgModule

### platform

Every service defined with 'platform' will be provided in the platform injector and is a singleton for all applications.

The difference between 'root' and 'platform' is that when two applications are running in the same window, each application has its own root injector but both share the platform injector.

### any

Every service defined with 'any' will be provided in every module it is used. This means there may be multiple instances of the same service. This is helpful to ensure a service is a singleton within module boundaries.
