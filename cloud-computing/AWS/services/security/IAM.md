## IAM (Identity Access Management)

A web service that helps in maintaining access to AWS services in a secure way. Enables you to create and control services for user authentication or limit access to a certain set of people who use your AWS resources.

IAM gives you flexibility to configure access based on your company's specific operational and security needs. You do this by using a combination of IAM features:

- IAM users, groups and roles
- IAM policies
- Multi-factor authentication

## Root user

When you create an AWS account, you begin with an identity known as the root user. Should not be used for everyday tasks.

The AWS root user has two sets of credentials:

- Email address and password used to create the account, to access the AWS Management Console
- Access keys (key ID and secret access key) to make programmatic requests from the AWS CLI for authentication

## IAM users

An IAM user is an identity you create in AWS (by root user). It represents the person or application that interacts with AWS services and resources. It consists of a name and credentials.

By default, no permissions are associated with a newly created IAM user. Requires to grant the IAM user with the necessary permissions i.e. creating an S3 bucket.

Individual IAM users should be created for each individual, even if they have similar level of access.

## IAM policies

An IAM policy is a JSON document that defines users, groups or roles' permissions to AWS services and resources (allow/deny). IAM policies enable you to customize users' levels of access to resources. Follow the security principle of **least privilege** when granting permissions i.e. don't give more permissions than the user needs.

### Structure

- Version: Policy language version
- Id: Identifier for the policy (optional)
- Statement: One or more individual statements (required)

#### Statement

- Sid: Identifier for the statement (optional)
- Effect: Whether the statement allows or denies access
- Principal: Account/user/role to which the policy is applied to
- Action: List of actions this policy allows or denies
- Resource: List of resources to which the actions are applied to
- Condition: Conditions for when this policy is in effect

```json
{
  "Version": "2012-10-17",
  "Statement": {
    "Sid": "1",
    "Effect": "Allow",
    "Principal": {
      "AWS": ["arn:aws:iam:1234567:root"]
    },
    "Action": ["s3:ListObject", "s3:GetObject"],
    "Resource": ["arn:aws:s3:::AWSDOC-EXAMPLE-BUCKET"]
  }
}
```

## IAM groups

An IAM group is a collection of IAM users. When you assign an IAM policy to a group, all users in the group are granted permissions specified by the policy.

Groups can only contain users, **not other groups**. Users can belong to multiple groups.

## IAM roles

An IAM role is an identity that you can assume to gain **temporary access** to permissions. Before an **IAM user, application or service can assume an IAM role**, they must be granted permissions to switch to the role.

When someone assumes an IAM role, they abandon all previous permissions they had under a previous role, and assume new permissions of the new role.

**Never enter IAM access ID and access keys into EC2 instance**. Instead, use IAM roles to provide EC2 with credentials.

## Mutli-factor authentication (MFA)

In IAM, MFA provides an extra layer of security for your AWS account. MFA device options include Google Authenticator, Authy, YubiKey Fob

### Elements

- **Principal**: An entity that can perform actions on an AWS resource (user/role/application)
- **Authentication**: Process of confirming the identity of the principal trying to access an AWS product, and must provide credentials/keys
- **Request**: A principal sends a request to AWS specifying the action and which resource should perform it
- **Authorization**: All resources are denied by default and IAM authorizes a request only if all parts are allowed by a matching policy
- **Actions**: Used to view, create, edit or delete a resource
- **Resources**: A set of actions that can be performed on a resource related to your AWS account

## Auditing IAM usage

### IAM Credentials Report (account-level)

A report that lists all your account's users and the status of their various credentials.

### IAM Access Advisor (user-level)

Access Advisor shows the service permissions granted to a user and when those services were last accessed.

## AWS IAM Identity Center (Single Sign-On)

One login for:

- All your AWS accounts in AWS Organizations
- Business cloud applications (Salesforce, Microsoft 365)
- SAML2.0-enabled applications
- EC2 Windows Instances

For Identity Providers, can either use:

- Built-in identity store in IAM Identity Center
- Third parties (AD, OneLogin, Okta)
