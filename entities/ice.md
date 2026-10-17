---
title: "ICE"
type: "Entity"
description: "The WebRTC NAT-traversal mechanism whose relay fallback quietly doubles bandwidth and adds latency."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, networking, nat-traversal, infrastructure]
sources:
  - "/sources/the-turn-tax-webrtcs-hidden-cost-center.md"
  - "/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# ICE

ICE (Interactive Connectivity Establishment) is the WebRTC mechanism that discovers how two peers can reach each other, trying direct paths first and falling back to a TURN relay. In this corpus it is the source of a hidden cost center: relay traffic is invisible in most cost models yet expensive in bandwidth and latency.

## Overview

- TURN-relayed traffic costs bandwidth twice — receiving and forwarding.
- Relay happens by default on symmetric NAT and restrictive firewalls, so it is common in real audiences.
- SFU egress models often ignore the expensive relay path entirely.
- The recommendation is to budget relay bandwidth explicitly and price it at double.
- Related operational risk: alert-driven video spikes arrive as a thundering herd, a step function that gradual load tests never surface; diagnose stage by stage (CPU, network, transcoding, latency, browser playback).

## Related

- [TURN](/entities/turn.md) — the relay ICE falls back to
- [Media relay](/concepts/media-relay.md) — the mechanism that doubles bandwidth
- [Egress bandwidth](/concepts/egress-bandwidth.md) — where the relay cost lands
- [Janus](/entities/janus.md) — a media server that relies on ICE for connectivity
- [The TURN Tax](/sources/the-turn-tax-webrtcs-hidden-cost-center.md) — primary source
