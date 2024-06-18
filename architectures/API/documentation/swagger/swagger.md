## Swagger

Machine-readable API descriptions are ubiquitous nowadays and OpenAPI is the most broadly adopted industry standard for documenting, describing, producing, consuming and visualizing RESTful APIs.

Specific format used to write OpenAPI documents is either YAML or JSON. Permits developers to define their API's essentials including:

- Present endpoints and each endpoint's operations
- Input and output operation parameters
- Authentication techniques

https://spec.openapis.org/oas/v3.1.0

### Development

- Swagger Editor to create OAS definition and SwaggerCodegen to generate server implementation.
- Swagger UI to visualize and document OAS definition
- SwaggerHub to design, document and develop APIs as a team (single source of truth).

https://swagger.io/tools/open-source/getting-started/

### Structure

May be a single document or divided into multiple, connected parts. Recommended that the root document is named openapi.json.

### Reusable Components

Reusable components are defined in the global components section, and are then referenced in the individual endpoints.

```
Schemas (data models)
Parameters
Request Bodies
Responses
Response Headers
Examples
Links
Callbacks
```

### Example

```yaml
openapi: 3.0.0
info:
  version: 1.0.0
  title: Simple API
  description: A simple API to illustrate OpenAPI concepts

servers:
  - url: https://example.io/v1

security:
  - BasicAuth: []

paths:
  /artists:
    get:
      description: Returns a list of artists
      parameters:
        - $ref: "#/components/parameters/PageLimit"
        - $ref: "#/components/parameters/PageOffset"
      responses:
        "200":
          description: Successfully returned a list of artists
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Artist"
        "400":
          $ref: "#/components/responses/400Error"
    post:
      description: Lets a user post a new artist
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Artist"
      responses:
        "200":
          description: Successfully created a new artist
        "400":
          $ref: "#/components/responses/400Error"

  /artists/{username}:
    get:
      description: Obtain information about an artist from his or her unique username
      parameters:
        - name: username
          in: path
          required: true
          schema:
            type: string

      responses:
        "200":
          description: Successfully returned an artist
          content:
            application/json:
              schema:
                type: object
                properties:
                  artist_name:
                    type: string
                  artist_genre:
                    type: string
                  albums_recorded:
                    type: integer

        "400":
          $ref: "#/components/responses/400Error"

components:
  securitySchemes:
    BasicAuth:
      type: http
      scheme: basic

  schemas:
    Artist:
      type: object
      required:
        - username
      properties:
        artist_name:
          type: string
        artist_genre:
          type: string
        albums_recorded:
          type: integer
        username:
          type: string

  parameters:
    PageLimit:
      name: limit
      in: query
      description: Limits the number of items on a page
      schema:
        type: integer

    PageOffset:
      name: offset
      in: query
      description: Specifies the page number of the artists to be displayed
      schema:
        type: integer

  responses:
    400Error:
      description: Invalid request
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
```
