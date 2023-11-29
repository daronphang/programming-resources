## LDAP (Lightweight-Directory Access Protocol)

LDAP is a vendor-neutral software protocol used for accessing and managing a directory service such as Active Directory (AD). Facilitates the sharing of information on users, systems, networks, services, and applications. Allows individual users and applications to find and verify whatever information they need within their organization i.e. printers, access groups, organization structure, etc.

LDAP is not limited to, but widely used to build central authentication servers. These servers store usernames and passwords for all the users within a network. Any application/service can connect to the LDAP server to authenticate and authorize users.

LDAP directories typically contain data that is regularly accessed, but rarely changed. LDAP is designed to deliver exceptionally fast READ performance.

It is not a server, database, authentication procedure, credentials repository and network service; it is a set of rules that must be followed to talk to an external server/database. Data managed via LDAP are key/value pairs grouped in a hierachical structure.

### LDAP Authentication

LDAP authentication is the process of verifying usernames and passwords stored in a directory service, like OpenLDAP or Microsoft Active Directory. Administrators can create user accounts within a directory and grant them permissions.

When a user tries to access a resource, a request is sent to the LDAP authentication server. The LDAP server validates the entered username-password against the data in the directory. If there is a match, it then checks whether the user is authorized to access the requested resource.

### How LDAP Works

User must have an LDAP client installed on their device.

1. Client establishes a secure connection with the LDAP directory
2. Client send a search query to the directory for a specific request i.e. user's acccess group
3. LDAP directory authenticates the user
4. Search operation is performed within the directory, and the result of the request is returned

## AD (Active Directory)

AD is Microsoft's proprietary database system that stores and manages domains, user information, credentials, computers, printers and other shared resources across an organizational network. Stores data as objects with unique distinguished name (DN) attribute. Helps organizations to locate objects throughout their digital infrastructure and carefully regulate who has access to what resources.

Without a directory:

- Users are required to provide username and password for each application
- IT admins would have to manually assign user to every application that needs to be accessed
- Updating credentials need to be performed across all applications

### Directory Organization Structure

Structure of LDAD directory:

- ROOT
- Domain Component
- Organization Unit User/Group
- Common Name John

```
Root (Domain Component)
  Countries
       Organizations
            Organizational Units
                  Individuals

dc      domain component
o       Organization name
ou      Organization unit
cn      Common name
sn      Surname
dn      Distinguish name
User    User object

DN for an entry can be known starting from entry in question and traversing up the tree until hit root
i.e. uid=roger,ou=people,dc=example,dc=com
```

## LDAP vs AD

LDAP is an application protocol for querying and editing items in directory service providers like AD, which supports LDAP. Together, LDAP and AD make it possible for clients throughout businesses to access the information they need.

LDAP is the protocol or language that servers use to communicate with AD and similar directory services. LDAP allows you to seearch for someone or something without knowing the location. In a nutshell, **LDAP is a language to talk to directory services, and AD is one such directory service (proprietary)**. AD provides a database and services for identity and access management (IAM). LDAP can be used to create secretive policy i.e. some users have acccess to view certain files.
