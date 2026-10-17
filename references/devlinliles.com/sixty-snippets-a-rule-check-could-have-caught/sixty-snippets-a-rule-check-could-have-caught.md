---
type: Reference
title: "Sixty Snippets a Rule Check Could Have Caught"
resource: "https://www.devlinliles.com/sixty-snippets-a-rule-check-could-have-caught/"
author: "Devlin Liles"
published: '2026-10-12'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## The problem

I built a compliance review pipeline for marketing copy: two hundred snippets that need clearing before they can publish, checking for banned words, missing disclaimers, broken links, and the harder stuff that actually requires reading the copy and judging whether it's misleading. The version I started with sent every one of those two hundred snippets through the same path: a full model-judge call, reading the whole snippet and rendering a nuanced verdict, every single time, regardless of what was actually wrong with it.

Of the two hundred snippets I ran, sixty had a violation a plain rule check would have caught instantly: a banned word sitting right there in the text, a disclaimer that was supposed to appear and didn't, a link that resolved to a dead page. Thirty had violations that genuinely needed judgment, phrasing that was technically accurate but misleading in context, the kind of thing a keyword search will never flag. Ten were real edge cases where even a careful human reviewer would want a second opinion. The rest were clean.

Every one of those two hundred snippets paid for the same expensive judge call, including the sixty where the answer was sitting in plain sight the moment you checked for a banned word or a missing disclaimer. That's the part that bothered me once I actually measured it. I was paying full judgment-call cost and full judgment-call latency on cases that never needed judgment at all, on top of paying it for the cases that genuinely did. The total cost and time for the batch reflected the most expensive check available applied uniformly, whether the actual answer required that much scrutiny or none.

## The pattern

The fix reorders the pipeline into three stages, run in strict cost order, and only escalates a snippet to the next stage if the current one doesn't resolve it. A deterministic rule check runs first: regex and keyword matching against the banned-word list, a check for the presence of the required disclaimer, a link-resolution check. Anything that check catches gets flagged and stops right there. No judge call, no model inference, just a rule firing on a pattern it was built to catch.

Whatever passes the rule tier moves to a model judge, and only what passes the rule tier moves there. This is the stage that reads the snippet as a whole and asks whether it's misleading, whether the tone crosses a line the rule check has no way to detect, whether the claim being made actually holds up. That's where the thirty genuinely nuanced violations get caught, by a check that's actually built to catch them instead of being burned on the sixty that a keyword search already handled for free.

Whatever the judge flags as ambiguous, rather than clearly clean or clearly violating, escalates one more time to a human reviewer. In my build this was a scripted stand-in for that reviewer, but the principle holds regardless of who or what sits at that final stage: this is the most expensive tier in the pipeline, and it should only ever see the cases that genuinely need it. In my run, that was ten snippets out of two hundred, not two hundred out of two hundred.

Running the identical two hundred snippets through this version drops total review cost by more than half while holding the catch rate the same or better across all three categories of violation. Nothing about what counts as a violation changed. What changed is which stage caught it, and how much each catch cost to make.

## Design considerations

The order of the stages is the entire mechanism, and getting it backwards defeats the whole point. Running the judge first and using the rule check as a cheap sanity pass afterward saves nothing, because you've already paid for the expensive call before the cheap one ever runs. The savings only materialize because the cheap, deterministic check runs first and absorbs everything it's capable of absorbing before anything more expensive gets involved. This sounds obvious stated plainly, and it's exactly the ordering mistake I see teams make when they bolt a rule check onto an existing judge-based pipeline as an afterthought instead of designing the escalation path from the start.

The harder design question is where the line sits between what the rule tier catches and what has to escalate to judgment. A rule check is only as good as what it was built to detect, and every violation type that isn't expressible as a keyword match, a presence check, or a link resolution has to fall through to the judge tier by definition. That's a description of what a deterministic check can and can't do, and it's a real limit of the rule tier rather than a defect in the design. The design work is in building out the rule tier as far as it can reasonably go, catching every mechanically detectable violation type you can think of, so the expensive tiers are left with only the cases that genuinely require a more expensive kind of attention.

The confidence threshold that decides what the judge escalates to human review is a calibration question with real consequences in both directions. Escalate too readily and the human tier fills up with cases the judge could have resolved on its own, which erodes the entire cost argument for building this pipeline in the first place. Escalate too conservatively and genuinely ambiguous cases get a confident verdict from a judge that shouldn't have been confident about them, which is a worse failure than an expensive review, because it looks resolved when it wasn't. I'd rather tune that threshold by watching what the human reviewer actually overturns from the judge's calls than by picking a number that sounds reasonable in the abstract.

This pattern assumes the three tiers genuinely differ in cost, which is true for rule checks versus model judges versus human review, and that assumption should get checked before assuming it applies elsewhere. If your "cheap" tier and your "expensive" tier cost close to the same amount, tiering buys you very little, and the engineering effort of building and maintaining the escalation logic may not be worth what you get back. The value here scales with how lopsided the cost gap actually is between stages, and in this case the gap was large enough that catching sixty snippets for free, before anything expensive ever ran, was most of the win by itself.
