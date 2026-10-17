---
title: "The Data Doesn't Pick the Model"
type: "Source Summary"
description: "Quine–Duhem underdetermination maps onto model architecture choices, whose baked-in assumptions benchmarks can't adjudicate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/the-data-doesnt-pick-the-model/the-data-doesnt-pick-the-model.md"
---

# The Data Doesn't Pick the Model — Summary

**Original source**: `references/devlinliles.com/the-data-doesnt-pick-the-model/the-data-doesnt-pick-the-model.md`

## Summary

Quine and Duhem argued that empirical evidence underdetermines theory: multiple incompatible theories fit the same observations. The post maps this onto applied AI — a standard transformer, a sparse mixture-of-experts transformer, a Mamba-style state space model, and hybrid SSM-attention designs score comparably at equal parameter counts, so architects choose on non-empirical grounds like inference cost, theoretical priors, hardware, and expertise. Those choices bake in assumptions the training data cannot correct, producing architecture-specific failure modes and portability risk.

## Key Claims

- Comparable benchmark scores at equivalent parameter counts mean the evaluation data does not strongly discriminate between major architecture families.
- Every architectural choice is an implicit claim: attention assumes pairwise token relations across arbitrary distances, tokenizer choice assumes a granularity, context window assumes how much history matters, positional encoding assumes sequence geometry.
- Different architectures fail differently — a state space model handles long documents cheaply but may miss non-local patterns that attention catches, so debugging a failure may mean interrogating an architectural assumption rather than the training data.
- Portability risk: workflows tuned to one model's assumptions may not translate to a different architecture even at equal aggregate benchmark scores.
- The "best model" is selected on non-empirical grounds (inference cost, safety evaluations, human preference data, output formatting) because the training signal does not uniquely determine the representation.

## Relevance

Informs [model selection](/concepts/model-selection.md) and [benchmark validity](/concepts/benchmark-validity.md); argues for evaluation tasks specific enough to stress the assumptions a workflow depends on.

## Quality

Practitioner blog post by Devlin Liles. A clear, faithful application of Quine–Duhem; largely conceptual with no empirical measurements, and the architecture-equivalence claim is asserted rather than demonstrated.

## Entities Mentioned

- None.

## Concepts Covered

- [model selection](/concepts/model-selection.md) — the non-empirical grounds on which architectures are chosen
- [benchmark validity](/concepts/benchmark-validity.md) — why scores don't adjudicate architectural assumptions
