---
title: "Split the Control Plane From the Data Plane, or Neither Will Scale"
type: "Source Summary"
description: "Separate WebRTC signaling from media relay early, because stateless control and stateful media have opposite scaling stories."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, realtime-video, devlinliles.com]
sources:
  - "references/devlinliles.com/split-the-control-plane-from-the-data-plane-or-neither-will-scale/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md"
---

# Split the Control Plane From the Data Plane, or Neither Will Scale — Summary

**Original source**: `references/devlinliles.com/split-the-control-plane-from-the-data-plane-or-neither-will-scale/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md`

## Summary

Argues that a live video system built on [WebRTC](/entities/webrtc.md) is doing two jobs with opposite scaling personalities — [control plane](/concepts/control-plane.md) signaling/room state, and the stateful [media relay](/concepts/media-relay.md) data plane — and that entangling them is a foundational mistake. A signaling exchange is a short, stateless conversation (offer, answer, ICE candidates, done); a media session is a long-lived, stateful relationship held on one specific server process. If the two live in one service, the whole system inherits the constraints of the harder problem, and teams end up scaling the easy half like the hard half.

## Key Claims

- Signaling is stateless and scales like any web API behind a generic load balancer; room state and auth can live in a shared store.
- The media relay is stateful and cannot be treated as interchangeable servers — a request landing on the wrong instance has no access to the session at all.
- Separating the planes also separates blast radiuses: a memory leak in room-state logic should not drop active video sessions, and a media CPU spike should not take down auth.
- Entangled systems inherit the media layer's constraints even for stateless parts, leading to over-provisioning signaling or under-provisioning media.
- The failure is common: wire signaling into the media server because it is convenient early, ship, then try to scale the combined unit behind a load balancer — which cannot see the stateful sessions. The fix is a rebuild, not a config change.

## Relevance

Informs [control plane](/concepts/control-plane.md) / [media relay](/concepts/media-relay.md) separation and the stream-sharding and autoscaling mechanics of the rest of the series.

## Quality

Practitioner blog post by Devlin Liles. Clear architectural reasoning and an illustrative failure anecdote, but no measurements; it is an opinionated design argument rather than a benchmarked result.

## Entities Mentioned

- [WebRTC](/entities/webrtc.md) — the stack whose signaling/media split motivates the whole argument.

## Concepts Covered

- [Control plane](/concepts/control-plane.md) — stateless signaling, auth, and room state that scales elastically.
- [Media relay](/concepts/media-relay.md) — the stateful data plane requiring deliberate, session-aware scaling.
- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the media server type mentioned as handling the relay.
- [state isolation](/concepts/state-isolation.md) — separating planes so failures in one do not take down the other.
