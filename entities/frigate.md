---
title: "Frigate"
type: "Entity"
description: "Open-source network video recorder used across the corpus for edge object detection, RTSP ingest, and activity understanding."
created: '2026-10-17'
updated: '2026-10-17'
tags: [product, video, edge, detection]
sources:
  - "/sources/beyond-detection-activity-understanding.md"
  - "/sources/processing-at-the-edge.md"
  - "/sources/the-gateway-layer-getting-rtsp-cameras-onto-webrtc.md"
---

# Frigate

Frigate is an open-source network video recorder that anchors this corpus's video-analytics arc. It is used both as the edge detection engine that decides which footage to stream and as a touchstone for the gap between object detection and true activity understanding.

## Overview

- Detect first, stream second: forward only footage that clears a threshold, trading central scaling cost for a fleet-management burden.
- A roughly $249 Jetson Orin Nano Super makes distributed detection cheap; Google Coral is discontinued, so avoid new deployments on it.
- Object detection answers what is in a frame; activity parsing asks what is happening — open-ended multi-actor parsing remains a research frontier, so build rules-based workflow checks today.
- Sequence verification and anomalous interaction flagging work today as state machines.
- Edge boxes create a fleet of models needing versioning, rollouts, and drift monitoring.

## Related

- [edge inference](/concepts/edge-inference.md) — detection before streaming
- [RTSP](/entities/rtsp.md) — the camera protocol feeding the gateway layer
- [WebRTC](/entities/webrtc.md) — the delivery path after the gateway
- [anomaly detection](/concepts/anomaly-detection.md) — anomalous interaction flagging
- [Processing at the Edge](/sources/processing-at-the-edge.md) — primary source
