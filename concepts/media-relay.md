---
title: "Media relay"
type: "Concept"
description: "The stateful data-plane tier that forwards real-time audio and video between participants, distinct from stateless signaling."
created: '2026-10-17'
updated: '2026-10-17'
tags: [webrtc, real-time, architecture]
sources:
  - "/sources/kurento-and-the-pipeline-approach.md"
  - "/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md"
---

# Media relay

A media relay is the component that carries real-time audio and video streams between participants in a conferencing or streaming system. It sits in the data plane, holding long-lived, stateful sessions, and is architecturally distinct from the short-lived, stateless signaling control plane.

## Key Claims

- Signaling is short-lived and stateless; media relay is long-lived and stateful, so the two scale on different terms.
- The control plane scales horizontally behind a standard load balancer; stateful media sessions cannot sit behind an interchangeable one.
- Entangling the planes forces a rebuild, not a config change, when load arrives.
- A lean SFU is the right choice for RTSP-in, WebRTC-out fan-out with no media processing.
- Pipeline frameworks such as Kurento earn their weight only when media needs mixing, recording, or computer vision in flight.

## Related

- [Selective Forwarding Unit](/concepts/selective-forwarding-unit.md) — the lean relay topology for simple fan-out
- [Control plane](/concepts/control-plane.md) — the stateless tier the relay is split from
- [RTP Passthrough](/concepts/rtp-passthrough.md) — forwarding media without processing it
- [In-pipeline processing](/concepts/in-pipeline-processing.md) — when a relay must do more than forward
- [state isolation](/concepts/state-isolation.md) — keeping long-lived sessions independent
- [Kurento](/entities/kurento.md) — a pipeline-based relay framework
- [Kurento and the Pipeline Approach](/sources/kurento-and-the-pipeline-approach.md) — primary source
- [Split the Control Plane From the Data Plane, or Neither Will Scale](/sources/split-the-control-plane-from-the-data-plane-or-neither-will-scale.md) — primary source
