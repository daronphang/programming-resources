## Background

The Internet is an insecure place. Many of the protocols used in the Internet do not provide any security. Tools to "sniff" passwords off of the network are in common use by malicious hackers. Thus, applications which send an unencrypted password over the network are extremely vulnerable.

## Kerberos

Kerberos is the computer network authentication protocol that was developed at MIT and is based on the Needham-Schroeder authentication protocol. The idea behind Kerberos is to authenticate users while preventing passwords from being sent over the internet. The Kerberos protocol uses strong cryptography so that a client can prove its identity to a server (and vice versa) across an insecure network connection. After a client and server has used Kerberos to prove their identity, they can also encrypt all of their communications to assure privacy and data integrity as they go about their business.

Kerberos can be viewed as a security system that assists clients in setting up a secure channel with any server that is part of a distributed system. Security is based on shared secret keys.

### Components

Kerberos uses symmetric key cryptography and a trusted third-party, the **key distribution center (KDC)**, to authenticate and verify user identities. A KDC involves three aspects:

- **Ticket-Granting service (TGS)** that setups secure channels and connects the user with the service server (SS) through issuing tokens (proof that the client is authenticated)
- A **Kerberos database** that stores the password and identification of all verified users
- An **authentication server (AS)** that performs the initial authentication

### How it works

1. Authentication Server Request: The client requests authentication from KDC. This authentication request would be in plain text
2. Authentication Server Response: KDC sends a TGT and a session key if the client exists in the database. If the client is not in the database, the authentication fails
3. Service Ticket Request: The client asks for the service ticket along with the TGT sent earlier by the KDC
4. Service Ticket Response: KDC sends the ticket encrypted with the session key. The client can use the session key sent earlier by KDC to decrypt the service ticket.
5. Application Server Request: The client requests the application server for access using the service ticket
6. Application Server Response: The application server authenticates the client. It sends a ticket that will grant access to that particular service

## Use cases

### Single Sign-On (SSO)

Kerberos enables users to authenticate once and obtain a ticket, known as a Kerberos ticket-granting ticket (TGT). This TGT can be used to request service tickets for various resources without repeatedly providing credentials. This SSO capability improves user convenience and reduces the need for managing multiple passwords.

### Network authentication

Kerberos provides a secure mechanism for verifying the identity of network services, such as servers and applications. Clients can request a service ticket from the Key Distribution Center (KDC) using their TGT, and the service ticket is used to authenticate and establish a secure session with the requested service.

### Mutual authentication

Kerberos ensures mutual authentication, meaning both the client and the server authenticate each other during the initial authentication process. This prevents impersonation and man-in-the-middle attacks by verifying the authenticity of both parties involved in the communication.

### Authorization

Kerberos can also be used to enforce access control policies. Once a client is authenticated, the Kerberos ticket includes information about the client's identity and access permissions. Servers can use this information to enforce authorization rules and grant or deny access to specific resources based on the client's privileges.
