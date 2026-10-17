---
title: "Thundering Herd: What Breaks When Everyone Looks at Once"
type: "Source Summary"
description: "Alert-driven traffic arrives as a step function, so load tests must reproduce bursts and diagnose failures stage by stage."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/thundering-herd-what-breaks-when-everyone-looks-at-once/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# Thundering Herd: What Breaks When Everyone Looks at Once — Summary

**Original source**: `references/devlinliles.com/thundering-herd-what-breaks-when-everyone-looks-at-once/thundering-herd-what-breaks-when-everyone-looks-at-once.md`

## Summary

Devlin Liles argues that security and alert-driven video products fail under a thundering herd — everyone opening one stream in the same few seconds — a step function, not the gradual ramp most load tests reproduce. Because ICE negotiation, keyframe requests, and TURN allocation all land at once, the margin a steady ramp hides is consumed in seconds. He then gives a stage-by-stage incident diagnosis order (CPU, network, transcoding, latency, browser playback) and argues the herd tests the whole architecture simultaneously.

## Key Claims

- A gradual ramp gives autoscalers, connection pools, and session-setup paths room to breathe; a herd compresses everything into one narrow window with no natural spacing.
- Push-notification fan-out clusters tightly, so client requests arrive at the gateway already spike-shaped; load tests should generate that clustering deliberately.
- Diagnose in order: per-stream CPU (transcoding dominates; host averages hide the one saturated stream), split network into ingress/inter-instance/egress, confirm transcoding is needed at all, break down latency, then check client-side playback.
- Eliminating a transcode step beats speeding one up, because the eliminated step costs nothing at any scale.
- GOP length and jitter buffer settings often eat more of the latency budget than network transit.

## Relevance

Extends the [latency budget](/concepts/latency-budget.md) discussion and the realtime topology themes of the series, tying them to burst load and diagnosis.

## Quality

Practitioner blog post by Devlin Liles. Rich in concrete operational detail from experience; the guidance is heuristic and drawn from his own deployments rather than benchmarks.

## Entities Mentioned

- [WebRTC](/entities/webrtc.md) — gateway-to-viewer transport
- [ICE](/entities/ice.md) — path negotiation each new viewer triggers
- [TURN](/entities/turn.md) — relay layer tested by viewers without a direct path
- [RTSP](/entities/rtsp.md) — source-to-gateway ingest

## Concepts Covered

- [Latency Budget](/concepts/latency-budget.md) — broken down segment by segment during diagnosis
- [Jitter buffer](/concepts/jitter-buffer.md) — a frequent consumer of the latency budget
- [Keyframe interval](/concepts/keyframe-interval.md) — GOP cadence tested by mid-event joiners
- [Egress bandwidth](/concepts/egress-bandwidth.md) — a separate network cost center
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — fan-out topology tested at the herd moment

## Related Sources

- [Failover in Live Video](/sources/failover-in-live-video.md)
- [The TURN Tax: WebRTC's Hidden Cost Center](/sources/the-turn-tax-webrtcs-hidden-cost-center.md)
