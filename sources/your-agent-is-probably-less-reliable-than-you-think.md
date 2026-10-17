---
title: "Your Agent Is Probably Less Reliable Than You Think"
type: "Source Summary"
description: "Reliability is a system property: chained agent steps compound errors, so shorter chains and quality gates beat per-step accuracy."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/your-agent-is-probably-less-reliable-than-you-think/your-agent-is-probably-less-reliable-than-you-think.md"
---

# Your Agent Is Probably Less Reliable Than You Think — Summary

**Original source**: `references/devlinliles.com/your-agent-is-probably-less-reliable-than-you-think/your-agent-is-probably-less-reliable-than-you-think.md`

## Summary

The post argues that the dangerous assumption in agentic AI is not hallucination but the belief that good per-component performance yields good system performance. Invoking Lusser's Law — series reliability is the product of component reliabilities, not the average — it shows how errors compound across multi-step agent chains. Because reliability is a property of the architecture rather than any single model, the responses are shorter chains, parallelization, and real quality gates that break error propagation.

## Key Claims

- Lusser's Law: a series chain of 95%-reliable components is 59.9% reliable by step 10 and crosses the coin-flip line by step 14.
- An agent at 98% per step over 20 steps succeeds only 67% of the time; raising per-step accuracy to 99% still yields just 82%.
- The only ways to raise system reliability are shortening the chain, parallelizing what can be parallelized, and adding checkpoints that catch and recover from failures.
- ICML 2025 multi-agent resilience work found adversarial inspector agents placed after each primary agent produced high recovery rates by breaking propagation rather than raising per-step accuracy.
- 2025 long-horizon research found that when a model's context contains its own earlier errors, it becomes more likely to make further errors — errors recruit the model to defend them.

## Relevance

Directly informs [Lusser's Law](/concepts/lussers-law.md), [error propagation](/concepts/error-propagation.md), [quality gates](/concepts/quality-gates.md), and [task decomposition](/concepts/task-decomposition.md) as design levers for agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. The reliability math is standard and checkable; the cited 2025 research is summarized without links, so those findings should be treated as secondhand.

## Entities Mentioned

- [Robert Lusser](/entities/robert-lusser.md) — formalized the series-reliability law the post is built on
- [John von Neumann](/entities/john-von-neumann.md) — applied the same principle to computing in a 1956 paper

## Concepts Covered

- [Lusser's Law](/concepts/lussers-law.md) — the mathematical core of the argument
- [Error Propagation](/concepts/error-propagation.md) — how faults compound through a chain
- [Quality Gates](/concepts/quality-gates.md) — interruption points that stop propagation
- [Task Decomposition](/concepts/task-decomposition.md) — shorter chains with explicit handoffs
