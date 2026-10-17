---
title: "Fun with IoT, Part 1"
type: "Source Summary"
description: "A maker project turns a Wemos D1 Mini and DHT22 sensor into a freezer temperature monitor that texts alerts via the Losant IoT platform."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, iot, improving.com]
sources:
  - "references/improving.com/fun-with-iot-part-1/fun-with-iot-part-1.md"
---

# Fun with IoT, Part 1 — Summary

**Original source**: `references/improving.com/fun-with-iot-part-1/fun-with-iot-part-1.md`

## Summary

To protect a basement deep freezer from a GFCI outlet that trips after power interruptions, Jeffrey Worner builds a temperature sensor that texts an alert when the freezer warms or loses power. The project pairs an inexpensive ESP8266 board with a temp/humidity sensor and reports to an IoT platform that handles notifications and dashboards.

## Key Claims

- The problem: a deep freezer on a GFCI outlet that trips unexpectedly, risking spoiled food; a friend's freezer had already failed.
- Hardware is a Wemos D1 Mini (ESP8266) Arduino board, typically under $3 each, paired with a DHT22 temperature/humidity sensor.
- The Arduino IDE flashes custom firmware; the board sends sensor data to the Losant IoT platform every 30 seconds.
- A Losant workflow sends a text message whenever the temperature rises above 20°F, and Losant provides a dashboard of current status and historical data.
- Because the sensor itself runs on A/C power, it stops reporting during an outage; Losant inactivity triggers at 15, 30, and 60 minutes cover that gap.

## Relevance

Informs [Internet of Things](/concepts/iot.md) sensing projects and [event-driven architecture](/concepts/event-driven-architecture.md), where threshold and inactivity events drive notifications.

## Quality

Practitioner maker walkthrough by Jeffrey Worner; concrete hardware and platform steps, light on production or security concerns.

## Entities Mentioned

- (none)

## Concepts Covered

- [Internet of Things](/concepts/iot.md) — sensing and reporting from a connected device
- [event-driven architecture](/concepts/event-driven-architecture.md) — workflow triggers on temperature and device-inactivity events
