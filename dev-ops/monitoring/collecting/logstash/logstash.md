## Logstash

Log analysis platform that is responsible for aggregating data from different sources, processing it, and sending it down the pipeline, usually to be directly indexed in Elasticsearch. Any type of event can be enriched and transformed with a broad array of input, filter and output plugins.

https://www.elastic.co/guide/en/logstash/8.6/introduction.html

## Docker

Location of pipeline in bind-mounted volume must be mapped to /usr/share/logstash/pipeline as this is the default location the container will look for pipeline configuration files. Every file in this directory will then be parsed by Logstash as pipeline configuration. If configuration is not provided, it will use the default defined in /usr/share/logstash/pipeline/logstash.conf.

https://www.elastic.co/guide/en/logstash/current/docker-config.html

## Connecting to Elastic

Elasticsearch security is enabled by default, and requires SSL to send data to elastic cluster. When starting Logstash, need to override XPACK settings to connect securely to the local elastic cluster. Configuration will also need to be provided in output plugin for elasticsearch.

https://www.elastic.co/guide/en/logstash/current/ls-security.html

1. Copy certs from elastic to host machine

```console
$ touch ca.crt
$ docker exec -it es01 bash
$ cd /usr/share/elasticsearch/config/certs/ca/ca.crt    # copy cert to local machine
$ curl --cacert ca.crt -u elastic https://localhost:9200    # enter password when prompted
```

2. Create bind mounts (separate pipeline configs with other data)

```console
$ docker volume create \
--driver local \
--opt type=none \
--opt o=bind \
--opt device=/home/daronphang/df_microservices/df_api_gateway/elk/pipeline \
--name pipeline

$ docker volume create \
--driver local \
--opt type=none \
--opt o=bind \
--opt device=/home/daronphang/df_microservices \
--name df_microservices
```

3. Deploy container and override default XPACK settings

```console
$ docker run \
--name logstash \
--env XPACK_MONITORING_ELASTICSEARCH_HOSTS="https://es01:9200" \
--env XPACK_MONITORING_ELASTICSEARCH_USERNAME=elastic \
--env XPACK_MONITORING_ELASTICSEARCH_PASSWORD=elastic123 \
--env XPACK_MONITORING_ELASTICSEARCH_SSL_CERTIFICATE_AUTHORITY=/app/df_api_gateway/elk/ca.crt \
--mount source=df_microservices,destination=/app/ \
--mount source=pipeline,destination=/usr/share/logstash/pipeline/ \
--rm -it --network=elastic docker.elastic.co/logstash/logstash:8.6.2
```
