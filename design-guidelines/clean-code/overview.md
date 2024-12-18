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
