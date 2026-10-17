---
title: "Choosing a Video Topology That Scales"
type: "Source Summary"
description: "Opening a series on WebRTC video architecture, arguing SFU is the right default topology for one-to-many live video."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/choosing-a-video-topology-that-scales/choosing-a-video-topology-that-scales.md"
---

# Choosing a Video Topology That Scales — Summary

**Original source**: `references/devlinliles.com/choosing-a-video-topology-that-scales/choosing-a-video-topology-that-scales.md`

## Summary

Opening a series on [WebRTC](/entities/webrtc.md) media-server architecture, Devlin Liles argues the first decision — the video topology — determines whether the rest of the system is easy or miserable. He defines [glass-to-glass latency](/concepts/glass-to-glass-latency.md) as the total delay from camera capture to screen render, then compares the three WebRTC topologies (mesh, MCU, SFU). For one-to-many live video, where few sources feed many viewers, he concludes the [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) is almost always the right choice.

## Key Claims

- Mesh connects every participant directly to every other; a four-way call uploads three copies per person and decodes three incoming streams, and it tops out around three to four participants.
- MCU decodes, composites, and re-encodes server-side; powerful but CPU-expensive and scales poorly when no compositing is needed.
- SFU forwards encoded packets without decode/re-encode, so ingest cost is paid once per source and fan-out scales to ten or ten thousand viewers.
- [LiveKit](/entities/livekit.md), [mediasoup](/entities/mediasoup.md), and [Janus](/entities/janus.md) are all built on SFU architecture — the pattern is "forward, don't transcode."
- Caveat: server-side mixing for recording or broadcast still calls for an MCU.

## Relevance

Foundational for [glass-to-glass latency](/concepts/glass-to-glass-latency.md) and [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md); frames the rest of the series on gateway design, sharding, and load testing.

## Quality

Practitioner blog post by Devlin Liles. Clear comparative reasoning and topology math; figures are illustrative scaling arguments rather than measured benchmarks, and the platform comparison is deferred to later posts.

## Entities Mentioned

- [WebRTC](/entities/webrtc.md) — the technology providing the three topologies
- [LiveKit](/entities/livekit.md) — SFU-based platform cited as example
- [mediasoup](/entities/mediasoup.md) — SFU-based platform cited as example
- [Janus](/entities/janus.md) — SFU-based platform cited as example

## Concepts Covered

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the recommended topology for one-to-many
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the metric the whole series is organized around
