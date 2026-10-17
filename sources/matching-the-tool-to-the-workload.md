---
title: "Matching the Tool to the Workload"
type: "Source Summary"
description: "There is no single best media server; each of five tools fits a specific workload shape, so ask what the system must do first."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/matching-the-tool-to-the-workload/matching-the-tool-to-the-workload.md"
---

# Matching the Tool to the Workload — Summary

**Original source**: `references/devlinliles.com/matching-the-tool-to-the-workload/matching-the-tool-to-the-workload.md`

## Summary

Wrapping up a run through five media servers, the author argues each tool is the right answer to a specific question and a weak answer everywhere else. All of LiveKit, mediasoup, and Janus share the SFU architecture — relaying without decoding — so they differ in packaging, not in the relay. Ant Media earns its place when sub-second latency is the product itself; Janus is for bridging WebRTC with SIP or legacy telephony. He offers an ordered decision framework: does anything need to touch media in flight, is the job fan-out at scale, is sub-second latency defining, does the platform need telephony. Adoption numbers and star counts are deliberately absent.

## Key Claims

- SFUs forward streams without decoding, which is why they cannot do the in-pipeline processing or mixed recording Kurento can.
- Ant Media's latency advantage comes from buffering and jitter-tolerance tradeoffs made throughout the stack.
- Janus is the right call only when a platform must bridge with SIP or legacy telephony.
- Picking a tool for its GitHub stars leads to fighting the tool on top of fighting the problem.
- The expensive mistake is picking an excellent tool for a problem you don't have, discovered six months into a build.

## Relevance

Informs [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) selection and [latency budget](/concepts/latency-budget.md) decisions in realtime video.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a clear workload-first decision framework synthesized across a five-tool series. Caveats: opinion-driven with no benchmarks; latency and feature claims are qualitative.

## Entities Mentioned

- [Janus](/entities/janus.md) — the SIP/telephony bridging option
- [Kurento](/entities/kurento.md) — the in-pipeline processing option
- [OpenVidu](/entities/openvidu.md) — grouped with Kurento for media-touching work
- [LiveKit](/entities/livekit.md) — the default for large-scale fan-out

## Concepts Covered

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the shared architecture beneath three of the five tools
- [Latency Budget](/concepts/latency-budget.md) — the requirement that justifies a specialist ultra-low-latency tool
