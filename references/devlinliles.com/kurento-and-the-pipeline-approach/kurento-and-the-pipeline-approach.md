---
type: Reference
title: "Kurento and the Pipeline Approach"
resource: "https://www.devlinliles.com/kurento-and-the-pipeline-approach/"
author: "Devlin Liles"
published: '2026-08-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Most teams building one-to-many live video reach for a media server and assume they need the most capable one they can find. That instinct is backwards. The right question is narrower: does anything need to touch the media while it's in flight, or does it just need to get from one source to many viewers intact?

Kurento answers the first question well. It carries a real cost for the second question, a cost you don't need to pay if all you're doing is moving frames from a camera to a crowd of viewers.

## What Kurento actually is

Kurento is a full GStreamer-based media pipeline framework. GStreamer is a general-purpose multimedia framework that lets you build a pipeline out of discrete processing elements: decode this, filter that, composite these three sources into one frame, encode and ship it out. Kurento wraps that power in a WebRTC-facing API. That means you can construct a media pipeline where every stream is actively processed on its way through, not simply passed along.

That processing capability is the whole value proposition. If you need in-pipeline mixing, recording, or computer-vision hooks, Kurento gives you a place to put that logic inside the media path itself. Face filters, AR overlays, QR or object detection running inline with the stream: all of that is exactly the kind of task GStreamer pipelines were built for. Kurento makes it addressable from a WebRTC-facing service, so the processing logic and the streaming logic live in the same system with the same operational surface.

Contrast that with a pure relay. A Selective Forwarding Unit takes a stream in and sends it back out to N viewers without decoding it. It never looks inside the frames. It can't, because looking inside the frames is exactly the work it's designed to avoid. Say your requirement is "detect a QR code in this camera feed and act on it while the stream is live." An SFU has nothing to offer you there. You'd have to bolt a separate processing path onto the side, subscribe to the stream a second time, decode it yourself, and hope the two paths stay in sync. Kurento handles that inline, as part of the pipeline the media already passes through, with one system responsible for the whole path.

For a video security platform specifically, this is where the pipeline framework earns its keep. RTSP ingest from a camera can flow straight into a GStreamer pipeline that runs motion detection, reads a license plate, or flags a defined zone crossing, and the same pipeline hands the processed stream off to WebRTC for the live viewer. One system owns ingest, analysis, and delivery. Build that same capability around an SFU and you're maintaining two systems that both need to stay synchronized with the same camera feed, which is its own operational burden on top of whatever the CV logic costs to run.

## The reputation problem, and why it's overstated

Kurento has a reputation in some WebRTC circles for being stalled or abandoned. That reputation is out of date. As of mid-2026, Kurento is still shipping point releases on its 7.x line. It's more alive than people assume, and it deserves to be evaluated on its current state. The project's momentum looked uncertain a few years ago; the current release history tells a different story.

I want to be direct about the tradeoff, because "still maintained" doesn't mean "lightweight." Kurento is heavier per stream than a lean SFU. A full GStreamer pipeline carries more moving parts per participant than a relay that never decodes anything: more CPU, more memory, more places for a misconfigured pipeline to become a debugging problem at two in the morning. That weight isn't a flaw in the project. It's the necessary cost of the thing it's built to do. You cannot mix three streams into one composited feed, run a CV filter across a frame, and write it to disk for a recording without decoding and re-encoding somewhere in the chain. That work carries a resource cost no matter which framework does it. Kurento's honesty is that it carries that cost in the media path itself, where you can see it, measure it, and tune it. A duct-taped side service bolted onto a relay hides the same cost without giving you any of that visibility.

That distinction matters when you're capacity-planning. A team that budgets CPU and memory as if Kurento were a relay will be surprised by their bill and their server count the first time recording or a CV hook goes live in production. A team that budgets for a pipeline framework from the start won't be.

The practical way to size this is to test the specific processing step you plan to run, not the pipeline framework in the abstract. A pipeline doing pass-through recording behaves very differently under load than one running a CV model on every frame. Object detection in particular can dominate the resource profile of the whole pipeline, to the point where the WebRTC delivery portion is almost a rounding error next to the inference cost. Measure the actual filter or model you intend to run, at the resolution and frame rate you intend to run it at, before committing to a server count. Guessing here tends to guess low.

## OpenVidu, or why you probably won't write raw GStreamer pipelines by hand

If you decide Kurento is the right tool, you're very unlikely to hand-write GStreamer pipeline definitions and wire up the Kurento client API from scratch. OpenVidu is the higher-level room framework built on top of Kurento, and in practice it's the only common path teams take when they don't want to build the pipeline layer themselves. OpenVidu gives you rooms, sessions, and a conventional application-facing API, while Kurento does the pipeline work underneath.

This is a normal pattern in this space, and it's worth internalizing early because it shows up again with other tools later in this series. The low-level media engine and the framework a product team actually builds against are usually two different projects, maintained by different groups, with the second one existing specifically to make the first one usable without a GStreamer specialist on staff. If you're evaluating Kurento, you're really evaluating "Kurento plus OpenVidu" as the practical unit of adoption. Very few teams touch the bare pipeline library directly, and fewer still should, given how much scaffolding OpenVidu already provides around session and room management.

OpenVidu doesn't remove the need for GStreamer knowledge entirely. If your CV hook or your mixing logic is custom, someone on the team still needs to understand how a GStreamer pipeline element behaves under load, what happens when a filter drops a frame, and how to trace a stall back to a specific stage in the chain. What OpenVidu removes is everything around that: session lifecycle, room membership, the WebRTC signaling plumbing that has nothing to do with your custom processing logic. That's a meaningful reduction in scope, and it's the reason OpenVidu is worth adopting even for a team that's comfortable with GStreamer. It lets your GStreamer expertise go toward the part of the problem that's actually unique to your product.

## Where this leaves you

Here's the framing I'd want a team to walk away with. If the actual need is RTSP-in, WebRTC-out fan-out at scale, meaning cameras or other sources publish and a growing number of viewers watch, with nothing touching the media in between, a full pipeline framework like Kurento is the wrong tool for the job. It solves a problem you don't have, and it makes you pay the resource cost of that solution anyway. A lean SFU is the right tool for that job, and the next post in this series covers which one to pick and why that choice is a real decision, not a coin flip.

Kurento and OpenVidu earn their weight when the requirement is specifically that the media gets touched in flight: composited, filtered, inspected, or recorded through a pipeline, not simply relayed byte for byte. If a product roadmap includes "detect X in the live feed" or "composite multiple camera angles into one output stream" as a real, near-term requirement, not a someday-maybe on a wishlist, that's the moment a pipeline framework stops being overkill and starts being the only tool that actually does the job. Everywhere else, you're carrying weight for capability you're not using, and paying for it in CPU, memory, and operational complexity you didn't need to take on.
