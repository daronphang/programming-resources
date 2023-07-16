## SAML (Security Assertion Markup Language)

SAML is an open standard used for exchanging authentication and authorization data between SP (Service Provider) and IP (Identity Provider). Its primary role in online security is that it enables you to access multiple web applications using one set of credentials (interoperability). It is a widely accepted way to communicate a user's identity to cloud service providers.

SAML is an XML-based (SOAP) open single sign-on (SSO) standard for transferring identity data between an SP and IP. Hence, you can use one set of credentials to log into many different websites.

Most organizations already know the identity of users as they are logged in to their Active Directory domain or intranet. Hence, it makes sense to use this information to log users into external services.

### Background

The technology industry created SAML to simplify the authentication process where users needed to access multiple independent web applications across domains. Prior to SAML, SSO was achievable but relied on cookies that were only viable within the same domain. It achieves this objective by centralizing user authentication with an identity provider. Web applications can then leverage SAML via the identity provider to grant access to their users. It also benefits service providers as it increases security of their own platform, primarily by avoiding the need to store (often weak and insecure) passwords and not having to address forgotten password issues.

## Parties

### Principal/Subject

A human user who is trying to access a cloud-hosted application.

### Identity Provider

A cloud software service that stores and confirms user identity, typicall through a login process. Identity Provider performs authentication and passes the user's identity and authorization level to the service provider i.e. Auth0.

### Service Provider

Service Provider trusts the IdP and authorizes the given user to access the requested resource that could be internal or external i.e. Salesforce, Jira, AWS, Expensify, etc.

### How Does SAML Work?

User's identity is exchanged via digitally signed XML documents.

- User tries to access a resource from SP
- SP responds by generating a SAML request
- Browser redirects user to an SSO URL provided by IdP
- IdP parses the SAML request and authenticates the user (skipped if user is authenticated)
- IdP generates an encoded SAML response and returns it to the browser
- Browser sends SAML response to SP for verification
- If verification is successful, user will be logged into the SP

## Benefits

### Improved user experience

Users only need to sign in one time to access multiple service providers. This allows for faster authentication process and less expectation of the user to remember multiple login credentials for every application.

### Increased security

SAML provides a single point of authentication, which happens at a secure Service Provider. SAML then transfers the identity information to the service providers. This form of authentication ensures that credentials are only sent to the IdP directly.

### Loose coupling of directories

SAML doesn't require user information to be maintained and synchronized between directories.
