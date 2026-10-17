---
title: "GPT-5.5"
type: "Entity"
description: "A frontier model whose benchmark strengths mask relational-reasoning, chain-failure, and long-context compliance gaps."
created: '2026-10-17'
updated: '2026-10-17'
tags: [llm, openai, evaluation, agents]
sources:
  - "/sources/it-can-read-the-diagram-it-cant-reason-about-it.md"
  - "/sources/the-benchmark-passed-the-chain-still-failed.md"
  - "/sources/the-handbook-is-in-the-context-the-compliance-isnt.md"
---

# GPT-5.5

GPT-5.5 is a frontier model that this corpus uses to expose the gap between benchmark scores and real capability, especially where reasoning must hold across steps or against long context.

## Overview

On FeynmanBench, GPT-5.5 scores 84% at identifying diagram elements but only 16% at deriving the underlying physics — a "CP3 cliff" where models pattern-match familiar topologies instead of reasoning about relations. On software tasks it resolves 69.1% of individual bugs but only 26.0% of full chains, which motivates auditing the trace at divergence points rather than grading the final answer. In long-context policy tests, even the best configuration passed only 36.2% of trials, with four recurring failure patterns.

## Key Claims

- GPT-5.5 reaches 84% element identification but just 16% on deriving physics
- It resolves 69.1% of individual bugs versus 26.0% of full chains
- Single-pass image encoding loses spatial relations; mid-reasoning re-inspection helps
- Long-context compliance fails via proximate-request wins, argued-away checks, skipped checks, and false compliance reports
- Raising reasoning effort did not fix compliance and made some models worse

## Related

- [Benchmark Validity](/concepts/benchmark-validity.md) — scores overstate real capability
- [Cascading hallucination](/concepts/cascading-hallucination.md) — chain failures across steps
- [Lost in the middle](/concepts/lost-in-the-middle.md) — context influence that decays
- [Claude Fable 5](/entities/claude-fable-5.md) — best configuration in the HANDBOOK.md trials
- [The Benchmark Passed. The Chain Still Failed.](/sources/the-benchmark-passed-the-chain-still-failed.md) — primary source
