---
title: "Following Someone Across Cameras"
type: "Source Summary"
description: "Appearance-based multi-camera re-identification preserves continuity without facial identity, but cross-camera hand-off failure remains unsolved."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/following-someone-across-cameras/following-someone-across-cameras.md"
---

# Following Someone Across Cameras — Summary

**Original source**: `references/devlinliles.com/following-someone-across-cameras/following-someone-across-cameras.md`

## Summary

Multi-camera re-identification can stitch a subject's movement across a facility without ever resolving their identity. Devlin Liles argues it should be done with appearance-based matching (clothing, gait, body shape) rather than facial recognition, which lowers the privacy and legal exposure for use cases that only need continuity. The genuinely hard problem is not detection but the hand-off between cameras, where occlusion forces a silent probabilistic guess.

## Key Claims

- Appearance-based re-identification answers "is this the same person" probabilistically, not "who is this" definitively; choosing the heavier facial capability when continuity suffices is a common overreach.
- Per-camera detection is solved; the cross-camera hand-off is not, and more compute does not close the information gap created by occlusion.
- Camera placement — deliberate overlap between adjacent views — helps more than most teams expect and is cheaper to fix than the algorithm.
- Treating every hand-off as resolved means acting on wrong identities with the same confidence as right ones; the fix is to flag breaks and route them to human review.

## Relevance

Informs [edge inference](/concepts/edge-inference.md) for privacy-sensitive video and the [human-in-the-loop](/concepts/human-in-the-loop.md) pattern of surfacing uncertainty instead of acting on it.

## Quality

Practitioner blog post by Devlin Liles. Strong on failure modes and architecture trade-offs; single-case and opinion-driven, with no measured data.

## Entities Mentioned

- None.

## Concepts Covered

- [edge inference](/concepts/edge-inference.md) — argues matching should run locally, centralizing only derived signals
- [human-in-the-loop](/concepts/human-in-the-loop.md) — recommends a review fallback on low-confidence hand-offs

## Related Sources

- [Crowd Counting and Environmental Hazard Detection](/sources/crowd-counting-and-environmental-hazard-detection.md)
- [Recognition at the Edge](/sources/recognition-at-the-edge.md)
