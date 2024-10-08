## Eviction policies

Caches employ eviction policies to decide which content to remove when cache space is needed. This helps manage storage and ensures that the most relevant content is kept readily accessible.

## Heuristic-based

Many heuristic cache algorithms maintain a priority queue for objects in the cache and select the lowest priority object to evict when a miss occurs. However, as they are not adaptive enough, they work well in some traces but not in others.

- First-In-First-Out (FIFO): Performs well for workloads where objects are accessed sequentially
- Last-In-Last-Out (LIFO)
- Least Recently Used (LRU): Good for workloads where objects that have been accessed recently are more likely to be accessed repeatedly
- Most Recently Used (MRU)
- Least Frequently Used (LFU)
- Random Replacement (RR): Randomly selects a candidate item and discards it to make space when necessary

## Adaptive-based

These are caching policies that can self-tune and balance between different features:

- Adaptive Replacement Cache (ARC): Recency and frequency
- Greedy-Dual-Size-Frequency (GDSF): Object size and frequency

Although these policies can cover a wider range of workloads, they can only adapt to specific features, limiting their performance for changing workloads.

## Machine-learning based

Learning-based algorithms like LRB achieve better performance than heuristic algorithms, because they train a model to learn the cache access pattern directly from the trace instead of assuming a static workload behavior.

AAs an example, LRB maintains features for objects that are both currently, and historically present in the cache, and trains a regression model to predict an object’s time to next access. When an eviction is required, it randomly samples 64 objects and runs this predictive model on them and evicts the object which is predicted to be accessed furthest in the future.

### Challenges

For a solution that uses machine learning to be deployed in a large-scale production environment, there are three main challenges that need to be tackled:

- **Computation overhead for learning**: Learning-based cache algorithms can be more computationally expensive to run compared to heuristic-based algorithms
- **Robust byte miss ratio improvement**: Learning-based cache algorithms can introduce regressions if their design does not include a regression prevention mechanism
- **Measuring impact under production noise**: It is challenging to accurately measure the impact of a new eviction algorithm in a large-scale environment; current production practice uses A/B testing
