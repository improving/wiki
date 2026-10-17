---
type: Reference
title: "Two Failure Modes in LLM-Generated Pull Requests: Capability-Gap and Scope-Discipline Haircuts in a Controlled 216-Run Evaluation"
resource: "https://www.devlinliles.com/two-failure-modes-in-llm-generated-pull-requests-capability-gap-and-scope-discipline-haircuts-in-a-controlled-216-run-evaluation/"
author: "Devlin Liles"
published: '2026-07-18'
fetched: '2026-10-17'
tags: [blog, devlinliles.com]
---

## Abstract

LLM-generated pull requests can fail mergeability review for two structurally distinct reasons. The first is a capability-gap haircut: the model cannot produce output that meets maintainer standards, even if it passes automated tests. The second is a scope-discipline haircut: the model produces functionally correct, test-passing output that exceeds the permitted diff envelope (size gates, file counts, banned patterns). These two failure modes are taxonomically distinct because they respond to opposite interventions. Capability-gap failures improve with better models and longer task horizons; scope-discipline failures worsen with more capable models on constrained tasks.

This paper tests both claims empirically. We ran 216 tasks across 24 enterprise-representative problems, 3 model tiers (high, mid, low) against an Anthropic provider, and 3 repetitions each, using devbox as the agent platform and a deterministic rubric grader for mergeability. The evaluation was designed to test the Cost-Adjusted Capacity (CAC) framework, which models the cost of a mergeable PR as dominated by an engineering verification tax rather than token spend.

The results confirm the verification-tax thesis: token spend is 0.1%–2.3% of total cost per mergeable PR across all task types and tiers. More importantly, they surface the scope-discipline haircut in sharp relief. All 25 mergeability failures were in the test-addition category; all 25 passed automated tests. The high tier performed worse than mid on these constrained tasks (47% vs. 53% merge rate), providing direct evidence that the two haircut types require different remediation paths.

## Experimental Setup

**Platform.** Devbox is an agentic development platform that accepts task specifications over an HTTP API, dispatches them to a configured LLM, and returns a diff for grading. It abstracts the agent scaffold, tool loop, and workspace management.

**Corpus.** 24 tasks drawn from a curated enterprise-representative set spanning four categories: 7 bugfixes (12–25 min human time), 6 features (40–110 min), 6 refactors (60–180 min), and 5 test-additions (28–60 min). Human-minutes are calibrated estimates from a senior engineer completing the task in a clean environment.

**Design.** Each task ran against three model tiers (high, mid, low) using Anthropic as the provider, with 3 repetitions per tier, for 9 runs per task and 216 total. Based on Anthropic's documented tier classification at the time of these runs (June 2026), high maps to an Opus-family model, mid to a Sonnet-family model, and low to a Haiku-family model.

**Grading rubric.** The mergeability bar is a maintainer standard: build passes, existing tests pass, lint is clean, diff stays within size gates, and no banned patterns (e.g., TODO comments). Tests passing is necessary but not sufficient. The rubric is deterministic, not a human judgment.

## Key Results

**Verification tax confirmed.** Token spend ranged from 0.1% to 2.3% of total cost per mergeable PR across all task types and model tiers. The CAC framework's central prediction — that human verification time dominates token cost — holds across the entire evaluation corpus. No task type or tier inverted this ratio.

**The scope-discipline haircut is real and tier-inverted.** All 25 mergeability failures occurred in the test-addition category. All 25 of those failures passed automated tests. The high tier's 47% merge rate on test-addition tasks was worse than the mid tier's 53%, despite the high tier having measurably better capability scores. More capable models produced more code and violated size gates more frequently, not less.

**Bugfix and feature tasks confirmed the capability model.** On bugfix tasks (12–25 human minutes), the high tier averaged 78% merge rate vs. 67% for mid and 44% for low, consistent with the CAC capability curve. Feature tasks (40–110 min) showed the predicted wall: merge rates declined steeply past the 28.7-minute conversion threshold, and tier differences compressed as task length increased.

**Refactor tasks showed a different pattern.** Refactors (60–180 min) were hardest for all tiers, with the high tier showing the most consistent advantage. This is consistent with the CAC framework's prediction that long, coherent tasks — where context and architectural judgment matter — are where premium tier capability earns its cost.

## Two Haircuts, Two Remediation Paths

The central finding is that the two failure modes require opposite interventions, and conflating them wastes resources in both directions.

Capability-gap failures (the model can't produce maintainer-quality code) improve with: better models, longer task horizons, more capable tiers, and improved scaffolding. The CAC framework accurately predicts which tasks sit in the capability-gap regime based on task length relative to the model's h₅₀.

Scope-discipline failures (the model produces correct code that overshoots the diff envelope) worsen with more capable models and improve with: explicit size constraints in the system prompt, pre-generation scope negotiation, diff budget enforcement at the tool level, and — counterintuitively — lower-capability models that generate less by default. A Haiku-family model on a constrained test-addition task may produce fewer size-gate violations than an Opus-family model, despite worse capability scores, because capability and verbosity correlate.

The practical routing implication: before selecting a model tier for a task, identify which failure mode is the binding constraint. Capability-gap tasks get the premium tier. Scope-discipline tasks get explicit constraints and potentially a mid or low tier. Conflating the two — using the premium tier on constrained tasks because "better is better" — is the error the test-addition results make concrete.

## Implications for the CAC Framework

The empirical results validate the CAC framework's core prediction across all four task categories while surfacing a refinement it did not anticipate. The framework models a single capability curve P(merge | t) derived from a mergeability factor D applied uniformly. The scope-discipline haircut is structurally different: it is not a capability shortfall but a constraint-following failure that intensifies with capability. A complete CAC model should parameterize the two haircut types separately, with D_capability for the gap between automated grading and maintainer judgment on quality, and D_scope for the gap attributable to diff envelope violations.

The practical upshot: cost per mergeable PR for test-addition tasks under size constraints is not well-modeled by the single-haircut CAC formula. Teams running significant volumes of constrained test-addition work should expect the actual cost to exceed the CAC prediction, because the premium tier's advantage is negative on the scope-discipline axis.

## Conclusion

Across 216 controlled task runs, the verification tax dominated token spend by a factor of 40x to 1,000x, confirming the CAC framework's central prediction. The scope-discipline haircut — observable only because the evaluation imposed explicit size gates — produced a tier inversion that standard capability benchmarks cannot predict and standard holdback designs would not surface. The two failure modes are real, distinct, and require different interventions. Treating model selection as a single dimension (better = more capable tier) misroutes investment on scope-constrained tasks. The routing decision belongs in the task classification layer, not the procurement decision.

---

*Related: Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs [Liles, 2026]. Sources: METR time-horizon methodology [Kwa et al., NeurIPS 2025]; SWE-Effi [Fan et al., 2025]; Constraint Decay [Dente et al., arXiv:2605.06445]; Verifier Tax [arXiv:2603.19328].*
