---
title: "WebRTC"
type: "Entity"
description: "Browser real-time media standard whose topology, latency, and cost tradeoffs recur across this corpus's live-video posts."
created: '2026-10-17'
updated: '2026-10-17'
tags: [real-time-video, streaming, standard]
sources:
  - "/sources/choosing-a-video-topology-that-scales.md"
  - "/sources/failover-in-live-video.md"
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md"
  - "/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
  - "/sources/the-turn-tax-webrtcs-hidden-cost-center.md"
  - "/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# WebRTC

WebRTC is the browser standard for real-time audio and video. It anchors this corpus's live-video series, where topology, latency, and bandwidth-cost decisions determine whether a pipeline scales.

## Key Claims

- SFU topology beats mesh and MCU for one-to-many delivery because it forwards encoded packets instead of decoding and re-encoding; mesh collapses past three or four participants.
- Glass-to-glass latency is dominated by keyframe interval and jitter buffering, not network transit, so shortening GOP is the cheapest win.
- RTSP and WebRTC both carry media over RTP, so repackaging usually removes the CPU-expensive transcode step.
- TURN-relayed traffic costs bandwidth twice and adds latency for viewers behind symmetric NAT and restrictive firewalls.
- Signaling is stateless and media relay is stateful, so the control plane and data plane must scale separately.
- A thundering herd is a step function, not the gradual ramp most load tests simulate.

## Related

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the scalable one-to-many topology
- [Media relay](/concepts/media-relay.md) — the stateful data plane
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the only user-facing measurement
- [RTP Passthrough](/concepts/rtp-passthrough.md) — why transcoding can be removed
- [TURN](/entities/turn.md) — the hidden relay cost center
- [RTSP](/entities/rtsp.md) — the camera protocol it must bridge
- [Choosing a Video Topology That Scales](/sources/choosing-a-video-topology-that-scales.md) — primary source
