---
title: "Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline"
type: "Source Summary"
description: "RTSP and WebRTC both carry RTP, so gateways can repackage packets instead of transcoding when codec profiles allow."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
---

# Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline — Summary

**Original source**: `references/devlinliles.com/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md`

## Summary

Argues the biggest CPU lever in an RTSP-to-WebRTC pipeline is eliminating transcoding entirely. Because both protocols carry media over RTP, a gateway can repackage camera RTP into SRTP for WebRTC without decoding or re-encoding a single frame. The only condition is codec profile compatibility between camera and browser decoders, which is cheap to check and often already satisfied.

## Key Claims

- RTSP and WebRTC both use RTP; WebRTC wraps it in SRTP negotiated over DTLS, so passthrough is a packaging change, not a media operation.
- Passthrough depends on codec profile: H.264 baseline and main are safe for broad browser decode; high profile and H.265 often force transcoding.
- Transcoding (decode plus re-encode) is the single most CPU-expensive operation in the pipeline; passthrough costs close to zero relative to it.
- Check camera SDP or run ffprobe before building — a camera profile setting, not a server optimization, is often the fix.
- Passthrough capacity scales with connection and packet-forwarding overhead; transcode-by-default scales with stream count times encode complexity.
- AV1 is more efficient but more CPU-expensive to encode and less universally decodable today; keep it on the radar, don't restructure around it.

## Relevance

Informs realtime-video architecture and the choice between [RTP passthrough](/concepts/rtp-passthrough.md) and transcoding, tying codec-profile decisions to [capacity planning](/concepts/capacity-planning.md).

## Quality

Practitioner blog post by Devlin Liles. Strong architectural reasoning; the relative CPU cost is explicitly flagged as illustrative rather than a benchmark from a specific deployment.

## Entities Mentioned

- [RTSP](/entities/rtsp.md) — camera-side protocol
- [WebRTC](/entities/webrtc.md) — browser-side protocol
- [H.264](/entities/h-264.md) — safe passthrough codec
- [AV1](/entities/av1.md) — future option discussed

## Concepts Covered

- [RTP Passthrough](/concepts/rtp-passthrough.md) — main topic
- [Capacity Planning](/concepts/capacity-planning.md) — scaling implication
