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
