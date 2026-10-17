---
type: Reference
title: "You Can&#x27;t Improve What You Can&#x27;t Measure — Agentic Evaluation Done Right"
resource: "https://www.devlinliles.com/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right/"
author: "Devlin Liles"
published: '2026-08-20'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

# You Can't Improve What You Can't Measure — Agentic Evaluation Done Right

Most teams know their agent's average quality in the same way they know their own health without a doctor: by how it feels. The code usually looks right. The summaries are usually reasonable. Failures are noticed when a user complains, not when a metric crosses a threshold. This is not evaluation. It is hope.

Evaluation is the discipline of measuring agent behavior against defined criteria with enough rigor to catch regressions before users do, and enough signal to make routing decisions from data rather than intuition. It is Level 5 in the maturity stack: the point where you stop managing by feel and start managing by signal. It is also the precondition for everything in the improvement domain. You cannot close a feedback loop if you don't know where the loop starts.

## Grader types: building the right measurement layer

The mistake most teams make is reaching for human review as their first evaluation mechanism, because human review is the most familiar. It is also the most expensive, the slowest, and the one that doesn't scale. The right approach is a layered stack.

Structural graders are rule-based checks: does the output have the required fields? Is the token length in range? Do required keywords appear? They are fast, deterministic, and cost zero inference. They should run on every output, always. Their signal is limited to form rather than substance, but the cost of not running them is catching formatting failures through user complaints.

Code-validator graders go beyond keyword matching. Does the code compile? Do the tests pass? Is the schema valid JSON? For code-producing agents, these are the most important automated graders available. Compilation and test passage are objective signals that require no model judgment at all.

LLM-as-judge uses a separate language model to evaluate output quality against a prompt-defined rubric. It is strong for subjective output quality: reasoning soundness, whether the tone matches the channel, whether retrieved context was actually used. The risks are well-documented. Model-specific bias, positional bias (where the judge prefers the first option presented), and length bias (where longer outputs score higher regardless of quality) are all real. Calibration is required before you trust the results. Braintrust documentation recommends targeting 80% rank-order agreement between automated and human judges as a baseline.

Process Reward Models evaluate the quality of intermediate reasoning steps rather than final outputs. They require training data and are more expensive to build than a judge prompt. For long-horizon tasks where step-level errors compound before anyone catches them, they are more reliable than output-level evaluation alone.

Human evaluation is the ground truth. It is also expensive and slow. The right use is calibrating automated graders, establishing ground truth on new task types, and handling the high-stakes quality gates that automated methods cannot safely own.

## Evals-as-code

The most important structural practice in agentic evaluation is evals-as-code: evaluation definitions stored as version-controlled artifacts alongside the prompts and workflows they test. Graders, test cases, expected behaviors: all code.

Run the eval suite on every prompt change and regression detection comes free. You find out within minutes whether you broke anything, not after the next incident. Wire evals into CI and they stop being a manual step someone runs when they remember. Treat test cases as code and you can review coverage gaps in a PR the same way you'd review a missing branch in a unit test.

The test case taxonomy from the OpenAI Evals framework gives the right structure. Happy path covers the intended use case. Ambiguous input handles underspecified or contradictory requests. Edge cases hit boundary conditions. Adversarial cases cover prompt injection and contradictory instructions. Failure mode cases capture what happens when something external breaks, and mid-workflow failure cases test what happens when that break occurs partway through a multi-step task.

A test suite without adversarial cases is not production-ready. This is the coverage gap that shows up most often in teams deploying with confidence: they've covered the happy path and some edge cases, but they've never tested what happens when a user actively tries to manipulate the agent. That's exactly how they find out.

## The benchmark suite that matters for your task type

If you're building in areas with existing benchmarks, use them. They provide the comparative signal that tells you whether you're competitive, not just whether you've improved.

SWE-bench is the standard for software engineering and code generation. GAIA covers general agentic capability. MemoryAgentBench covers agent memory systems (documented in Post 5 of this series). AgentBench covers multi-environment agent performance, and FRAMES evaluates long-context retrieval and reasoning.

The caution: benchmark performance and production performance are not the same number. Benchmarks test specific capabilities on specific tasks; your users bring different distributions. Use benchmarks to validate that your foundation is solid, not as a substitute for production evaluation on your actual task distribution.

## A/B routing as evaluation infrastructure

The most actionable evaluation pattern for teams making changes to prompts or models is A/B routing: send a fraction of live traffic to the new variant, measure outcome delta against the current baseline, then promote or rollback based on results. This requires both execution infrastructure (routing live traffic, not just test cases) and enough patience to reach statistical significance before concluding.

The mistake teams make with A/B routing is concluding too early. The rule from conversion rate optimization is to run until you hit at least 95% confidence on a two-tailed test before calling it, and to pre-register your sample size target before launching rather than after. Concluding on insufficient samples either promotes a change that was actually neutral or rolls back one that was actually positive.

The payoff for doing this well is that you can make prompt and model changes with quantified risk rather than informed optimism. That is what it means to have an evaluation practice rather than an evaluation event.

---

*Sources: OpenAI Evals framework — test case taxonomy (happy path, ambiguous, edge case, adversarial, failure, mid-workflow failure); Braintrust documentation — LLM-as-judge calibration (80% rank-order target); Confident AI / DeepEval documentation — open-source eval metrics; SWE-bench (software engineering benchmark); GAIA (general agentic benchmark); MemoryAgentBench (2026); AgentBench; FRAMES (long-context benchmark); Augment Code agentic design pattern catalog (2026); Vellum agentic workflows guide.*
