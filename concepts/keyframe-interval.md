---
title: "Keyframe interval"
type: "Concept"
description: "The spacing between intra-coded frames; a shorter GOP cuts join latency for live viewers at bandwidth cost."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, latency, encoding]
sources:
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# Keyframe interval

The spacing between intra-coded frames (the GOP length). It matters because a long keyframe interval forces every newly joined viewer to wait for the next keyframe before they see anything, which is often the largest controllable slice of [glass-to-glass latency](/concepts/glass-to-glass-latency.md).

## Key Claims

- Glass-to-glass latency is the only measurement that captures user experience.
- Long camera GOPs force new viewers to wait seconds for the first keyframe.
- Cameras default to long GOPs for recording efficiency, which hurts live viewing.
- Shortening the GOP via [ONVIF](/entities/onvif.md) is the cheapest latency win available to most teams.
- The [jitter buffer](/concepts/jitter-buffer.md) needs separate tuning; GOP changes do not cover it.
- Per-device capability detection at connection time drives [simulcast](/concepts/simulcast.md) and SVC layer selection, and `isConfigSupported` should be called then rather than baked into a build flag.

## Related

- [jitter buffer](/concepts/jitter-buffer.md) — the other half of the latency budget
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — what GOP length moves
- [ONVIF](/entities/onvif.md) — configuration surface for camera GOPs
- [Simulcast](/concepts/simulcast.md) — layer selection driven by endpoint capability
- [Keyframes and Latency](/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md) — primary source
- [The Last Few Feet: Endpoint Optimization](/sources/the-last-few-feet-endpoint-optimization.md) — primary source
