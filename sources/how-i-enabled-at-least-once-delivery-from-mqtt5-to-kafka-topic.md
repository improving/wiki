---
title: "How I Enabled “At Least Once” Delivery from MQTT5 to Kafka Topic"
type: "Source Summary"
description: "Shows how MQTT5 session persistence and manual acknowledgements achieve at-least-once delivery from MQTT to a Kafka topic."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, data, streaming, improving.com]
sources:
  - "references/improving.com/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic.md"
---

# How I Enabled “At Least Once” Delivery from MQTT5 to Kafka Topic — Summary

**Original source**: `references/improving.com/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic/how-i-enabled-at-least-once-delivery-from-mqtt5-to-kafka-topic.md`

## Summary

At-least-once delivery guarantees messages reach their target despite disruptions, which matters for fault tolerance, data integrity, and high availability. Setting MQTT QoS to 1 is not enough: the client session must survive disconnects and the connector must confirm messages were actually flushed to Kafka. The author combines MQTT5's `cleanStart=false` with `sessionExpiryInterval>0` to persist sessions, and enables manual acknowledgements in Paho MQTT5 so the broker waits until messages are processed to Kafka. The fix was contributed upstream to Apache Camel.

## Key Claims

- At-least-once delivery ensures messages are delivered to the target at least once; the receiver ACKs each message and the sender retransmits on missing ACKs.
- MQTT QoS 1 alone is insufficient because it does not cover session loss or failures between the connector and Kafka.
- Setting `cleanStart=false` with `sessionExpiryInterval>0` persists the client session across disconnects.
- Paho's documentation says `sessionExpiryInterval` defaults to -1 (no expiry), but the author's tests required a positive value for it to take effect.
- Paho MQTT5 defaults connector QoS to 2, which lets the broker assume delivery even if the connector-to-Kafka link drops.
- Enabling `manualAcks` makes the connector acknowledge only after processing to Kafka, via `messageArrivedComplete`.
- The test used Kafka Connect in Docker with an Azure Event Hubs namespace and Mosquitto; messages sent during a connection interruption were delivered after the fix.
- The fix was submitted as Apache Camel PR CAMEL-21589 (issue CAMEL-21589).

## Relevance

Informs [real-time data streaming](/concepts/real-time-data-streaming.md), [event-driven architecture](/concepts/event-driven-architecture.md), and [data integration](/concepts/data-integration.md) with a concrete delivery-guarantee implementation.

## Quality

Hands-on engineering write-up by Ravjot Brar; specific, test-backed, and includes a contributed upstream fix.

## Entities Mentioned

- [Apache Kafka](/entities/apache-kafka.md) — the delivery target topic
- [MQTT](/entities/mqtt.md) — publish-subscribe protocol carrying the messages
- [Apache Camel](/entities/apache-camel.md) — connector where the manual-ack fix was made

## Concepts Covered

- [real-time data streaming](/concepts/real-time-data-streaming.md) — delivery guarantees and ordering
- [event-driven architecture](/concepts/event-driven-architecture.md) — decoupled producers and consumers
- [data integration](/concepts/data-integration.md) — connecting MQTT and Kafka
