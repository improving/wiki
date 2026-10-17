---
type: Reference
title: "Structuring the Middle of the Pipeline"
resource: "https://www.devlinliles.com/structuring-the-middle-of-the-pipeline/"
author: "Devlin Liles"
published: '2026-09-03'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Edge filtering, the subject of the last post, doesn't eliminate central processing. It shrinks it and makes it more meaningful. You still need recording, cross-camera correlation, alert enrichment, and any detection work the edge tier couldn't handle on its own. That work has to live somewhere in your central pipeline. The question this post answers is where exactly, because getting this wrong is one of the most common ways teams quietly destroy the low-latency architecture they spent the rest of this series building.

## The mistake, stated plainly

Here's the failure mode: a team builds a clean SFU-based fan-out path for live viewers, gets the transcoding discipline right, tunes keyframes, budgets TURN accurately, does everything the first dozen posts in this series recommended. Then they need to add a CV model, or start recording streams, or correlate events across cameras, and they route that work through the same process that's doing live fan-out to viewers.

It feels natural in the moment. The pipeline is already touching the stream. Why not have it do the extra work too? Because now every slow model, every recording write, every cross-stream correlation job sits directly on the critical path of what a live viewer experiences. A spike in processing load stops being a processing problem and becomes a viewer-facing latency problem, immediately, with no isolation between the two. Every bit of latency discipline you built into the fan-out path gets spent the moment something in the processing branch runs long. You didn't add a feature. You added a new failure mode to your live path.

## Branch the stream, not the pipeline

The fix is architectural, and it's simpler than it sounds once you say it out loud: branch the stream. Don't route it through a single pipeline that does everything.

Your SFU or gateway fans a copy of the stream to viewers on the low-latency path, exactly the way it always has. Separately, it hands a copy of the stream, or in many cases just the relevant frames or metadata, to a processing tier that consumes it asynchronously off a queue. That processing tier is fully decoupled from the viewer-facing path. It can run slow, it can back up, it can even fall over entirely, and a viewer watching the live feed never knows anything happened.

This is the same principle that shows up everywhere in distributed systems once you're doing anything beyond the simplest request path: separate the fast path from the slow path, and don't let the slow path apply backpressure to the fast one. Live video just makes the consequences of skipping that separation viscerally obvious, because the fast path here is something a person is watching in real time.

Mechanically, this usually means the SFU or gateway publishes a copy of the stream, or the extracted frames and metadata a processing job actually needs, onto a message bus or a queue: Kafka, a Redis stream, a plain job queue, whatever fits your stack. Workers pull from that queue at whatever pace they can sustain. If a model runs slow on a given frame, or a recording write backs up because a disk is under pressure, the queue absorbs it. Depth grows, workers catch up when they can, and the viewer-facing path never notices, because it was never waiting on any of this to begin with. The queue is doing exactly one job: making sure a slow consumer can never become a slow producer's problem.

## Where a pipeline framework still earns its place

I spent a full post earlier in this series making the case that a heavyweight, GStreamer-based framework like Kurento is the wrong default for a plain one-to-many live path, because it adds overhead most teams don't need. That's still true for the viewer-facing path. It is not an argument against pipeline frameworks generally.

If your team actually needs in-pipeline mixing, or a CV model heavy enough that it needs real pipeline plumbing around it, a GStreamer-based framework is a legitimate tool for exactly that job. The distinction that matters is where it sits. It belongs in the processing branch, consuming a copy of the stream off the queue, not sitting inline between the camera and the viewer. Same tool, right job, wrong location is the difference between a smart architectural choice and a latency bug you'll spend weeks diagnosing.

## Scale them separately, because they fail on different signals

This has a direct consequence for how you autoscale, and it connects straight back to the sharding post earlier in this series. A processing worker pool and an SFU tier are not the same kind of workload, and they don't fail under the same kind of pressure.

Your SFU tier is bound by egress bandwidth and per-connection overhead. It scales with viewer count and stream count, and the signal that tells you to add capacity is bandwidth headroom and connection count on existing nodes. Your processing tier is bound by CPU and inference load. It scales with event volume and model complexity, and the signal that tells you to add capacity is queue depth and worker utilization, which has nothing to do with how many viewers are currently watching anything.

Put them in the same autoscaling group and you've tied two unrelated signals together. A burst of processing-heavy events, correlated CV triggers across a camera cluster, say, drives up CPU load and triggers scale-out for the whole group, including SFU capacity you didn't actually need. Worse, a real CPU-bound processing spike can crowd out the headroom your SFU nodes needed for a completely unrelated viewer surge, because the two workloads are now sharing a resource pool that autoscaling logic can't tell apart. Separate groups with separate triggers means each workload scales on the signal that actually describes its own pressure, and neither one starves the other's headroom during an unrelated spike.

Give the two tiers separate monitoring while you're at it, not just separate scaling groups. An SFU dashboard should be built around egress bandwidth, connection count, and packet loss to viewers. A processing dashboard should be built around queue depth, worker utilization, and inference latency per job. Merge those two views into one general-purpose "system health" dashboard and you'll spend an incident staring at aggregate CPU wondering why viewers are fine while inference is drowning, or the reverse. Keeping them visually and operationally separate is a small thing that pays for itself the first time you're on call and need an answer in under a minute.

## The design question to keep asking

Every time a new central processing requirement comes up, whether it's a detection model, a recording feature, or a cross-camera correlation job, there's one question that settles where it belongs: does this need to touch a live viewer's path.

Teams get this wrong even when they know the rule, and it's rarely a knowledge gap. It's a deadline problem. Someone needs a recording feature shipped by the end of the sprint, the SFU already has a hook into the raw stream, and wiring the recording write directly into that hook is the fastest path to a demo. It works in the demo. It works for weeks, sometimes months, right up until disk I/O on the recording path hits contention at the same moment a viewer count spikes, and now two unrelated problems are fighting over the same process. The queue-and-worker pattern costs you a day or two more up front, a message bus topic, a worker process, a bit of serialization. That cost is fixed and small. The cost of skipping it is variable and shows up exactly when you can least afford it, during the traffic spike that was supposed to be your best day.

If the answer is yes, it goes through the same discipline as everything else in your fan-out tier, minimal, fast, protected. If the answer is no, and in my experience it almost always is, it goes on a queue and gets its own autoscaling group with its own triggers. That's the whole rule. It doesn't require a diagram or a design review process. It requires asking the question directly every time, without defaulting to "it's already touching the stream, might as well."

Get the edge tier and the middle tier right and you've done the hard architectural work. The stream is filtered before it arrives, and the processing that remains never competes with the viewer for latency budget. There's still one place left where all of that discipline can go to waste, and it's not anywhere in your infrastructure. It's the device in the viewer's hand. That's where we finish this series.
