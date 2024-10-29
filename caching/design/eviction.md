## Eviction policies

Caches employ eviction policies to decide which content to remove when cache space is needed. This helps manage storage and ensures that the most relevant content is kept readily accessible. Such algorithms are efficient when they can retain more valuable objects in the cache to achieve a lower miss ratio.

### Trouble with complexity

Multiple problems come with increasing complexity:

- Complex cache eviction algorithms are **difficult to debug** due to their intricate logic
- Complexity may **affect efficiency** in surprising ways
- Complexity often negatively correlates with throughput performance. A more intricate algorithm performs more computation with potentially longer critical sections, reducing both throughput and scalability
- More per-object metadata needs to be stored, which reduces the effective cache size that can be used for caching data e.g. CACHEUS is 3.3x larger than LRU
- Complex algorithms often have parameters that can be difficult to tune

### Simplicity wins

**Simplicity** is a key appealing feature for an algorithm to be deployed in production since it commonly correlates with effectiveness, maintainability, scalability, and low overhead. Most caching systems such as ATS, Varnish, Nginx, Redis, groupcache use only FIFO and LRU policies.

### Lazy promotion and quick demotion

Promotion and demotion are two cache internal operations used to maintain the logical ordering between objects, and are important properties of efficient cache eviction algorithms.

**Lazy promotion** refers to the strategy of promoting cached objects only at eviction time. It aims to retain popular objects with minimal effort. An example is adding reinsertion to FIFO. In contrast, FIFO has no promotion, and LRU performs **eager promotion** i.e. moving objects to the head of the queue on every cache hit. Lazy promotion can improve throughput due to less computation and efficiency due to more information about an object at eviction.

**Quick demotion** removes most objects quickly after they are inserted (i.e. remove newly-inserted unpopular objects), which can be performed from a scan. Web cache workloads benefit from this as object popularity follows a power-law distribution, and many objects are unpopular. Quick demotion is crucial for achieving **high cache efficiency**.

### Slab-based space management

Cache systems often store a wide range of variable-sized objects e.g. few bytes to GB. On-demand heap memory allocators such as ptmalloc and jemalloc can cause **large and unbounded external memory fragmentation**, which is highly undesirable for production environment.

To avoid this, slab-based space management can be employed in which **evictions happen on objects of similar sizes**. Slab-based allocator eliminates external memory fragmentation at the cost of bounded internal memory fragmentation.

Memory is allocated as fixed size chunks called slabs e.g. 1 MB. Each slab is then evenly divided into smaller chunks called items. An object is mapped to the slab class that best fits it, including metadata. Higher slab classes correspond to larger items.

### Applications

- MemC3 uses Cuckoo hashing and CLOCK eviction to improve Memcached's throughput and scalability
- MICA uses log-structured storage, data partitioning and a lossy hash table to improve key-value cache throughput and scalability
- Segcache uses segment-structured storage with FIFO-based algorithm and leverages macro management to improve scalability
- Frozenhot improves cache scalability by freezing hot objects in the cache to avoid locking

## Heuristic-based

Many heuristic cache algorithms maintain a priority queue for objects in the cache and select the lowest priority object to evict when a miss occurs. However, as they are not adaptive enough, they work well in some traces but not in others.

### Cache primitives

Having an efficient cache primitive not only provides an effective and simple eviction algorithm but also enables other approaches to design more efficient and advanced eviction algorithms.

- **First-In-First-Out (FIFO)**: Performs well for workloads where objects are accessed sequentially
- **Last-In-Last-Out (LIFO)**
- **Least Recently Used (LRU)**: Good for workloads where objects that have been accessed recently are more likely to be accessed repeatedly
- **Most Recently Used (MRU)**
- **Least Frequently Used (LFU)**
- **Random Replacement (RR)**: Randomly selects a candidate item and discards it to make space when necessary
- **SIEVE**: A simple and efficient turn-key cache eviction policy
- **CLOCK (Second Chance Page Replacement Policy)**: Candidate pages for removal are considered in a round robin matter, and a page that has been accessed between consecutive considerations will not be replaced

### Advanced

- **FIFO-Reinsertion**
- **LRU-K**: Designed by changing the recency metric

## Adaptive-based

These are caching policies that can self-tune and balance between different features:

- Adaptive Replacement Cache (ARC): Recency and frequency
- Greedy-Dual-Size-Frequency (GDSF): Object size and frequency

Although these policies can cover a wider range of workloads, they can only adapt to specific features, limiting their performance for changing workloads.

## Machine-learning based

Learning-based algorithms achieve better performance than heuristic algorithms, because they train a model to learn the cache access pattern directly from the trace instead of assuming a static workload behavior.

### LRB

LRB maintains features for objects that are both currently, and historically present in the cache, and trains a regression model to predict an object’s time to next access. When an eviction is required, it randomly samples 64 objects and runs this predictive model on them and evicts the object which is predicted to be accessed furthest in the future.

### HALP

HALP is a novel caching algorithm which achieves low CPU overhead and robust byte miss ratio improvement by augmenting a heuristic policy with machine learning.

### Challenges

For a solution that uses machine learning to be deployed in a large-scale production environment, there are three main challenges that need to be tackled:

- **Computation overhead for learning**: Learning-based cache algorithms can be more computationally expensive to run compared to heuristic-based algorithms
- **Robust byte miss ratio improvement**: Learning-based cache algorithms can introduce regressions if their design does not include a regression prevention mechanism
- **Measuring impact under production noise**: It is challenging to accurately measure the impact of a new eviction algorithm in a large-scale environment; current production practice uses A/B testing
