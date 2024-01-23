## Declarative design

No matter how model-driven our design is, we still end up writing procedures to produce the effect of the conceptual interactions. Assertions, intention revealing interfaces and other patterns can help, but can never give conventional OOP formal rigor.

Declarative design indicates a way to write a program as a kind of executable specification. In its various forms, this could be done through a reflection mechanism or at compile-time code generation i.e. producing code automatically based on the declaration.

However, its pitfalls include:

- A declarative language not expressive enough to do everything needed, but a framework that makes it difficult to extend the software beyond the automated portion
- Code generation techniques that cripple the iterative cycle by merging generated code into hand-written code, making regeneration very destructive

### Extending specifications in a declarative style

A specification is an adaptation of an established formalism i.e. is an example of a predicate. When using specifications, you quickly come across situations in which you would like to combine them.

As significant generalized capability is built into specifications, it becomes very useful to create an abstract class or interface that can be used for specifications of **all sorts**.

```java
public interface Specification {
    boolean isSatisfiedBy(Object candidate);
    Specification and(Specification other);
    Specification or(Specification other);
    Specification not();
}

public abstract class AbstractSpecification implements Specification {
    public Specification and(Specification other) {
        return new AndSpecification(this, other);
    }
    public Specification or(Specification other) {
        return new OrSpecification(this, other);
    }
    public Specification not() {
        return new NotSpecification(this);
    }
}

public class ContainerSpecification implements Specification {
    private ContainerFeature requiredFeature;

    public ContainerSpecification(ContainerFeature requiredFeature) {
        this.requiredFeature = requiredFeature;
    }

    boolean isSatisfiedBy(Object candidate){
        if (!candidate instanceof Container) return false;
        return (Container)aContainer.getFeatures().contains(requiredFeature);
    }
}

public class AndSpecification extends AbstractSpecification {
    Specification one;
    Specification other;
    public AndSpecification(Specification x, Specification y) {
        one = x;
        other = y;
    }
    public boolean isSatisfiedBy(Object candidate) {
        return one.isSatisfiedBy(candidate) && other.isSatisfiedBy(candidate);
    }
}

public class OrSpecification extends AbstractSpecification {
    Specification one;
    Specification other;
    public OrSpecification(Specification x, Specification y) {
        one = x;
        other = y;
    }
    public boolean isSatisfiedBy(Object candidate) {
        return one.isSatisfiedBy(candidate) || other.isSatisfiedBy(candidate);
    }
}

public class NotSpecification extends AbstractSpecification {
    Specification wrapped;
    public NotSpecification(Specification x) {
        wrapped = x;
    }
    public boolean isSatisfiedBy(Object candidate) {
        return !wrapped.isSatisfiedBy(candidate);
    }
}
```

### Subsumption

Subsumption is an operation that is used to compare two specifications directly to each other. **A more stringent specification subsumes a less stringent one**. It could take its place without any previous requirement being neglected. A new specification subsumes an old specification because any candidate that would satisfy the new specification would also satisfy the old, but not the other way around.

```java
public class MinimumAgeSpecification {
    int threshold;
    public boolean isSatisfiedBy(Person candidate) {
        return candidate.getAge() >= threshold;
    }
    public boolean subsumes(MinimumAgeSpecification other) {
        return threshold >= other.getThreshold();
    }
}

drivingAge = new MinimumAgeSpecification(16);
votingAge = new MinimumAgeSpecification(18);
assertTrue(votingAge.subsumes(drivingAge));
```

```java
// All men are mortal.
// Socrates is a man.
// Therefore socrates is mortal.

Specification manSpec = new ManSpecification();
Specification mortalSpec = new MortalSpecification();
assert manSpec.subsumes(mortalSpec);

Man socrates = new Man();
assert manSpec.isSatisfiedBy(socrates);

assert mortalSpec.isSatisfiedBy(socrates);
```
