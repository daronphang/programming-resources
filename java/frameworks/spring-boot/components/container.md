## Container

## Interfaces

One of the main features of the Spring framework is the IoC container which manages the objects of an application. It uses dependency injection to achieve IoC. The interfaces BeanFactory and ApplicationContext represent the Spring IoC container.

### BeanFactory

The BeanFactory is the root interface for accessing the Spring container, and provides functionalities for managing the lifecycle of beans.

### ApplicationContext

Spring ApplicationContext is where Spring holds instances of objects (beans) that it has identified to be managed and distributed automatically. **It is responsible for instantiating, configuring, and assembling beans**. Using the IoC principle, Spring collects bean instances from the application and uses them at the appropriate time.

The ApplicationContext is a sub-interface of the BeanFactory, and hence offers all the functionalities of BeanFactory. It also provides more enterprise-specific functionalities including resolving messages, supporting internationalization, publishing events, and application-layer specific contexts.

The application context is read-only while the application is running, but may be reloaded if the implementation supports it. An application context provides:

- Bean factory methods for accessing application components
- The ability to load file resources in a generic fashion
- The ability to publish events to registered listeners
- The ability to resolve messages, supporting internationalization
