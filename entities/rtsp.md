---
title: "RTSP"
type: "Entity"
description: "Camera streaming protocol that carries media over RTP, letting gateways repackage feeds for WebRTC instead of transcoding."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, streaming, protocol]
sources:
  - "/sources/failover-in-live-video.md"
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
  - "/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# RTSP

RTSP is the streaming protocol used by most IP cameras. Across this corpus it is the ingest half of a recurring RTSP-to-WebRTC pipeline, and the source of a set of practical trade-offs about transcoding, latency, failover, and load.

## Overview

Because RTSP and WebRTC both carry media over RTP, the expensive transcode step is often unnecessary. Writers recommend a purpose-built gateway in front of the SFU, with go2rtc or MediaMTX chosen by protocol needs, and camera reconnection logic kept close to the protocol.

## Key Claims

- RTSP and WebRTC both carry media over RTP, so repackaging can replace transcoding.
- Passthrough depends on codec profile compatibility; H.264 baseline and main maximize decode support.
- Long camera GOPs force new viewers to wait seconds for a first keyframe.
- Duplicate ingest buys a near-zero failover gap at continuously doubled ingest cost.
- Alert-driven thundering herds are a step function that gradual load tests never surface.

## Related

- [RTP Passthrough](/concepts/rtp-passthrough.md) — the technique that avoids transcoding RTSP
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the measure RTSP tuning targets
- [WebRTC](/entities/webrtc.md) — the egress protocol RTSP is bridged to
- [The Gateway Layer](/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md) — primary source
