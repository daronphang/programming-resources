## Overview

When communicating with other systems or persisting data, you need to serialize Python objects to a raw data format that can be transmitted or stored, and deserialize back to Python objects for application usage.

### Serialization

Serialization is the process of converting app-level objects (classes, dictionaries) into a format that allows us to store or transmit the data such as JSON, CSV, YAML, XML, Binary, HDF5, and etc (either text-based or binary-based). In other words, serialization is the process of converting a structured object into a sequence of bytes which can be stored in a file system or database, or sent through the network.

### Deserialization

Deserialization is the reverse process whereby data such as dictionaries or JSON objects are converted back into app-level objects. Often used in web development when backend receives input data from frontend or retrieving data from database, and then converting them back into custom objects.

## Comparison

Built-in solutions including pickle or json are limited. Pickle only works if both serialization and deserialization are under your control, and json only converts between strings and python dicts, but not classes.

### Marshmallow

- Returns a cleaned, validated dict
- Conversion from the cleaned dict to a class instance is optional
- Type checking applied at specific points i.e. schema.load(), schema.dump()

### Pydantic

- Returns a Python object right away.
- Applies dynamic type checking at runtime i.e. instantiating an object
