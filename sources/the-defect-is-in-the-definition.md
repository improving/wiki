---
title: "The Defect Is in the Definition"
type: "Source Summary"
description: "Argues agentic failures trace to under-specified task definitions, and prescribes four explicit elements plus pre-execution validation."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-defect-is-in-the-definition/the-defect-is-in-the-definition.md"
---

# The Defect Is in the Definition — Summary

**Original source**: `references/devlinliles.com/the-defect-is-in-the-definition/the-defect-is-in-the-definition.md`

## Summary

The post argues that most agentic development failures trace back to weak task definition, not faulty execution: the agent did exactly what it was told, but what it was told was underspecified. Autonomy sharpens the penalty because a confident agent pursuing a misspecified goal produces irreversible actions, consumed budget, and downstream artifacts that must be unwound. It prescribes four explicit elements per task—goal, definition of done, out-of-scope boundaries, and assumptions—plus machine-readable formats and a requirements-validation gate before execution.

## Key Claims

- Late defect discovery costs 10x–100x more; autonomy multiplies that penalty through irreversible actions and consumed budget.
- A well-defined task states four things explicitly: what you want, how you'll know it's done, what's off-limits, and what you're assuming going in.
- Acceptance criteria in BDD Given/When/Then bake the definition of done into the task artifact, serving as both human-readable requirement and executable test specification.
- Machine-readable formats (OpenAPI, JSON Schema, Gherkin) give agents ground truth; prose specifications force interpretation and reintroduce ambiguity.
- Rule of thumb: if you can't write a test that fails when the requirement is violated, the requirement isn't defined well enough to execute.

## Relevance

Foundational for agentic delivery and task definition, especially [acceptance criteria](/concepts/acceptance-criteria.md) as an internal check rather than external review.

## Quality

Practitioner blog post by Devlin Liles. Grounded in an agentic design pattern catalog and named standards (OpenAPI, Gherkin), but the evidence is illustrative rather than empirical.

## Entities Mentioned

- [Augment Code](/entities/augment-code.md) — cited as source of the agentic design pattern catalog

## Concepts Covered

- [acceptance criteria](/concepts/acceptance-criteria.md) — central mechanism for encoding definition of done

## Related Sources

- [Coherent But Wrong - The Case for a Second Planning Checkpoint](/sources/coherent-but-wrong-the-case-for-a-second-planning-checkpoint.md)
