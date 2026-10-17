---
title: "Sharding Streams at Scale"
type: "Source Summary"
description: "Shard live video by source stream, route viewers through a lookup table, and autoscale on per-instance metrics rather than fleet averages."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/sharding-streams-at-scale/sharding-streams-at-scale.md"
---

# Sharding Streams at Scale — Summary

**Original source**: `references/devlinliles.com/sharding-streams-at-scale/sharding-streams-at-scale.md`

## Summary

Argues that a one-to-many media fleet must shard by source stream, not by viewer: each stream lives on exactly one instance and every viewer routes to it, whether that stream has ten viewers or ten thousand. This forces a placement-and-routing layer that maps stream identifiers to the instance currently holding them. The post then warns that autoscaling built on fleet-wide averages hides the failure that actually threatens the system, because media servers fail one instance at a time.

## Key Claims

- Shard the stream population, not the viewer base; viewers follow wherever their stream lives.
- A fast lookup table (Redis or equivalent) maps stream ID to holding instance, and it is the mechanism failover runs on, not a routing convenience.
- New streams should be placed load-aware (e.g. least-loaded instance), not round-robin, to avoid manufacturing hotspots.
- A media server saturates on CPU when transcoding, or on [egress bandwidth](/concepts/egress-bandwidth.md) when fanning out; a fleet-wide average can look healthy while one hot instance drops frames.
- Ingress is per-source and small; egress scales with viewer count and concentrates unevenly on whichever instances hold the most popular streams.

## Relevance

Informs [egress bandwidth](/concepts/egress-bandwidth.md) and capacity planning for real-time video fan-out, and sets up the stream-routing mechanics assumed by the control-plane/data-plane split.

## Quality

Practitioner blog post by Devlin Liles. Concrete and operationally specific, but makes no measured claims; failure modes and the "ten percent CPU, minutes from failing" figure are illustrative rather than empirical.

## Entities Mentioned

- None.

## Concepts Covered

- [Egress bandwidth](/concepts/egress-bandwidth.md) — the resource that saturates first on pure fan-out instances and the reason to split network metrics by direction.
