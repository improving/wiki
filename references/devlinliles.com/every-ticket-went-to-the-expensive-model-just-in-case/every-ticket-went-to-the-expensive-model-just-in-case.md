---
type: Reference
title: "Every Ticket Went to the Expensive Model, Just in Case"
resource: "https://www.devlinliles.com/every-ticket-went-to-the-expensive-model-just-in-case/"
author: "Devlin Liles"
published: '2026-10-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

A freight-logistics operation I worked with handles shipment exceptions: customs holds, missed connections, damaged-goods claims. An assistant drafts a resolution for a human dispatcher to approve on each one. I ran 600 tickets through it, spanning a realistic distribution: a large majority of routine cases sitting next to a genuine minority of ambiguous multi-party disputes. Two model tiers were available, a cheap one running about two-tenths of a cent per ticket and a premium one running roughly fifteen times that. Every ticket, regardless of difficulty, went to the premium tier, under a policy that amounted to using the best model for everything, just in case something turned out to be hard.

Total spend scaled linearly with ticket volume instead of with actual difficulty. The premium tier's quality advantage got spent entirely on the roughly 70 percent of tickets the cheap tier would have resolved identically anyway. Nobody had done anything unreasonable to get here. Guessing difficulty in advance and routing accordingly sounds sensible until it turns out nobody was actually doing the guessing. The default became "send it to the good one," because building a mechanism to route cheaper felt like the riskier engineering choice compared to just paying for certainty on every single ticket.

That's the shape of the waste that shows up whenever a system defaults to its most capable, most expensive option out of caution rather than evidence. This failure hides in plain sight. Every ticket got resolved. Dispatchers approved recommendations at whatever rate they always did. The only thing wrong with the system was a number nobody was tracking closely enough: dollars spent per resolved ticket, measured against what the same quality bar would have cost if routine work had gone somewhere cheaper.

## The pattern

The fix sends every ticket to the cheap tier first. Its recommendation gets scored against a fixed quality bar, a lightweight check against the ticket's known-correct resolution class, and only the tickets that fail that check escalate to the premium tier for a second attempt. Escalation triggers only once a real attempt has produced measured evidence of failure. The decision gets made on what the cheap tier actually produced, after it runs, never on a guess made from the sidelines before anything ran.

Run the same 600 tickets through this version and total spend drops by at least 40 percent against the all-premium baseline, at an equal or better rate of passing the quality bar. The escalation rate tracks roughly the share of genuinely hard tickets in the workload, which is the whole point: the mechanism discovers which tickets are hard by watching them fail, and only pays the premium price for the ones that actually need it.

This pattern has the deepest paper trail behind it of anything I work with in this space. FrugalGPT, published in 2023, is its direct academic ancestor: a cascade of models with a learned scoring function that decides, after a cheap-tier call, whether to accept the answer or escalate, reporting cost reductions as high as 98 percent at matched quality against a frontier model. Azure AI Foundry's Model Router, generally available this year across more than two dozen models from multiple providers, ships this same retrospective-escalation shape with automatic failover as a platform primitive rather than something a team has to build from scratch. That tells me the shape is considered infrastructure now, the kind of thing a platform ships as a default rather than something a team has to invent on its own.

## Design considerations

I want to draw a hard line around something people keep confusing this pattern with, because the confusion is easy to fall into and it matters. Some routing approaches train a classifier on comparative data to predict, before any model call happens, whether a cheap or expensive model will produce an acceptable answer for a given query. That's a prospective decision, made before spending a cent. It's a genuinely different mechanism from what I've described here, which only ever escalates after a real attempt has already run and failed a check. Swap the training methodology out for a plain heuristic triage classifier in the prospective version and the same purpose survives untouched: decide the tier before spending on the expensive one. That purpose belongs to a different pattern entirely, one built around triage before any model tier gets chosen. The two get lumped together constantly because they both save money by routing across cost tiers, and they solve genuinely different problems. One decides ahead of time. This one decides on evidence.

The limitation that actually matters is the quality bar itself. This pattern only escalates on failures the quality check can catch. A cheap-tier answer that's confidently, plausibly wrong in a way the fixed check doesn't detect never escalates at all, and the system reports it as a routine success, indistinguishable from a genuinely correct cheap-tier resolution. The mechanism has no way of knowing it got fooled. That means the entire pattern's safety depends almost entirely on how good the quality-bar check actually is; the escalation logic sitting on top of it is the easy part by comparison. Building this without investing real effort into the check itself is building a system that looks like it's catching failures while quietly letting a category of them straight through.

There's also a volume-and-cost-gap threshold below which this pattern isn't worth the engineering. If the price difference between tiers is small, or if the overwhelming majority of a workload genuinely needs the expensive tier's capability, the escalation machinery adds complexity without much to show for it. The pattern pays off in proportion to how lopsided the actual difficulty distribution is and how large the price gap between tiers happens to be. A workload that's mostly routine, sitting on top of a meaningful price difference between a cheap and a premium tier, is exactly the shape this pattern is built for. A workload where almost everything is hard, or where both tiers cost about the same, doesn't have much slack for this pattern to recover.
