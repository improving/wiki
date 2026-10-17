---
type: Reference
title: "Every Stage Logged Green While Acme Corp Split in Two"
resource: "https://www.devlinliles.com/every-stage-logged-green-while-acme-corp-split-in-two/"
author: "Devlin Liles"
published: '2026-10-07'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I ran a legal-ops pipeline once that ingested sixty vendor contracts into a knowledge graph through five stages: parse, extract, resolve, classify, embed. I seeded the contracts with deliberately inconsistent party naming on purpose, the same vendor showing up as "Acme Corp" in one contract, "Acme Corporation" in another, and "ACME CORP INC" in a third, specifically so the entity-resolution stage would have real work to do.

## The problem

The pipeline as I first built it collapsed all five stages into one monolithic ingest function with exactly one final status: complete or failed, nothing in between. Then I introduced a bug that anyone who has run a real pipeline will recognize on sight. Entity resolution only ran on documents ingested in the first batch, the exact kind of mistake that happens when a fix ships to part of a fleet before it reaches the rest.

Here is what makes this failure instructive. Parsing succeeded. Extraction succeeded. Classification succeeded. Embedding succeeded. Every single stage logged green, and green in this pipeline carried exactly one meaning: the function returned without raising an exception. Whether the data coming out of that stage was actually correct was a separate question that green never answered. Those are two different claims wearing the same color, and the gap between them is where the damage happened. "Acme Corp" and "Acme Corporation" landed as two separate nodes in the graph. Per-vendor obligation totals came out wrong, because the totals for one real vendor were now split across two graph entities that had no idea they were the same company. Nothing in the pipeline's own logs ever suggested a problem existed, because nothing in the pipeline was checking for this specific kind of problem. I measured a duplicate-entity rate of at least twenty-five percent of known name-variant pairs left unresolved, against a ground-truth mapping I kept alongside the sixty contracts specifically to catch this.

The uncomfortable lesson sitting underneath that number is that a pipeline reporting success and a pipeline doing its job are two separate claims, and a monolithic ingest function can only ever report the first one. It has no seam anywhere in it where a stage could stop and say "the data I just produced doesn't meet the bar," because there was never a bar defined stage by stage in the first place. The whole pipeline either finishes or it throws, and contamination that doesn't throw an exception sails straight through.

## The pattern

The fix keeps the same five stages. What changes is treating each one as a genuinely separate, monitored unit instead of five sequential function calls hiding inside one chain. Parse, extract, resolve, classify, and embed each run as distinct steps, and the resolve stage specifically has to report a resolution rate against a minimum-expected-match threshold before classify or embed are allowed to run at all.

I ran the identical injected bug, resolution silently skipped for the first batch, against this version, and this time the resolve-stage gate caught it immediately. The affected batch got held and flagged before contamination ever reached classification or embedding. The duplicate-entity rate dropped to near zero, against the twenty-five-plus percent from the monolithic version, and the stage-by-stage trace showed the resolve stage flagged red for the affected batch instead of falsely green.

What makes this work is a simple discipline: giving each stage its own opinion about whether it did its job, instead of letting one final status speak for all five. A stage that can only say "ran" or "didn't run" is a stage that cannot tell you anything useful about the quality of what it produced. A stage that reports a specific health signal, a resolution rate compared against a threshold in this case, gives the next stage in line a reason to refuse the handoff.

## Design considerations

A real limitation here is that a threshold can only see what it was written to check for. A resolution-rate gate catches a stage that broke completely, the case where an entire batch's worth of resolution silently never ran. It is a coarser instrument than what I would need to catch a resolution stage that ran, reported a resolution rate comfortably above threshold, and still left a handful of name-variant pairs unmerged because the matching logic itself made an imperfect call on a few edge cases. A threshold answers one question: did this stage do its job at a level worth trusting. A separate question, did this stage get every individual case right, sits outside what any threshold can tell you, and conflating the two is how a team ends up trusting a gate more than it deserves.

That gap is a different problem from what this pattern solves, and it needs a different fix: a dedicated entity-resolution technique, applied at the exact point where an entity is about to be written, catching the individual mismatches a rate threshold is structurally blind to. The staged-gate pattern and a dedicated resolution technique answer different-grained questions, one about the batch, one about the individual record, and a production system handling anything at real scale probably needs both.

There is also a calibration decision buried in choosing the threshold itself, one to revisit rather than set once and forget. Set the resolution-rate bar too strict and batches get halted on noise, legitimate edge cases that were never going to resolve cleanly regardless of how good the matching logic is. Set it too loose and the exact blind spot this pattern exists to close comes right back, just with an extra step in between that gives false comfort. The right number depends on how clean the source data actually is, which changes over time as new suppliers and formats enter the pipeline.

The last thing I would say plainly: this pattern costs you pipeline latency and operational complexity you did not have before. Five monitored stages with gates between them take longer to run and more code to maintain than one function that just does the work. That cost pays for itself exactly when contamination that slips through is expensive to find later and expensive to unwind once it has propagated. If your downstream consumers can tolerate the occasional bad record and correct it cheaply when it surfaces, the monolithic version might genuinely be the right amount of engineering for the problem you actually have.
