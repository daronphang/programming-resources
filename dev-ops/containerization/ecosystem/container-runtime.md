## containerd

containerd is a **high-level container runtime** built by Docker and implements the CRI specification. It pulls images from registries (OCI-compliant), manages them and hen hands over to a lover-level runtime, which uses the features of the Linux kernel to create processes called 'containers'.

containerd is available as a daemon for Linux and Windows that controls runc. It manages the complete container lifecycle of its host system, from image transfer and storage to container execution and supervision, to low-level storage, to network attachments and beyond.

## CRI-O

CRI-O is a **high-level container runtime** which implements the Kubernetes CRI. It is an alternative to containerd that was born out of Red Hat, IBM, Intel, SUSE, and others.

## runC

runC is an OCI-compatible, lightweight, portable container runtime written in Golang that was spun out by Docker as a standalone tool (no dependency on Docker platform), to be used as plumbing by infrastructure plumbers everywhere. runC provides all of the low-level functionality for containers, interacting with existing low-level Linux features i.e. namespaces and control groups. It is a CLI tool for spawning and running containers according to the OCI specification.

## crun

A container runtime that implements the OCI specification written in C.

## firecracker-containerd

A container runtime created by AWS which implements the OCI specification as individual lightweight VMs.

## gVisor

A container runtime created by Google that has its own kernel. It implements the OCI specification in its runtime called runsc.
