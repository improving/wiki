---
title: "Janus"
type: "Entity"
description: "An open-source WebRTC media server chosen in this corpus for SIP-bridging and SFU workloads."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, media-server, sfu, video]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/matching-the-tool-to-the-workload.md"
---

# Janus

Janus is an open-source WebRTC media server that forwards encoded packets rather than decoding and re-encoding them. In this corpus it appears both as the generic example of an SFU topology and as the specific tool to pick when video must bridge with SIP telephony.

## Overview

- As an SFU, Janus pays ingest once per source and fans out cheaply to many viewers.
- Mesh topology collapses past three or four participants; an MCU decodes, composites, and re-encodes, so its cost scales with streams.
- Server-side compositing is the case where an MCU remains correct.
- Janus is the choice when video must bridge with SIP telephony.
- Tool selection should follow workload requirements, not popularity — LiveKit and mediasoup share an SFU architecture differing mainly in packaging.
- Picking a tool by star count means fighting both the tool and the problem.

## Related

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the topology Janus implements
- [WebRTC](/entities/webrtc.md) — the transport it serves
- [LiveKit](/entities/livekit.md) — an SFU alternative
- [mediasoup](/entities/mediasoup.md) — another SFU in the same comparison
- [ICE](/entities/ice.md) — the connectivity layer beneath it
- [Matching the Tool to the Workload](/sources/matching-the-tool-to-the-workload.md) — primary source
