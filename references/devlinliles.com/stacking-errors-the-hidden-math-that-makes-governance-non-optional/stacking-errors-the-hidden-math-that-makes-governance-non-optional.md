---
type: Reference
title: "Stacking Errors: The Compounding Math Behind AI Governance"
resource: "https://www.devlinliles.com/stacking-errors-the-hidden-math-that-makes-governance-non-optional/"
author: "Devlin Liles"
published: '2026-06-16'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

Trust in autonomous agents is an infrastructure question. You trust them when you have built the systems that make them trustworthy, and the reason that infrastructure is necessary comes down to one piece of math.

## The Math

Imagine a 10-step autonomous agent pipeline. Each step is a sub-task the agent executes independently, with 95% accuracy on each step. That sounds reasonably reliable. 95% is better than many human processes.

Here is what happens to the pipeline: `0.95^10 ≈ 0.60`

A 10-step pipeline where each step runs at 95% accuracy produces correct end-to-end results approximately 60% of the time. Extend the pipeline to 20 steps at 95%: `0.95^20 ≈ 0.36`. Roughly one in three full pipeline executions completes correctly.

The agents are doing nothing wrong. This is the mathematics of chained systems: each step introduces an independent probability of error, and those probabilities multiply.

Reliability engineers have known this since the 1940s. Robert Lusser, working on German rocket programs during the Second World War, formalized what became known as Lusser's law: the reliability of a series system is the product of the reliabilities of its components. A rocket with thousands of parts, each individually dependable, still fails often, because the product of many numbers just below one is a number well below one. John von Neumann carried the idea into computing with his 1956 paper on synthesizing reliable organisms from unreliable components, which asked how to get dependable computation out of parts that individually fail. His answer, redundancy and checking, is the intellectual ancestor of every quality gate described below.

## Why This Changes the Governance Argument

The governance argument for autonomous agents is usually framed as risk management: we need oversight because AI can go wrong. That is true and insufficient, because it casts governance as friction, an overhead cost paid to manage a risk you hope never materializes.

The stacking errors math reframes governance as a capability enabler. Without quality gates between steps, a 10-step pipeline at 95% step-accuracy delivers 60% end-to-end reliability. With quality gates that catch and correct errors at each step, the effective step-accuracy approaches the gate's reliability, and the pipeline's end-to-end reliability rises dramatically. Governance, on this reading, is the mechanism that lets autonomy operate at the reliability level the organization requires.

## What Governance Looks Like at Each Step

For every autonomous pipeline that runs more than two or three steps, there should be a governance mechanism at each transition point. The type of mechanism depends on the step.

**Automated quality gate:** a rule-based or AI-based check that validates the output of a step against defined criteria before passing it forward. If the output does not meet the criteria, the pipeline pauses, logs the failure, and routes to recovery: retry, fallback, or human review.

**Structured output validation:** if a step produces data that the next step will consume, enforce a schema. Unstructured or malformed output that passes unchecked to the next step is the most common source of cascading failures.

**Confidence thresholds:** for steps where the agent produces a probabilistic output (a classification, a recommendation, a generated document), define the confidence level below which the output does not pass forward without review. A step that completes at 94% confidence when the threshold is 80% passes automatically. A step that completes at 60% confidence routes to human review.

**Human approval points:** for steps whose failure would be difficult to reverse, a message sent, a record updated, a transaction initiated, require explicit human approval before execution. These are reserved for the irreversible steps, never sprinkled across all of them.

## The 5-Step vs. 20-Step Pipeline Strategy

The stacking errors math suggests a design principle: prefer shorter, well-bounded pipelines with clear quality gates over longer pipelines that minimize human touchpoints.

A 20-step pipeline that runs autonomously from end to end sounds impressive. At 95% per-step accuracy, it delivers 36% reliable end-to-end results. A 5-step pipeline with a quality gate at each transition, designed to run the same 20-step work in four sequential executions, delivers the same total work with far better reliability.

This is the autonomy paradox. The pipelines that appear most autonomous, with the fewest human touchpoints and the longest chains, are often the least reliable and the hardest to debug when things go wrong. The pipelines that build structured checking into each transition are more reliable, more debuggable, and more trustworthy at the organizational level.

## Where the Argument Could Break

The math invites two serious objections. The first is that the independence assumption is wrong. Real pipeline steps do not fail independently: a bad input tends to fail at several steps, and a well-built step can absorb an upstream mistake. True. The model is a simplification, and what survives the simplification is the shape of the curve. Whether the exponent is exact or approximate, end-to-end reliability decays as chains lengthen, and nobody who has operated a long pipeline in production disputes the decay.

The second objection is that self-correction makes external governance unnecessary: have the agent check its own work, or have a second model verify the first. I agree, and that is governance. A verifier model is a quality gate. A self-consistency check is a confidence threshold. The argument was never for committees and sign-off meetings. It is for checking machinery between steps, and it does not matter whether the checker is a rule, a model, or a person, only that it exists and that its failure modes differ from the step it checks.

## The Organizational Implication

Teams that get bad results from autonomous agents and conclude that agentic AI does not work are usually experiencing the stacking errors problem. The agents are operating at their specified accuracy. The pipeline architecture is the problem: it was designed assuming that 95% per step means 95% end to end.

The fix is better governance infrastructure: quality gates, structured output validation, confidence thresholds, and human approval points at the right places. Governance is the engine of trust. Without the engine, the car does not move, and without governance, autonomous agents never reach the reliability the organization needs from them.
