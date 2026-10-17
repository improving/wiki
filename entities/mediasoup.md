---
title: "mediasoup"
type: "Entity"
description: "An open-source SFU library offering the lowest CPU per participant at the cost of building platform layers yourself."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, sfu, video, library]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# mediasoup

mediasoup is an open-source selective forwarding unit (SFU) library for WebRTC, presented in this corpus as the low-level, high-ownership alternative to a batteries-included SFU platform.

## Overview

For one-to-many live video, SFU topology beats mesh and MCU because it forwards encoded packets instead of decoding and re-encoding. mediasoup sits at the lowest level of that space: it offers the lowest CPU per participant but requires teams to build their own platform layers, whereas LiveKit's distributed mesh absorbs unpredictable many-to-many concurrency out of the box. On the endpoint side, simulcast and SVC give per-viewer adaptive quality without server transcoding, and capability detection at connection time drives layer selection.

## Key Claims

- SFU pays ingest once per source and fans out cheaply to many viewers
- mediasoup offers the lowest CPU per participant but requires building platform layers
- Simulcast and SVC give per-viewer adaptive quality without server transcoding
- isConfigSupported should be called at connection time, not baked into a build flag
- The SFU choice is expensive to reverse once woven into application code

## Related

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the topology mediasoup implements
- [Simulcast](/concepts/simulcast.md) — per-viewer adaptive layer selection
- [Scalable Video Coding](/concepts/scalable-video-coding.md) — the SVC alternative
- [LiveKit](/entities/livekit.md) — the higher-level SFU platform
- [WebRTC](/entities/webrtc.md) — the transport it builds on
- [LiveKit vs mediasoup](/sources/livekit-vs-mediasoup.md) — primary source
