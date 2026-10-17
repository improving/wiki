---
title: "Apache Camel"
type: "Entity"
description: "Integration framework whose MQTT5-to-Kafka connector was patched here for at-least-once delivery."
created: '2026-10-17'
updated: '2026-10-17'
tags: [integration, streaming, apache]
sources:
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic.md"
  - "/sources/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md"
---

# Apache Camel

Apache Camel is an open-source integration framework, stewarded by the [Apache Software Foundation](/entities/apache-software-foundation.md), that routes messages between protocols and systems. In this corpus it appears as the connector between [MQTT](/entities/mqtt.md) and [Apache Kafka](/entities/apache-kafka.md), and as the place where a delivery-guarantee bug was fixed and contributed upstream.

## Role in the MQTT-to-Kafka Pipeline

- The Camel MQTT5 connector carries sensor messages from an MQTT broker into a Kafka topic.
- Its Paho MQTT5 integration defaults connector QoS to 2, which lets the broker assume delivery even if the connector-to-Kafka link drops.
- Enabling `manualAcks` and calling `messageArrivedComplete` only after a message is processed to Kafka prevents premature acknowledgement.

## Upstream Contribution

- The author reproduced message loss with Kafka Connect in Docker, Mosquitto, and an Azure Event Hubs namespace, then confirmed delivery after the fix.
- The change was contributed upstream as Apache Camel PR and issue CAMEL-21589.
- The work is a concrete example of [data integration](/concepts/data-integration.md) and [event-driven architecture](/concepts/event-driven-architecture.md) delivery guarantees.

## Related

- [MQTT](/entities/mqtt.md) — the protocol carrying the messages
- [Apache Kafka](/entities/apache-kafka.md) — the delivery target topic
- [Apache Software Foundation](/entities/apache-software-foundation.md) — stewards of Camel and Kafka
- [real-time data streaming](/concepts/real-time-data-streaming.md) — the delivery guarantees at stake
