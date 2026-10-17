---
title: "Internet of Things"
type: "Concept"
description: "Networked physical devices that sense and act, feeding data pipelines from maker sensors to factory floors."
created: '2026-10-17'
updated: '2026-10-17'
tags: [iot, data, engineering]
sources:
  - "/sources/fun-with-iot-part-1.md"
  - "/sources/fun-with-iot-part-2.md"
  - "/sources/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md"
  - "/sources/it-outsourcing-trends-to-watch-closely-in-2023.md"
---

# Internet of Things

The Internet of Things spans cheap maker sensors and industrial factory floors alike: physical devices that sense their environment, report events, and feed downstream pipelines. In this corpus IoT is the data source that makes [event-driven architecture](/concepts/event-driven-architecture.md) and [real-time data streaming](/concepts/real-time-data-streaming.md) worth building, from a freezer alert to a production line.

## Key Claims

- A maker freezer monitor pairs a Wemos D1 Mini (ESP8266) with a DHT22 sensor, reporting to the Losant platform every 30 seconds and texting alerts above 20°F; inactivity triggers at 15, 30, and 60 minutes cover power loss.
- A DIY driveway monitor used a QMC5883L magnetic sensor over ~150ft of Cat-6 with an I2C range extender and a rolling-average detector, chosen over infrared to avoid wildlife false alarms.
- At industrial scale, Medtronic streams data from sensors, MES systems, and MQTT brokers into Kafka; Kafka Connect and MQTT connectors ingest it and Confluent Cloud scales across 350 sites.
- MQTT is the lightweight publish-subscribe protocol for IoT; guaranteeing at-least-once delivery from MQTT5 to Kafka required `cleanStart: false` with a positive `sessionExpiryInterval` plus manual acknowledgements.
- The global IoT market was expected to grow from $243 billion to $575 billion by 2027.
- IoT devices are a major driver of enterprise data volume, feeding analytics and machine learning.

## Related

- [event-driven architecture](/concepts/event-driven-architecture.md) — sensor events trigger workflows and alerts
- [real-time data streaming](/concepts/real-time-data-streaming.md) — delivering device events with guarantees
- [Medtronic](/entities/medtronic.md) — manufacturer streaming production-line IoT data
- [MQTT](/entities/mqtt.md) — the lightweight IoT messaging protocol
- [Apache Kafka](/entities/apache-kafka.md) — the event backbone IoT data lands in
