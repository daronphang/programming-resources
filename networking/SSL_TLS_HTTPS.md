## SSL (Secure Sockets Layer)

Standard technology for keeping an internet connection secure, safeguarding sensitive data that is being sent via packets between two systems, and preventing attackers from reading and modifying data that is transferred. Data exchange applies between client to client, client to server, and server to server. Browsers will only trust SSL certificates issued by authorized issuers (Certificate Authorities) such as DigiCert. For organizations that want to offer services encrypted by TLS, they have to prove to CAs of their legitimacy and that they control the domain.

### How SSL Works

Encryption uses asymmetrical cryptography which requires public and private keys. Both keys are related to each other by complex mathematical formula that is difficult to reverse-engineer by brute force.

### Self-Signed vs CA (Certificate Authority)

|            | Self-Signed                                                                                | CA                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Definition | Created, signed, and issued by the subject of the certificate (the entity it is issued to) | Created, signed and issued by a third party called CA that is authorized to validate the identity of the applicant |
| Usage      | Private networks/Intranet                                                                  | Public networks to build trust among website visitors                                                              |
| Signature  | Signed by your own private keys                                                            | Signed by third parties including Sectigo, Symantec, Digicert, Thawte, GeoTrust, GlobalSign, GoDaddy, and Entrust  |

## TLS (Transport Layer Security)

An updated, more secure version of SSL (SSL successor). Asymmetrical cryptography requires significant computing resources; encrpyting all information would be expensive. TLS gets around this by using it at beginning of communications session whereby the server and client agrees on single session key that will be used to encrypt packets from that point forward. Session/shared key is established using asymmetrical cryptography, and data is encrypted with shared key which uses symmetrical crpytography and is much less computationally intensive. Session keys are only used once.

## TLS Handshake

1. Client contacts server and requests a secure connection and server responds with list of cipher suites.
2. Cipher suites are a collection of algorithms that work together to securely encrypt connection with website.
3. Client compares against its own cipher suites, decides on one that is mutually supported and informs server.
4. Server provides its digital certificate issued by third-party authority confirming the server's identity which contains public key.
5. Client sends a random string and premaster secret (random string) that is encrypted with public key and server decrypts with private key.
6. Server also sends random string to client.
7. TLS Handshake is established whereby both client/server use client random, server random and premaster secret to generate session keys.
8. Session keys generated are client write key, server write key, client write MAC key, and server write MAC key.
9. Client uses its session write key to encrypt data, and server decrypts using same key (symmetric cryptography).

## HTTPS

Hyper Text Transfer Protocol secure. Appears in URL when a website is secured by an SSL/TLS certificate.
