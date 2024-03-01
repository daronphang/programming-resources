## XML (Extensible Markup Language)

The XML format allows you to express the hierarchy and record repeated elements without contortions.

```xml
<configuration>
    <title>
        <font>
            <name>Helvetica</name>
            <size>36</size>
        </font>
    </title>
    <body>
        <font>
            <name>Times Roman</name>
            <size>12</size>
        </font>
    </body>
    <window>
        <width>400</width>
        <height>200</height>
    </window>
    <color>
        <red>0</red>
        <green>50</green>
        <blue>100</blue>
    </color>
    <menu>
        <item>Times Roman</item>ss <item>Helvetica</item>
 <item>Goudy Old Style</item>
    </menu>
</configuration>
```

### XML vs HTML

- XML is case-sensitive i.e. H1 and h1 are different tags
- You can never omit an end tag
- Allows elements with single tag i.e. `<input />`
- Attribute values must be enclosed in quotation marks
- HTML allows attributes without values, but all attributes in XML must have values
