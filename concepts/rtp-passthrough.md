---
title: "RTP Passthrough"
type: "Concept"
description: "Repackaging RTP from RTSP to WebRTC without transcoding, removing the CPU-expensive decode/encode step when codecs are compatible."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, webrtc, streaming]
sources:
  - "/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
---

# RTP Passthrough

RTP passthrough is the practice of moving media from an RTSP camera to a WebRTC viewer by repackaging RTP packets rather than transcoding the video. Because both protocols already carry media over RTP, a gateway can often strip and rebuild the signaling and transport wrappers while leaving the encoded payload untouched. In this corpus passthrough is described as the biggest single lever in an RTSP-to-WebRTC pipeline: eliminating transcoding beats speeding it up for CPU scaling.

## Key Claims

- RTSP and WebRTC both carry media over RTP, so repackaging can suffice where the codec matches.
- Passthrough depends on codec profile compatibility with browser decoders.
- H.264 baseline and main profiles maximize WebRTC decode compatibility.
- Eliminating transcoding is a larger win than optimizing it.
- Camera reconnection and retry logic belongs in the gateway, close to the protocol.
- go2rtc is WebRTC-first and restreams on demand, so unused camera streams cost nothing; MediaMTX speaks RTSP, RTMP, HLS, WebRTC, and SRT for non-WebRTC clients.

## Related

- [RTSP](/entities/rtsp.md) — the ingest protocol whose payload is reused
- [WebRTC](/entities/webrtc.md) — the delivery protocol the payload is repackaged for
- [H.264](/entities/h-264.md) — the codec profile whose compatibility decides passthrough feasibility
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the downstream element a gateway shields from ingest concerns
- [media relay](/concepts/media-relay.md) — the broader class of forwarding that passthrough avoids transcoding within
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the metric passthrough improves by skipping transcode delay
- [Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline](/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md) — primary source
