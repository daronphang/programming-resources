## Mapping

Within a search engine, mapping defines how a document is indexed and how it indexes and stores stores its fields in Lucene, similar to a database schema that describes the fields and properties that documents hold (string, integer, date). An inappropriate definition and mapping may result in the wrong search results.

The very first time Elasticsearch finds a new field whose mapping is not pre-defined inside the index, it automatically tries to guess the data type and analyzer of that field and set its default value.

### Common Problems

- An incorrectly defined mapping limits the functionality of the field i.e. if the field is set as text, it cannot be used for aggregations
- Elasticsearch automatically creates an \_all field and should be disabled in production to conserve space

### API Requests

```
GET /_mapping
GET /<index>/_mapping
GET /,/_mapping                 Multiple indices at once
GET /verbs,nouns/_mapping
```

### Data Types

https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html

### Mapping Types

**Dynamic mapping** or **static mapping**. Dynamic mapping allows ongoing flexibility so that documents can store extra attributes.

### Example

```
PUT /index_name

{
    "mappings":{
        "type_1":{
            "_all" : {"enabled" : true},
            "properties":{
                "field_1":{ "type":"string"},
                "field_2":{ "type":"long"}
            }
        },
        "type_2":{
            "properties":{
                "field_3":{ "type":"string"},
                "field_4":{ "type":"date"}
            }
        }
    }
}
```

```
{
    "name" : {"first" :"Alice","last":"John"},
    "age" : 26,
    "joiningDate" : "2015-10-15"
}

PUT /company

{
    "mappings": {
        "employeeinfo": {
            "_all": { "enabled": true },
            "properties": {
                "name": {
                    "type": "object",
                    "properties": {
                        "field_1": {
                            "type": "string"
                        },
                        "field_2": {
                            "type": "string"
                        }
                    }
                },
                "age": {
                    "type": "long"
                },
                "joiningDate": {
                    "type": "date"
                }
            }
        }
    }
}
```
