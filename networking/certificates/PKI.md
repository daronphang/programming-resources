## Public Key Infrastructure (PKI)

Public key infrastructure (PKI) **governs the issuance of digital certificates** to protect sensitive data, provide unique digital identities for users, devices and applications and secure end-to-end communications.

PKI encompasses everything used to establish and manage public key encryption. This includes software, hardware, policies, and procedures that are used to create, distribute, manage, store, and revoke digital certificates. PKI is used to ensure the **privacy of the message being sent** and to **verify that the sender is who they claim to be**.

PKI uses cryptographic public keys that are connected to a digital certificate, which authenticates the device or user sending the digital communication. Digital certificates are issued by a trusted source, a certificate authority (CA), and act as a type of digital passport to ensure that the sender is who they say they are.

A digital certificate cryptographically links a public key with the device or user who owns it. This helps to authenticate users and devices and ensure secure digital communications.

### Components

- **Certificate Authority (CA)**: A trusted entity that issues, stores and signs digital certificate
- **Registration Authority (RA)**: Verifies the identity of the user or device requesting the digital certificate
- **Certificate database**: Stores the digital certificate and its metadata
- **Central directory**: Secure location where the cryptographic keys are indexed and stored
- **Certificate management system**: system for managing the delivery of certificates as well as access to them
- Certificate policy: Outlines the procedures of the PKI

### How PKI works

Public key infrastructure uses asymmetric encryption methods to ensure that messages remain private and also to authenticate the device or user sending the transmission.

Asymmetric encryption involves the use of a public and private key. A cryptographic key is a long string of bits used to encrypt data.

Complex algorithms are used to encrypt and decrypt public/private key pairs. The **public key authenticates the sender of the digital message**, while the **private key ensures that only the recipient can open and read it**.

### PKI certificates

The core of a public key infrastructure is trust. It is important for a recipient entity to know without a doubt that the sender of the digital certificate is exactly who they claim to be.

**Digital certificates are also called PKI certificates or X.509 certificates**. PKI certificate includes the following:

- The subject domain name (for example, proton.me)
- The name of the issuing CA
- Issuing CA’s digital signature
- Additional subject domain names, including subdomains, if any
- The date of issue
- The expiry date
- The public key used to establish an encrypted connection for all subsequent data exchanges (server keeps private key secret)

### Why is PKI used?

- **TLS/SSL** for securing encrypted HTTP communications
- Email encryption and authentication of the sender
- Signing documents and software
- Using database servers to secure internal communications
- Securing web communications, such as e-commerce
- Authentication and encryption of documents
- Securing local networks and smart card authentication
- Encrypting and decrypting files
- Restricted access to VPNs and enterprise intranets
- Secure communication between mutually trusted devices such as IoT (internet of things) devices

### Types of open-source PKI

- EJBCA Enterprise
- OpenSSL
- CFSSL
- XiPKI
- Dogtag Certificate System
