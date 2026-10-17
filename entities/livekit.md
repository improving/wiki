---
title: "LiveKit"
type: "Entity"
description: "Open-source SFU media server that is the default real-time video platform for most teams in this corpus."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, media-server, sfu]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/matching-the-tool-to-the-workload.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# LiveKit

LiveKit is an open-source [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) for real-time video and audio. Across these posts it is treated as the default SFU choice for most teams: a packaged platform that absorbs unpredictable concurrency, contrasted with mediasoup's lower-level library approach and with tools built for narrower problems.

## Key Claims

- LiveKit's distributed mesh via Redis absorbs unpredictable many-to-many concurrency, at the cost of more moving parts ([livekit vs mediasoup](/sources/livekit-vs-mediasoup.md))
- It shares the SFU architecture with mediasoup but differs in packaging, offering platform layers that mediasoup leaves to the team to build ([matching the tool to the workload](/sources/matching-the-tool-to-the-workload.md))
- SFU topology beats mesh and MCU for one-to-many because it forwards encoded packets instead of decoding and re-encoding ([choosing a video topology that scales](/sources/choosing-a-video-topology-that-scales.md))
- [Simulcast](/concepts/simulcast.md) and [SVC](/concepts/scalable-video-coding.md) give per-viewer adaptive quality without server transcoding, driven by capability detection at connection time ([the last few feet](/sources/the-last-few-feet-endpoint-optimization.md))
- The platform choice is expensive to reverse once woven into application code.

## Related

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — LiveKit's topology
- [mediasoup](/entities/mediasoup.md) — the library alternative
- [Simulcast](/concepts/simulcast.md) — adaptive quality mechanism
- [Janus](/entities/janus.md) — the SIP-bridging alternative
- [WebRTC](/entities/webrtc.md) — the transport it builds on
