---
title: "Load Testing WebRTC at Scale: The Two Axes Most Test Plans Miss"
type: "Source Summary"
description: "WebRTC load tests should vary viewers-per-stream and streams-per-instance independently, because the two patterns stress bandwidth versus CPU."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md"
---

# Load Testing WebRTC at Scale: The Two Axes Most Test Plans Miss — Summary

**Original source**: `references/devlinliles.com/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md`

## Summary

The author argues most WebRTC load tests collapse two independent stress patterns into a single connection-count line. One thousand viewers on one stream stresses egress bandwidth and forwarding; one thousand viewers spread across two hundred streams stresses CPU and transcode density. A plan that only varies total connections can pass while missing the failure that actually occurs. He recommends a matrix varying each axis independently, choosing viewer simulation by question (browser swarms for realism, Pion or GStreamer synthetic clients for scale), and injecting network conditions. CI runs lightweight tools continuously; periodic real-scale exercises validate client experience.

## Key Claims

- 1,000 viewers on one stream and 1,000 viewers across 200 streams are the same connection count but different systems under test.
- Scenario one stresses egress (NIC, SFU forwarding, TURN); scenario two stresses CPU and transcode density.
- Headless-browser swarms surface client-side failures like jitter-buffer misconfiguration; synthetic clients scale higher but never render a frame.
- Network-condition injection (tc/netem) is needed, or a clean datacenter network hides jitter-buffer and packet-loss problems.
- Run lightweight tools like webrtcperf in CI and a browser-fidelity platform like Loadero periodically, logging the same core metrics both ways.

## Relevance

Informs [egress bandwidth](/concepts/egress-bandwidth.md), [jitter buffer](/concepts/jitter-buffer.md), and [capacity planning](/concepts/capacity-planning.md) for realtime video.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete test matrix and a clear split between CI and periodic testing. Caveats: the 1,000/200 figures are illustrative, and tool recommendations carry no measured results.

## Entities Mentioned

- [GStreamer](/entities/gstreamer.md) — its webrtcbin element is one option for lightweight synthetic clients

## Concepts Covered

- [Egress bandwidth](/concepts/egress-bandwidth.md) — the constraint in the one-stream-to-many-viewers scenario
- [Jitter buffer](/concepts/jitter-buffer.md) — surfaces only under realistic network conditions
- [Capacity Planning](/concepts/capacity-planning.md) — the flawed single-axis number this test replaces
