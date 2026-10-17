---
title: "Simulcast"
type: "Concept"
description: "Sending multiple resolution layers so each viewer receives quality matched to its decode capability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, webrtc, realtime]
sources:
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# Simulcast

Simulcast sends several independently encoded layers of the same video so a selective forwarding unit can hand each viewer the layer its device and network can actually handle. It is the mechanism behind per-viewer adaptive quality without server-side transcoding, and in the corpus it sits alongside SVC as one of the two ways real-time platforms match stream to endpoint.

## Key Claims

- Simulcast and SVC give per-viewer adaptive quality without server transcoding.
- Layer selection depends on per-device capability detection at connection time.
- WebCodecs hardware decode is near-universal, but AV1 encode covers only about 88% of sessions.
- Firefox for Android lacks WebCodecs entirely, making the API desktop-only there.
- isConfigSupported should be called at connection time, not baked into a build flag.
- The SFU choice that carries these layers is expensive to reverse once woven into application code.

## Related

- [Scalable Video Coding](/concepts/scalable-video-coding.md) — the other adaptive-quality mechanism
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the component that selects layers per viewer
- [AV1](/entities/av1.md) — a codec whose encode support limits layer coverage
- [WebRTC](/entities/webrtc.md) — the transport stack these layers ride on
- [LiveKit vs mediasoup](/sources/livekit-vs-mediasoup.md) — primary source
- [The Last Few Feet: Endpoint Optimization](/sources/the-last-few-feet-endpoint-optimization.md) — primary source
