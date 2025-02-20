## Storing enums as numeric values in databases

Storing enums in a database is a common practice, and it can be a good approach, but it depends on the specific use case. One practice is to store the mapping of textual description in a **reference lookup table**.

### Advantages

- **Space efficiency**: More space efficient to store numbers than string, can be important in high-performance systems where disk I/O and storage are significant concerns -**Performance**: Numeric values are faster to query than string values
- **Consistency across systems**: Avoid long text values in databases and reduces confusion across systems. Easier to map numeric values to full textual description when necessary

### Drawbacks

- Lack of readability
- Data integrity
