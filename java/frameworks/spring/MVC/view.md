## View Controllers

When a controller is simple enough that it doesn't populate a model or process input, you can redefine the controller as a view controller i.e. a controller that does nothing but forward the request to a view.

```java
package tacos.web;

import org.springframework.context.annotation.Configuration;
import
org.springframework.web.servlet.config.annotation.ViewControllerRegistry
;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/").setViewName("home");
    }
}
```
