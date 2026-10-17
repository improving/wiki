---
type: Reference
title: "The Last Few Feet: Endpoint Optimization"
resource: "https://www.devlinliles.com/the-last-few-feet-endpoint-optimization/"
author: "Devlin Liles"
published: '2026-09-04'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Sixteen posts ago I started this series with a claim: one-to-many live video at scale is a systems problem, not a video problem. Topology, planes, TURN budgets, transcoding, keyframes, gateways, pipeline frameworks, platform choice, migration, sharding, failover, load testing, edge filtering, middle-tier structure. Every one of those posts was about getting the stream from a source to a viewer as fast and as cleanly as possible. This last post is about what happens in the final few feet, on the device actually decoding what you sent, because everything upstream can be perfect and still get thrown away right there.

## Decode is close to solved. Encode isn't there yet.

The tool that makes this last mile tractable is the WebCodecs API, which gives web applications low-level, hardware-accelerated encode and decode control directly in the browser, operating frame by frame, without hiding everything behind a black-box media element. Support in 2026 is strong: Chrome 94 and later, Edge 94 and later, Firefox 130 and later on desktop, and Safari 26.0 and later on macOS, iOS, and iPadOS.

Real-world usage data backs that up. Across more than a million sessions, hardware decode support is close to universal. AV1 plus HEVC decode covers roughly 99.7 percent of sessions on Chrome, Edge, and Firefox across desktop and Android, and VP9 decode is as universal as H.264 at this point. If your only concern were decoding, you could reasonably stop worrying about device capability and move on.

Encoding is a different story. Roughly 88 percent of sessions support AV1 encoding, and only with the correct codec string specified, which in production practice means Profile 0, 8-bit. That's still a strong number. It's also not universal, and the gap between "decode is basically solved" and "encode still has real constraints" is exactly the kind of gap that gets ignored in architecture diagrams and then shows up as a support ticket in production.

## "Close to universal" still has real edges

The gap on the decode side is narrow but not zero, and where it shows up matters more than how big it is. Firefox for Android doesn't support WebCodecs in any version, so on that browser the API is desktop-only. Safari's audio-side support, AudioDecoder and AudioEncoder, lagged well behind its video-side support for a long stretch, with versions 16.4 through 18.7 shipping video-only support. If your endpoint strategy assumed uniform capability across every browser and device combination, both of those are places it quietly breaks.

The practical implication isn't that WebCodecs is unreliable. It's that "close to universal" is not the same as "universal," and the difference lands on real viewers: someone on an older device, someone on Firefox for Android, someone whose device technically decodes AV1 but can't encode it at the profile you need for a two-way stream. An endpoint strategy that assumes every viewer can handle the same stream is going to be wrong for a small but real slice of your audience, and that slice doesn't shrink just because the average case looks great in aggregate. You have to check actual capability per device at connection time. Not once at build time, not as a static browser-version lookup table, but live, at the point where a specific viewer's specific device is about to start receiving frames.

In practice, that check is a call to isConfigSupported before you commit to a codec and profile for a given session, not an assumption baked into a build flag. Ask the browser what it can actually do with the exact codec string you intend to use, get an answer back, and route the connection accordingly. It's a small amount of code relative to everything else in this series. Skipping it is how a platform ends up shipping a single "modern" codec configuration to every viewer and quietly losing the tail of devices that can't keep up with it, without ever generating an error message that points at the real cause.

## This is what makes simulcast and SVC worth the complexity

I spent a post earlier in this series comparing LiveKit and mediasoup, and one of the features that came up was simulcast and SVC, sending multiple quality layers of the same stream at once. At the time I framed it mostly as a bandwidth and network-variance tool. It's that, and it's also the mechanism that turns per-device capability checking into something you can actually act on.

Detecting that a specific viewer's device can only decode H.264 efficiently, or can decode AV1 but not encode it, or has a decoder fast enough for 1080p but not for a heavier codec at the same resolution, only matters if you have something to do with that information. Simulcast and SVC are the something. The server sends multiple quality layers and picks the right one per viewer, matched to that viewer's actual decode capability and current bandwidth. It doesn't send one quality level to everyone and hope the weakest device keeps pace. Send the low-end viewer the layer built for high-end devices and you've queued up dropped frames and decoder stalls no amount of server-side tuning will fix. Send everyone the layer the weakest device needs and you've quietly degraded every viewer who could have had a better stream. Capability detection is the input. Simulcast and SVC are what let you act on it correctly, per viewer, without picking one setting for your whole audience.

## The diagnosis this series ends on

This also loops back to the keyframe post from earlier in the series. Keyframe interval and GOP structure were framed there as a latency decision on the encode side, and they are. They're also a decode-side cost. A decoder on a lower-end device spends real time reconstructing frames between keyframes, and a GOP structure tuned purely for glass-to-glass latency without any regard for decode cost can hand a weak device more work per second than it can keep up with, even when the bitrate itself looks reasonable. Capability detection is what tells you which viewers can absorb that decode cost and which ones need a gentler encode profile through their assigned simulcast layer.

Go back to the thundering-herd post, where I made a point about diagnosis that applies directly here: when your server-side metrics are clean and playback is still choppy, the cause is client-side, not server-side. Jitter buffer tuning, packet loss concealment, decoder performance on a lower-end device. No amount of upstream optimization fixes a client-side problem, because the problem was never upstream.

That diagnosis is the whole argument of this post, generalized. Treat capability detection, what this specific viewer's browser and device can actually decode, in hardware, right now, as a first-class part of connection setup, not an afterthought bolted on after the stream is already flowing. Drive your simulcast or SVC layer selection off that detection. And stop assuming that a well-engineered server-side pipeline guarantees a good viewer experience, because it doesn't. It guarantees a good stream arrives at the edge of the device. What the device does with it from there is a separate problem, with its own failure modes, and it deserves its own attention. Waving it away as "not our layer" is how good server-side engineering ends up wasted on a bad viewer experience.

## Where this series ends

A system can get the topology right. It can split the control plane from the data plane cleanly, budget TURN accurately and catch the bill before it arrives, kill transcoding it never needed, tune keyframes for the latency it's actually trying to hit, put the right gateway in front of legacy cameras, reach for a heavyweight pipeline framework only when the workload actually calls for one, pick the platform that matches its real traffic pattern over the one with the best marketing, migrate off a legacy media server without a weekend of downtime, shard its streams cleanly, plan failover before it needs it, load-test the failure pattern that will actually happen, not the one that's easiest to simulate, filter at the edge so the center only sees what matters, and structure its middle tier so nothing ever blocks the viewer path.

And it can still lose that viewer in the last few feet, at the one device on the other end that can't decode what's arriving fast enough to keep up. That's not a smaller problem than everything else in this series. It's the same problem, one layer further out, at the one place you don't control: the glass on the other end of glass-to-glass. Everything in between is engineering. That last few feet is where you find out if you actually understood who you built it for.
