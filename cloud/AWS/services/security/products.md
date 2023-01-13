## IAM (Identity Access Management)

A web service that helps in maintaining access to AWS services in a secure way. Enables you to create and control services for user authentication or limit access to a certain set of people who use your AWS resources.

### Elements

1. **Principal**: An entity that can perform actions on an AWS resource (user/role/application)
2. **Authentication**: Process of confirming the identity of the principal trying to access an AWS product, and must provide credentials/keys
3. **Request**: A principal sends a request to AWS specifying the action and which resource should perform it
4. **Authorization**: All resources are denied by default and IAM authorizes a request only if all parts are allowed by a matching policy
5. **Actions**: Used to view, create, edit or delete a resource
6. **Resources**: A set of actions that can be performed on a resource related to your AWS account

## KMS

Enables users to create and manage the encryption keys that are used for encrypting data.
