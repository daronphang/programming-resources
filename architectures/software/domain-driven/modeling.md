## Modelling

In domain-driven design, the uses that determine the choice of a model are:

- The model dictates the form of the design of the heart of the software (intimate link between model and implementation that makes the model relevant)
- Binding of a model and implementation helps maintenance and continuing development as the code can be interpreted based on understanding the model
- Model is the backbone of a language used by all team members; developers can communicate with domain experts without translation
- The model is distilled knowledge i.e. agreed-upon way of structuring domain knowledge, and distinguishing the elements of most interest
- A model captures how we choose to think about the domain as we select terms, break down concepts, and relate them
- Models must evolve, be practical and useful in making sense of the domain, yet be simple to implement and understand

Ultimately, one model should underlie implementation, design and team communication. Having separate models for these purposes poses a hazard. Domain-driven design calls for a model that is the very foundation of the design.

### The centrality of domain functionality

The heart of software is its ability to solve domain related problems for the user, and all other features support this basic purpose. When the domain is complex, developers have to steep themselves in the domain to build up knowledge of the business i.e. PCB design. They must **hone their modeling skills and master domain design**.

Yet, this is not the priority on most software projects. Most developers do not have much interest in learning about the specific domain they are working in, much less making a major commitment to expand their domain modeling skills. Leaders who understand the centrality of the domain can put their software project back on course when enthusiastic developers get caught up in develop elaborate technical frameworks that do not serve, or actually get in the way of domain development, while development of a model that reflects deep understanding of the domain is lost in the shuffle.

### Crunching knowledge

Effective domain modelers are knowledge crunchers, likewise financial analysts crunch numbers. They take a torrent of information and probe for the relevant trickle. They try one organizing idea after another, searching for the simple view that makes sense of the mass. Success comes in an emerging set of abstract concepts that make sense of all the detail.

Crunching knowledge involves brainstorming, refining, questioning, and explaining together with domain experts. The model developed along with the developer's understanding of the domain and their understanding of how the model would play into the solution.

### Communication and use of language

Domain experts have limited understanding of the technical jargon of software development, and vice versa. On a project without a common language, developers have to translate for domain experts and vice versa. **Translation is always inaccurate and hides and disconnects in understanding between the domain experts and developers**. Translation muddles model concepts, which leads to destructive refactoring of code.

It is a serious problem when the language used on a project is **fractured** i.e. domain experts use their jargon while developers use their own language. The overhead cost of all the translation and risk of misunderstanding is too high.

A project needs a common language of which the **domain model can provide the backbone for**. The vocabulary includes the names of classes and prominent operations. This same model should provide the language for developers and domain experts to communicate with each other.

### Model-driven design

If the design, or some central part of it, does not map to the conceptual domain model, that model is of little value, and the correctness of the software is suspect. At the same time, complex mappings between models and design functions are difficult to understand, and, in practice, impossible to maintain as the design changes. A deadly divide opens between analysis and design so that insight gained in each of those activities does not feed into the other.

Model-driven design discards the dichotomy of analysis model versus design to search out a single model that serves both purposes. Each object in the design plays a conceptual role described in the model.

Design a portion of the software system to reflect the domain model in a very literal way, so that mapping is obvious. Revisit the model and modify it to be implemented more naturally in software. To do this usually requires software development tools and languages that support a modeling paradigm, such as **object-oriented programming**.

When a design is based on a model that reflects the basic concerns of the users and domain experts, the bones of the design can be revealed to the user to a greater extent than with other design approaches. Revealing the model gives the user more access to the potential of the software and yields consistent, predictable behavior.
