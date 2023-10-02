## HATEOAS (Hypermedia as the Engine of Application State)

HATEOAS is a constraint of the REST application architecture. "Hypermedia" refers to any content that contains links to other forms of media such as images, movies and text.

REST architectural style lets you use the hypermedia links in the API response contents. It allows the client to dynamically navigate to the appropriate resources by transversing the hypermedia links. Navigation is conceptually the same as browsing through the web pages by clicking the relevant hyperlinks to achieve a final goal.

Typically when we perform a REST request, we only get the data and not any actions related to it, or operations that you can perform on the resources. This is where HATEOAS comes in and fills the gap.

### Why HATEOAS?

Most important reason is for loose coupling. If a consumer of a REST service needs to hard-code all the resource URLs, then it is tightly coupled with your service implementation.

Traditional API responses have no functionality present to allow an application to interact with the server through the response. HATEOS acts as a way to address this.

If you return the URLs, it could be used for the actions. There is no tight dependency on the URI structure. The client needs not have prior knowledge of the service or the different steps involved in a workflow.

Additionally, the backend decides which actions are available so that the UI does not need to know the business logic. For instance, if a bank account has no balance, the link to withdraw will be hidden.

```json
{
  "departmentId": 10,
  "departmentName": "Administration",
  "locationId": 1700,
  "managerId": 200,
  "links": [
    {
      "href": "10/employees",
      "rel": "employees",
      "type": "GET"
    }
  ]
}
```

```json
{
  "payroll": {
    "employee_number": "employee_123",
    "salary": 1000,
    "links": {
      "increment": "/payroll/employee_123/increment",
      "decrement": "/payroll/employee_123/decrement",
      "close": "/payroll/employee_123/close"
    }
  }
}
```

## Formats

### RFC 5988 (Web Linking)

Puts forward a framework for building links that define the relationships between resources on the web. Each link in RFC 5988 contains the following properties:

- Target URI: This is represented by the href attribute
- Link Relation Type: Describes how the current context (source) is related to the target resource (represented by the rel attribute)
- Attributes for target URI: extension link parameters including hreflang, media, title and type

### JSON Hypermedia API Language (HAL)

With HAL, you have a few categories of representations:

- Links: Specified as a combination of target URI and relation
- Embedded Resources: Other resources contained within a given REST resource
- State: The actual resource data

```json
{
  "links": {
    "self": { "href": "http://api.com/items" },
    "item": [
      { "href": "http://api.com/items/1" },
      { "href": "http://api.com/items/2" }
    ]
  },
  "data": [{ "shirt": 10 }, { "pants": 5 }]
}
```
