---
title: "TURN"
type: "Entity"
description: "Traversal Using Relays around NAT: the WebRTC relay server that forwards media when direct peer connections fail, at double bandwidth cost."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, networking, media-delivery]
sources:
  - "/sources/the-turn-tax-webrtcs-hidden-cost-center.md"
  - "/sources/thundering-herd-what-breaks-when-everyone-looks-at-once.md"
---

# TURN

Traversal Using Relays around NAT — the WebRTC relay protocol and server used when two peers cannot connect directly. TURN forwards media through a relay, which makes it the hidden cost center of WebRTC deployments: relayed traffic is received and forwarded, so it consumes bandwidth twice, and most cost models ignore the path entirely.

## Overview

Relay happens by default on symmetric NAT and restrictive firewalls, so a meaningful share of viewers silently take the expensive path. [SFU](/concepts/selective-forwarding-unit.md) egress models typically assume direct media and never price the relay leg. The second source broadens the operational picture: when demand arrives as a [thundering herd](/concepts/alert-fatigue.md) — a step function rather than a gradual climb — gradual load tests verify only one shape of demand, and diagnosis must proceed stage by stage through CPU, network, transcoding, latency, and browser playback.

## Key Claims

- TURN-relayed traffic costs bandwidth twice, receiving and forwarding
- Relay happens by default on symmetric NAT and restrictive firewalls
- SFU egress models ignore the expensive relay path entirely
- Budget relay bandwidth explicitly and price it at double
- A thundering herd is a step function, not a gradual climb

## Related

- [Media Relay](/concepts/media-relay.md) — the general mechanism TURN implements
- [Egress Bandwidth](/concepts/egress-bandwidth.md) — the cost TURN doubles
- [WebRTC](/entities/webrtc.md) — the stack TURN serves
- [The TURN Tax: WebRTC's Hidden Cost Center](/sources/the-turn-tax-webrtcs-hidden-cost-center.md) — primary source
