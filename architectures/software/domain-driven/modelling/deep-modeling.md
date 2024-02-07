## Deep Modeling

A deep model has power because it contains the central concepts and abstractions that can succinctly and flexibly express essential knowledge of activities of the users, their problems and their solutions.

Many transformations of domain models and the corresponding code take the form of recognizing a concept that has been hinted at implicitly, and representing it with one or more **explicit** objects or relationships in the model. Nonetheless, this requires experimentation to understand what works and doesn't.

### Making implicit concepts explicit

**Listen to the language the domain experts use**. When the users or domain experts use vocabulary that is nowhere in the design, that is a warning sign.
The ubiquitous language is made of the vocabulary that pervades speech, documents, model diagrams, and code. If a term is absent from the design, it is an **opportunity** to improve the model and design by including it.

### Explicit constraints

Constraints make up an important category of model concepts. They often emerge implicitly, but expressing them explicitly can greatly improve a design.

Factoring the constraint into its own method allows us to give it an intention revealing name that makes the constraint explicit in our design. It also gives the constraint room for more complex rules.

```java
// implicit constraint
classBucket {
    private float capacity;
    private float contents;
    public void pourIn(float addedVolume) {
        if (contents + addedVolume > capacity) {
            contents = capacity;
        } else {
            contents = contents + addedVolume;
        }
    }
}

// explicit constraint
classBucket {
    private float capacity;
    private float contents;
    public void pourIn(float addedVolume) {
        float volumePresent = contents + addedVolume; contents = constrainedToCapacity(volumePresent);
    }
    private float constrainedToCapacity(float volumePlacedIn) {
        if (volumePlacedIn > capacity) return capacity;
        return volumePlacedIn;
    }
}
```

However, there are cases when a constraint can't fit comfortably in a single method i.e. calling on information that the object does not need for its primary responsibility. The following may **distort the design of its host object**:

- Evaluating a constraint requires data that does not otherwise fit the object’s definition
- Related rules appear in multiple objects, forcing duplication or inheritance between objects that are not otherwise a family
- A lot of design and requirements conversation revolves around the constraints, but in the implementation, they are hidden away in procedural code

When the constraints are obscuring the object’s basic responsibility, or when the constraint is prominent in the domain yet not prominent in the model, you can **factor it out into an explicit object** or even model it as a set of objects and relationships.
