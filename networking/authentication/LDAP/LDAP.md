## Lightweight-Directory Access Protocol (LDAP)

LDAP is a vendor-neutral software protocol used for accessing and managing a directory service such as Active Directory (AD). Facilitates the sharing of information on users, systems, networks, services, and applications. Allows individual users and applications to find and verify whatever information they need within their organization i.e. printers, access groups, organization structure, etc.

LDAP is not limited to, but widely used to build central authentication servers. These servers store usernames and passwords for all the users within a network. Any application/service can connect to the LDAP server to authenticate and authorize users.

LDAP directories typically contain data that is regularly accessed, but rarely changed. LDAP is designed to deliver exceptionally fast READ performance.

It is not a server, database, authentication procedure, credentials repository and network service; it is a set of rules that must be followed to talk to an external server/database. Data managed via LDAP are key/value pairs grouped in a hierarchical structure.

### Authentication

LDAP authentication is the process of verifying usernames and passwords stored in a directory service, like OpenLDAP or Microsoft Active Directory. Administrators can create user accounts within a directory and grant them permissions.

When a user tries to access a resource, a request is sent to the LDAP authentication server. The LDAP server validates the entered username-password against the data in the directory. If there is a match, it then checks whether the user is authorized to access the requested resource.

### How LDAP works

User must have an LDAP client installed on their device.

1. Client establishes a secure connection with the LDAP directory
2. Client send a search query to the directory for a specific request i.e. user's access group
3. LDAP directory authenticates the user
4. Search operation is performed within the directory, and the result of the request is returned

### Directory entry

Implementing an LDAP directory service proceeds in much the same way as implementing a naming service e.g. DNS.

<table>
<tr>
<th>Attribute</th>
<th>Abbreviation</th>
<th>Value</th>
</tr>
<tr>
<td>Country</td>
<td>C</td>
<td>NL</td>
</tr>
<tr>
<td>Locality</td>
<td>L</td>
<td>O</td>
</tr>
<tr>
<td>Organization</td>
<td>O</td>
<td>VU University</td>
</tr>
<tr>
<td>OrganizationalUnit</td>
<td>OU</td>
<td>Computer Science</td>
</tr>
<tr>
<td>CommonName</td>
<td>CN</td>
<td>Main Server</td>
</tr>
<tr>
<td>FTP_Server</td>
<td>-</td>
<td>137.37.20.3, 130.37.24.6</td>
</tr>
</table>

### Searching

LDAP allows users to search for a directory entry given a set of criteria that attributes of the searched entries should meet.

```
search(“(C=NL)(O=VU University)(OU=*)(CN=Main server)”)
```

Searching in a directory service is generally an expensive operation. We will generally need to access several leaf nodes in a directory information tree (DIT). However, by allowing several trees to co-exist, we can create a forest of LDAP domains.

## LDAP vs AD

LDAP is an application protocol for querying and editing items in directory service providers like AD, which supports LDAP. Together, LDAP and AD make it possible for clients throughout businesses to access the information they need.

LDAP is the protocol or language that servers use to communicate with AD and similar directory services. LDAP allows you to search for someone or something without knowing the location. In a nutshell, **LDAP is a language to talk to directory services, and AD is one such directory service (proprietary)**. AD provides a database and services for identity and access management (IAM). LDAP can be used to create secretive policy i.e. some users have access to view certain files.
