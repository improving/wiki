---
title: "AI Evals Have a Replication Problem"
type: "Source Summary"
description: "AI evaluation repeats psychology's replication crisis: undisclosed prompts and drifting models make published benchmark scores unfalsifiable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/ai-evals-have-a-replication-problem/ai-evals-have-a-replication-problem.md"
---

# AI Evals Have a Replication Problem — Summary

**Original source**: `references/devlinliles.com/ai-evals-have-a-replication-problem/ai-evals-have-a-replication-problem.md`

## Summary

AI evaluation is repeating psychology's replication crisis. A November 2025 study of 640 LLM software-engineering papers found systematic gaps in artifact availability, environment specification, versioning, and documentation, while a separate study found only "same model, same prompt" reproduces reliably. The hidden variable is prompt engineering treated as undisclosed methodology: the exact prompt, sampling parameters, few-shot examples, and retry logic often *are* the score. Model drift closes the replication window further, since silently updated weights mean a Q1 score may describe a model that no longer exists by Q3.

## Key Claims

- A November 2025 study of 640 LLM software engineering papers (2017–2025) found persistent gaps in artifact availability, environment specification, versioning rigor, and documentation clarity.
- "Artifact available" badges do not guarantee execution fidelity or long-term reproducibility.
- "Same model, same prompt" reproduces reliably, but any variation in prompt framing, evaluation setup, or research group produces substantially lower consistency.
- A different prompt on the same model and benchmark can move performance by 20 percentage points or more.
- The capability claim does not travel; the conditions that produced a score are frequently not documented well enough to reproduce.

## Relevance

Informs [replication crisis](/concepts/replication-crisis.md) and [prompt engineering](/concepts/prompt-engineering.md), and argues for [evaluation harnesses](/concepts/evaluation-harness.md) built with [version pinning](/concepts/version-pinning.md) and [model drift detection](/concepts/model-drift-detection.md).

## Quality

Practitioner blog post by Devlin Liles. Strong analogy-driven argument citing specific studies and figures; the 20-point prompt sensitivity is stated without a named source, and the psychology parallel is illustrative rather than empirical.

## Entities Mentioned

- [Karl Popper](/entities/karl-popper.md) — invoked as the standard for what counts as falsifiable, reproducible evidence

## Concepts Covered

- [Replication Crisis](/concepts/replication-crisis.md) — the central parallel for AI evaluation
- [Prompt Engineering](/concepts/prompt-engineering.md) — framed as hidden, unreported methodology
- [evaluation harness](/concepts/evaluation-harness.md) — recommended as persistent, version-pinned infrastructure
- [Version Pinning](/concepts/version-pinning.md) — required to make evals reproducible
- [Model Drift Detection](/concepts/model-drift-detection.md) — re-running evals when model versions change

## Related Sources

- [Prompt Engineering Is Just Wittgenstein With a GPU](/sources/prompt-engineering-is-just-wittgenstein-with-a-gpu.md)
