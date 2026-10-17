---
title: "Selective Forwarding Unit"
type: "Concept"
description: "A media server that forwards encoded packets to many viewers, paying ingest once instead of decoding and re-encoding."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, media-server, video, scaling]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/matching-the-tool-to-the-workload.md"
  - "/sources/migrating-off-a-legacy-media-server.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
---

# Selective Forwarding Unit

The Selective Forwarding Unit (SFU) is the default topology for one-to-many and many-to-many live video: it accepts a stream once per source and forwards the encoded packets to each viewer, so cost grows with fan-out rather than with decode work. Across this corpus it is the baseline media-server architecture, with MCU pipelines reserved for the cases that genuinely need in-flight processing.

## Key Claims

- Mesh topology collapses past three or four participants because upload and decode costs grow with every peer.
- An MCU decodes, composites, and re-encodes every stream, so its cost scales with the number of streams; server-side compositing is the case where an MCU is still correct.
- The SFU pays ingest once per source and fans out cheaply to many viewers.
- Simulcast and SVC give each viewer adaptive quality without server transcoding.
- A lean SFU is better for RTSP-in, WebRTC-out fan-out with no media processing; GStreamer pipelines (Kurento) earn their weight only when media must be mixed, recorded, or analyzed in flight.
- LiveKit and mediasoup share the SFU architecture but differ in packaging: LiveKit is the default, mediasoup is a library for teams wanting lower CPU per participant.

## Related

- [Simulcast](/concepts/simulcast.md) — per-viewer adaptive quality without transcoding
- [Media relay](/concepts/media-relay.md) — the forwarding behavior an SFU generalizes
- [Scalable Video Coding](/concepts/scalable-video-coding.md) — the layered alternative to simulcast
- [LiveKit](/entities/livekit.md) — packaged SFU default
- [mediasoup](/entities/mediasoup.md) — SFU library
- [Choosing a Video Topology That Scales](/sources/choosing-a-video-topology-that-scales.md) — primary source
