---
title: "How I Enabled “At Least Once” Delivery from MQTT5 to a Kafka Topic"
type: "Source Summary"
description: "Details the MQTT5 session-persistence and manual-ack changes needed to guarantee at-least-once delivery from MQTT into Kafka."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, improving.com]
sources:
  - "references/improving.com/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md"
---

# How I Enabled “At Least Once” Delivery from MQTT5 to a Kafka Topic — Summary

**Original source**: `references/improving.com/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic/how-i-enabled-at-least-once-delivery-from-mqtt5-to-a-kafka-topic.md`

## Summary

The author shows why setting MQTT QoS to 1 is not enough to guarantee at-least-once delivery from MQTT5 into Kafka, because connections to the broker and to Kafka can drop mid-flight. The fix combines MQTT5's `cleanStart` and `sessionExpiryInterval` to persist sessions across disconnects with manual acknowledgements in the Paho MQTT5 consumer, so the broker only considers a message delivered after it is flushed to Kafka. A test with Mosquitto and Azure Event Hubs confirmed the fix.

## Key Claims

- Two problems must be solved: sessions must survive client–broker disconnects, and messages must reliably reach Kafka even if the connector–Kafka connection breaks.
- `cleanStart: false` with a positive `sessionExpiryInterval` keeps the session alive across disconnects (note: Paho's default of -1 did not take effect in testing).
- The Paho MQTT5 connector defaults to QoS 2, but if the connector–broker link drops after receipt, the broker assumes delivery succeeded.
- Enabling `manualAcks` and calling `messageArrivedComplete` only after the message is processed to Kafka prevents premature acknowledgement.
- A Kafka Connect test with Mosquitto and Azure Event Hubs reproduced the loss, then confirmed delivery with the fix.
- The author contributed the fix upstream as Apache Camel PR CAMEL-21589.

## Relevance

Informs [real-time data streaming](/concepts/real-time-data-streaming.md) and [event-driven architecture](/concepts/event-driven-architecture.md); touches [Internet of Things](/concepts/iot.md).

## Quality

Hands-on engineering write-up by Ravjot Brar; concrete and test-backed, with an upstream contribution to show for it.

## Entities Mentioned

- [Apache Camel](/entities/apache-camel.md) — the connector fixed
- [MQTT](/entities/mqtt.md) — the publish-subscribe protocol
- [Apache Kafka](/entities/apache-kafka.md) — the delivery target
- [Apache Software Foundation](/entities/apache-software-foundation.md) — stewards of Camel and Kafka

## Concepts Covered

- [real-time data streaming](/concepts/real-time-data-streaming.md) — delivery guarantees
- [event-driven architecture](/concepts/event-driven-architecture.md) — broker-to-stream pipelines
- [Internet of Things](/concepts/iot.md) — the MQTT sensor context
