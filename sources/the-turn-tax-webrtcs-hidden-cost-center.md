---
title: "The TURN Tax: WebRTC's Hidden Cost Center"
type: "Source Summary"
description: "TURN relay bandwidth, not SFU egress, is where WebRTC cost models break; price it at double and budget it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/the-turn-tax-webrtcs-hidden-cost-center/the-turn-tax-webrtcs-hidden-cost-center.md"
---

# The TURN Tax: WebRTC's Hidden Cost Center — Summary

**Original source**: `references/devlinliles.com/the-turn-tax-webrtcs-hidden-cost-center/the-turn-tax-webrtcs-hidden-cost-center.md`

## Summary

Argues that WebRTC cost models usually start with SFU capacity and egress bandwidth and miss the line item that actually blows budgets: TURN relay bandwidth. When ICE can't find a direct or STUN-assisted path — common behind symmetric NAT and restrictive corporate firewalls — media relays through a TURN server, costing bandwidth twice and adding latency. The fix is to budget relay bandwidth as its own explicit line item before committing to a number.

## Key Claims

- A relayed connection consumes twice the bandwidth of a direct or STUN-assisted one: once arriving at the TURN server from the sender, again forwarding to the receiver.
- ICE deliberately prefers the cheapest working path and only pays for TURN when there's no other option — but "no other option" happens on a meaningful fraction of real-world connections.
- TURN also adds latency, because the relay is a physical detour through wherever the server sits — directly relevant to glass-to-glass latency.
- Cost models that account only for SFU egress model the cheap path and ignore the expensive one, so real bills come in above projection.
- Budget relay bandwidth explicitly: estimate the relay fraction from the actual viewer network mix (corporate networks and certain mobile carriers push it up) and price it at double; coturn is the common open-source TURN/STUN server.

## Relevance

Ties a network-topology cost decision to [glass-to-glass latency](/concepts/glass-to-glass-latency.md) and [egress bandwidth](/concepts/egress-bandwidth.md), showing how [media relay](/concepts/media-relay.md) scales against the viewer mix a [selective forwarding unit](/concepts/selective-forwarding-unit.md) alone doesn't cover.

## Quality

Practitioner blog post by Devlin Liles. Strengths: explains the mechanism (ICE candidate ordering, double bandwidth, physical detour) and gives an actionable budgeting rule. Caveat: figures are directional — it names no concrete relay rates or costs.

## Entities Mentioned

- [WebRTC](/entities/webrtc.md) — the platform whose costs the post models
- [TURN](/entities/turn.md) — the relay fallback that drives the hidden cost
- [ICE](/entities/ice.md) — the negotiation process that decides when TURN is used

## Concepts Covered

- [glass-to-glass latency](/concepts/glass-to-glass-latency.md) — the latency cost of a TURN detour
- [egress bandwidth](/concepts/egress-bandwidth.md) — the cost line teams model while missing relay bandwidth
- [media relay](/concepts/media-relay.md) — relaying every packet through a TURN server
- [selective forwarding unit](/concepts/selective-forwarding-unit.md) — the SFU whose egress is the wrong thing to budget around

## Related Sources

- [Thundering Herd: What Breaks When Everyone Looks at Once](/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md)
