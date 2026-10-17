---
title: "Latency Budget"
type: "Concept"
description: "The finite delay a system can spend before a task fails, allocated across inference, network, and buffering stages."
created: '2026-10-17'
updated: '2026-10-17'
tags: [latency, edge, video, architecture]
sources:
  - "/sources/crowd-counting-and-environmental-hazard-detection.md"
  - "/sources/recognition-at-the-edge.md"
  - "/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# Latency Budget

A latency budget is the finite delay a system can spend before a task stops being useful, allocated across inference, network, and buffering stages. Across this corpus the budget is the constraint that decides where inference runs and what load behavior a system must survive.

## Key Claims

- Fire and smoke detection carries a hard sub-100 millisecond constraint, forcing inference onto camera SoCs rather than the cloud.
- [Edge recognition](/concepts/edge-inference.md) answers in 30-100ms versus 800-2000ms in the cloud, and keeps access decisions working during WAN outages.
- Crowd counting is density estimation rather than people counting; pushing inference to the camera and shipping counts, not video, preserves the budget.
- Alert-driven traffic arrives as a step function, not a gradual ramp; gradual load tests verify only one shape of demand, not the shape that matters.
- Diagnosing a latency blowout requires stage-by-stage inspection — CPU, network, transcoding, latency, browser playback — profiled per stream, because host-level averages hide the saturated stream.

## Related

- [edge inference](/concepts/edge-inference.md) — how the budget forces computation local
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the end-to-end measurement of budget spent
- [Egress bandwidth](/concepts/egress-bandwidth.md) — a coupled resource cost under load
- [Recognition at the Edge](/sources/recognition-at-the-edge.md) — primary source
