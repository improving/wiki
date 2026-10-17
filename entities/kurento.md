---
title: "Kurento"
type: "Entity"
description: "A GStreamer-based media pipeline framework with a WebRTC-facing API, used when media must be processed in flight."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, media-server, pipeline]
sources:
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/matching-the-tool-to-the-workload.md"
  - "/sources/migrating-off-a-legacy-media-server.md"
  - "/sources/processing-at-the-edge.md"
  - "/sources/structuring-the-middle-of-the-pipeline.md"
---

# Kurento

Kurento is a [GStreamer](/entities/gstreamer.md)-based pipeline framework that exposes a WebRTC-facing API. In this corpus it stands for the heavyweight end of the media-server spectrum: the right choice when media must be transformed, not merely relayed, and the wrong choice when a lean forwarder would do.

## Overview

Pipelines earn their weight when media needs mixing, recording, or computer vision in flight. For plain RTSP-in, WebRTC-out fan-out with no processing, a lean [selective forwarding unit](/concepts/selective-forwarding-unit.md) is the better fit. Teams typically build against [OpenVidu](/entities/openvidu.md), the higher-level room framework layered over Kurento.

## Key Claims

- Kurento is a GStreamer-based pipeline framework with a WebRTC-facing API.
- Pipelines justify themselves only when media is mixed, recorded, or analyzed in flight.
- A lean SFU beats a pipeline framework for pure relay fan-out.
- Any in-pipeline processing still needed after a migration should move to a separate service beside the SFU, reached via a queue rather than the live viewer path.
- Before proposing a swap away from a heavyweight framework, re-verify why it was chosen in the first place.

## Related

- [GStreamer](/entities/gstreamer.md) — the framework Kurento is built on
- [OpenVidu](/entities/openvidu.md) — the room framework teams build against
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — the workload that justifies Kurento
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the lean alternative
- [Kurento and the Pipeline Approach](/sources/kurento-and-the-pipeline-approach.md) — primary source
