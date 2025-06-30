## Characterization tests

For writing tests for legacy code, our goal should not be finding and fixing all bugs, as we would never finish. Instead, one way of approaching this is to find out what the software is supposed to do (requirements) and then write tests based on those ideas. However, in nearly every legacy system, **what the system does is more important** than what it is supposed to do.

A characterization test is a test that characterizes/records the actual behavior of a piece of code. They are not tests that the software must live up to. Instead, they just sit there documenting what pieces of the legacy system really do. If we find something unexpected when we write them, it pays to get some clarification. A little algorithm for writing characterization tests is as follows:

1. Use a piece of code in a test harness
2. Write an assertion that you know will fail
3. Let the failure tell you what the behavior is
4. Change the test so that it expects the behavior that the code produces
5. Repeat

### Example

```java
// I know that PageGenerator does not produce fred
void testGenerator() {
PageGenerator generator = new PageGenerator(); assertEquals("fred", generator.generate());
}

/*
.F
Time: 0.01
There was 1 failure:
1) testGenerator(PageGeneratorTest) junit.framework.ComparisonFailure: expected:<fred> but was:<>
at PageGeneratorTest.testGenerator (PageGeneratorTest.java:9)
at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:39)
at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:25)
*/

// Now, i know it generates an empty string when instantiated
void testGenerator() {
PageGenerator generator = new PageGenerator(); assertEquals("", generator.generate());
}
```
