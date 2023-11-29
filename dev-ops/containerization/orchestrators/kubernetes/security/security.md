## Thread Modeling

Thread modeling is the process of identifying vulnerabilities so you can put measures in place to prevent and mitigate them. The STRIDE model defines six categories of potential threat:

- Spoofing
- Tampering
- Repudiation
- Information disclosure
- Denial of service
- Elevation of privilege

## Secure configuration

The Centre for Information Security (CIS) has published an industry standard benchmark for Kubernetes security, and Aqua Security has written an easy-to-use tool called **kube-bench** to implement CIS tests.

You run kube-bench against each node in your cluster and get a report outlining which tests passed and failed. Many organizations consider it a best practice to run kube-bench on all production nodes as part of the node provisioning process.
