## Spring Security

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

### Configuring Spring Security

```java
package tacos.security;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web
 .configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web
 .configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {
}
```

## CSRF

Spring Security has built-in CSRF protection by default. you only need to make sure that any forms submitted include a field named \_csrf that contains the CSRF token.

```html
<input type="hidden" name="_csrf" th:value="${_csrf.token}" />
```
