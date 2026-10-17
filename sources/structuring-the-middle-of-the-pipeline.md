---
title: "Structuring the Middle of the Pipeline"
type: "Source Summary"
description: "Branch the stream, not the pipeline: route central processing off the live path via queues and scale it separately."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/structuring-the-middle-of-the-pipeline/structuring-the-middle-of-the-pipeline.md"
---

# Structuring the Middle of the Pipeline — Summary

**Original source**: `references/devlinliles.com/structuring-the-middle-of-the-pipeline/structuring-the-middle-of-the-pipeline.md`

## Summary

Central processing (recording, cross-camera correlation, detection) still exists after edge filtering, and routing it through the live fan-out path destroys the low-latency architecture. The fix is to branch the stream: the SFU fans a copy to viewers on the fast path and hands another copy to an asynchronous queue-and-worker processing tier that can slow, back up, or fail without affecting viewers.

## Key Claims

- Routing processing through the live fan-out process puts every slow model or recording write directly on the viewer's critical path.
- Publish a copy of the stream (or just frames and metadata) to a queue such as Kafka or a Redis stream; workers consume at their own pace and the queue absorbs backpressure.
- A GStreamer-based framework like Kurento is legitimate inside the processing branch, just not inline between camera and viewer.
- Scale the SFU and processing tiers separately: the SFU scales on egress bandwidth and connection count; processing scales on queue depth and worker utilization.
- Monitor them separately too — an SFU dashboard tracks bandwidth and loss; a processing dashboard tracks queue depth and inference latency.
- The recurring design question: does this need to touch a live viewer's path? Usually no.

## Relevance

A distributed-systems discipline for realtime video: separating the fast [selective forwarding unit](/concepts/selective-forwarding-unit.md) path from slow [in-pipeline processing](/concepts/in-pipeline-processing.md) protects the [latency budget](/concepts/latency-budget.md).

## Quality

Practitioner blog post by Devlin Liles. Clear architectural reasoning drawn from operating these pipelines; opinionated and benchmark-free, and it explicitly builds on an earlier post in the series.

## Entities Mentioned

- [Redis](/entities/redis.md) — example queue/stream
- [GStreamer](/entities/gstreamer.md) — pipeline framework for the processing branch
- [Kurento](/entities/kurento.md) — heavyweight framework discussed

## Concepts Covered

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the fast path
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — work to move off the live path
- [Latency Budget](/concepts/latency-budget.md) — what inline processing destroys
- [Egress bandwidth](/concepts/egress-bandwidth.md) — SFU scaling signal
