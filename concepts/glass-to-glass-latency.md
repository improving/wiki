---
title: "glass-to-glass latency"
type: "Concept"
description: "The delay from a camera capturing a frame to a viewer seeing it, dominated by keyframes and buffering rather than network transit."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, latency, streaming, realtime]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/the-turn-tax-webrtcs-hidden-cost-center.md"
---

# glass-to-glass latency

Glass-to-glass latency is the total delay from the moment a camera captures a frame to the moment a viewer sees it. It is the only measurement that captures the live-video user experience, and across this corpus it is treated as the metric that determines whether a system feels live or merely near-live.

## Key Claims

- Glass-to-glass latency is dominated by [keyframe interval](/concepts/keyframe-interval.md) and [jitter buffering](/concepts/jitter-buffer.md), not network transit.
- Long camera GOPs force new viewers to wait seconds for the first keyframe; cameras default to long GOPs for recording efficiency, hurting live viewing.
- Shortening GOP via [ONVIF](/entities/onvif.md) is described as the cheapest latency win available, with jitter buffer tuning as the follow-on fix.
- Relay paths add latency: [TURN](/entities/turn.md)-relayed traffic is received and forwarded, costing bandwidth twice for viewers behind restrictive networks.
- Topology choices bound latency: [SFU](/concepts/selective-forwarding-unit.md) forwarding avoids the decode/re-encode cost that MCU compositing adds.

## Related

- [Keyframe interval](/concepts/keyframe-interval.md) — the cheapest lever over this metric
- [Jitter buffer](/concepts/jitter-buffer.md) — buffering that trades smoothness for delay
- [Latency Budget](/concepts/latency-budget.md) — the allocation this metric consumes
- [Keyframes and Latency](/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md) — primary source
