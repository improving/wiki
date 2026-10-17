---
type: Reference
title: "The Backward Rerun - Attribution for a Failure Three Weeks Late"
resource: "https://www.devlinliles.com/the-backward-rerun-attribution-for-a-failure-three-weeks-late/"
author: "Devlin Liles"
published: '2026-10-15'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

I ran a three-agent inventory-reordering chain, forecast, supplier-selection, order-placement, over a sixty-day simulated retail scenario. On day twelve, the supplier-selection agent picked a cheaper supplier with a longer lead time for a key SKU. Every node scored well at the moment it acted. The forecast looked reasonable. The supplier choice matched the cost-optimization rubric it was graded against. The order got placed correctly. Nothing about that day-twelve decision looked wrong under a per-node quality check, because a per-node check only ever grades what's visible at the moment of handoff.

The longer lead time caused a stockout on day thirty-four, three weeks later. Across ten scenarios, each with a documented delayed cause, the rate at which the system correctly named the true causal node came out to zero percent, because nothing in that version of the pipeline ever went back and re-examined an earlier decision once a delayed failure got flagged.

## The problem

A decision that looks fine when it's made can still be the exact cause of a failure that only shows up much later. That's the structural problem with grading a pipeline at the moment each step hands off. A per-node score is a snapshot, and a snapshot can't see forward in time. The supplier-selection agent's choice was, by every metric available to it on day twelve, a good decision. It optimized cost the way it was supposed to. The information that would have made it look bad, that the longer lead time would leave no buffer against a demand spike three weeks out, didn't exist as a scoreable fact at the moment the decision was made. Day thirty-four is what turned a cost-optimal choice into the cause of a stockout.

This is a different failure mode from a node simply doing bad work. The node did its job correctly by every standard available to it in the moment. The problem is that "correctly by the standard available in the moment" and "actually the cause of a downstream failure" are two different claims, and any attribution mechanism that only ever looks at the moment of handoff will keep missing the second one entirely, no matter how good its rubric is.

## The pattern

When a flagged outcome occurs, I re-execute the chain backward from the outcome: counterfactually substituting or removing candidate causal nodes at checkpointed states, then checking whether the outcome still occurs in replay. Concretely, that meant checkpointing state at every node-day of the sixty-day simulation, then taking day twelve's supplier choice, swapping in the alternate supplier with the shorter lead time, and re-running the remainder of the simulation from that checkpoint forward. If the day-thirty-four stockout stops happening once I make that one substitution, I've found the cause. If it keeps happening, I move to the next candidate node and test again.

A ranking step orders the candidate nodes by how much swapping each one actually changes the outcome. That ranking is what turns a list of plausible candidates into a single answer: the node whose removal does the most work. On the same ten scenarios, this got the delayed-cause identification rate to eighty percent or better, against the zero percent baseline where nothing ever looked backward at all.

I log a `replay_compute_cost` metric on purpose: the number of counterfactual re-runs a given scenario needs before the ranking step converges. Causal replay works by actually re-running the simulation, which costs real compute for every candidate tested, and I want that cost sitting in the open on the same dashboard as the benefit, visible to anyone reviewing the project, instead of tucked out of a slide that only shows the win.

The technique itself isn't something I invented in isolation. AgenTracer, a 2026 attribution model, trains itself against the same causal-intervention logic: re-run a multi-agent trajectory with a candidate step swapped and check whether the failure persists. For them that's a training procedure for a learned model. For me it's a live system mechanism I run directly against my own checkpointed state, no separate model required, at the moment an outcome gets flagged.

## Design considerations

The replay approach tests one candidate node at a time, and that's a real limit on what it can find. A 2026 paper on minimal repair families shows, formally and with actual measurement, that pointwise attribution can't distinguish a jointly necessary cause from an alternative singleton cause. My replay pattern finds the single node responsible for a delayed failure. It has no mechanism for finding two nodes that are each individually harmless and only fatal together. If the true cause of my stockout had been a combination of the day-twelve supplier choice and a separate, smaller forecasting error on day twenty that neither substitution alone would fix, this pattern would test each one in isolation, find that neither swap alone prevents the stockout, and conclude, wrongly, that neither is the cause. I haven't built the fix for that gap yet. I know it exists, and I know exactly which failures it would miss.

The compute cost is the second real tradeoff, and it scales with how many candidate nodes and checkpoints exist between the flagged outcome and its plausible origins. A sixty-day simulation with three agent types per day gives a bounded, manageable search space. A longer chain with more branching decision points would multiply the number of counterfactual re-runs needed before the ranking step converges, and at some point that cost has to be weighed against just accepting a lower-confidence attribution from a cheaper method. I don't think there's a universal answer to where that line sits. It depends on how expensive a wrong attribution is downstream, since a system that writes a wrong judgment into a live registry is a worse outcome than one that spends more compute getting the judgment right first.

The pattern also only runs when triggered by a flagged outcome, never on a continuous schedule, and that's deliberate. Checkpointing every node-day costs almost nothing. Re-running the simulation forward from a checkpoint with a substitution costs real compute every time, and doing that proactively for every decision, on the chance it might someday matter, would turn a diagnostic tool into a standing tax on every run whether or not anything ever goes wrong. I pay the replay cost only once I already know something went wrong.
