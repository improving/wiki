---
title: "MQTT"
type: "Entity"
description: "Lightweight publish-subscribe protocol for IoT sensor and device messaging, here feeding Kafka pipelines."
created: '2026-10-17'
updated: '2026-10-17'
tags: [iot, streaming, protocols]
sources:
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic.md"
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md"
  - "/sources/how-a-global-healthcare-manufacturer-transformed-production-lines.md"
  - "/sources/crowd-counting-and-environmental-hazard-detection.md"
---

# MQTT

MQTT is a lightweight publish-subscribe messaging protocol used by IoT devices and sensors to move small messages over constrained networks. In this corpus it is the factory-floor and edge protocol that feeds [Apache Kafka](/entities/apache-kafka.md) pipelines, and the subject of a hard-won at-least-once delivery fix.

## In the Streaming Pipeline

- At Medtronic, data from IoT devices, sensors, MES systems, and MQTT brokers streams into Kafka, with Kafka Connect MQTT connectors ingesting production-line data.
- MQTT carries the sensor context for [real-time data streaming](/concepts/real-time-data-streaming.md) and [event-driven architecture](/concepts/event-driven-architecture.md).
- Edge computer-vision deployments keep raw video local and ship only small structured signals (counts, zone states) over MQTT or REST.

## Delivery Guarantees

- Setting MQTT QoS to 1 alone is insufficient for at-least-once delivery into Kafka, because it does not cover session loss or failures between the connector and Kafka.
- MQTT5's `cleanStart=false` with a positive `sessionExpiryInterval` persists the client session across disconnects; Paho's default of -1 did not take effect in testing.
- Paho MQTT5 defaults connector QoS to 2, so the broker can assume delivery even when the connector-to-Kafka link drops — the gap fixed in [Apache Camel](/entities/apache-camel.md) PR CAMEL-21589.

## Related

- [Apache Camel](/entities/apache-camel.md) — the connector where the manual-ack fix was made
- [Apache Kafka](/entities/apache-kafka.md) — the delivery target
- [Medtronic](/entities/medtronic.md) — factory-floor case using MQTT brokers
- [Internet of Things](/concepts/iot.md) — the device context MQTT serves
