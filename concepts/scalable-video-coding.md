---
title: "Scalable Video Coding"
type: "Concept"
description: "Layered video encoding that lets an SFU forward adaptive quality per viewer without server-side transcoding."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, webrtc, streaming]
sources:
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# Scalable Video Coding

Scalable Video Coding (SVC) encodes a single video stream into layered temporal and spatial enhancement layers so a Selective Forwarding Unit can drop or forward layers per viewer without transcoding. Alongside simulcast, it is how this corpus achieves per-viewer adaptive quality at the server: rather than re-encode for each participant, the sender produces layers and the SFU selects. The choice between SVC and simulcast is then driven by per-device capability detection at connection time, not by a build-time flag.

## Key Claims

- Simulcast and SVC give per-viewer adaptive quality without server transcoding.
- LiveKit's distributed mesh via Redis absorbs unpredictable many-to-many concurrency; mediasoup offers the lowest CPU per participant but requires building platform layers.
- WebCodecs hardware decode is near-universal, but AV1 encode covers only about 88% of sessions.
- Firefox for Android lacks WebCodecs support entirely, making the API desktop-only there.
- `isConfigSupported` should be called at connection time, not baked into a build flag.
- Simulcast and SVC act on capability detection to match each viewer's decode ability.

## Related

- [Simulcast](/concepts/simulcast.md) — the sibling technique for per-viewer adaptation
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the server element that selects SVC layers
- [LiveKit](/entities/livekit.md) — an SFU that uses these techniques
- [mediasoup](/entities/mediasoup.md) — a lower-CPU library alternative
- [AV1](/entities/av1.md) — the codec whose limited encode support shapes layer selection
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the metric adaptive layering protects
- [LiveKit vs mediasoup](/sources/livekit-vs-mediasoup.md) — primary source
