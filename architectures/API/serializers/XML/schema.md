## XML schema

To specify the document structure, you can supply a DTD or an XML Schema definition.

```
<?xml version="1.0"?>
<configuration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="config.xsd">
    ...
</configuration>
```

```
<xsd:element name="font">
    <xsd:sequence>
    <xsd:element name="name" type="xsd:string"/>
    <xsd:element name="size" type="xsd:int"/>
    </xsd:sequence>
</xsd:element>
```
