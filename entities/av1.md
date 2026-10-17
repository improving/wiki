---
title: "AV1"
type: "Entity"
description: "Open video codec whose hardware encode support limits browser endpoint optimization in WebRTC pipelines."
created: '2026-10-17'
updated: '2026-10-17'
tags: [codec, video, webrtc]
sources:
  - "/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
  - "/sources/the-last-few-feet-endpoint-optimization.md"
---

# AV1

AV1 is an open video codec that appears in this corpus at the endpoint, where browser decode and encode support determine what a live-video pipeline can actually deliver. It sits alongside [H.264](/entities/h-264.md) as one of the codec choices that decide whether a pipeline can avoid transcoding entirely.

## Overview

- One post argues that because RTSP and [WebRTC](/entities/webrtc.md) both carry media over RTP, repackaging via [RTP passthrough](/concepts/rtp-passthrough.md) can remove the CPU-expensive transcode step.
- That passthrough depends on codec profile compatibility with browser decoders, which is why H.264 baseline and main profiles maximize WebRTC decode compatibility.
- The companion post finds WebCodecs hardware decode near-universal, but AV1 **encode** covers only about 88% of sessions.

## Key Claims

- Eliminating transcoding beats speeding it up for CPU scaling.
- AV1 encode support lags decode support across real sessions.
- Firefox for Android lacks WebCodecs support entirely, making the API desktop-only there.
- Capability detection (isConfigSupported) should run at connection time, driving [simulcast](/concepts/simulcast.md) and [SVC](/concepts/scalable-video-coding.md) layer selection.

## Related

- [RTP Passthrough](/concepts/rtp-passthrough.md) — the lever that avoids transcoding
- [Simulcast](/concepts/simulcast.md) — layer selection driven by codec capability
- [Scalable Video Coding](/concepts/scalable-video-coding.md) — the SVC alternative
- [WebRTC](/entities/webrtc.md) — the delivery target
- [H.264](/entities/h-264.md) — the compatibility baseline it is compared against
- [Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline](/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md) — primary source
- [The Last Few Feet: Endpoint Optimization](/sources/the-last-few-feet-endpoint-optimization.md) — companion source
