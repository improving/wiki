---
title: "The Gateway Layer: Getting RTSP Cameras Onto WebRTC"
type: "Source Summary"
description: "A dedicated RTSP-to-WebRTC gateway layer keeps SFU fan-out separate from camera ingest; go2rtc vs MediaMTX."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/the-gateway-layer-getting-rtsp-cameras-onto-webrtc/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
---

# The Gateway Layer: Getting RTSP Cameras Onto WebRTC — Summary

**Original source**: `references/devlinliles.com/the-gateway-layer-getting-rtsp-cameras-onto-webrtc/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md`

## Summary

Argues every one-to-many IP-camera system needs a gateway layer between camera and SFU: take RTSP in, put WebRTC out, using passthrough where possible. Asking a general-purpose SFU to also own RTSP ingest, ONVIF control, and reconnection logic conflates two problem domains. Two purpose-built open-source tools fit: go2rtc (WebRTC-first, on-demand restreaming, RTP passthrough, sub-second latency, proven in Frigate-style NVR tooling) and MediaMTX (broader protocol support across RTSP, RTMP, HLS, WebRTC, and SRT).

## Key Claims

- A purpose-built gateway keeps the SFU focused on fan-out and lets camera ingest scale independently of viewer count.
- go2rtc restreams on demand, tying resource usage to actual viewership rather than camera count, and does RTP passthrough without re-encoding.
- MediaMTX (formerly rtsp-simple-server) speaks RTSP, RTMP, HLS, WebRTC, and SRT; HLS latency is often 6 to 30-plus seconds end to end.
- Both handle RTSP reconnection natively; that logic belongs in the gateway, not the SFU or application layer.
- Deployment shape matters: running the gateway near cameras shortens the RTSP hop and shields the pipeline from camera-side instability.
- Decision rule: WebRTC-only viewers favor go2rtc; any non-WebRTC downstream client favors MediaMTX.

## Relevance

Informs [selective forwarding unit](/concepts/selective-forwarding-unit.md) architecture and [RTP passthrough](/concepts/rtp-passthrough.md) as the pipeline's biggest performance lever.

## Quality

Practitioner blog post by Devlin Liles. Strengths: concrete tool comparisons and protocol tradeoffs. Caveat: opinionated recommendations without independent benchmarks.

## Entities Mentioned

- [WebRTC](/entities/webrtc.md) — the output protocol the gateway produces
- [RTSP](/entities/rtsp.md) — the camera-side input protocol
- [ONVIF](/entities/onvif.md) — camera discovery and control, kept out of the SFU
- [Frigate](/entities/frigate.md) — NVR ecosystem where go2rtc is battle-tested

## Concepts Covered

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the fan-out layer the gateway sits in front of
- [RTP Passthrough](/concepts/rtp-passthrough.md) — avoiding re-encoding at the gateway

## Related Sources

- [Beyond Detection: Activity Understanding](/sources/beyond-detection-activity-understanding.md)
