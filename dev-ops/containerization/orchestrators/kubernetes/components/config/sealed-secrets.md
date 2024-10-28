## Sealed secrets

Sealed secrets present an innovative solution to securely manage sensitive data in Kubernetes environments. They enable users to encrypt their Secrets into a ‘SealedSecret’, which is safe to store in a public repository. The SealedSecret can only be decrypted by the controller running in the target cluster, meaning that it is not accessible until it reaches the Kubernetes cluster where it is intended to be used.

### How it works

- A Sealed Secrets Controller is deployed in the Kubernetes cluster
- Users encrypt their Secret into a SealedSecret using kubeseal and the controller's public key
- The SealedSecret is committed to version control
- Once applied to the cluster, the Sealed Secrets Controller decrypts the SealedSecret and creates a standard Secret
- The standard Secret is then used by your pods, ensuring a secure secret management lifecycle
