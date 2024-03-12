## Fitness functions

Fitness function was initially stated in Evolutionary computing and Genetic Algorithm to guide simulations towards optimal design solutions. Evolutionary computing is all about **guided incremental changes**, in which engineers access the current state and measure how close it is to the desired state.

Fitness function is an object function used to assess how close the output comes to achieving the aim. In other words, it takes a candidate solution to a problem as input and produces as output how 'fit' the solution is with respect to the problem.

Fitness function is any mechanism that provides an objective integrity assessment of some architecture characteristic or combination of architecture characteristics. They are not some new framework for architects to download, but rather a new perspective on many existing tools.

Regardless of the application architecture (monolith, microservices), fitness function-driven development can introduce continuous feedback for architectural conformance and inform the development process as it happens, rather than after the fact.

For example, when using a genetic algorithm to optimize wing design, the fitness function assesses wind resistance, weight, airflow, and other characteristics desirable to good wing design.

### Governing

An architect can ensure that developers adhere to guidelines and principles by implementing fitness functions to build protections around unexpected change in architecture characteristics.

Without fitness functions, architects have to perform code reviews, but may be too late in the development cycle to be effective.

## Examples

### Checking for cyclic dependencies

```java
public class CycleTest {
    private JDepend jdepend;
    @BeforeEach
    void init() {
    jdepend = new JDepend();
        jdepend.addDirectory("/path/to/project/persistence/classes");
        jdepend.addDirectory("/path/to/project/web/classes");
        jdepend.addDirectory("/path/to/project/thirdpartyjars");
    }
    @Test
    void testAllPackages() {
        Collection packages = jdepend.analyze();
        assertEquals("Cycles exist", false, jdepend.containsCycles());
    }
}
```
