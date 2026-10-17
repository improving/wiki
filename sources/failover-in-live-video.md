---
title: "Failover in Live Video"
type: "Source Summary"
description: "Lays out the tradeoff between duplicate-ingest failover and accepting a reconnect gap, and argues the choice is a product decision."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/failover-in-live-video/failover-in-live-video.md"
---

# Failover in Live Video — Summary

**Original source**: `references/devlinliles.com/failover-in-live-video/failover-in-live-video.md`

## Summary

Failover in live video is a genuine design tradeoff that most teams never consciously make. Liles lays out two options: duplicate ingest to a warm standby, giving a near-zero gap but paying for a second live ingest path per stream continuously; or accepting a few seconds of reconnect gap (an RTSP re-establish plus WebRTC renegotiation) that costs nothing in steady state. Which is right depends on what a gap costs the specific product, not on infrastructure alone.

## Key Claims

- Duplicate ingest holds a second live copy of every stream, so failover is seamless but the doubled ingest cost is paid per stream for the stream's entire life.
- The reconnect path stacks two re-establishments — gateway-to-source over RTSP, then viewer WebRTC renegotiation — which is where the few seconds of blackout come from.
- Neither option is universally correct; the deciding question is what a five-second drop costs at the worst possible moment for that use case.
- A platform can tier the choice: duplicate ingest for a small set of highest-priority streams, reconnect gap for the larger lower-priority population.
- The real failure mode is not choosing at all and inheriting the reconnect gap by default.

## Relevance

Frames [RTSP](/entities/rtsp.md) and [WebRTC](/entities/webrtc.md) session mechanics as inputs to a product-level failover decision in realtime video.

## Quality

Practitioner blog post by Devlin Liles. Clear tradeoff analysis; no measured cost or gap figures are given.

## Entities Mentioned

- [RTSP](/entities/rtsp.md) — the source-side reconnection step in the reconnect-gap option
- [WebRTC](/entities/webrtc.md) — the viewer-side session renegotiation step

## Concepts Covered

- None.

## Related Sources

- [Keyframes and Latency: The Cheapest Win Most Teams Never Touch](/sources/keyframes-and-latency-the-cheapest-win-most-teams-never-touch.md)
- [Kurento and the Pipeline Approach](/sources/kurento-and-the-pipeline-approach.md)
- [Thundering Herd: What Breaks When Everyone Looks at Once](/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md)
