---
title: "GStreamer"
type: "Entity"
description: "A multimedia pipeline framework that underpins Kurento and other media-processing stacks in this corpus."
created: '2026-10-17'
updated: '2026-10-17'
tags: [media, pipeline, webrtc]
sources:
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md"
  - "/sources/migrating-off-a-legacy-media-server.md"
  - "/sources/structuring-the-middle-of-the-pipeline.md"
---

# GStreamer

GStreamer is a multimedia pipeline framework that appears in this corpus as the processing engine beneath [Kurento](/entities/kurento.md) and similar media stacks. It represents the ability to transform media in flight — mixing, recording, transcoding, analysis — as opposed to merely relaying packets.

## Overview

The corpus treats GStreamer-based [in-pipeline processing](/concepts/in-pipeline-processing.md) as a deliberate cost: it earns its weight only when media must be changed, not just forwarded. When a platform is migrated, processing that is still needed is best moved to a separate service beside the [selective forwarding unit](/concepts/selective-forwarding-unit.md) and fed by a queue, keeping it off the live viewer path.

## Key Claims

- GStreamer pipelines justify themselves when media is mixed, recorded, or analyzed in flight.
- A lean SFU is the better fit for RTSP-in, WebRTC-out fan-out with no media processing.
- Processing routed through the live fan-out path adds viewer-facing latency.
- SFU and processing tiers scale on different signals — egress bandwidth versus CPU and transcode density — so they need separate autoscaling groups.
- Monitoring the two tiers separately speeds incident response.

## Related

- [Kurento](/entities/kurento.md) — the framework built on GStreamer
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — the workload GStreamer enables
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the lean alternative to a pipeline
- [Egress bandwidth](/concepts/egress-bandwidth.md) — the bottleneck that scales differently from CPU
- [Structuring the Middle of the Pipeline](/sources/structuring-the-middle-of-the-pipeline.md) — primary source
