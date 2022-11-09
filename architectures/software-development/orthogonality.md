## Orthogonality (Modular/Layered)

Critical concept if you want to produce systems that are easy to design, build, test and extend. Refers to a kind of independence or decoupling. Two or more things are orthogonal if changes in one do not affect any of the others i.e. user interface and database code. However, non-orthogonal systems are inherently more complex to change and control, with components being highly interdependent on each other.

## Benefits

### Productivity Gain

- Development and testing times are reduced as changes are localized
- Easier to write small, self-contained components than a large block of code
- Promotes reuse if components have specific, well-defined responsibilities

### Reduced Risk

- Diseased sections of code are isolated
- Resulting system is less fragile and better tested

## Coding

- Keep code decoupled by writing shy code i.e. modules that don't reveal anything unnecessary to others, and that don't rely on other modules' implementations
- Avoid global data, or use Singleton pattern to ensure one instance of an object
- Avoid similar functions
