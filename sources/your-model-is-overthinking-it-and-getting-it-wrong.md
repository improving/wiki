---
title: "Your Model Is Overthinking It — And Getting It Wrong"
type: "Source Summary"
description: "Extended thinking follows an inverted curve: extra reasoning tokens often signal confusion, so route tasks by complexity."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/your-model-is-overthinking-it-and-getting-it-wrong/your-model-is-overthinking-it-and-getting-it-wrong.md"
---

# Your Model Is Overthinking It — And Getting It Wrong — Summary

**Original source**: `references/devlinliles.com/your-model-is-overthinking-it-and-getting-it-wrong/your-model-is-overthinking-it-and-getting-it-wrong.md`

## Summary

The post maps Kahneman's System 1/System 2 dual-process theory onto LLM generation: standard single-pass token generation is System 1, and extended thinking (chain-of-thought, scratchpads) is the model's System 2. It argues more reasoning tokens do not yield more correct answers — wrong answers consistently accumulate more tokens than right ones, and accuracy peaks then declines past an optimal thinking length. The fix is task routing by complexity plus evals that measure accuracy per token spent.

## Key Claims

- Wrong answers in extended-thinking modes consistently use more reasoning tokens than correct ones; one study on AIME, HMMT, and GPQA found incorrect outputs averaged roughly 27,700 tokens versus substantially fewer for correct outputs.
- There is an optimal thinking length per problem that scales with difficulty; past the peak, extra tokens indicate the model has lost the thread while cost grows without bound.
- Production failure mode: enabling extended thinking on every API call triples latency, doubles inference cost, and degrades accuracy on simple tasks by second-guessing high-confidence completions.
- The remedy is task routing — classify requests by complexity, keep high-frequency low-complexity work on fast inference, reserve reasoning mode for multi-step or error-expensive tasks.
- The evaluation question is which tasks extended thinking improves and by how much: test the reasoning path against the direct path and measure accuracy per token.

## Relevance

Informs [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md), [model routing](/concepts/model-routing.md), and [token cost](/concepts/token-cost.md) tradeoffs in production LLM deployments.

## Quality

Practitioner blog post by Devlin Liles. The token-count figure comes from cited arXiv papers (given as IDs) but is reported secondhand, and the System 1/System 2 framing is an analogy rather than a mechanism.

## Entities Mentioned

- [Daniel Kahneman](/entities/daniel-kahneman.md) — source of the dual-process theory the post maps onto LLMs

## Concepts Covered

- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — the model's approximation of deliberate reasoning
- [model routing](/concepts/model-routing.md) — the proposed fix of routing by complexity
- [token cost](/concepts/token-cost.md) — the unbounded cost curve of extra reasoning tokens
