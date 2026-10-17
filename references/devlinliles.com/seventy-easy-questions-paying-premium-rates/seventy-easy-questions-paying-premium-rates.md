---
type: Reference
title: "Seventy Easy Questions Paying Premium Rates"
resource: "https://www.devlinliles.com/seventy-easy-questions-paying-premium-rates/"
author: "Devlin Liles"
published: '2026-10-10'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I ran a hundred requests through an internal help-desk triage agent, the kind of thing that answers whatever an employee types into the IT support channel. Seventy of those requests were trivial: what's the guest wifi password, how do I request a new monitor, where's the VPN setup guide. Twenty were medium, needing a bit of actual reasoning about which of several plausible causes applied. Ten were genuinely hard, the kind of multi-log root-cause question where you have to trace a failure across several systems before you can even name what's actually wrong.

Every one of those hundred requests ran through the same fixed reasoning budget, 4,096 thinking tokens, regardless of which bucket it belonged to. That number had been chosen the way these numbers usually get chosen: big enough to comfortably handle the hard cases, applied uniformly because nobody had built a mechanism to apply it selectively.

I measured cost and latency per request, tagged by the true difficulty label I'd seeded into the set, and the picture was almost embarrassing once I looked at it directly. The seventy trivial requests were burning the identical 4,096-token budget as the ten hard ones, and getting no accuracy benefit from it whatsoever. Accuracy on the trivial bucket was already sitting at its ceiling with a small fraction of that budget. The guest wifi password question didn't need four thousand tokens of reasoning to answer correctly. It needed a lookup and a sentence. The other three thousand-plus tokens weren't buying anything except a bigger bill on the seventy percent of requests that made up the bulk of daily volume.

## The pattern

The fix inserts a cheap classifier ahead of the main reasoning call, and its only job is to tag each incoming request as easy, medium, or hard before anything expensive happens. That classification runs on a much smaller budget than the main call, since deciding "is this trivial or not" is a far cheaper judgment than actually answering a hard multi-log question. Once a request is tagged, it routes to a budget matched to that tier: minimal or zero reasoning tokens for easy, a moderate allocation for medium, the full budget for hard.

Running the same hundred requests through this version routes at least ninety of them to their correct true-difficulty tier, and the seventy trivial requests that used to burn the full budget now burn a fraction of it, with no measurable drop in their already-high accuracy. Average cost per request across the full hundred drops by forty percent or more compared to the flat-budget version. Accuracy on the ten genuinely hard requests, the ones that still get the full budget, holds at the same level it held before, because those are the requests this mechanism was never trying to shortchange.

What makes this a different pattern than calibrating a single reasoning ceiling is the shape of the workload it's solving for. A calibrated ceiling answers "how much budget does this one task type need." This pattern answers a different question: given a mixed population of requests with genuinely different difficulty, how do you avoid paying the hard-case price on every easy case just because they arrived through the same endpoint. The classifier is what makes that possible. Without it, you're stuck choosing one budget for a population that actually needs several.

## Design considerations

The classifier's own accuracy is the load-bearing assumption underneath the entire mechanism, and it deserves more scrutiny than it usually gets. If the classifier misroutes a genuinely hard request into the easy tier, that request now gets a fraction of the reasoning budget it actually needed, and the accuracy loss on that one request is the exact failure this pattern was supposed to prevent. Routing ninety percent of requests correctly, which is the number I hit, still means one in ten gets tagged wrong. Whether that's an acceptable rate depends entirely on what a misrouted hard request costs downstream. A wrong triage guess on a slow VPN connection is an annoyance. A wrong triage guess that shortchanges a security-relevant multi-log investigation is a different category of mistake, and I'd want a much higher classifier accuracy, or a fallback path that lets a request escalate to a higher tier mid-flight, before trusting this pattern on anything with those stakes.

The tier boundaries themselves are a real design decision, not something the data hands you automatically. Three tiers worked here because the underlying request population actually clustered into three reasonably distinct difficulty bands. A different workload might need two tiers, or five, or a continuous budget scaled off a difficulty score rather than a discrete bucket. Forcing a workload that doesn't naturally cluster into your chosen number of tiers just relocates the misclassification problem from "easy versus hard" to "which of five arbitrary buckets does this belong in," which isn't actually a simpler problem.

There's a caveat from recent research I'd rather state directly than leave for someone else to discover the hard way. Some studies of reasoning models have found that past a certain complexity threshold, more reasoning budget stops helping and accuracy can fall off outright rather than simply plateauing. That complicates the core assumption this pattern depends on, that more budget reliably buys the same or better accuracy as difficulty increases. If your hard tier includes requests that sit past that threshold, giving them the "full" budget isn't actually guaranteed to produce the accuracy you're routing them there to get. This pattern also only implements one of several strategies for deciding when to reason at all; a classifier making the call up front is a different approach than letting the model decide for itself whether a given step needs deeper reasoning, and the choice between them isn't free of tradeoffs either way.

The place I'd skip this pattern entirely is a workload that's already reasonably uniform in difficulty. Building a classifier, validating its accuracy, and maintaining the tier-routing logic is real ongoing engineering work, and if seventy percent of your traffic isn't dramatically easier than the rest, there's no lopsided cost gap here to recover. The value is proportional to how skewed the difficulty distribution actually is. A help desk fielding mostly password resets and the occasional genuine outage is exactly the shape this pattern was built for. A workload where every request needs roughly the same amount of thought isn't.
