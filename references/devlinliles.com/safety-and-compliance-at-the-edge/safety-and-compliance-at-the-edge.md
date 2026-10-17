---
type: Reference
title: "Safety and Compliance at the Edge"
resource: "https://www.devlinliles.com/safety-and-compliance-at-the-edge/"
author: "Devlin Liles"
published: '2026-09-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

PPE compliance monitoring and weapon detection sit in a different category from everything else in this arc. Recognition, which I covered in the last post, benefits from edge processing. PPE and weapon detection require it. There's no cloud-hybrid version of either use case that actually works, because the value both deliver comes entirely from running continuously, and continuous is not a word that survives a network round trip on every frame.

## Why continuous beats periodic

Start with PPE. Cameras watching for hardhats, high-visibility vests, gloves, safety glasses, and similar equipment show up primarily in construction, energy, and manufacturing, the industries where a missing piece of equipment turns an ordinary shift into an incident report. The detection itself isn't exotic computer vision. Object classifiers have been able to spot a hardhat for years. What makes it valuable is running that classifier on every frame, all shift, every day.

Compare that to how safety compliance has traditionally been checked: a supervisor walks the floor, or a compliance officer runs a scheduled audit. Both are snapshots. Both catch whoever happens to be out of compliance at the exact moment the check happens. Neither catches the worker who puts the hardhat on for the badge scan at the gate and takes it off ten minutes later once they're on the floor. That's not a hypothetical edge case. It's the single most common failure mode in PPE compliance, and it's structurally invisible to any audit that only samples a moment in time.

Continuous inference doesn't have that blind spot. It's watching the whole shift, not a sampled minute of it. The gap between what a spot-check can see and what continuous monitoring catches isn't a matter of degree. It's categorical. One approach can, by design, only ever catch a fraction of lapses. The other is built to catch all of them, bounded only by camera coverage and detection accuracy.

Some deployed systems extend this well past basic PPE, detecting helmets, vests, gloves, and masks alongside 50-plus categories of unsafe acts or conditions in real time. What I'd flag as the more interesting design constraint, separate from raw detection breadth, is that these systems are built to preserve worker privacy while doing it. They flag a compliance state, not an identity. The output is "person in zone 4, no hardhat detected," not a name attached to a face. That distinction keeps the system focused on the safety outcome it exists to produce, and it sidesteps a chunk of the privacy exposure I covered in the recognition post, since there's no PII payload riding along with the compliance signal.

That privacy-preserving framing also changes how the alert gets consumed downstream. A supervisor getting a "zone 4, no hardhat" notification can walk over and address it directly, without the system needing to have first identified who the worker is. The compliance system and any identity system, badge access, time clock, whatever else runs on the same site, can stay decoupled. If a company wants to correlate a compliance event with a specific worker for coaching or disciplinary purposes, that's a deliberate, human-initiated lookup against a separate system, not something baked into the detection pipeline by default. Keeping those two concerns separate is good architecture on its own merits, and it happens to be good privacy practice as a side effect.

One more operational detail worth planning for: alert fatigue. A continuous system watching an entire shift will generate more raw detections than a human audit ever would, simply because it's checking constantly, all day, every day. That's the whole point, but it means the alerting logic needs a sensible threshold, something like "no hardhat detected for more than N consecutive seconds in an active work zone." Firing on every single frame where a hardhat happens to be briefly out of view is the wrong tuning choice. Get that threshold wrong and you either drown the safety team in noise or tune the system so conservatively it misses real lapses. This is a tuning problem, not an architecture problem, but it's the kind of detail that determines whether a deployment actually gets used six months in.

## Weapon detection: same architecture, higher stakes

Brandished-weapon detection runs on the identical principle. Inference happens at the device, in real time, identifying a firearm the moment it becomes visible in frame and distinguishing it from other carried objects a person might reasonably have on them. The goal is to trigger deterrence or escalation immediately, not after review, because the entire value of the capability is measured in the seconds between a weapon appearing and a response beginning.

This shows up most acutely in schools, healthcare facilities, and retail environments, for reasons that don't need much explanation. But the underlying capability, knowing the moment a weapon appears on premises, generalizes to any site where an armed threat is a credible risk worth planning for. The specific vertical changes. The architecture doesn't.

Here's the part that doesn't get said enough in vendor pitches: reliable weapon detection needs adequately high resolution and frame rate to work. This isn't a minor spec footnote. A firearm in frame at low resolution, or captured at a frame rate too low to resolve motion cleanly, is a much harder detection problem than the same firearm captured clearly. Plenty of existing security camera deployments, especially older analog systems or budget IP cameras installed years ago for basic recording, simply don't have the image quality this use case demands.

That has a direct consequence for how you plan a rollout. Weapon detection isn't purely a software project you layer onto an existing camera estate. At specific chokepoints, entrances, hallways, anywhere a weapon detection zone actually needs to work, camera hardware may need to be upgraded first. Skipping that step doesn't make the project cheaper: it makes the detection unreliable in exactly the spots where reliability matters most, and you won't find out until the system misses something it was deployed to catch.

The escalation path matters as much as the detection itself. A weapon detection alert firing into an empty inbox, or into a dashboard nobody's watching at that moment, doesn't actually shorten anyone's response time. The value of the sub-second detection gets thrown away the instant it sits in a queue behind a human checking a screen every few minutes. The systems that actually work pair the edge detection with an escalation path built for immediacy: a push alert to whoever's carrying a radio or a phone on-site, a direct line to a monitoring center that's staffed to react, or an automated lockdown trigger for the specific zone involved. Design the response chain with the same urgency you designed the detection latency for, or the latency gain never reaches anyone who can act on it.

## The spine of it

Both PPE and weapon detection make a stronger case for edge-first design than almost any other category in this series, and the reason comes down to what happens when you take the edge away. With most other edge CV use cases, moving inference to the cloud costs you latency or adds a privacy question you have to answer. With PPE and weapon detection, moving to a periodic or delayed model doesn't just degrade the system. It defeats the reason the system exists. A PPE check that only samples occasionally will always miss the ten-minutes-later hardhat removal. A weapon detection system that reviews footage after the fact isn't detection anymore, it's forensics, and forensics doesn't stop anything from happening.

My recommendation has two parts. First, treat continuous, local inference as non-negotiable for both categories. Don't accept an architecture that trades continuity for cost savings or simplicity, because the trade isn't a modest one. It's giving up the entire point of the capability. Second, treat camera resolution and frame rate as an explicit line item you verify before committing to a weapon-detection rollout, not an assumption baked into the budget. Walk the site, check the actual camera specs at the actual chokepoints that matter, and price in any hardware upgrade before you promise a go-live date. Finding out the image quality isn't sufficient after the system is live is a far more expensive conversation than having it during planning.

The next post in this arc takes on the piece of edge CV that still doesn't have a clean answer: following the same person across multiple camera views without relying on facial recognition to do it.
