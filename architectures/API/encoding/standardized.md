## Standardized Encoding

JSON, XML and CSV can be written/read by many programming languages, and are widely supported. However, they also have subtle problems:

- There is a lot of ambiguity around the encoding of numbers i.e. cannot distinguish between number and string
- Integers greater than 2^53 cannot be represented and requires workaround i.e. Twitter's API returns tweet IDs twice, once as JSON number and another as decimal string
- JSON and XML have good support for unicode character strings but not for binary strings; workaround is to encode the binary data as text using Base64

## CSV

CSV output format is a text file with each record from the crawl per line, with columns separated by commas. Useful when data is strictly tabular, structure is known and both generation and consumption of data file is in your control.

## XML (Extensible Markup Language)

In today's world, there are many applications built on different programming languages. Exchanging of data between applications is crucial in today's networked world. However, data exchange between heterogeneous applications would be complex.

One of the methods used to combat this complexity is to use XML as the intermediate language. XML is a simple and flexible text format widely used for data storage and exchange over the internet or other networks. XML defines a set of rules for encoding documents in a format that both humans and machines can read. Enforces strict validation and can be reliably processed by programs.

XML is a markup language similar to HTML, but without predefined tags to use. Instead, you define your own tags designed specifically for your needs. Essentially, HTML was designed to focus on the presentation of content, while XML was designed to store data as structured information.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<message>
    <warning>
         Hello World
    </warning>
</message>
```

### Benefits

Has larger overhead than CSV, but with strengths as follows:

- Can validate XML data against XSD
- Can have one-to-many relations in multi-levels in XML data representation
- Can have more complex hierarchy and structure i.e. more flexibility
- More readable than CSV (debatable)
- Natively supported by .NET framework
- Have standard parsers available everywhere
- Preferred over CSV when data is unstructured i.e. unknown Schema

### WSDL

WSDL is an XML notation for describing a web service. A WSDL definition tells a client how to compose a web service request and describes the interface that is provided by the web service provider.
