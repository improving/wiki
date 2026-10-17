---
type: Reference
title: "Adding a Spring Boot App to the Grafana Observability Platform"
resource: "https://www.improving.com/thoughts/adding-a-spring-boot-app-to-the-grafana-observability-platform/"
author: "Scott Bock"
published: '2023-05-09'
fetched: '2026-10-17'
tags: [blog, improving.com]
---

There are many vectors for an API’s complexity to increase. For example: As it adds capabilities, it can grow into a complex monolith. or become a bunch of microservices. As its usage grows, it can push the abilities of the hardware, or become distributed. These are just some of the issues and possible solutions. Each of these choices or changes makes it harder to keep track of the health, debug errors, and identify bottlenecks. That is why observability is important.

Unfortunately, it can be expensive to outsource this responsibility; however, there are open-source solutions, and one of the best is the Grafana platform. Grafana is the visualization tool for a variety of data sources, but the Grafana team also has its own data sources for logs (Loki), metrics (Mimir), and traces (Tempo). In this article, we will see how to connect a Spring Boot application to this ecosystem.

Our first step is to set up our observability environment. We will use docker compose to create this environment with this docker-compose.yaml file:

```yaml
version: "3.9"

networks:
telemetry:

volumes:
influxdb-storage:
grafana-storage:

services:

grafana:
image: grafana/grafana:9.3.1
depends_on:
- influxdb
volumes:
- ./docker/grafana-datasources.yaml:/etc/grafana/provisioning/datasources/datasources.yaml
- grafana-storage:/var/lib/grafana
environment:
- GF_SECURITY_ADMIN_USER=admin
- GF_SECURITY_ADMIN_PASSWORD=admin1
- GF_SERVER_HTTP_PORT=3000
- INFLUXDB_HOST=influxdb
- INFLUXDB_PORT=8086
- INFLUXDB_NAME=db0
- INFLUXDB_USER=influxuser
- INFLUXDB_PASS=influxuser1
ports:
- "3000:3000"
networks:
- telemetry

influxdb:
image: influxdb:latest
ports:
- '8086:8086'
volumes:
- influxdb-storage:/var/lib/influxdb
environment:
- INFLUXDB_URL=http://influxdb:8086
- INFLUXDB_ADMIN_USER=influxuser
- INFLUXDB_ADMIN_PASSWORD=influxuser1

loki:
image: grafana/loki:2.7.1
ports:
- "3100:3100"
command: -config.file=/etc/loki/loki.yaml
volumes:
- ./docker/loki.yaml:/etc/loki/loki.yaml
networks:
- telemetry

tempo:
image: grafana/tempo:1.5.0
command: [ "-config.file=/etc/tempo.yaml" ]
volumes:
- ./docker/tempo.yaml:/etc/tempo.yaml
- ./data/tempo:/tmp/tempo
ports:
- "14268:14268" # jaeger ingest
- "3200:3200" # tempo
- "55680:55680" # otlp grpc
- "55681:55681" # otlp http
- "9411:9411" # zipkin
- "4318:4318" # new http
- "4317:4317" # new grpc

networks:
- telemetry

mimir:
image: grafana/mimir:2.5.0
command: "-config.file=/etc/mimir/mimir.yaml"
ports:
- "9009:9009"
volumes:
- "./docker/mimir.yaml:/etc/mimir/mimir.yaml"
- "/tmp/mimir/rules:/tmp/mimir/rules"
networks:
- telemetry
```

Here you can see that we are spinning up a Grafana instance backed by an Influxdb along with instances of Loki, Tempo, and Mimir. We expose the appropriate ports configure each instance with the corresponding files from our docker folder. Most interesting is the grafana-datasources.yaml which tells configures grafana to connect to Loki, Mimir, and Tempo.

```yaml
apiVersion: 1

datasources:

- name: Tempo
type: tempo
access: proxy
orgId: 1
url: http://tempo:3200
basicAuth: false
isDefault: true
version: 1
editable: false
apiVersion: 1
uid: tempo

- name: Loki
type: loki
access: proxy
orgId: 1
url: http://loki:3100
basicAuth: false
isDefault: false
version: 1
editable: false
apiVersion: 1
jsonData:
derivedFields:
- datasourceUid: tempo
matcherRegex: (?:traceID|trace_id)=(\w+)
name: TraceID
url: $${__value.raw}

- name: Mimir
type: prometheus
access: proxy
orgId: 1
url: http://mimir:9009/prometheus
isDefault: false
version: 1
editable: true
```

Once we run “docker compose up” we can hit localhost:9000 and login to Grafana with our admin/admin1 credentials defined in the docker compose file. Now let’s work on getting some data from our Spring Boot app out there. We’ll start with adding logs to loki.

## Logs

By default, Spring Boot includes slf4j so we don’t need to add anything to our build.gradle. However, in this example, we’ll use Grafana Agent to scrape our logs and export them to Loki so we need to update our application.properties file to write our logs to a file and set a root logging level like this:

```java
logging.file.name=logs/app.log
logging.level.root=INFO
```

Next we add the Grafana Agent to our docker-compose.yaml file:

```markup
grafana-agent:
image: grafana/agent:v0.22.0
volumes:
- ./docker/grafana-agent.yaml:/etc/agent-config/grafana-agent.yaml
- ./logs/:/var/log/
entrypoint:
- /bin/agent
- -config.file=/etc/agent-config/grafana-agent.yaml
- -prometheus.wal-directory=/tmp/agent/wal
ports:
- "12345:12345"
networks:
- telemetry
extra_hosts:
- "host.docker.internal:host-gateway"
```

And we tell Grafana Agent how to scrape our logs by setting its config file (grafana-agent.yaml).

```yaml
server:
 log_level: debug
 http_listen_port: 12345
 
logs:
 configs:
 - name: default
 positions:
 filename: /tmp/localhost-positions.yaml
 clients:
 - url: http://loki:3100/loki/api/v1/push
 scrape_configs:
- job_name: system
 static_configs:
- labels:
 job: localhostlogs 
__path__: /var/log/*log
 env: "local"
 app: "observability-example"
```

## Metrics

To send our metrics we need to include a few dependencies in our gradle.build

```yaml
dependencies {
implementation 'org.springframework.boot:spring-boot-starter-actuator'

//enable /actuator/prometheus
runtimeOnly 'io.micrometer:micrometer-registry-prometheus'

//for timed aspect
implementation 'org.springframework:spring-aspects'
}
```

Now let’s enable the metrics endpoints in our app by adding some properties to the application.properties:

```yaml
management.endpoint.health.show-details=always management.endpoints.web.exposure.include=health,info,prometheus
```

Finally, we tell Grafana Agent how where to read our metrics from and where to write them to by updating the grafana-agent.yaml config file:

```yaml
management.endpoint.health.show-details=always management.endpoints.web.exposure.include=health,info,prometheus
```

Our Spring Boot app acutaor endpoint contains a bunch of great metrics, if you want to see example of some custom metrics you can look at the FactorService in my example application.

## Traces

To add trace data to our app we need to include a few more dependencies in our gradle.build

```java
dependencies {
implementation("io.micrometer:micrometer-tracing")
implementation("io.micrometer:micrometer-tracing-bridge-otel")
implementation("io.opentelemetry:opentelemetry-exporter-zipkin")
}
```

Now let’s enable the add our trace info to our logs and enable tracing and endpoints in our app by adding some properties to the application.properties:

```yaml
logging.pattern.level="trace_id=%mdc{traceId} span_id=%mdc{spanId} trace_flags=%mdc{traceFlags} %p"

management.tracing.enabled=true
management.tracing.sampling.probability=1.0
management.zipkin.tracing.endpoint=http://localhost:9411
```

That’s it! Start the app and relaunch your docker compose so that we pick up all the changes. You can find the whole example application repo here [https://github.com/scottbock/observability-example](https://github.com/scottbock/observability-example)
