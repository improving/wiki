---
type: Reference
title: "Split the Control Plane From the Data Plane, or Neither Will Scale"
resource: "https://www.devlinliles.com/split-the-control-plane-from-the-data-plane-or-neither-will-scale/"
author: "Devlin Liles"
published: '2026-08-27'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Here's a decision that looks small on a whiteboard and turns out to be load-bearing for everything downstream: split the control plane from the data plane. Do it early, do it deliberately, and most of your scaling problems later in this series become tractable. Skip it, and you end up with a system where scaling the easy part and scaling the hard part are tangled together, which means you can't scale either one well.

I picked this as post two in this series because it's the architectural decision that everything else, sharding, autoscaling, failover, sits on top of. Get it right, and those later posts optimize a sound foundation. Get it wrong, and they end up patching a foundational problem.

## Two different jobs wearing one system

A live video system built on WebRTC is doing two fundamentally different jobs at once, and it's worth naming them separately because they have almost nothing in common under the hood.

The first job is signaling: the out-of-band negotiation that happens before any media flows. Two peers, or a peer and a media server, need to exchange SDP offers and answers describing what codecs and media types they support, and ICE candidates describing the network paths available to reach each other. This negotiation typically happens over a WebSocket connection to a signaling server. It's a conversation about how to set up a connection, not the connection itself. Alongside signaling sits everything else in the control plane: authentication, authorization, room and stream state, who's allowed to view what.

The second job is the media relay itself: once signaling has done its work and a connection is established, actual audio and video packets start flowing through the media server, whether that's an SFU or something else. This is the data plane. It's stateful, it's continuous, and it's the part actually consuming your bandwidth and CPU.

These two jobs have opposite scaling personalities, and that's the whole point of separating them.

Look at what each one is actually holding onto. A signaling exchange is a short conversation: offer, answer, a handful of ICE candidates, done. Once that negotiation completes, the signaling server doesn't need to remember much about it. A media session, by contrast, is a long-lived relationship between a specific viewer and a specific server process, and it stays open for as long as that viewer is watching. Minutes, sometimes hours. The signaling layer's job is finished in milliseconds. The media layer's job just started, and it's going to keep running.

That asymmetry, short-lived and stateless versus long-lived and stateful, is the real reason these two jobs need different treatment. It's not an aesthetic preference for clean architecture. It's a direct consequence of what each layer is being asked to hold onto over time.

## Why signaling scales like a normal web service

The control plane, the signaling and room-state layer, is fundamentally stateless in the way that matters for scaling. A request to negotiate a connection or check a viewer's authorization doesn't need to be handled by the same server every time. You can put a generic load balancer in front of a fleet of interchangeable signaling instances, scale that fleet horizontally the same way you'd scale any web API, and none of it requires special awareness of which instance handled the last request from a given client. This is the same scaling story you already know from building ordinary backend services, and that's a feature, not a limitation. You don't need to reinvent anything here.

Push traffic up on a Tuesday afternoon because a big event is driving viewers to the platform, and the fix is exactly what you'd expect from any web service under load: add instances behind the load balancer, let health checks and routing sort out the distribution. Room state and authorization checks can live in a shared store that any signaling instance can read from, so it truly doesn't matter which instance handles which request. This is the boring, well-trodden part of the system, and boring is exactly what you want from your control plane. The interesting engineering problems in a WebRTC platform live elsewhere, and that's by design once this layer is split off cleanly.

## Why the media relay does not

The data plane is a different animal entirely. Once a viewer's connection is established and media is flowing, that session lives on a specific media server instance, holding state (active streams, buffers, encoder and decoder context) for as long as the session is active. You cannot put a generic load balancer in front of a fleet of media servers and treat them as interchangeable the way you can with stateless web servers. A request that lands on the wrong instance doesn't just get a slower response. It doesn't have access to the media session at all, because that session doesn't exist there.

This is the mistake I see teams make when they carry over intuition from scaling ordinary web infrastructure: treating a fleet of media servers like a fleet of stateless API servers, and reaching for the same load-balancer-in-front-of-everything pattern. It doesn't work, because the media server isn't stateless. It's holding an active session. Scaling this layer correctly means routing new streams to specific instances with awareness of what each instance is already carrying, sharding load across instances deliberately. That's a big enough topic that it gets its own post later in this series. For now, the point I want to land is narrower: the media relay needs a scaling strategy built for stateful sessions, and that strategy is not the one you already know from web services.

There's a failure isolation benefit here too, and it matters as much as the scaling story. If your signaling logic and your media relay logic live in the same process or the same deployable unit, a bug or a resource spike in one takes down the other, even though they have nothing to do with each other functionally. A memory leak in your room-state logic shouldn't be able to drop active video sessions. A spike in media server CPU load shouldn't take your authentication service down with it. Separating the planes doesn't just give you two different scaling stories, it gives you two different blast radiuses. When something breaks, and something always eventually breaks, you want to know which half of the system it broke, not have both halves go down together because they were never really separate to begin with.

## Why the split matters more than either half

Neither of these facts is surprising in isolation. Stateless services scale one way, stateful services scale another. What matters is what happens if you don't formally separate them in your architecture. If signaling and media relay logic live entangled in the same service, you inherit the constraints of the harder problem (stateful media sessions) even for the parts of the system that don't need them (stateless negotiation and auth). You end up either over-provisioning your signaling layer to satisfy media server constraints it doesn't actually have, or under-provisioning your media layer because you're scaling it like a web tier.

Split them, and each layer scales according to its own nature. Signaling and room state scale cheaply and elastically behind a standard load balancer. Media relay scales by adding capacity where the sessions actually are, sharded deliberately across instances. Each half gets the playbook that actually fits it.

I've seen the entangled version of this play out the same way more than once. A team stands up a media server, wires signaling logic directly into it because it's convenient early on, and ships. It works fine at low volume. Then viewer count grows, someone notices the system isn't scaling smoothly, and the instinct is to add more of the same combined unit behind a load balancer, because that's the pattern that's always worked before. It doesn't work here, because half of that combined unit is holding stateful sessions that the load balancer has no visibility into. The fix at that point is a rebuild, not a config change, because the two concerns were never actually separated. Doing the split up front costs you a bit of extra structure early. Not doing it costs you a rebuild later, usually under the exact traffic pressure that made the problem visible in the first place.

This is the decision that makes the rest of this series legible. Once control plane and data plane are cleanly separated, questions like "how do we route new streams to the right instance" and "how do we autoscale the media layer under load" become answerable on their own terms, without also having to answer "which part of this system are we even talking about." I'll get into the mechanics of stream sharding and routing directly in a later post. For now, the architectural discipline is the whole lesson: draw the line between control and data early, and hold it.
