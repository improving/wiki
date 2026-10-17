---
title: "Processing at the Edge"
type: "Source Summary"
description: "Run detection at the edge before streaming, not centrally on every frame; the cost is fleet management, not bandwidth."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/processing-at-the-edge/processing-at-the-edge.md"
---

# Processing at the Edge — Summary

**Original source**: `references/devlinliles.com/processing-at-the-edge/processing-at-the-edge.md`

## Summary

The default architecture — stream every camera to a central server and run detection on every frame — pays full bandwidth and compute for the roughly 95% of footage where nothing happens. The better order is detect first, stream second: run detection on the camera's own SoC or a local per-cluster box, and only forward, alert on, or record moments that clear a threshold. Frigate plus NVIDIA Jetson hardware (TensorRT, YOLO-class models) makes this practical, though it trades a scaling problem for a fleet-management problem.

## Key Claims

- Edge detection cuts central bandwidth and CPU dramatically, making central cost scale with event volume instead of camera count.
- Frigate is the near-default open-source local NVR/detection layer; the Jetson Orin Nano Super (~$249) runs YOLO-class models at 20-40ms per-frame latency.
- Google's Coral Edge TPU is effectively discontinued and community-maintained; use a GPU-class board like the Orin Nano Super for anything new.
- One box can serve several nearby cameras; clustering is a cost-control decision.
- The real cost is operational: versioned model artifacts, staged rollouts, and drift monitoring across a fleet of edge boxes.
- Better edge filtering also reduces false triggers, changing the shape of downstream load spikes.

## Relevance

Informs [edge inference](/concepts/edge-inference.md), [Model Drift Detection](/concepts/model-drift-detection.md), and realtime video pipeline architecture.

## Quality

Practitioner blog post by Devlin Liles. Concrete hardware and pricing guidance from direct field experience; figures like the 95% idle share are illustrative rather than measured.

## Entities Mentioned

- [Frigate](/entities/frigate.md) — the recommended local NVR and detection layer
- [Kurento](/entities/kurento.md) — the heavyweight pipeline framework this series pushes back on

## Concepts Covered

- [edge inference](/concepts/edge-inference.md) — running detection before the stream leaves the camera cluster
- [Model Drift Detection](/concepts/model-drift-detection.md) — monitoring edge models across a fleet

## Related Sources

- [Beyond Detection: Activity Understanding](/sources/beyond-detection-activity-understanding.md)
