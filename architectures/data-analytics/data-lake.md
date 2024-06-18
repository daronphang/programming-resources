## Data lake pattern

As in many reactionary responses to the complexity, expense, and failures of the data warehouse, the design pendulum swung to the opposite pole, exemplified by the **Data Lake pattern**, intentionally the inverse of the Data Warehouse pattern.

While it keeps the centralized model and pipelines, it inverts the “transform and load” model of the data warehouse to a “load and transform” one. Rather than do the immense work of transformation, the philosophy of the Data Lake pattern holds that, rather than do useless transformations that may never be used, **do no transformations**, allowing business users access to analytical data in its natural format, which typically required transformation and massaging for their purpose. Thus, the burden of work was made **reactive rather than proactive** i.e. transformation work done on demand. Moreover, many machine learning models work better with data “closer” to the semi-raw format rather than a transformed version.

## Characteristics

### Data extracted from many sources

Operational data is still extracted in this pattern, but less transformation into another schema takes place i.e. data is often stored in its native form. Nonetheless, some transformation may still occur in this pattern i.e. files to column-based snapshots.

### Loaded into the lake

The lake, often deployed in cloud environments, consists of regular data dumps from the operational systems.

## Drawbacks

### Difficulty in discovery of proper assets

Much of the understanding of data relationships within a domain evaporates as data flows into the unstructured lake. Thus, domain experts must still involve themselves in crafting analysis.

### PII and sensitive data

Dumping unstructured data into a lake often risks exposing information that can be stitched together to violate privacy. Unfortunately, just as in the discovery process, domain experts have the knowledge necessary to avoid accidental exposures, forcing them to reanalyze data in the lake.

### Still technically partitioned

Generally, architects design each of those solutions with distinct ingestion, transformation, loading, and serving partitions, each focused on a technical capability.

However, modern architecture patterns favor domain partitioning, encapsulating technical implementation details.
