---
type: Reference
title: "Failover in Live Video"
resource: "https://www.devlinliles.com/failover-in-live-video/"
author: "Devlin Liles"
published: '2026-08-31'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Failover in live video is a real design decision with a real tradeoff. Most teams don't treat it that way. They build whichever option is easier to ship first, call it done, and only discover they made a decision at all when an instance dies during exactly the wrong moment.

There are two real options when a stream-holding instance fails, and they sit at opposite ends of a cost-versus-gap spectrum. Understanding both, and being honest about which one your product actually needs, matters more than either option in isolation.

## Option one: duplicate ingest

The first option is to duplicate ingest to a standby instance. A second copy of the source stream is already flowing into a second instance at all times, decoded or passed through in parallel with the primary, sitting there doing nothing except being ready. When the primary instance fails, the standby is already holding a live copy of the stream. Viewers get rerouted to it, and the gap is close to zero. No reconnect. No renegotiation. The stream just keeps flowing, because a second version of it was never not flowing.

That's a strong guarantee, and it's expensive in a specific, unavoidable way: you're running and paying for two live copies of every stream's ingest path, continuously, whether or not the primary ever fails. If a stream never fails once in its entire lifetime, you paid the full cost of duplicate ingest for nothing but insurance. That's not a criticism of the approach. Insurance you never claim isn't wasted money, it's the reason nothing went wrong. But it is a cost that has to be budgeted in full, per stream, for the entire duration every stream is live, not treated as a rounding error on the infrastructure bill. Multiply that per-stream cost across a fleet of thousands of cameras and the number stops looking like a rounding error fast, which is exactly why this option needs a clear justification, not a reflexive "safer is better" instinct.

## Option two: accept the reconnect gap

The second option is to accept a few seconds of re-establish time when a failure happens. There's no standby holding a duplicate copy. When the primary instance fails, the system has to notice, reconnect to the source over RTSP, and renegotiate the WebRTC session with every affected viewer. That's two separate re-establishment steps stacked on top of each other, not one. First the gateway has to detect the failure and open a new RTSP session back to the camera or encoder, which takes its own round trip. Then, once media is flowing into the gateway again, every viewer's WebRTC session has to renegotiate against whichever instance now holds the stream, which is its own signaling exchange and connection setup. Both steps have to complete before a viewer sees live video again, and that stacked sequence is where the few seconds of gap actually comes from.

This option costs nothing extra in steady state. No duplicate ingest path, no standby instance sitting idle, no doubled infrastructure bill for streams that never fail. The cost only shows up at the moment of failure, concentrated into a real, if short, blackout window exactly when an instance goes down. It's simpler to build, because it's the default failure behavior of a system that isn't specifically engineered around eliminating that gap. That simplicity is also exactly why it tends to get chosen without anyone deciding it on purpose.

## The tradeoff, made explicit

The shape of the tradeoff is clean once you see both options side by side. Duplicate ingest buys you a failover gap close to zero, at the cost of paying for a second live ingest path on every stream, all the time. Accepting the reconnect gap costs nothing extra in steady state, at the cost of a real blackout window whenever a failure actually happens. Neither option is free. Neither option is universally correct. The right one depends entirely on what a gap costs your specific business in the worst case, and that's a question this post can't answer for you, because it's not an infrastructure question at all.

## Why this decision belongs to the product, not the platform

Here's the part that actually matters: which option is right depends entirely on how much a short gap costs for the specific use case you're building.

Think about security footage. If a camera feed is being watched live specifically because something might happen on it right now, a break-in in progress, a safety incident, a moment someone needs to see as it unfolds, a several-second gap during exactly the wrong moment can matter enormously. That's not a hypothetical edge case for a security platform. That's the scenario the entire product exists to serve, and a reconnect gap that lands during it is a failure of the product's core promise, not just an infrastructure hiccup.

Now think about a lower-stakes live view: a general activity feed, a casual monitoring stream, something viewers check in on without the moment-to-moment stakes of a security incident. A few seconds of reconnect during a rare instance failure might be a genuine non-issue there. Nobody's safety depends on that exact frame, and the cost of building and running duplicate ingest for every stream in that product would be money spent solving a problem the business doesn't actually have.

Same technical failure. Same two options on the table. Completely different right answer, because the thing that determines the right answer isn't a technical property of either failover strategy. It's a business judgment about what a gap costs in the worst case, for this specific product, for these specific users, at this specific moment of use.

It's also worth saying plainly that the choice doesn't have to be all-or-nothing across an entire platform. A security platform running thousands of camera feeds can reasonably apply duplicate ingest to a small, defined tier of highest-priority streams, entrances, cash handling areas, wherever a gap truly can't happen, while accepting the reconnect gap on the much larger population of lower-priority feeds where the cost of a doubled ingest bill isn't justified. That's a tiering decision, and it's a legitimate answer to "which option is right," as long as the tiers were drawn deliberately based on what each stream's gap actually costs, not drawn by default because someone had to draw a line somewhere.

## Don't let this get decided by default

The failure mode I want to flag isn't picking the wrong option. It's not picking at all, and ending up with the reconnect gap by default because it's simpler to build first and nobody stopped to ask whether that gap is acceptable.

This is a product and business decision wearing an infrastructure costume. The engineering team can lay out both options, the real cost of duplicate ingest, and the real duration and behavior of a reconnect gap. What the engineering team can't do alone is decide how much that gap costs the business when it happens at the worst possible moment, because that number lives in the product's value proposition, not in the media server's configuration. That conversation needs to happen explicitly, with someone who owns the product outcome in the room, before a failover strategy gets locked in by whichever path was easiest to ship in the first sprint.

The question worth putting in front of that room is a simple one: if this exact stream drops for five seconds at the worst possible moment, what does that cost us? Sometimes the honest answer is a shrug, and the reconnect gap is the right call, saved budget with no real downside. Sometimes the honest answer is a liability conversation, a missed incident, a customer who churns because the one time they needed the feed it wasn't there. Neither answer is wrong. What's wrong is not asking the question and discovering the answer for the first time during an actual outage, with a customer or an incident report on the other end of it.

Have that conversation early, and you end up with a failover strategy that matches what the product actually needs, whether that's duplicate ingest for a use case where gaps are unacceptable, or a reconnect-based approach for a use case where the savings are real and the risk is truly tolerable. Skip that conversation, and you end up with whatever the path of least resistance produced, discovered as the right or wrong call only after a real failure puts it to the test in production.
