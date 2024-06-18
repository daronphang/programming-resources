## General Purpose (A and T tags)

Provides a balance of compute, memory and networking resources. You can use them for application servers, gaming servers, backend servers for enterprise applications, and small/medium databases.

### T-instance

Many general purpose workloads are on average not busy, and do not require a high level of sustained CPU performance.

These low-to-moderate CPU utilization workloads lead to wastage of CPU cycles and, as a result, you pay for more than you use. To overcome this, you can leverage the low-cost burstable general purpose instances, which are the T instances.

The T-instance family provides a baseline CPU performance with the **ability to burst above the baseline** at any time for as long as required. The baseline CPU is defined to meet the needs of the majority of general purpose workloads.

## Compute optimized (C tag)

Ideal for compute-bound applications that benefit from high-performance processors including high performance web servers, compute-intensive applications, and dedicated gaming servers. You can also use them for batch processing workloads.

## Memory optimized (R tag)

Designed to deliver fast performance for workloads that process large datasets in memory. Can be useful for situations where you have a workload that requires large amounts of data to be preloaded before running an application.

## Accelerated computing (G and P tags)

Instances that use hardware accelerators (coprocessors) to perform functions more efficiently than is possible in software running on CPUs. Examples include machine learning, computational fluid dynamics, autonomous vehicles, floating-point number calculations, graphics processing, game streaming, application streaming, and data pattern matching.

## Storage optimized (I, D, and H tags)

Designed for workloads that require high, sequential read and write access to large datasets on local storage. Example of workloads include distributed file systems, data warehousing applications, and high frequency OLTP (online transaction processing) systems.

In computing IOPS (input/output operations per second) is a metric that measures the performance of a storage device. Storage optimized instances are designed to deliver tens of thousands of low-latency, random IOPS to applications.

## HPC optimized (High Performance Computing)

HPC instances are purpose built to offer the best price performance for running HPC workloads at scale on AWS. Ideal for applications that benefit from high-performance processors, such as large, complex simulations and deep learning workloads.
