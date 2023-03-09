## Pipeline

Pipeline is created by stringing together plugins of inputs, outputs and filters.

### Configuration

For Docker, Logstash expects to find all configuration files at /usr/share/logstash/config i.e. logstash.yml, pipelines.yml.

## Multiple Conf Files

By default, Logstash has a single event pipeline and will concatenate configuration files into a single configuration. Hence, each event will process through all filters and outputs. When separating out pipelines, need to define pipelines.yml file.

https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html

```yml
- pipeline.id: api_monitoring
  path.config: "/usr/share/logstash/pipeline/api_monitoring.conf"
- pipeline.id: task_monitoring
  path.config: "/usr/share/logstash/pipeline/task_monitoring.conf"
```

### Docker Deployment

Need to include the following configuration, else Logstash container will ignore pipelines.yml file.

```yml
version: "2"
services:
  logstash:
    image: docker.elastic.co/logstash/logstash:6.0.0
    environment:
      - path.config=null
    volumes:
      - ./pipelines.yml:/usr/share/logstash/config/pipelines.yml
```
