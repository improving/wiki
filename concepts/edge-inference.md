---
title: "Edge Inference"
type: "Concept"
description: "Running model inference on the device itself, rather than round-tripping to the cloud, for latency, reliability, and privacy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [edge-ai, latency, computer-vision]
sources:
  - "/sources/crowd-counting-and-environmental-hazard-detection.md"
  - "/sources/following-someone-across-cameras.md"
  - "/sources/recognition-at-the-edge.md"
  - "/sources/safety-and-compliance-at-the-edge.md"
---

# Edge Inference

Edge inference runs model inference on the device — a camera SoC, NVR, or gateway — rather than round-tripping to the cloud. Across this corpus it is prescribed for identity-level recognition, safety detection, and continuous monitoring, because latency, WAN reliability, and privacy all favor answering locally.

## Key Claims

- Edge recognition answers in 30–100ms versus 800–2000ms in the cloud, and keeps access decisions working during WAN outages.
- Fire and smoke detection carries a hard sub-100ms latency constraint; periodic cloud checks defeat the reason such systems exist.
- Pushing inference onto camera SoCs with integrated NPUs lets systems ship counts, not video, reducing egress and shrinking the privacy surface.
- License plate recognition is moving into camera firmware, removing separate appliances; edge matching keeps raw facial imagery on-premises.
- Privacy-preserving detection flags a compliance state (for example, missing PPE) rather than an identity.
- Multi-camera re-identification's hardest problem is the hand-off; more compute improves in-frame detection but cannot close the information gap at occlusion, so systems should flag low-confidence matches for human review.
- Calibration against real foot traffic determines whether a threshold succeeds in the field.

## Related

- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the end-to-end delay edge inference targets
- [Latency Budget](/concepts/latency-budget.md) — the constraint sub-100ms detection consumes
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — where inference sits in the video path
- [Egress bandwidth](/concepts/egress-bandwidth.md) — the cost that shipping counts instead of video avoids
- [Recognition at the Edge](/sources/recognition-at-the-edge.md) — primary source
