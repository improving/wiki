---
type: Reference
title: "Choosing a Video Topology That Scales"
resource: "https://www.devlinliles.com/choosing-a-video-topology-that-scales/"
author: "Devlin Liles"
published: '2026-08-27'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

If you're building anything that streams live video from a small number of sources to a large number of viewers, the first architectural decision you make determines whether the rest of the system is easy or miserable. That decision is the video topology: how streams get from cameras or encoders to viewers' screens. Get it wrong and no amount of clever engineering downstream saves you. Get it right and most of what follows is tuning, not firefighting.

I've spent enough time inside WebRTC media server architecture to have a strong opinion here, and I want to open this series with it before anything else, because everything else in the series assumes you've made this call correctly.

## What glass-to-glass latency actually means

Before I get into topology, one term is going to show up in every post in this series, so I want to nail it down now. Glass-to-glass latency is the total delay from the moment a camera's lens (the glass) captures a frame to the moment that frame appears on a viewer's screen (more glass). It covers capture, encoding, network transit, any server-side processing, decoding, and rendering. It's the number that actually matters to a viewer watching a live camera feed, and it's the number this entire series is organized around. Every choice I cover in this series, from topology to gateway design to autoscaling, either adds to that number or protects it.

## Three ways to move video between people

WebRTC gives you three broad topologies for connecting participants: mesh, MCU, and SFU. They solve the same basic problem (get media from senders to receivers) with completely different tradeoffs on bandwidth, CPU, and how far they scale.

**Mesh** is the simplest conceptually and the worst in practice for anything beyond a handful of participants. Every participant connects directly to every other participant. No server sits in the middle relaying media. That sounds appealing until you do the math: each participant has to upload their stream once for every other participant in the call, and decode a separate incoming stream from each of them too. Add a fifth person to a mesh call and everyone's upload bandwidth and CPU load jumps again. Mesh tops out around three to four participants before it falls over. It's fine for a small ad hoc video chat. It is not an architecture for one-to-many live video at scale, and I mention it here mainly to rule it out.

Walk the math forward and it gets worse fast. A participant in a four-way mesh call is uploading their stream three times and decoding three incoming streams. Push that to eight participants and each person is now uploading seven copies of their own video and decoding seven incoming feeds simultaneously, all on whatever upload bandwidth and CPU their device happens to have. Nothing about that curve bends in your favor. It's why mesh works fine for a handful of coworkers on a call and falls apart the moment you try to point it at a one-to-many viewing problem, where the participant count on the viewing side is exactly the number you're trying to grow.

That's also the tell for why mesh doesn't belong in this series at all beyond this paragraph. One-to-many live video, a small number of cameras or encoders feeding a large number of viewers, isn't a mesh problem, and no amount of tuning turns it into one. Every viewer would need a direct connection to every camera, which means every camera's upload bandwidth would need to scale with the total viewer count. That's the opposite of what you want.

**MCU (Multipoint Control Unit)** takes the opposite approach. A server-side component receives every incoming stream, decodes all of it, composites or mixes it into a single output, and re-encodes that composite before sending it back out. This is powerful. An MCU can mix multiple camera feeds into one deliverable, apply layouts, do server-side processing on the combined video. That flexibility comes at a steep price: decoding and re-encoding every stream server-side is CPU-expensive, and that cost scales with every stream you add. If your use case requires server-side compositing, an MCU earns its keep. If you're just trying to get N viewers watching a handful of source feeds without recombining them, you're paying for compute you don't need.

**SFU (Selective Forwarding Unit)** is the middle path, and for one-to-many live video, it's almost always the right one. An SFU receives each incoming stream once and forwards the encoded packets straight to whichever viewers need them, with no decode or re-encode step in between. No transcoding per viewer. No compositing overhead. You ingest a camera feed once, and the SFU fans the same encoded packets out to however many viewers are watching, whether that's ten or ten thousand.

## Why SFU wins for one-to-many

The math is what makes the call. In a mesh, cost scales with the number of peers in the conversation. In an MCU, cost scales with CPU-intensive transcoding work per stream. In an SFU, ingest cost is paid once per source stream, and fan-out is comparatively cheap because you're forwarding packets, not re-encoding them.

For a video security platform, or any system where a small number of cameras or source encoders need to reach a large number of concurrent viewers, that asymmetry is exactly what you want. You have few sources and many sinks. SFU architecture matches that shape directly: pay the ingest cost once, forward cheaply to everyone watching.

Think about what decoding and re-encoding actually costs a server. It means running a full video codec pipeline, decompressing the incoming stream into raw frames, then compressing it again into an outgoing stream, and doing that work on a CPU or GPU budget that has to be provisioned per stream. An SFU skips all of that on the forwarding path. It inspects just enough of each packet to know where to route it, and sends the same encoded bytes the source produced on to every viewer who needs them. You're not paying compute for every viewer. You're paying network cost, and network cost scales far more gracefully than transcode compute does.

That difference compounds as viewer count grows. Add a hundred more viewers to an MCU-based system, and if any of that increase touches the transcode path, you're adding real CPU load. Add a hundred more viewers to an SFU-based system, and you're adding forwarding load, which is a fundamentally cheaper problem to solve at scale. This is also why the operational story downstream, autoscaling, capacity planning, cost per viewer, gets so much easier once you've picked SFU. You're solving a forwarding problem, and forwarding problems have well-understood scaling patterns.

This is also why SFU has become the dominant pattern behind the modern generation of WebRTC infrastructure tools. LiveKit, mediasoup, and Janus are all built on this architecture. I'm not going to compare those three against each other in this post. Each gets its own treatment later in the series, because the differences between them matter once you're choosing a specific platform to build on. What matters right now is the pattern underneath all three: forward, don't transcode, and let that discipline carry your bandwidth and CPU budget as the audience grows.

There's a caveat worth stating plainly. SFU is the right default for one-to-many viewing. A product that requires server-side mixing, like compositing multiple feeds into a single output stream for recording or broadcast, calls for an MCU instead, and trying to force an SFU into that job will cost more engineering effort than just using the tool built for it. For the specific problem this series is about, watching live camera or source feeds at scale, SFU is the architecture I'd choose every time, and it's the one the rest of this series assumes.

## Where this series goes from here

Choosing SFU as the topology answers one question and opens several more. You still have to decide how signaling and session state get managed separately from the media itself, how to route and shard streams as you scale past a single server, which specific SFU implementation fits your workload, and how to actually load test the thing before it meets real traffic. That's the rest of this series: the gateway layer that sits in front of your media servers, the tradeoffs between the major SFU platforms, how sharding and scaling work in practice, and what it takes to validate all of it under real load before you bet a product on it.

Topology is the foundation. Everything else in glass-to-glass latency gets built on top of whichever one you pick.
