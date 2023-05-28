## Index Template

An index template is a way to tell Elasticsearch how to configure an index when it is created. For data streams, the index template configures the stream's backing indices as they are created. **Templates are configured prior to index creation**.

https://www.elastic.co/guide/en/elasticsearch/reference/current/index-templates.html

## Component Template

Component templates are reusable building blocks that configure mappings, settings and aliases. While you can use component templates to construct index templates, they aren’t directly applied to a set of indices. Index templates can contain a collection of component templates, as well as directly specify settings, mappings, and aliases.

## Logstash Elasticsearch Output Index

Default is [data_stream_type]-[data_stream_dataset]-[data_stream_namespace]-%{+yyyy.MM.dd}.
