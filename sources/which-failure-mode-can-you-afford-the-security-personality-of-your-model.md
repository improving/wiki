---
title: "Which Failure Mode Can You Afford? The Security Personality of Your Model"
type: "Source Summary"
description: "Frontier models fail in distinct patterns, so model selection should match a model's failure profile to what the compliance environment can absorb."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, security, devlinliles.com]
sources:
  - "references/devlinliles.com/which-failure-mode-can-you-afford-the-security-personality-of-your-model/which-failure-mode-can-you-afford-the-security-personality-of-your-model.md"
---

# Which Failure Mode Can You Afford? The Security Personality of Your Model — Summary

**Original source**: `references/devlinliles.com/which-failure-mode-can-you-afford-the-security-personality-of-your-model/which-failure-mode-can-you-afford-the-security-personality-of-your-model.md`

## Summary

Using the Sonar leaderboard study of 4,000+ Java coding tasks, the author argues that frontier models have distinct "security personalities" — characteristic patterns of failure that don't track overall capability scores. The right [model selection](/concepts/model-selection.md) question is not which model is better but which failure mode your compliance environment can absorb, evaluated with task-specific profiling rather than a leaderboard ranking. He pairs static defect data with [METR's](/entities/metr.md) PR-mergability findings to cover semantic correctness too.

## Key Claims

- GPT-5.2 High had the best security posture (16 blocker vulnerabilities per million lines) but the worst concurrency error rate (470 per MLOC, ~7x Gemini 3.1 Pro's 69).
- Claude Opus 4.5 Thinking reached 44 blocker vulnerabilities per MLOC (vs. Sonnet 4.5's 198) and the highest functional pass rate at 83.6 percent, but generated the most code, adding defect surface area.
- Gemini 3.1 Pro had middling vulnerability density (72 per MLOC) with the best concurrency reliability.
- Models within four points on SWE-bench Verified span a 12x range in security-critical defect density.
- [SOC 2 Type II](/entities/soc-2-type-ii.md) and the [EU AI Act](/entities/eu-ai-act.md) Annex III obligations make documented, task-specific selection rationale auditable.
- METR's March 2026 study found roughly half of 296 AI-generated PRs that passed automated grading would not have been merged, a ~24-point grader-versus-maintainer gap.

## Relevance

Reframes model selection as failure-profile matching for compliance, informing [model selection](/concepts/model-selection.md) and [benchmark validity](/concepts/benchmark-validity.md).

## Quality

Practitioner blog post by Devlin Liles. Rich with specific study figures; it depends on third-party benchmark studies and presents one author's interpretation of them.

## Entities Mentioned

- [METR](/entities/metr.md) — source of the PR-mergability study
- [EU AI Act](/entities/eu-ai-act.md) — Annex III obligations on selection documentation
- [SOC 2 Type II](/entities/soc-2-type-ii.md) — control requirements that make selection auditable

## Concepts Covered

- [Model selection](/concepts/model-selection.md) — the central decision the post reframes
- [Benchmark Validity](/concepts/benchmark-validity.md) — leaderboards mispredict task-specific failure profiles
