---
type: Reference
title: "Sharding Streams at Scale"
resource: "https://www.devlinliles.com/sharding-streams-at-scale/"
author: "Devlin Liles"
published: '2026-08-31'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Shard by stream, not by viewer. That single rule decides how the rest of your fan-out architecture behaves once you're running more source streams than one instance can hold, and it's the rule I see teams get backwards most often.

Here's the model. Each source stream, one camera, one encoder, one feed, lives on exactly one instance at a time. Every viewer watching that stream connects to whichever instance happens to hold it. It doesn't matter if that stream has ten viewers or ten thousand. It has one home, and every viewer's connection routes there. You're not sharding your viewer base across instances the way you'd shard a database by user ID. You're sharding your stream population, and viewers just follow wherever their stream lives.

## Why the placement problem shows up immediately

The moment you accept that model, a question follows immediately: how does a viewer's connection find the right instance? A new stream starts on some instance in your fleet. A viewer requests to watch it. Something has to answer "which instance is holding that stream right now" before the viewer's connection can go anywhere.

That's the placement and routing layer, and it's not optional once you're running more than one instance. You need a fast lookup, something like Redis or an equivalent in-memory store, that maps stream identifiers to the instance currently holding them. Every time a stream starts, that mapping gets written. Every time a stream stops, it gets removed. Every time an instance scales up or down, or fails and a stream gets reassigned somewhere else, the mapping updates. A viewer's connection request becomes a lookup against this table, followed by a routing decision to the instance the table points at.

Get this layer wrong and you get one of two failure modes. Either viewers can't find streams that are actually running, because the mapping is stale or was never written correctly, or two instances both think they're holding the same stream, because the mapping wasn't updated atomically during a handoff. Both failure modes are the kind of bug that looks intermittent and infrastructure-specific right up until you trace it back to a lookup table that was treated as an afterthought, not a core piece of the architecture.

The lookup layer also has to answer a second, less obvious question: where does a brand-new stream land? When a camera or encoder starts publishing for the first time, something has to pick an instance for it, and that decision should account for current load, not just round-robin to whatever instance is next in line. Placing a new stream on an instance that's already carrying your most-watched feed is how you manufacture a hotspot before it even has viewers. A placement decision that checks current load, even something as simple as picking the least-loaded instance at that moment, avoids stacking risk on top of risk before the first viewer connects.

The same lookup layer earns its cost again during failure. When an instance goes down, every stream it was holding has to move somewhere else, and the mapping table has to reflect that new location before viewers can reconnect. That's a real operational sequence: detect the failure, re-place each affected stream on a healthy instance, update the table, let viewers' clients retry their connection against the new location. The lookup table isn't just a routing convenience during steady state. It's the mechanism your failover story runs on, and it needs to be built with that responsibility in mind from the start.

## Why fleet-wide averages lie to you

Once streams are placed and viewers are routed, the next question is when to scale. This is where I see the most expensive mistake in this whole layer: building autoscaling triggers around fleet-wide averages when the failure that actually threatens you is always local to one instance.

A media server doesn't fail as a fleet. It fails one instance at a time, and it fails on one of two resources: CPU, if that instance is doing any transcoding work, or egress bandwidth, if that instance is fanning a stream out to a lot of viewers. Either way, the failure is local to whichever instance happens to be holding the most-watched stream at that moment. Everything else in the fleet can be sitting comfortably under load while that one instance saturates and starts dropping frames or refusing new connections.

Average CPU or average bandwidth across the fleet doesn't surface this. If nine instances are idling at low load and one instance is pinned because it's holding the stream everyone's watching right now, the fleet-wide average still looks fine. Your dashboard says the system is healthy. Your viewers on that one stream are seeing buffering and dropped frames. That gap between what the average says and what's actually happening on the hot instance is exactly where an outage starts, and it's invisible until you build monitoring and autoscaling triggers that look at each instance on its own, separate from the fleet-wide blend.

The trigger itself needs to match the resource that actually saturates. On instances doing any transcoding work, that's CPU: watch per-instance CPU and scale that instance's replacement in before it pegs. On instances purely fanning streams out with no transcoding, CPU tends to stay low even under heavy load, and the resource that saturates first is egress bandwidth. A single instance can be at ten percent CPU and still be minutes from failing outright if the stream it's holding just went from a hundred viewers to ten thousand. A trigger built around CPU alone would miss that instance entirely, right up until it stopped accepting new connections.

## Ingress and egress aren't the same number

Getting per-instance visibility right also means splitting network traffic into the two directions that actually behave differently, because folding them into one blended "network" metric hides where the real cost sits. This distinction sounds almost too basic to call out in an architecture conversation, and that's exactly why it gets skipped. A generic infrastructure dashboard often reports "network in" and "network out" as one combined throughput figure per instance, because that's how the underlying compute platform tends to expose it. That default view is the wrong lens for a media server, and it needs to be split apart deliberately, with its own alert thresholds on each side.

Ingress is the traffic moving from camera or source into your gateway. It's usually small: one stream coming in per source, regardless of how many people end up watching it. Egress is the traffic moving from your gateway out to viewers, and it scales with viewer count on every stream you're serving. Watch one stream with one viewer and egress looks a lot like ingress. Watch that same stream with ten thousand viewers and egress on that instance is now ten thousand times the ingress load for that stream, while ingress hasn't moved at all.

This is usually where the bigger cost lives in a one-to-many system, and it's also where autoscaling triggers need to be sharpest, because egress load concentrates unevenly. It doesn't spread itself across your fleet. It piles onto whichever instances happen to be holding your most popular streams at any given moment, which can shift from hour to hour depending on what's live and who's watching. That's the picture a fleet-wide average will never show you. The hottest instance is heading toward trouble well before the blended number moves enough to trip an alert built around it.

## Build this in from day one

None of this is exotic. It's a lookup table, a load-aware placement decision, and a set of per-instance metrics split by direction and by resource. It has to be there before you scale past a single instance, built in from the start. The alternative is learning it during an outage, discovering the hard way that averages don't reflect how a media server actually fails.

The teams that get this right treat the placement layer and the per-instance, per-direction metrics as part of the initial architecture, not an operational improvement to schedule later. The teams that get burned are usually running a fleet-wide CPU dashboard that says everything's fine right up until a popular stream saturates one instance and takes its viewers down with it, invisible to every other metric they were watching. Shard by stream, route through a real lookup layer, and watch egress and ingress and CPU per instance, not blended and not averaged. That's the whole discipline, and it's a lot cheaper to build upfront than to retrofit during an incident.
