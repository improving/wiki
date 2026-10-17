---
type: Reference
title: "The Breakeven Point Nobody Was Watching For"
resource: "https://www.devlinliles.com/the-breakeven-point-nobody-was-watching-for/"
author: "Devlin Liles"
published: '2026-10-16'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

A media company I worked with generates automatic captions and summaries for its video archive using a per-minute-billed vendor API. That decision got made once, at launch, and never revisited. I modeled the company's actual 24-month growth: starting at 2,000 minutes of video a month and scaling to 180,000 minutes a month by month 24, as the archive and the licensing catalog behind it both grew. Two alternative hosting modes existed the entire time as cost models sitting on the shelf. A self-hosted option with a fixed monthly infrastructure cost plus a small per-minute compute cost. An on-premises option with a larger upfront hardware cost amortized monthly and near-zero marginal cost per minute after that. Neither one ever got evaluated against what was actually happening to volume.

Vendor-API cost scales linearly with volume. No ceiling, no discount curve, no mercy. By month 24, the company was paying well past the point where self-hosting, and eventually on-premises hosting, would have been cheaper, because nothing in the system ever surfaced that crossover to anyone who could act on it. I tracked cumulative overspend against the optimal hosting mode available at each month's volume, and it crossed the self-hosted breakeven point somewhere around month 10 to 14, then the on-premises breakeven point by month 20 or later. By month 24, that overspend was clearly positive and still climbing.

What makes this failure different from a bad initial decision is that the initial decision wasn't necessarily wrong. At 2,000 minutes a month, paying per-minute to a vendor was probably the right call. Building self-hosted infrastructure for that volume would have been over-engineering a problem that didn't exist yet. The mistake was treating that choice as permanent rather than as correct-for-now, and never building anything that would notice when "now" had changed underneath it.

## The pattern

The fix recomputes what each of the three hosting modes would cost at every simulated month's actual volume, tracks which mode is currently cheapest, and fires a logged re-evaluation event the moment the payback period for switching modes drops below a configured threshold, defaulted to six months, so the system stops continuing silently on the original mode like nothing had changed. The recompute surfaces the crossover, with the numbers behind it, to whoever owns that decision. Switching anything automatically falls outside its job.

Run the same 24-month volume ramp through this version and cumulative overspend against the optimal mode drops by at least half compared to the unmonitored baseline, because the re-evaluation events give someone a chance to act well before the gap has had years to compound. The payback-window threshold itself stays configurable rather than hardcoded, because how much certainty an organization wants before switching hosting modes is a real business judgment specific to that organization. A six-month payback window is a reasonable default, though plenty of other numbers would also be defensible.

The mechanism itself is almost boring by design, and that's the point. It's a monitoring service built on plain cost arithmetic, no model call involved. It runs against the volume trend, computes three numbers every period, and compares them. There's no reasoning model involved in deciding whether self-hosting has become cheaper than a vendor API this month. That's arithmetic. Treating it as a judgment call is part of how these decisions end up frozen at whatever they were when someone last looked.

## Design considerations

This pattern's real limitation is that it's a monitoring and alerting mechanism sitting next to the decision. Whoever owns the decision still has to make it. The pattern surfaces the crossover clearly, with the dollar amounts attached, but a re-evaluation event that nobody reads is functionally identical to never having computed the crossover at all. Building this pattern and stopping there gives an organization the information it needs and none of the institutional habit of actually checking. Skipping the second one quietly reproduces most of the original failure, just with better instrumentation attached to it.

The threshold itself deserves more scrutiny than a default number usually gets. A six-month payback window assumes the organization is comfortable committing engineering effort to a switch that pays for itself within roughly half a year. An organization under real budget pressure might want a shorter window, catching crossovers faster at the cost of more frequent re-evaluation churn. One with a slower internal process for approving infrastructure changes might need a longer window, because a six-month payback that takes four months to get approved and built has already eaten most of its own advantage before it ships. The number only becomes wrong if nobody adjusts it to match how fast the organization can actually act on what it learns.

There's also a volume-shape question this pattern assumes without stating outright: it works best against a workload that's actually growing or shrinking in a way that crosses real thresholds. A stable, flat workload that was correctly matched to its hosting mode at launch will run this recompute every period and never fire a single re-evaluation event. That silence is the correct outcome, evidence the workload never crossed a threshold rather than evidence the mechanism is idle. The pattern's value is proportional to how much a workload's volume is expected to move over the life of the system. A one-off internal tool with a fixed, small, predictable usage pattern doesn't need a recurring breakeven calculation watching over it. A growing product surface with volume that could plausibly 10x or 100x over a couple of years absolutely does, because the hosting decision that was right at launch has no reason to still be right by the time that growth shows up.
