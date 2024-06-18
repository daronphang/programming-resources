## Parsing

The Java library supplies two kinds of parsers: DOM parser that reads an XML document into a tree structure, and Streaming parser that generates events as they read a document.

### DOM

When traversing child nodes, it will include whitespaces.

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
DocumentBuilder builder = factory.newDocumentBuilder();
File f = . . .
Document doc = builder.parse(f);

// analyzing
Element root = doc.getDocumentElement();
NodeList children = root.getChildNodes();
for (int i = 0; i < children.getLength(); i++) {
    Node child = children.item(i);
    if (child instanceof Element) {
        Element childElement = (Element) child;
        ...
    }
}
```
