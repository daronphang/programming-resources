## Overview

Design patterns are reusable solutions to commonly occurring problems in software design. It is rarely the case that the problems we solve or systems we build are truly unique. Patterns allow us to learn from the mistakes of others. They are proven solutions, easily reusable and expressive. They lower the size of your codebase, prevent future refactoring, and make your code easier to understand by other developers.

Design patterns should be used to solve specific problems or improve aspects like maintainability, scalability, or performance. However, misuse or over-engineering can lead to undesirable effects such as unnecessary complexity, overhead on performance or spawning of new anti-patterns. Hence, don't commit to patterns until there is a real need. Use patterns only if they improve clarity, not just because they are trendy.

Design patterns are all about increasing abstraction in code and hence, objects have less dependencies between them. However, every extra layer of indirection will open up more places for developers to change code. Patterns are best in the hands of framework designers i.e. events as Observer pattern, Prototype pattern in JS, MVC pattern in server-side web frameworks.

The power of design patterns is in communication i.e. easier to say 'use a factory pattern' rather than describing in code. Moreover, these patterns are most likely being used in code long before you knew they had names. When coding web services, most likely are using Facade pattern.

### Creational

Focus on handling object creation mechanisms by controlling the creation process. A basic object creation approach in a program can lead to an added complexity. Patterns include Constructor, Factory, Prototype, Singleton, etc.

### Structural

Deal with object relationships. They explain simple ways to assemble objects and classes into larger structures. Help to ensure that when one part of system changes, the entire structure of system does not need to do the same, keeping them flexible and efficient. Patterns include Module, Decorator, Facade, Adapter, Proxy, etc.

### Behavioral

Patterns focus on improving communication and assignment of responsibilities between dissimilar objects in a system. Patterns include Chain of Responsibility, Command, Observer, Iterator, Strategy, Template, etc.

### Concurrency

Deal with multi-threaded programming paradigms; examples include Active Object, Nuclear Reaction and Scheduler.

### Architectural

Examples include Model-View-Controller, Model-View-Presenter, and Model-View-ViewModel.

## Pragmatics on design patterns

Perspectives from Martin Fowler:

- The term 'best practices' or 'design principles' should be avoided, but having good ideas for a given context is valid
- There are no free lunches, **all abstractions come at a cost**

Design principles should:

- Be violated sometimes
- Are often at odds with each other
- Often mixed together for something even better when used in isolation
- Often overlap with other ones

By calling something a principle, when you are pragmatic you will most likely violate it. Instead, replace the term 'principle' with 'guideline'.

Whether we call something a principle or a guideline, the ability to make an **informed decision to disregard a design principle** is a good place to strive towards.
