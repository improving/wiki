---
title: "OpenVidu"
type: "Entity"
description: "Higher-level room framework built on Kurento that teams actually build against for WebRTC media applications."
created: '2026-10-17'
updated: '2026-10-17'
tags: [video, webrtc, framework]
sources:
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/matching-the-tool-to-the-workload.md"
---

# OpenVidu

OpenVidu is a higher-level room framework built on Kurento, and in this corpus it is the layer teams actually build against when they need in-flight media processing without managing GStreamer pipelines directly. It sits between Kurento's raw pipeline model and the application.

## Overview

The Kurento post explains the underlying split: Kurento is a GStreamer-based pipeline framework with a WebRTC-facing API, and pipelines earn their weight only when media needs mixing, recording, or computer vision in flight. A lean SFU is better for RTSP-in, WebRTC-out fan-out with no processing. OpenVidu wraps that pipeline machinery in room-level abstractions.

The workload-matching post generalizes the principle: media server selection should follow workload requirements, not popularity. Ant Media Server earns its place when sub-second latency is the product; Janus is chosen when video must bridge with SIP telephony; LiveKit and mediasoup share an SFU architecture differing in packaging. OpenVidu is the pipeline-based option when the workload genuinely needs processing.

## Key Claims

- Kurento is a GStreamer-based pipeline framework with a WebRTC-facing API.
- Pipelines earn their weight when media needs mixing, recording, or CV in flight.
- A lean SFU is better for RTSP-in, WebRTC-out fan-out with no media processing.
- OpenVidu is the higher-level room framework teams actually build against.
- Picking a tool by star count means fighting the tool and the problem.

## Related

- [Kurento](/entities/kurento.md) — the pipeline engine beneath OpenVidu
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — the workload it serves
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the leaner alternative
- [Media relay](/concepts/media-relay.md) — the fan-out pattern it can replace
- [Matching the Tool to the Workload](/sources/matching-the-tool-to-the-workload.md) — primary source
