## Active Directory (AD)

AD is Microsoft's proprietary database system that stores and manages domains, user information, credentials, computers, printers and other shared resources across an organizational network. Stores data as objects with unique distinguished name (DN) attribute. Helps organizations to locate objects throughout their digital infrastructure and carefully regulate who has access to what resources.

Without a directory:

- Users are required to provide username and password for each application
- IT admins would have to manually assign user to every application that needs to be accessed
- Updating credentials need to be performed across all applications

### Directory organization structure

Structure of LDAP directory:

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
