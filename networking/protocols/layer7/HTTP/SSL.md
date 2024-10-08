## SSL (Secure Sockets Layer)

Standard technology for keeping an internet connection secure, safeguarding sensitive data that is being sent via packets between two systems, and preventing attackers from reading and modifying data that is transferred. Data exchange applies between client to client, client to server, and server to server. Browsers will only trust SSL certificates issued by authorized issuers (Certificate Authorities) such as DigiCert. For organizations that want to offer services encrypted by TLS, they have to prove to CAs of their legitimacy and that they control the domain.

### SSL Certificate

SSL certificates includes the following information in a single data file:

- Domain name that the certificate was issued for
- Which person, organization or device it was issued to
- Which certificate authority issued it
- Associated subdomains
- Issue date of certificate
- Expiration date of certificate
- Public key (private key is kept secret in the server)

The certificate is hosted on a website's origin server, and is sent to any devices that request to load the website. The public and private keys are used for encrypting and signing data. Data encrypted with the public key can only be decrypted with the private key.

### SSL Encryption

Encryption uses asymmetrical cryptography which requires public and private keys. Both keys are related to each other by complex mathematical formula that is difficult to reverse-engineer by brute force.

### How SSL Certificates Work

1. A browser/server attempts to connect to a website secured with SSL
2. Browser/server requests that the web server identifies itself
3. Web server sends the browser/server a copy of its SSL certificate
4. Browser/server checks to see whether it trusts the SSL certificate and signals to the web server
5. Web server then returns a digitally signed acknowledgement to start an SSL encrypted session
6. Encrypted data is shared between the browser/server and the web server during the session
