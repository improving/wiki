---
title: "The Last Few Feet: Endpoint Optimization"
type: "Source Summary"
description: "The final few feet of a video pipeline are the viewer's device: detect per-device decode capability and drive simulcast/SVC selection from it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/the-last-few-feet-endpoint-optimization/the-last-few-feet-endpoint-optimization.md"
---

# The Last Few Feet: Endpoint Optimization — Summary

**Original source**: `references/devlinliles.com/the-last-few-feet-endpoint-optimization/the-last-few-feet-endpoint-optimization.md`

## Summary

Closes a sixteen-post series by arguing the last mile — the device actually decoding the stream — can waste otherwise perfect upstream engineering. WebCodecs makes this tractable: hardware decode is close to universal (AV1 plus HEVC covers roughly 99.7% of sessions on Chrome, Edge, and Firefox), but encode is constrained (about 88% support AV1, only with the correct codec string). "Close to universal" still has edges. The fix is a live per-device capability check at connection time, used to drive simulcast and SVC layer selection rather than one setting for every viewer.

## Key Claims

- Decode is close to solved; encode still has real constraints, and the gap shows up as production support tickets.
- Roughly 88% of sessions support AV1 encoding, and only with the correct codec string — Profile 0, 8-bit.
- Firefox for Android supports WebCodecs in no version; Safari shipped video-only support across versions 16.4 through 18.7.
- Capability must be checked live per device via isConfigSupported before committing to a codec and profile, not as a build flag or static browser-version table.
- Simulcast and SVC are the mechanism that lets you act on capability detection, matching a layer per viewer.
- Keyframe interval is also a decode-side cost; a GOP tuned purely for glass-to-glass latency can overwhelm a weak device.
- When server-side metrics are clean and playback is choppy, the cause is client-side.

## Relevance

Informs [simulcast](/concepts/simulcast.md), [scalable video coding](/concepts/scalable-video-coding.md), [keyframe interval](/concepts/keyframe-interval.md), [glass-to-glass latency](/concepts/glass-to-glass-latency.md), and [jitter buffer](/concepts/jitter-buffer.md) considerations.

## Quality

Practitioner blog post by Devlin Liles. Strengths: concrete usage percentages and API guidance. Caveat: figures come from the author's own aggregated sessions and are not independently verified.

## Entities Mentioned

- [LiveKit](/entities/livekit.md) — platform compared earlier in the series
- [mediasoup](/entities/mediasoup.md) — platform compared earlier in the series
- [AV1](/entities/av1.md) — the codec whose encode support is the constraint
- [H.264](/entities/h-264.md) — the baseline decode codec
- [WebRTC](/entities/webrtc.md) — the transport whose endpoint this post optimizes

## Concepts Covered

- [Simulcast](/concepts/simulcast.md) — acting on per-device capability
- [Scalable Video Coding](/concepts/scalable-video-coding.md) — the alternative layering mechanism
- [Keyframe interval](/concepts/keyframe-interval.md) — a decode-side cost, not just latency
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the pipeline metric this layer affects
- [Jitter buffer](/concepts/jitter-buffer.md) — a client-side factor in choppy playback
