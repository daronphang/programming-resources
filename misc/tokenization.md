## Tokenization

Tokenization is the process of replacing sensitive data with unique identification symbols that retain all the essential information about the data without compromising its security. It can be used to **protect sensitive data** or to efficiently **process large amounts of data**.

### Tokenization vs encryption

A core issue with data encryption is that it is **reversible**. Encrypted data is designed to be restored to its initial, unencrypted state. The safety of encryption is reliant on the algorithm used to protect the data. A more complex algorithm means safer encryption that is more challenging to decipher.

In contrast to encryption systems, which allow data to be deciphered using a secret key, a tokenization system links the original data to a token but **does not provide any way to decipher the token and reveal the original data**.

### Use cases

- AI: Used to break down data for easier pattern detection
- Web3: Used as a digitization process to make assets more accessible
- Payments: Used for cybersecurity and to obfuscate the identity of the payment itself, essentially to prevent fraud

### How tokens are generated

In general, tokenization is the process of issuing a digital, unique, and anonymous representation of a real thing by:

- Using a mathematically reversible cryptographic function with a key
- Using a nonreversible function i.e. hash function
- Using an index function or randomly generated number

The sensitive information that the token stands in for is stored safely in a centralized server known as a **token vault**. The token vault is the only place where the original information can be mapped back to its corresponding token.

## Machine learning

Tokenization in the realm of NLP and ML refers to the process of converting a sequence of text into smaller parts for easier machine analysis, helping machines to understand human language.

## Payments

Tokenization of data safeguards credit card numbers and bank account numbers in a virtual vault, so organizations can transmit data via wireless networks safely. For tokenization to be effective, organizations must use a **payment gateway** to safely store sensitive data.

A payment gateway is a merchant service that stores credit card numbers securely and generates the random token.

### How it works

1. A customer provides their payment details at a point-of-sale (POS) system or online checkout form
2. The details, or data, are substituted with a randomly generated token, which is generated usually by the merchant's payment gateway
3. Tokenization information is then encrypted and sent to a payment processor
4. The original sensitive payment information is stored in a token vault in the merchant's payment gateway
5. The tokenized information is encrypted again by the payment processor before being sent for final verification

### Vaultless

Some tokenization is vaultless. Instead of storing the sensitive information in a secure database, vaultless tokens are stored using an **algorithm** i.e. similar to encryption. If the token is reversible, then the original sensitive information is generally not stored in a vault.
