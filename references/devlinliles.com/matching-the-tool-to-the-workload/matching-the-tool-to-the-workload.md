---
type: Reference
title: "Matching the Tool to the Workload"
resource: "https://www.devlinliles.com/matching-the-tool-to-the-workload/"
author: "Devlin Liles"
published: '2026-08-29'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

There is no single best media server. I've now walked through five of them across three posts, and if you take one thing away from this run, take this: every one of those tools is the right answer to a specific question, and a weak answer to almost every other question. A team that picks a tool for its GitHub star count and skips the question of fit for the actual workload doesn't end up with a better system for having done so. It ends up fighting the tool on top of fighting the problem, which is a worse position than the one it started in, because now there are two problems and less time to solve either.

Before naming the two specialist tools worth knowing, it's worth restating the architecture underneath most of what I've covered so far. An SFU, a Selective Forwarding Unit, is a media server architecture that forwards each participant's stream to others without decoding or re-encoding it. That's the architecture underlying LiveKit, mediasoup, and Janus alike. All three relay media without ever decoding it for processing, which is why none of them can do what Kurento does with an in-pipeline CV hook or a mixed recording, and why none of them carry Kurento's per-stream weight either. Grasping that these three share one architecture, and differ mainly in how they package and implement it, does most of the work of comparing them sensibly. The differences that matter are in what surrounds the relay, not in the relay itself.

## Ant Media Server: for when latency itself is the product

Ant Media Server earns a place on this list when ultra-low latency broadcast turns out to be the sharpest pain point in a product. I mean sub-second, the kind of urgency where the gap between something happening on camera and a viewer seeing it is itself the feature, not an incidental property of the system. Picture a motion-alert-to-viewer scenario: an event triggers on a camera, and the entire value of the product is measured by how fast a human can see that event and react to it. Shave a few hundred milliseconds off that path and you've materially changed what the product can promise a customer.

That's a purpose-built case, and Ant Media is a purpose-built tool for it. If a product's core value proposition depends on closing that gap as tightly as possible, it deserves direct evaluation against your actual latency budget, measured on real hardware and real network paths, not a vendor's best-case number. If a product's viewers can tolerate the latency profile of a well-run general SFU, which is already low by the standards of anything outside WebRTC, there's no need for a tool that specializes in shaving the last few hundred milliseconds further. General-purpose fan-out done well, the subject of the previous two posts, already covers that ground.

The trap here runs in both directions, and it's worth naming both sides of it. A team with a real sub-second requirement that settles for a general SFU will ship a product that quietly underperforms its own promise, and won't necessarily notice until a customer times the gap themselves and asks why it's slower than expected. A team without that requirement that adopts a specialist ultra-low-latency tool anyway takes on a narrower, more specialized piece of infrastructure, with a smaller community and fewer integration patterns already worked out, for a latency improvement nobody downstream actually needs. Neither mistake shows up on day one. Both show up months later, as either a support ticket you can't answer or an operational cost nobody remembers signing up for.

## What "specialist" actually buys you

It's worth being specific about why a tool like Ant Media can hit that latency target when a general SFU, built on the same fundamental relay architecture, can't get quite as low. The gap comes from decisions made throughout the stack in service of one goal: buffering strategy, how aggressively the system pushes frames out ahead of waiting to smooth out jitter, and how much tolerance the pipeline has for the kind of network variance that a general-purpose SFU is built to absorb gracefully. A tool tuned for latency above all else makes different tradeoffs at each of those decision points than a tool tuned for broad robustness across a wide range of network conditions and use cases. That's a real design choice with real consequences, not a marketing distinction, and it's why a specialist tool earns its place only when the workload actually calls for what those choices optimize for.

## Janus: for when video and telephony have to coexist

Janus is the right call in one specific situation: a team also needs SIP or telephony hybrid alongside video. SIP is the signaling protocol behind most traditional telephony and PBX systems, and Janus has real, mature support for bridging that world with WebRTC. If part of a platform needs a live camera feed to interoperate with a phone system, a dispatch console, or any SIP-based voice infrastructure, Janus is built for exactly that bridge in a way none of the other tools on this list are.

That's a narrow, specific need, and it's worth being clear about how narrow. If nothing in your architecture touches SIP or legacy telephony, Janus doesn't earn its place over LiveKit or mediasoup on general merits. You'd be adopting a tool for a capability you're never going to exercise, and carrying its particular quirks and operational surface for nothing in return.

I bring this one up specifically because it's the case most likely to get argued into a general-purpose decision on the strength of a single feature. Someone on the team has used Janus before, knows its SIP bridging works well, and pushes for it as the default media server even though nothing else about the platform touches telephony. That's the same mistake as picking a tool for its GitHub stars. This time it's dressed up as domain expertise, but the underlying error is identical. A team's familiarity with a tool's strongest feature doesn't make that feature relevant to the workload in front of them.

## The decision framework, not the feature chart

Here's how I'd actually run this evaluation, in order, before ever opening a tool comparison spreadsheet or reading a benchmark thread.

- Does anything need to touch the media in flight: mixing, recording, computer-vision hooks? If yes, you're in Kurento and OpenVidu territory, and the pipeline weight is the price of admission for a real requirement, not a design mistake.
- Is the core job fan-out at scale, one or many sources to many viewers, with no in-flight processing at all? If yes, you're choosing between LiveKit and mediasoup, and the default is LiveKit unless a team specifically wants to own more engineering in exchange for a lower CPU floor.
- Is sub-second latency a defining requirement of the product, not a nice-to-have sitting somewhere on a feature list? If yes, look hard at Ant Media before assuming a general SFU will get you there on its own.
- Does the platform need to bridge with SIP or legacy telephony? If yes, Janus is the tool built for that bridge, and nothing else covered in this series does it as well.

Notice what's absent from that list: adoption numbers, star counts, which tool a conference talk happened to be hyping this year. None of that tells you whether a tool fits your workload. The only input that actually matters is what your system has to do, asked plainly, before you look at a single feature comparison. Ask the workload question first, every time, even when the pressure is to move fast and just pick something with momentum behind it.

## Tying the run together

Across this run of five tools, the pattern repeats at every layer. Kurento and OpenVidu answer "does the media need to be touched in flight." LiveKit and mediasoup answer "how much of the distributed-systems engineering do you want to own, and how much CPU headroom do you need per participant." Ant Media answers "is sub-second latency the product." Janus answers "does this also need to be a phone system." None of those five tools is competing to be the best media server in the abstract, because there's no such prize to win. Each is competing to be the best fit for one specific shape of problem, and most platforms only have one or two of those shapes to solve for at any given time.

The expensive mistake isn't picking a mediocre tool. It's picking a truly excellent one for a problem you don't actually have, and then discovering the problem you do have six months into a build that assumed the wrong architecture from day one. Ask what the workload demands first. The tool comparison chart is useful only after you already know which rows of it you're allowed to ignore.
