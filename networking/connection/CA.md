## Certificate Authority (CA)

A website wants to communicate with you securely. In order to prove its identity and make sure it is not an attacker, you must have the server's public key. However, you can't store all keys from all websites, and the solution is CA.

A CA is a trusted organization that can issue a **digital certificate** i.e. GlobalSign, DigiCert, GoDaddy. TLS/SSL makes a connection secure by validating SSL/TLS certificate. Digital certificates are data files used to cryptographically link an entity with a public key. A digital certificate provides:

- Authentication by serving as a credential to validate the identity of the entity that it is issued to
- Encryption for secure communication over insecure networks
- Integrity of the documents signed with the certificate

When you install and OS or browser, a list of trusted CAs will come with it. In this list, the CA's public keys are also stored.

If one of the CAs you trust is compromised, an attacker can use the stolen private key to sign a certificate for any website they like. The client will not know that the public key is forged.

### How digital certificates are generated

1. The applicant for a digital certificate generates a key pair consisting of public key and private key (not shared with anyone else including CA)
2. The applicant generates a certificate signing request (CSR) which is an encoded text file containing the public key and other information about the entity i.e. domain name, organization, address, etc.
3. The CSR is sent to the CA who verifies the information and digitally signs the certificate with an issuing private key
4. The signed certificate is sent back to the applicant
5. When the signed certificate is presented to a third party, the recipient can cryptographically confirm the CA's digital signature via the CA's public key

### Chain of trust

In a chain of trust, certificates are issued and signed by certificates that live higher up in the hierarchy. It consists of several parts including:

- Trust anchor
- At least one intermediate certificate
- End-entity certificate

#### Trust anchor (root certificate)

The root CA serves as the trust anchor in a chain of trust. The validity of this trust anchor is vital to the integrity of the chain a a whole.

The root certificate (along with private key) is treated with the highest level of security and is usually stored offline in a protected facility.

#### Intermediate certificate

The trust anchor has the ability to sign and issue intermediate certificates. Intermediate certificates provide a flexible structure for conferring the validity of the trust anchor to additional intermediate and end-entity certificates in the chain.

Intermediate certificates serve an administrative function; each intermediate can be used for a specific purpose i.e. issuing SSL/TLS certificates, confer the root CA's trust to other organizations, etc.

They also provide a buffer between end-entity certificate and root CA, protecting the private root key from compromise. For publicly trusted CAs, the CA baseline requirements prohibit issuing end-entity certificates directly from the root CA, which must be kept securely offline.

#### End-entity certificate (SSL certificate)

An end-entity certificate is the final link in the chain of trust. It serves to confer the root CA's trust, via any intermediates in the chain, to an entity such as a website, company or person.

An end-entity certificate differs from a trust anchor or intermediate certificate in that it cannot issue additional certificates.

## CA bundle

CA Bundle is the file that contains root and intermediate certificates i.e. issued for server's domain. It is used to verify the authenticity of SSL certificates presented by a web server during SSL/TLS handshake. The browser/client uses the CA bundle to verify the chain of trust from the website's SSL certificate up to a trusted root CA. The chain is required to improve the compatibility of the certificates with web browsers, email clients and mobile devices.

A missing intermediate is one of the most common causes of SSL connection errors. To avoid this issue, need to **import the right file**, and the certificates **must be in the correct order**.

To extract certificate from browser, the certificate can be downloaded in .pem format. Can also be done with openssl.

```
# Locations of crt in Linux
/etc/cert-bundle.crt
/etc/pki/tls/certs/ca-bundle.crt
/etc/ssl/certs
```

### ca-bundle.crt

Contains a list of CA certificates trusted for TLS server authentication usage without distrust information.

### ca-bundle.trust.crt

Contains a list of CA certificates which includes trust (and/or distrust) flags specific to certificate usage i.e. **with extended validation**. Has extended BEGIN/END TRUSTED CERTIFICATE file format.

### Creating CA bundle

When your domain has been validated by CA, you will receive an SSL certificate (yourdomain.crt), a root certificate and intermediate certificates.

The CA bundle file should contain codes in the following order:

1. Intermediate CA Certificate 2
2. Intermediate CA Certificate 1
3. Root CA Certificate

Save the file as ca-bundle.crt, and paste the file in CABUNDLE field on your server.

## Certificate verification (curl)

libcurl performs peer SSL certificate validation by default. This is done by using a CA certificate store that the SSL library can use.

Verification will fail for the following:

- The remote server uses a self-signed certifiate
- No CA cert store is installed
- Server uses a cert signed by a CA that is not included in the store

To successfully validate, can perform the following:

- Ignore verification with --insecure
- Add CA cert for your server to the existing default CA cert store. Can be changed at compile time with configure options of --with-ca-bundle=FILE or --with-ca-path=PATH (files must be concatenated in PEM format)

## Installing in CA Trust Store

To install a certificate in the trust store, it must be in PEM format i.e. BEGIN CERTIFICATE and END CERTIFICATE in human-readable format.

```bash
$ sudo apt-get install -y ca-certificates
$ sudo cp your-ca.crt /usr/local/share/ca-certificates
$ sudo update-ca-certificates
```

### Environment variables

```
CURL_CA_BUNDLE      For curl, specify own CA cert file
REQUESTS_CA_BUNDLE  For Python requests
```

CA trust store generated by update-ca-certificates is available at:

- /etc/ssl/certs/ca-certificates.crt (single PEM bundle, includes both certificates provided by distribution and user-added)
- /etc/ssl/certs (as an OpenSSL directory)

## Self-signed certificate

However, a CA might be too expensive or complicated for testing websites in development. This is where self-signed certificates come in. A self-signed certificate is a TLS/SSL certificate that is signed by the person who creates it rather than a trusted CA. Open source tools for generating certificates include OpenSSL, EasyRSA, CFSSL, Lemur, etc.

To sign a certificate yourself, you need the private key which should only be known to you.

## Self-Signed vs CA

|            | Self-Signed                                                                                | CA                                                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Definition | Created, signed, and issued by the subject of the certificate (the entity it is issued to) | Created, signed and issued by a third party called CA that is authorized to validate the identity of the applicant |
| Usage      | Private networks/Intranet                                                                  | Public networks to build trust among website visitors                                                              |
| Signature  | Signed by your own private keys                                                            | Signed by third parties including Sectigo, Symantec, Digicert, Thawte, GeoTrust, GlobalSign, GoDaddy, and Entrust  |
