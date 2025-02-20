## Clean code

- Code to be elegant and efficient
- Meaningful names
- Has unit and acceptance tests
- Straightforward logic to make it hard for bugs to hide
- Minimal dependencies to ease maintenance
- Complete error handling according to an articulated strategy (race conditions, memory leaks)
- Reduced duplication
- Early building of simply abstractions/interfaces
- Avoid using reflection i.e. getattr() and hasattr() in Python

## Naming

- Use intention-revealing names
- Avoid disinformation
- Make meaningful distinction
- Avoid redundant words i.e. table should never appear in a table name
- Use pronounceable names
- Use searchable names
- Avoid encodings
- Pick one word per concept i.e. avoid writing fetch, retrieve, and get methods in the same class
- Avoid using the same word for different purposes
- Use solution domain names i.e. CS terms, algorithm names, etc.
- Use problem domain names

### Class

- Should have noun or noun phrase i.e. Customer, WikiPage, Account
- Should not be a verb
- ATtributes should be lowercasing i.e. Student.name

### Method

- Should have verb or verb phrase names i.e. postPayment, deletePage, save

### Constants

- Name constants in uppercase i.e. config.SERVICE_NAME

## Classes

Reduce number of arguments
Keep the number of arguments low, and group them into meaningful objects if possible.

## Functions

- Should be small
- Indent level should not be greater than two
- Should do one thing and do it well, avoid flag arguments
- one level of abstraction per function
- Use descriptive names
- Flag/boolean arguments are ugly i.e. should have different functions handling them
- Should be pure i.e. no side effects
- Avoid output arguments in OOP as 'this' or 'self' is intended to act as an output argument i.e. report.appendFooter() rather than appendFooter(report)
- Separate command queries where functions should either do something or answer something, but not both i.e. set the value of an attribute and return True if successful
- Prefer exceptions to returning error codes
- Hide switch statements in Factory methods
- Dependent functions in a class should be read top-down i.e. top functions calling those below

### Should do one thing

Keep each function small, doing at most one thing (single responsibility principle) and doing it well. Having multiple responsibilities mean higher coupling, and we have to look deeper to find what we want which decreases productivity. Be explicit about its purpose. Separate command queries where functions should either do something or answer something, but not both.

### Should be deterministic

Functions should be deterministic. A deterministic function always returns the same results if given the same input values. For handling side effects (changing non-local state or non-deterministic output such as HTTP calls, IO operations, etc.), make them explicit and isolate them as much as possible.

### Avoid declaring dependencies implicitly, opt for dependency injection (DI)

Avoid declaring/instantiating dependencies in functions implicitly and mutating global variables, instead opting for DI. DI helps to achieve inversion of control (IoC) by decreasing coupling and increasing adhesion. Other benefits include making testing easier, improving application modularity, and increasing flexibility of configurable components.

### Reduce number of arguments

Keep the number of arguments low, and group them into meaningful objects if possible.

## Error handling

### Masking errors with logs

When a logger exists in a package, it’s tempting for people to log any errors and continue, with the original caller utterly unaware of the error. Hence, the best way to handle an error is to pass it up to the original caller. The original caller has the context of why the operation was performed e.g. retry, perform an alternative action, or log. What to do with an error should be decided where there is context, not deeply embedded within a utility package.

Logging at the caller level (when there are no more frames to return) is a good practice instead of logging at every stack level i.e. return error or log, but not both. Logging at every level causes a lot of noise in the application logs for little value. Errors further down the call stack can be wrapped with relevant information and returned. Wrap your errors until you are going to handle them, then log.

```go
func GetFoo() (string, error) {
    x, err := foo()
    if err != nil {
        // error should not be handled here as there is no context
        nil, return fmt.Errorf("foo: %w", err)
    }
    return x, nil
}

func ExecuteTask() {
    v, err := GetFoo()
    if err != nil {
        // original caller, error should be handled here
        log.Error(err)
    }
}
```

All library code should wrap errors liberally, and return them. The application using the package should have appropriate logging for those errors.

## Emergence

For creating well-designed software, four rules from Kent Beck are of significant help in order of importance:

1. Runs all the tests
2. Contains no duplication
3. Expresses the intent of the programmer
4. Minimizes the number of classes and methods

### Runs all the tests

A system that is comprehensively tested and passes all of its tests all of the time is a testable system. Systems that aren't testable aren't verifiable and should never be deployed.

Fortunately, making our systems testable pushes us toward a design where our classes are small and single purpose, that conform to SRP, and use principles such as DIP to minimize coupling. Writing tests leads to better designs.

### Refactoring

Once we have tests, we are empowered to keep our code and classes clean by incrementally refactoring the code.
