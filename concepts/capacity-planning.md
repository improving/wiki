---
title: "Capacity Planning"
type: "Concept"
description: "Deciding where compute and human capacity go, from RTP passthrough to AI-freed time redeployed against demand."
created: '2026-10-17'
updated: '2026-10-17'
tags: [operations, scaling, ai-adoption]
sources:
  - "/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md"
  - "/sources/the-2x2-ai-impact-matrix-what-to-do-based-on-where-you-are.md"
---

# Capacity Planning

Capacity planning is deciding how much capacity a system or team needs and where that capacity should be spent. Across this corpus it operates at two levels: the CPU budget of a real-time video pipeline, and the human time that AI frees inside an organization.

## Key Claims

- RTSP and WebRTC both carry media over RTP, so repackaging can replace the CPU-expensive transcode step entirely.
- Passthrough depends on codec profile compatibility with browser decoders; H.264 baseline and main profiles maximize compatibility.
- Eliminating transcoding beats speeding it up for CPU scaling.
- Time impact and demand limit, not AI capability, decide what to do with freed capacity.
- High impact plus high demand means redeploy freed capacity into demand generation; high impact plus low demand forces honest headcount or role-growth decisions.
- Quadrant assignments expire as AI capability rises and cost falls.

## Related

- [RTP Passthrough](/concepts/rtp-passthrough.md) — removes the transcode step that dominates CPU capacity
- [demand limit](/concepts/demand-limit.md) — decides whether freed capacity can be redeployed
- [Competency Floor](/concepts/competency-floor.md) — the judgment teams must retain as capacity shifts
- [Stop Transcoding: The Biggest Lever in an RTSP-to-WebRTC Pipeline](/sources/stop-transcoding-the-biggest-lever-in-an-rtsp-to-webrtc-pipeline.md) — primary source
- [The 2x2 AI Impact Matrix: What to Do Based on Where You Are](/sources/the-2x2-ai-impact-matrix-what-to-do-based-on-where-you-are.md) — primary source
