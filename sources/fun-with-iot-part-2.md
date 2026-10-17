---
title: "Fun With IoT Part 2"
type: "Source Summary"
description: "A DIY driveway monitor built from a magnetic sensor, Wemos D1 Mini, and range-extended I2C after an off-the-shelf unit failed."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, iot, engineering, improving.com]
sources:
  - "references/improving.com/fun-with-iot-part-2/fun-with-iot-part-2.md"
---

# Fun With IoT Part 2 — Summary

**Original source**: `references/improving.com/fun-with-iot-part-2/fun-with-iot-part-2.md`

## Summary

Jeffrey Worner documents building a driveway monitor after a retail Mighty Mule unit failed to penetrate his ICF-walled home. He pairs a QMC5883L magnetic sensor with a Wemos D1 Mini over Cat-6 with an I2C range extender, uses a rolling average to detect passing vehicles, and alerts indoors via a second Wemos unit that texts him through Losant.

## Key Claims

- The Mighty Mule monitor failed because the home's insulating concrete forms block radio waves, requiring a prior 4G signal booster.
- An outdoor WiFi access point hard-wired to the LAN provided a path for the signal into the house.
- A QMC5883L 3-axis magnetic sensor was chosen over infrared because it detects only ferrous metal, avoiding wildlife false alarms.
- The sensor's X/Y/Z readings are normalized to one value; a rolling average adapts to conditions and triggers when a reading deviates too much.
- The Wemos D1 Mini uses I2C, designed for short on-board distances, so the ~150ft Cat-6 run needed an I2C range extender rated for 100ft.
- An indoor Wemos D1 Mini plays a tone and sends data to Losant for a text alert.
- The build cost more time and money than the retail product, but the learning was the point.

## Relevance

An [Internet of Things](/concepts/iot.md) build that is effectively a small [event-driven architecture](/concepts/event-driven-architecture.md) of sensor and alert.

## Quality

Maker write-up by Jeffrey Worner; candid about false starts and cost, with hardware specifics but no performance measurements.

## Entities Mentioned

- (none)

## Concepts Covered

- [Internet of Things](/concepts/iot.md) — networked devices that sense and act
- [event-driven architecture](/concepts/event-driven-architecture.md) — a sensor event triggers an alert
