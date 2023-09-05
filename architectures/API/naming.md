## API Naming Conventions

### Use nouns to represent resources, not verbs

Always make sure that your URIs are named with nouns to specify the resource instead of using verbs. They should not indicate any CRUD operations as they should already be specified in the HTTP request (GET, POST, PUT, PATCH, DELETE). Start from the fact that the **resource is the document**, not the side effect that you want the document to have.

```
http://localhost:8000/api/v1/users/{id}
http://localhost:8000/api/v1/store/prices/{order-id}
```

For non-CRUD operations, you can execute them as **controllers**. A controller resource models a procedural concept. Controller resources are like executable functions, with parameters and return values; inputs and outputs. Like a traditional web application’s use of HTML forms, a REST API relies on controller resources to perform application-specific actions that cannot be logically mapped to one of the standard methods (create, retrieve, update, and delete, also known as CRUD). Controller names typically appear as the last segment in a URI path, with no child resources to follow them in the hierarchy.

POST should be used to create a new resource within a collection and execute controllers.

```
PATCH engines/123 "activate"
PUT engines/123/state "active"
POST engines/123/activation null

PATCH engines/123 "deploy"
PUT engines/123/state "before-deploy"
POST engines/123/execution null
```

### Use pluralized nouns for resources

Use plural when possible unless they are singleton resources.

```
http://api.example.com/v1/store/employees/{emp-id}/address
```

### Avoid using file extensions

They are unncessary and add length and complexity to URIs.

### Version your APIs

Always attempt to version your APIs. You can provide an upgrade path without making any fundamental changes to the existing APIs.
