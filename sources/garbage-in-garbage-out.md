---
title: "Top 10 Reasons AI Projects Fail #3: Garbage In, Garbage Out"
type: "Source Summary"
description: "Bad data makes AI confidently wrong; run readiness assessments, data contracts, and CI quality gates before modeling."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, data, improving.com]
sources:
  - "references/improving.com/garbage-in-garbage-out/garbage-in-garbage-out.md"
---

# Top 10 Reasons AI Projects Fail #3: Garbage In, Garbage Out — Summary

**Original source**: `references/improving.com/garbage-in-garbage-out/garbage-in-garbage-out.md`

## Summary

AI systems amplify whatever data they learn from, so incomplete, stale, or biased inputs produce confident wrong answers at scale. Teams often assume better modeling can compensate for messy inputs and burn weeks on manual cleanup instead of fixing the source. The post argues data quality must be measured, monitored, and enforced with the same rigor as code quality, long before modeling begins.

## Key Claims

- "Models can be trained on anything… and they'll underperform, or worse, mislead," with telltales of endless feature-wrangling and outputs that look confident but fail on edge cases.
- Poor data quality erodes trust: once business users see inconsistent or biased outputs, adoption drops and confidence is hard to regain.
- Four causes: incomplete lineage, inconsistent refresh cycles, bias in collection or labeling, and reactive manual cleanup.
- Run a data readiness assessment for coverage, timeliness, consistency, lineage, and bias before committing to scope.
- Establish data contracts defining schemas, acceptable ranges, and update cadences so upstream systems cannot silently break downstream models.
- Automate quality gates in CI/CD so missing, stale, or out-of-range data fails fast.
- Where data is weak, limit exposure with RAG, source citation, or constrained use cases, and red-team data and prompts for bias and hallucination.
- Example: a parts-forecasting app narrowed to SKUs with at least 18 months of history and enriched through a vendor API, improving accuracy dramatically.

## Relevance

Connects [data quality](/concepts/data-quality.md), [data readiness](/concepts/data-readiness.md), [data contracts](/concepts/data-contract.md), and [data lineage](/concepts/data-lineage.md) to [AI bias](/concepts/ai-bias.md) and mitigation via [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md).

## Quality

Practitioner advice by Devlin Liles (Improving CCO); concrete and example-backed, though part of a vendor series.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author, Improving CCO
- [Improving](/entities/improving.md) — publisher and delivery firm

## Concepts Covered

- [data quality](/concepts/data-quality.md) — accuracy, completeness, consistency
- [data readiness](/concepts/data-readiness.md) — whether data is fit for AI
- [data contract](/concepts/data-contract.md) — enforceable schema, ownership, and SLOs
- [data lineage](/concepts/data-lineage.md) — tracing origin and transformation
- [AI bias](/concepts/ai-bias.md) — systematic unfairness from data and objectives
- [retrieval-augmented generation](/concepts/retrieval-augmented-generation.md) — grounding outputs when data is imperfect
