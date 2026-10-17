---
title: "Redis"
type: "Entity"
description: "In-memory data store used as the coordination layer behind distributed SFU meshes and as a queue between live and processing tiers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [infrastructure, realtime, messaging]
sources:
  - "/sources/livekit-vs-mediasoup.md"
  - "/sources/structuring-the-middle-of-the-pipeline.md"
---

# Redis

Redis is an in-memory data store commonly used for caching, pub/sub, and lightweight message brokering. In this corpus it appears twice in real-time media architectures: as the coordination backbone of LiveKit's distributed mesh, and as the queue that decouples stream processing from the live viewer path.

## Overview

The LiveKit-versus-mediasoup comparison notes that LiveKit's distributed mesh uses Redis to absorb unpredictable many-to-many concurrency — the kind of scale a single node cannot predict in advance. The pipeline-structuring post uses a queue (a Redis-style component) to branch heavy central processing off the live fan-out path, protecting viewer latency while letting the processing tier autoscale independently.

## Key Claims

- LiveKit's distributed mesh via Redis absorbs unpredictable many-to-many concurrency
- Routing processing through the live fan-out path adds viewer-facing latency, so the stream is branched to a decoupled tier via a queue
- SFU and processing tiers scale on different signals and need separate autoscaling groups
- Monitoring the two tiers separately speeds incident response
- The LiveKit-versus-mediasoup choice is expensive to reverse once woven into application code

## Related

- [LiveKit](/entities/livekit.md) — uses Redis for its distributed mesh
- [mediasoup](/entities/mediasoup.md) — the alternative that leaves more platform layers to the team
- [In-Pipeline Processing](/concepts/in-pipeline-processing.md) — the pattern Redis-backed queues decouple
- [Structuring the Middle of the Pipeline](/sources/structuring-the-middle-of-the-pipeline.md) — primary source
