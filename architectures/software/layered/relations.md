## Relating the layers

Layers are meant to be loosely coupled, with design dependencies in **only one direction**. Upper layers can use or manipulate elements of lower ones directly by calling their public interfaces, holding references to them, or using conventional means of interactions. However, when a lower-level object needs to communicate with its parent, mechanisms such as **callbacks or observers** can be used.

### UI

The grandfather of patterns for connecting the UI to the application and domain layers is MVC.

### Services

The infrastructure layer usually does not initiate action in the domain layer. Such technical capabilities are most often offered as services i.e. sending email.

### Application, Domain

The application and domain layers call on the services provided by the infrastructure layer. When the scope of a service has been well chosen and its interface well-designed, the caller can remain loosely coupled and uncomplicated by the elaborate behavior encapsulated by the interface.
