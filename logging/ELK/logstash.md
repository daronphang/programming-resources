## Logstash

Log analysis platform that is responsible for aggregating data from different sources, processing it, and sending it down the pipeline, usually to be directly indexed in Elasticsearch. Any type of event can be enriched and transformed with a broad array of input, filter and output plugins.

https://www.elastic.co/guide/en/logstash/8.6/introduction.html

## Pipeline

Pipeline is created by stringing together plugins of inputs, outputs and filters.

## Example

```conf
input {
    file {
        path => [
            "/usr/share/logstash/pipeline/df_api_gateway/src/logs/DF_API_GATEWAY_TESTING_INFO.log",
            "/usr/share/logstash/pipeline/df_espec_service/src/logs/*.log",
            "/usr/share/logstash/pipeline/df_email_service/src/logs/*.log"
        ]
        sincedb_path => "/dev/null"
    }
}

filter {
    json {
        source => "message"
    }
    aggregate {
        task_id => "%{correlation_id}"
        code => "map['combined_msg'] ||= '' ; map['combined_msg'] += event.get('message') + ', '"
        push_map_as_event_on_timeout => true
        timeout => 60
        timeout_task_id_field => "correlation_id"
    }
}

output {
    stdout { codec => rubydebug }
}
```
