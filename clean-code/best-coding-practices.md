## Best coding practices

### Purpose

- Improve code quality and readability
- Increase efficiency
- Facilitate collaboration
- Ensure compatibility
- Reduce maintenance costs

### Standards

- Domain encapsulation with bounded contexts
- Abstract common functions as utilities (DRY)
- Use ubiquitous language
- Use design patterns where appropriate (factory, chain-of-responsibility, saga, decorator, singleton, etc.)
- Safeguard sensitive data with access control
- Create reader-friendly README files with documentation
- Don't be afraid to question existing code architecture or ask questions if you need help
- Find ways to optimize the code, don't code imperatively
- Take into account of memory management, performance and optimization i.e. chunks, compression
- SOLID principles (https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
- Code reviews for quality assurance (use this as a learning platform where we can exchange knowledge with each other)
- Continuous learning and improvement

### Angular

https://angular.io/guide/styleguide

## Writing clean code

Code that is clean must be:

- Elegant and efficient
- Has meaningful names
- Has unit and acceptance tests
- Straightforward logic to make it hard for bugs to hide
- Minimal dependencies to ease maintenance
- Complete error handling according to an articulated strategy (race conditions, memory leaks)
- Reduced duplication
- Early building of simply abstractions/interfaces

### Naming

- Use intention-revealing names
- Avoid disinformation
- Make meaningful distinction
- Avoid redundant words i.e. table should never appear in a table name
- Use pronounceable names
- Use searchable names
- Avoid encodings
- Pick one word per concept i.e. avoid writing fetch, retrieve, and get methods in the same class
- Avoid using the same word for different purposes
- Use solution domain names i.e. CS terms (composites, stacks, hashmaps), algorithm names (binarySearch, dfs, priority queues), etc.
- Use problem domain names

#### Methods

- Should have verb or verb phrase names i.e. postPayment, deletePage, saveCharts

#### Classes

- Should have noun or noun phrase i.e. Customer, WikiPage, Account
- Should not be a verb
- Attributes should be lowercasing i.e. Student.name

#### Constants

- Name constants in uppercase i.e. config.SERVICE_NAME

### Functions

- Should be small
- Indent level should not be greater than two
- Should do one thing and do it well, avoid flag arguments
- one level of abstraction per function
- Use descriptive names
- Flag/boolean arguments are ugly i.e. should have different functions handling them
- Should be pure i.e. maintain idempotency
- Should not have any side effects i.e. doing things that are not part of its responsibility
- Avoid output arguments (anything that gets modified or mutated but is not returned) in OOP as 'this' or 'self' is intended to act as an output argument i.e. report.appendFooter() rather than appendFooter(report)
- Separate command queries where functions should either do something or answer something, but not both i.e. set the value of an attribute and return True if successful
- Prefer exceptions to returning error codes
- Bury switch statements in an abstract factory class to not violate OCP (Open Closed Principle) i.e. different types of Employees
- Dependent functions in a class should be read top-down i.e. top functions calling those below
- Number of arguments should be as minimum as possible (group them into meaningful objects if possible)

### Classes

- Should be small (measured in terms of responsibilities)
- Should follow SRP (Single Responsibility Principle) that a class or module should have one reason to change
