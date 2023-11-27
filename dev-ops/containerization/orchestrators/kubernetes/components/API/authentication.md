## Authentication

All requests to the API server have to include credentials, and the authentication layer is responsible for verifying them.

Kubernetes does not have its built-in identity database and hence, it is impossible to create user accounts. Nonetheless, the authentication layer is pluggable, and popular modules include client certs, webhooks, and integration with external identity management system such as AD and IAM.
