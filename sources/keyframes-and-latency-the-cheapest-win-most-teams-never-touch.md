---
title: "Keyframes and Latency: The Cheapest Win Most Teams Never Touch"
type: "Source Summary"
description: "In RTSP-to-WebRTC video, shortening the camera keyframe interval is the cheapest latency fix, far cheaper than network optimization."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/keyframes-and-latency-the-cheapest-win-most-teams-never-touch/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
---

# Keyframes and Latency: The Cheapest Win Most Teams Never Touch — Summary

**Original source**: `references/devlinliles.com/keyframes-and-latency-the-cheapest-win-most-teams-never-touch/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md`

## Summary

Teams debugging live-video latency reach first for network transit, but in most RTSP-to-WebRTC setups the time is going elsewhere. Walking the full glass-to-glass path, Liles shows that two configuration stages dominate: waiting for a usable keyframe at capture/encode, and client-side jitter buffering. IP cameras ship with long GOPs tuned for recording efficiency, so a new viewer can stare at black for seconds. Shortening the keyframe interval via ONVIF is the cheapest available win; jitter buffer tuning is the second lever, matched to real network conditions rather than minimized.

## Key Claims

- Network transit is typically tens of milliseconds per hop, and gateway passthrough processing is near zero; neither is the real bottleneck.
- A new viewer cannot render until the next keyframe arrives, so a 2–4 second GOP means up to 4 seconds of black screen — independent of network.
- Cameras default to long GOPs for storage efficiency; the recording tradeoff inverts the moment a live viewer appears.
- Target a 0.5–1 second keyframe interval; moving from a 4-second to a 1-second GOP roughly quadruples keyframe frequency but adds only a modest percentage of total bandwidth.
- Verify the setting landed on the camera: some firmware silently ignores unsupported ONVIF parameters.

## Relevance

Core to [glass-to-glass latency](/concepts/glass-to-glass-latency.md), [keyframe interval](/concepts/keyframe-interval.md), and [jitter buffer](/concepts/jitter-buffer.md) tuning in real-time video systems.

## Quality

Practitioner blog post by Devlin Liles. Concrete and actionable with clear mechanism; latency numbers are explicitly labeled illustrative rather than measured from a specific deployment.

## Entities Mentioned

- [ONVIF](/entities/onvif.md) — standard protocol used to push the GOP shorter at the source
- [WebRTC](/entities/webrtc.md) — the delivery stack on the viewer side
- [RTSP](/entities/rtsp.md) — camera-to-gateway transport

## Concepts Covered

- [Glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the full-path metric that matters
- [Keyframe interval](/concepts/keyframe-interval.md) — the primary configuration lever
- [Jitter buffer](/concepts/jitter-buffer.md) — the second lever, a tuning problem not a removal problem
- [Latency budget](/concepts/latency-budget.md) — stages that consume the delay allowance

## Related Sources

- [Failover in Live Video](/sources/failover-in-live-video.md)
