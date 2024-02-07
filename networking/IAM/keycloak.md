## Keycloak

Keycloak is an open-source software solution designed to provide single sign-on access to applications and services i.e. **open source Identity and Access Management (IAM)**. It allows users to authenticate once and access multiple applications without needing to re-enter their credentials.

Security features that developers normally have to write for themselves are provided out of the box and are easily tailorable to the individual requirements of your organization. Keycloak provides customizable user interfaces for login, registration, administration, and account management. You can also use Keycloak as an integration platform to hook it into existing LDAP and Active Directory servers. You can also delegate authentication to third party identity providers like Facebook and Google.

### Features

- SSO (sign-in and sign-out) for browser applications
- Multiple protocols support i.e. OpenID Connect, OAuth 2.0, SAML 2.0
- Identity Brokering
- Social login
- User federation (sync users from LDAP and AD servers)
- Kerberos bridge (automatically authenticate users that are logged-in to a Kerberos server)
- Account Management console that allows users to centrally manage their account
- 2FA support
- Login flows i.e. user self-registration, recover password, verify email, etc.
- Session management
- CORS support

### Operations

Keycloak is a separate server that you manage on your network. Applications are configured to point to and be secured by this server. Keycloak uses open protocol standards like **OpenID connect or SAML2.0** to secure your applications.

Browser applications redirect a user's browser from the application to the Keycloak authentication server where they enter their credentials. Applications instead are given an identity token or assertion that is cryptographically signed. These tokens can have identity information like username, address, email, and other profile data. They can also hold permission data so that applications can make authorization decisions. These tokens can also be used to make secure invocations on REST-based services.
