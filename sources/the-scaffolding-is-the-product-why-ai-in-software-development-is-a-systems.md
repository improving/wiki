---
title: "The Scaffolding Is the Product: Why AI in Software Development Is a Systems Integration Problem"
type: "Source Summary"
description: "LLM capability falls off on complexity like arithmetic, so differentiation lives in the engineering scaffolding around a commodity model."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems.md"
---

# The Scaffolding Is the Product — Summary

**Original source**: `references/devlinliles.com/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems/the-scaffolding-is-the-product-why-ai-in-software-development-is-a-systems.md`

## Summary

Devlin Liles argues that AI-assisted software development is a systems integration problem, not a model capability problem. Using an o3-mini multiplication heatmap, he shows LLM accuracy is near-perfect on small, well-represented problems and collapses on novel complexity, and that software follows the same curve: clean output for a React component, broken behavior for a 200-file service with undocumented business rules. General intelligence creates a commodity floor; differentiation lives in the scaffolding around the model, which converts 70% solutions into 95%.

## Key Claims

- Multiplication accuracy is 100% on small operands but falls to single digits by fifteen-digit multiplication; the model did not get less capable, it ran out of patterns to match.
- Research on grokking suggests models memorize first and only sometimes discover the underlying algorithm; for internet-scale models we cannot distinguish reasoning from retrieval.
- Correct answers with broken reasoning are common: in math the final number is right while intermediate steps are wrong more than half the time.
- Compositional generalization does not emerge from scale alone, an argument older than the current architecture (Fodor and Pylyshyn, 1988).
- Recurring scaffolding patterns: structured context and domain retrieval, [test-driven development](/concepts/test-driven-development.md) as the primary feedback mechanism, review shifted to intent alignment, CI/CD pipelines as verification gates, and feedback loops that capture learning the model cannot.
- Tool use does not defeat the argument: the calculator call, retrieval step, and verification harness are themselves scaffolding.

## Relevance

Central to [test-driven development](/concepts/test-driven-development.md) as the verification layer for generated code, and it informs [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) and the [evaluation harness](/concepts/evaluation-harness.md).

## Quality

Practitioner blog post by Devlin Liles. Strong use of a concrete benchmark figure and it answers counterarguments; the 70%/95% split is an illustrative heuristic, and the grokking claim is summarized rather than cited precisely.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author

## Concepts Covered

- [test-driven development](/concepts/test-driven-development.md) — test-first as the guardrail for generated code
- [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md) — feeding structured domain context
- [evaluation harness](/concepts/evaluation-harness.md) — CI/CD as verification scaffolding
