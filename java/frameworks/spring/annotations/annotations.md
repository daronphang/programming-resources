## Spring Annotations

Spring annotations are a form of metadata that provides data about a program. Annotations are used to provide supplemental information about a program. It does not have a direct effect on the operation of the code they annotate. **It does not change the action of the compiled program**.

## @Component vs @Bean

| Key              | @Bean                                                                                              | @Component                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Auto detection   | It is used to explicitly declare a single bean, rather than letting Spring do it automatically     | Spring will automatically detect by using classpath scan        |
| Spring Container | Bean can be created even if the class is outside the container (decouples the declaration of bean) | Cannot create bean if class is outside of the container         |
| Annotation       | Method level annotation                                                                            | Class level annotation                                          |
| @Configuration   | Works only when class is also annotated with @Configuration                                        | Works without @Configuration annotation                         |
| Use case         | Should use @Bean if you want specific implementation based on dynamic condition                    | Cannot write specific implementation based on dynamic condition |
