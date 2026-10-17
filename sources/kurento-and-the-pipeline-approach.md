---
title: "Kurento and the Pipeline Approach"
type: "Source Summary"
description: "Kurento's pipeline framework earns its cost only when media must be touched in flight; pure fan-out belongs to a lean SFU."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/kurento-and-the-pipeline-approach/kurento-and-the-pipeline-approach.md"
---

# Kurento and the Pipeline Approach — Summary

**Original source**: `references/devlinliles.com/kurento-and-the-pipeline-approach/kurento-and-the-pipeline-approach.md`

## Summary

Teams building one-to-many live video tend to reach for the most capable media server they can find, which is backwards. The right question is narrower: does anything need to touch the media in flight, or does it just need to move from one source to many viewers intact? Kurento, a full GStreamer-based pipeline framework wrapped in a WebRTC-facing API, answers the first question well and carries a real resource cost for the second. Liles argues a lean SFU is the right tool for pure fan-out, while Kurento plus OpenVidu earns its weight only when media gets composited, filtered, inspected, or recorded inline.

## Key Claims

- A Selective Forwarding Unit never decodes frames, so it has nothing to offer requirements like "detect a QR code in this live feed."
- Kurento handles processing inline, keeping ingest, analysis, and delivery in one system rather than two paths that must stay synchronized.
- Kurento's reputation for being abandoned is out of date: as of mid-2026 it still ships point releases on its 7.x line.
- Kurento is heavier per stream than a lean SFU; that weight is the necessary cost of decoding and re-encoding in the media path.
- Size capacity by testing the specific processing step — object detection can dominate the resource profile, making WebRTC delivery nearly a rounding error.

## Relevance

Core to [in-pipeline processing](/concepts/in-pipeline-processing.md), [media relay](/concepts/media-relay.md), and [selective forwarding unit](/concepts/selective-forwarding-unit.md) tradeoffs in real-time video architecture.

## Quality

Practitioner blog post by Devlin Liles. Balanced and specific about tradeoffs and capacity planning; the maintenance-status claim and cost framing are the author's assessment rather than benchmarked data.

## Entities Mentioned

- [Kurento](/entities/kurento.md) — the GStreamer-based pipeline framework under discussion
- [GStreamer](/entities/gstreamer.md) — the general-purpose multimedia framework Kurento builds on
- [OpenVidu](/entities/openvidu.md) — the higher-level room framework over Kurento
- [WebRTC](/entities/webrtc.md) — the delivery layer Kurento faces
- [RTSP](/entities/rtsp.md) — camera ingest into the pipeline

## Concepts Covered

- [In-pipeline processing](/concepts/in-pipeline-processing.md) — the capability that justifies a pipeline framework
- [Media relay](/concepts/media-relay.md) — pure pass-through contrasted with processing
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the lean tool for untouched fan-out
- [RTP passthrough](/concepts/rtp-passthrough.md) — relay behavior that never inspects frames

## Related Sources

- [Failover in Live Video](/sources/failover-in-live-video.md)
