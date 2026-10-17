---
title: "Jitter buffer"
type: "Concept"
description: "A receiver-side buffer that absorbs network timing variance, trading added latency for smoother playback."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, latency, video]
sources:
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md"
---

# Jitter buffer

A receiver-side buffer that holds arriving packets long enough to absorb network timing variance, trading added latency for smoother playback. It matters because it is one of the two dominant contributors to [glass-to-glass latency](/concepts/glass-to-glass-latency.md), and because its right size only shows up under injected network conditions.

## Key Claims

- Glass-to-glass latency, not network transit, is dominated by [keyframe interval](/concepts/keyframe-interval.md) and jitter buffering.
- The jitter buffer needs tuning; shortening the camera GOP via ONVIF is the cheaper win of the two.
- WebRTC load tests must vary viewers-per-stream and streams-per-instance independently because each stresses a different bottleneck.
- Viewers-per-stream stresses egress bandwidth rather than CPU, while streams-per-instance stresses CPU and transcode density.
- Synthetic clients scale connection counts, but browser swarms reveal real playback experience.
- Network condition injection is what surfaces jitter-buffer and packet-loss problems.

## Related

- [keyframe interval](/concepts/keyframe-interval.md) — the other dominant latency term
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the measurement that captures user experience
- [Egress bandwidth](/concepts/egress-bandwidth.md) — the viewers-per-stream bottleneck
- [WebRTC](/entities/webrtc.md) — transport context
- [Keyframes and Latency](/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md) — primary source
- [Load Testing WebRTC at Scale](/sources/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md) — primary source
