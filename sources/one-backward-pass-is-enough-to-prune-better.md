---
title: "One Backward Pass Is Enough to Prune Better"
type: "Source Summary"
description: "F-WANDA adds a single backward pass to WANDA pruning, using Fisher-style loss sensitivity to spend sparsity where the model can afford it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, other, devlinliles.com]
sources:
  - "references/devlinliles.com/one-backward-pass-is-enough-to-prune-better/one-backward-pass-is-enough-to-prune-better.md"
---

# One Backward Pass Is Enough to Prune Better — Summary

**Original source**: `references/devlinliles.com/one-backward-pass-is-enough-to-prune-better/one-backward-pass-is-enough-to-prune-better.md`

## Summary

WANDA prunes a model by multiplying each weight's magnitude by the norm of its incoming activation and cutting the smallest scores until half the weights are gone — one forward pass, no gradients, no fine-tuning. That proxy tells you how loud a weight is, not whether removing it moves the loss, and it hands every output neuron the same pruning budget. F-WANDA folds in a Fisher-style sensitivity estimate from a single backward pass, so neurons that looked identically prunable stop looking identical and the sparsity budget lands where the model can afford it.

## Key Claims

- Magnitude-times-activation is a proxy: a large-activation weight can be redundant and a small one can be load-bearing, and WANDA cannot distinguish them.
- One backward pass yields a read on how sensitive the output is to each weight, built from the loss rather than raw activation.
- WANDA's zero-gradient design let it prune a 70B model without a training cluster; fine-tuning recovery methods pay for accuracy with dozens or hundreds of calibration passes.
- F-WANDA spends one pass — costly versus zero, but near-free next to the alternatives, so the comparison stops being interesting.
- Preserved accuracy is accuracy nobody has to buy back later with a bigger model or longer recovery run; the saved inference cost is paid out over every request for the deployed model's life.

## Relevance

Informs post-training model compression and deployment economics; a standalone "other" piece rather than part of the observability or governance arcs.

## Quality

Practitioner blog post by Devlin Liles. Clear explanation of the pruning tradeoff; it makes no empirical accuracy claims and cites no specific benchmark numbers, so the argument is conceptual.

## Entities Mentioned

- None.

## Concepts Covered

- None.

## Related Sources

- [The Compression Cliff Nobody Budgeted For](/sources/the-compression-cliff-nobody-budgeted-for.md)
- [The Neuron Count Tell](/sources/the-neuron-count-tell.md)
