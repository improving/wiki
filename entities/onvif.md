---
title: "ONVIF"
type: "Entity"
description: "IP-camera interoperability standard the corpus uses to shorten GOPs and tune latency from the camera itself."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, cameras, standard]
sources:
  - "/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
---

# ONVIF

ONVIF is the interoperability standard for IP cameras, and in this corpus it is the control surface for the cheapest latency win available: shortening the camera's keyframe interval. Because glass-to-glass latency is the only measurement that captures user experience, ONVIF's configuration interface matters as much as the transport beneath it.

## Overview

The keyframes post argues latency is dominated by keyframe interval and jitter buffering, not network transit. Cameras default to long GOPs for recording efficiency, which forces new viewers to wait seconds for a first keyframe. Shortening the GOP via ONVIF is the cheapest fix; the jitter buffer then needs tuning to match.

The gateway post supplies the pipeline context: a purpose-built RTSP-to-WebRTC gateway should sit in front of the SFU, with camera reconnection and retry logic kept close to the protocol. ONVIF sits at the far end of that chain, where the camera's own settings determine how much of the latency budget is already spent before the gateway sees a frame.

## Key Claims

- Glass-to-glass latency is the only measurement that captures user experience.
- Long camera GOPs force new viewers to wait seconds for the first keyframe.
- Cameras default to long GOPs for recording efficiency, hurting live viewing.
- Shortening GOP via ONVIF is the cheapest latency win; jitter buffers need tuning.
- Camera reconnection and retry logic belongs in the gateway, close to the protocol.

## Related

- [Keyframe interval](/concepts/keyframe-interval.md) — the setting ONVIF exposes
- [RTSP](/entities/rtsp.md) — the ingest protocol cameras speak
- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the measure ONVIF tuning targets
- [Jitter buffer](/concepts/jitter-buffer.md) — the companion setting
- [Keyframes and Latency](/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md) — primary source
