---
title: "Egress bandwidth"
type: "Concept"
description: "The outbound throughput a media instance spends fanning streams to viewers; the bottleneck that scales with viewers per stream."
created: '2026-10-17'
updated: '2026-10-17'
tags: [streaming, capacity, webrtc]
sources:
  - "/sources/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md"
  - "/sources/sharding-streams-at-scale.md"
---

# Egress bandwidth

Egress bandwidth is the outbound network throughput an instance spends delivering media to viewers. In WebRTC and streaming systems it is a distinct bottleneck from CPU: fanning one stream out to many viewers consumes egress while transcoding consumes compute, and the two must be measured and scaled separately.

## Key Claims

- Viewers-per-stream stresses egress bandwidth, not CPU; streams-per-instance stresses CPU and transcode density.
- Ingress and egress bandwidth must be measured separately per instance.
- Fleet-wide averages hide the single hot instance that actually fails.
- Each stream should live on exactly one instance, with viewers routed to wherever it lives.
- A stream-to-instance lookup table is required for routing and failover.
- Autoscale on per-instance CPU and egress metrics rather than aggregate fleet health.

## Related

- [Capacity Planning](/concepts/capacity-planning.md) — sizing fleets against egress and CPU limits
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the relay component whose egress fan-out this measures
- [Media relay](/concepts/media-relay.md) — the instance egress bandwidth is accounted against
- [cost-adjusted capacity](/concepts/cost-adjusted-capacity.md) — valuing bandwidth against delivered streams
- [Load Testing WebRTC at Scale: The Two Axes Most Test Plans Miss](/sources/load-testing-webrtc-at-scale-the-two-axes-most-test-plans-miss.md) — primary source
- [Sharding Streams at Scale](/sources/sharding-streams-at-scale.md) — primary source
