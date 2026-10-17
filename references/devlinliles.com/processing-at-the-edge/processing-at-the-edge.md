---
type: Reference
title: "Processing at the Edge"
resource: "https://www.devlinliles.com/processing-at-the-edge/"
author: "Devlin Liles"
published: '2026-09-01'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

A few posts back, I mentioned that computer vision hooks are one of the main reasons teams reach for a heavyweight pipeline framework like Kurento in the first place. You want to detect something in the stream, so you build a place in your architecture for that detection to happen. That's a reasonable instinct. It's also the wrong first question.

The right first question isn't which framework runs your CV model. It's where the model runs at all. This post, and the two after it, go deep on that question across the three places processing can live: at the edge before a stream ever reaches you, in the middle of your own pipeline, and at the endpoint on the viewer's device. We start at the edge, because getting this one right changes how much work the other two tiers ever have to do.

## Detect first, stream second

Here's the default architecture I still see teams build without thinking twice about it: every camera streams continuously to a central server, and the central server runs detection on every frame of every stream, all the time. It works. It's also backwards. You're paying full bandwidth and full compute cost for every second of footage, including the 95 percent of it where nothing happened.

The alternative is to flip the order. Run detection where the frame originates, on the camera's own compute if it has an adequate SoC, or on a small local box sitting close to a cluster of cameras if it doesn't. Only forward, alert on, or record the moments that actually clear a detection threshold. Everything else stays local and gets discarded or held in a short local buffer.

Frigate is the tool most teams reach for to do this. It's a local NVR and detection layer that adds real-time object detection directly to camera feeds, using a hardware detector that analyzes frames on site so they don't have to ship anywhere else for analysis. It's open source, it's mature, and it's become close to the default answer for "how do I add detection without building my own inference pipeline from scratch."

## The hardware side of the equation

Frigate needs somewhere to run its model, and the current answer for most deployments is an NVIDIA Jetson board running TensorRT. Which Jetson depends on how much you're asking it to do. A Jetson Nano handles a handful of cameras fine. A Xavier NX steps up for more cameras or heavier models when you need it. And as of this year, the easy default for anyone starting fresh is the Jetson Orin Nano Super, at roughly $249, which runs YOLO-class detection models at real-time framerates with inference latency in the 20 to 40 millisecond range per frame, depending on which model you're running and how you've clocked the board.

That price point matters more than it looks like on the surface. It puts real-time, hardware-accelerated detection within reach of a per-cluster deployment, at a price point a single expensive central appliance never offered. The old choice between "cheap and centralized" and "expensive and distributed" is gone. Distributed got cheap.

I'd flag one thing before you go shopping, because it comes up in almost every planning conversation about edge detection hardware: Google's Coral Edge TPU used to be the classic budget accelerator for exactly this pattern, and if you've read any older edge-AI literature, it's probably in there. Don't build around it in 2026. Google has effectively discontinued and abandoned Coral. Drivers are community-maintained at this point, not vendor-supported, and Google's announced successor, an open-source NPU design called Coral NPU, isn't shipping as real hardware from any silicon partner yet. Coral is a legacy option at best for an existing deployment you're not ready to touch. For anything new, a GPU-class board like the Orin Nano Super is the safer default, and it's not close.

That per-cluster box question deserves a beat of its own, because it's the first fork in the road for most deployments. Some current camera hardware ships with an SoC capable enough to run a lightweight detection model directly on the camera, no separate box required. When that's true, use it. It's one less piece of hardware to rack, power, and maintain. Most fleets, though, especially anything deployed over the last several years, are running cameras whose onboard compute was sized for encoding and streaming, not inference. For those, a shared local box per cluster is the practical answer: one Jetson-class board serving detection for a handful of nearby cameras, sized to the camera count and the model weight, not to any single camera's limitations. The clustering itself is a cost-control decision. One Orin Nano Super per camera would work, but it's wasteful when a single board can carry several cameras at once without missing its latency target.

## What you actually gain, and what it costs you

The gain is simple to state and easy to underestimate in practice. When detection happens at the edge, you cut central bandwidth and central CPU dramatically. Only the footage that clears a threshold gets forwarded, alerted on, or recorded, and everything else stays local, all day, from every camera, without ever needing central attention. For a deployment with any meaningful camera count, that's the difference between a central architecture that scales linearly with camera count and one that scales with actual event volume, which is a much friendlier curve.

The cost is real too, and it's not a bandwidth or compute cost. It's an operational one. Every edge box you deploy is now a small fleet of independent computers running a model that needs versioning, needs updates, and needs drift monitoring, spread across however many camera clusters you've got in the field. A purely central architecture never had this problem, because there was exactly one place the model lived. Push detection to the edge and you've traded a scaling problem for a fleet-management problem. That's a good trade for almost everyone, but it's still a trade, and you should walk into it with your eyes open. The alternative is discovering it six months in, when nobody can tell you which sites are running which model version.

Plan for that fleet problem the same way you'd plan for any other fleet of production machines, because that's what it is. Version every model artifact, not just every code release. Roll updates out in stages, a handful of clusters first, then the rest. Pushing every edge box at once means you find out at scale that a new model version regressed on a lighting condition your test set never covered. Watch for drift: a detection model tuned against summer daylight will not perform the same way against winter glare or a camera that got bumped three degrees during maintenance, and you want to catch that from a dashboard, not from a missed alert. None of this is exotic. It's the same discipline you'd apply to any fleet of edge devices in any industry. The only new part is that a video platform team has to own it now, on top of everything else in this series, because the alternative of not owning it costs you the detection accuracy the whole architecture depends on.

This is also where edge filtering pays off in a place you might not expect: further down your own pipeline. Go back to the sharding and thundering-herd posts earlier in this series. Both of those were about handling load spikes and correlated failure across your fan-out tier. A big share of the ugliest spikes in a video platform trace back to false triggers, correlated events, or noisy streams that shouldn't have demanded central attention in the first place. Better edge filtering doesn't just reduce steady-state load. It changes the shape of the spikes your central architecture has to absorb, because fewer false triggers means fewer full-herd events downstream. If you did the work in those earlier posts to make your sharding and autoscaling resilient, edge filtering is what reserves that resilience for the days that actually matter.

## Where I'd land

For most teams building a camera-based product today, detection belongs at the edge. Run it on the camera's own compute if the SoC is adequate for the model you need. If it isn't, run it on a local box per cluster, Jetson-class hardware running TensorRT and a YOLO-family model through something like Frigate. Treat "stream everything centrally and analyze it there" as the wrong default for anything beyond a small pilot deployment, not a reasonable starting architecture you'll optimize later.

The fleet-management burden is real, and I'm not going to pretend it isn't. But it's a solvable, well-understood problem: versioned model artifacts, staged rollouts, drift alerts. The alternative, a central pipeline drowning in footage nobody looked at, isn't a problem you solve. It's a problem you pay for indefinitely, in bandwidth and compute that scale with camera count, whether or not anything in that footage ever mattered.

Once detection has done its job at the edge, you're left with a smaller, more meaningful stream of events and footage that does need central attention: recording, cross-camera correlation, alert enrichment, the things a single edge box can't do on its own. How you structure that central processing so it never competes with your live viewer path is the subject of the next post.
