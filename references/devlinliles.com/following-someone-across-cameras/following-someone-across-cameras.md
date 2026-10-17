---
type: Reference
title: "Following Someone Across Cameras"
resource: "https://www.devlinliles.com/following-someone-across-cameras/"
author: "Devlin Liles"
published: '2026-09-02'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Every use case in this arc so far has had a clean answer. Recognition earns edge processing because the payload is time-sensitive and legally sensitive at once. PPE and weapon detection require continuous local inference because the alternative defeats the point entirely. Multi-camera re-identification is the one that doesn't resolve that cleanly, and I want to spend this post being honest about where the real difficulty sits, because it's not where most pitches put it.

The problem itself is simple to state. A camera at the loading dock sees someone leave its frame heading toward the warehouse entrance. A different camera covering that entrance needs to recognize that the person who just walked into its view is the same person, not a new individual. Do that reliably across a facility with dozens of cameras and you get something worth having: a continuous trajectory of movement through a site, built without a human ever having to manually stitch clips together.

## An approach that doesn't need a face

The way this gets solved doesn't have to run through facial recognition at all. Appearance-based re-identification matches a person across cameras using clothing color and texture, body shape and proportion, gait, any objects they're carrying, and the coarse spatial arrangement of those features relative to each other. None of that requires capturing or matching biometric facial data.

That's a meaningfully different position from the identity matching I covered two posts back. Facial recognition tells you specifically who someone is, matched against a name or a record. Appearance-based re-identification tells you that the person in this frame is probably the same person who was in that frame ninety seconds ago, without ever needing to know who they are. For a lot of the operational use cases this serves, tracking dwell time, understanding movement patterns through a facility, following a subject of interest through a building during an active incident, that's all the system actually needs. It doesn't need a name. It needs continuity.

That gap matters for anyone weighing privacy exposure against capability. A re-identification system built this way can operate on cheaper legal footing than one built on facial matching, because the data it's working with isn't biometric identity data in the same regulatory sense. It's still worth a compliance review, since jurisdictions vary on how they treat non-facial appearance tracking, but the exposure is a different order of magnitude from running facial recognition across an entire site.

It's worth being precise about what the two approaches actually give you, because they're not interchangeable and picking the wrong one for the job costs you either capability or unnecessary exposure. Facial recognition answers "who is this person," definitively, against a known record. Appearance-based re-identification answers "is this the same person as before," probabilistically, without ever resolving to a name. A retail loss-prevention program tracking a specific person of interest by name needs the first. A facility trying to understand how people flow through a floor plan, or a security team trying to maintain situational awareness on a subject during an active incident without needing to know their identity, only needs the second. Building the heavier, more exposed capability when the lighter one would do the job is a common overreach, and it's usually driven by not having framed the actual requirement precisely enough before selecting the tool.

## The part that's actually unsolved

Here's where I want to push back on how this capability sometimes gets sold. Detecting a person within a single camera's frame is a solved problem. Object detection and tracking within one field of view works well, has worked well for years, and isn't where the difficulty lives.

The hand-off is where it lives. The moment a subject leaves one camera's field of view and has to be re-acquired in another, the system is making a probabilistic match with less information than it had a second earlier, and the world doesn't cooperate. Someone walks behind a pillar for two seconds. A forklift or a truck passes between the camera and the subject at exactly the wrong moment. The subject briefly overlaps with someone wearing a similar jacket. Any of these can cause a tracker to swap two different people's identifiers, and it does this silently. The system doesn't flag "I'm not sure," it just picks an answer and keeps going, and the trajectory it's been building gets corrupted from that point forward without any obvious signal that it happened.

That's the detail that separates this from an engineering problem waiting on more compute. More compute helps with detection accuracy within a frame. It doesn't resolve the fundamental information gap at the moment of occlusion, when the system briefly has nothing to match against and has to guess based on what it saw before the gap. That's a harder problem than throughput, and it's the reason re-identification hasn't converged on a plug-and-play answer the way object detection or even recognition largely has.

Camera placement helps more than most teams expect, and it's usually cheaper to fix than the algorithm. Wide gaps between camera fields of view, blind corners, and choke points with only one viable camera angle all make the hand-off harder than it needs to be by giving the tracker less overlap to work with. A site designed with deliberate overlap between adjacent camera views, even a few seconds of shared coverage at each transition point, gives the re-identification system a much easier problem to solve than a site with hard cuts between camera zones. This is worth raising during the design phase of any deployment that depends on cross-camera tracking, because it's far cheaper to plan camera placement around this constraint up front than to retrofit coverage into a site that's already wired.

## What a sound architecture actually does with that

Given that the hand-off problem is real and not going away with the next hardware generation, the architecture question becomes what to do about it, not how to eliminate it.

Running the tracking and re-identification matching at the edge still matters here, for the same reason it's mattered throughout this arc: it means raw video never has to travel off-device for a task that's fundamentally about correlating movement, not archiving footage of faces. The strongest deployments I've seen combine local inference, the actual matching computation happening on-device or on a local server, with centralized management, monitoring, and analytics dashboards. Raw video stays local. What gets centralized is the derived signal: this trajectory, this event, this dwell time in this zone. The pixels don't need to make that trip, and keeping them local shrinks the same kind of privacy surface that matters everywhere else in this series.

But the piece that actually matters for reliability is what the system does at the moment of a hand-off failure. Treating every hand-off as successfully resolved, and building alert logic on top of that assumption, is the mistake. If a system is confident about a match it can't actually verify, and that confidence feeds directly into an automated alert or an automated action, you've built a system that will occasionally act on a wrong identity with the same certainty it acts on a correct one. Nothing downstream of that decision knows the difference.

The better design flags the break. When a tracker loses confidence at a hand-off, whether because of an occlusion, a lighting change, or an ambiguous match against multiple candidates, the right behavior is to surface that uncertainty for human review. Silently picking the most likely candidate and continuing as if nothing happened is the wrong call, even though it's the easier one to build. That's a small design decision with a large downstream effect. It's the difference between a system that degrades gracefully under real-world conditions and one that fails silently and tells everyone downstream it succeeded.

My recommendation is direct: architect for graceful degradation on hand-off failure. Build the human-in-the-loop fallback into the design from the start. Adding it later, after the first time a corrupted trajectory causes a false alarm or, worse, a missed one, means retrofitting judgment into a pipeline that's already been trusted to run without it. Re-identification is a useful capability, and it's mature enough to deploy today. It is not mature enough to trust blindly, and any deployment that treats it as a solved, always-correct input to an alerting pipeline is setting itself up for a failure mode nobody will notice until it's already caused a problem.

This arc has moved from general detection to recognition to continuous safety monitoring to the hard, still-unsolved problem of tracking identity across space. The next post shifts up a level again, into what a system can understand about behavior and workflow once it's looking at more than a single event in a single frame.
