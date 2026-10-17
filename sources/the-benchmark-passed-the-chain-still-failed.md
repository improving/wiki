---
title: "The Benchmark Passed. The Chain Still Failed."
type: "Source Summary"
description: "Benchmark scores and majority votes miss chained failure; audit the reasoning trace at divergence points, not the final answer."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-benchmark-passed-the-chain-still-failed/the-benchmark-passed-the-chain-still-failed.md"
---

# The Benchmark Passed. The Chain Still Failed. — Summary

**Original source**: `references/devlinliles.com/the-benchmark-passed-the-chain-still-failed/the-benchmark-passed-the-chain-still-failed.md`

## Summary

Liles argues that the number that gets an agent deployment signed off — a model benchmark score or a per-task success rate with the environment reset between runs — does not describe what the model does across many steps with nothing reset. Four independent 2025-2026 research efforts on maintenance, retrieval, uncertainty, and multi-agent adjudication converge on the same prescription: stop grading the answer, start auditing the trace. The failure is a category error in what the tools measure, because confidence earned step by step compounds even when each step looks fine.

## Key Claims

- On ChainSWE's 304 issues across 54 Python projects, GPT-5.5 resolves 69.1% of individual bugs but only 26.0% of full chains; Claude-Opus-4.7 shows the same shape (64.5% vs 22.0%).
- UProp found existing uncertainty methods estimate only internal uncertainty, ignoring the extrinsic doubt a decision should inherit from everything before it.
- Majority voting assumes independent errors, but LLM agents share blind spots, producing "confabulation consensus"; AgentAuditor's trace auditing gained up to 5 points over majority vote and 3 over LLM-as-judge.
- The check must sit at divergence points inside the chain, not at the finish line, and be evidence-based rather than a headcount.

## Relevance

Central to [cascading hallucination](/concepts/cascading-hallucination.md) and eval design; bears on [compounding error](/concepts/compounding-error.md), [end-to-end success rate](/concepts/end-to-end-success-rate.md), and [model-as-judge](/concepts/model-as-judge.md).

## Quality

Practitioner blog post by Devlin Liles. Strength: synthesizes four cited papers with concrete figures and links to sources; caveat: the 2026 arXiv identifiers reflect a fast-moving, partly preprint literature.

## Entities Mentioned

- [GPT-5.5](/entities/gpt-5-5.md) — model whose per-bug vs full-chain gap is cited.
- [CHARM](/entities/charm.md) — framework naming and mitigating cascading hallucination.

## Concepts Covered

- [Cascading hallucination](/concepts/cascading-hallucination.md) — small early retrieval error becoming a confident wrong answer.
- [Compounding error](/concepts/compounding-error.md) — errors that accumulate across chained steps.
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — the chain-level metric that diverges from per-task success.
- [Model-as-judge](/concepts/model-as-judge.md) — the single-judge baseline AgentAuditor outperforms.
