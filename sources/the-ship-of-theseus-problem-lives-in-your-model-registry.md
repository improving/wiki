---
title: "The Ship of Theseus Problem Lives in Your Model Registry"
type: "Source Summary"
description: "Silent model updates mean the model you validated may not be running; treat model identity as an operational variable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-ship-of-theseus-problem-lives-in-your-model-registry/the-ship-of-theseus-problem-lives-in-your-model-registry.md"
---

# The Ship of Theseus Problem Lives in Your Model Registry — Summary

**Original source**: `references/devlinliles.com/the-ship-of-theseus-problem-lives-in-your-model-registry/the-ship-of-theseus-problem-lives-in-your-model-registry.md`

## Summary

Uses the Ship of Theseus to name a governance gap: providers ship "silent updates" that change model weights without incrementing the version pinned in your code, so the model you validated last quarter may not be the model in production. Identity continuity — knowing that "this model" is the same entity across time — underpins compliance evidence, reproducibility, and trust, and most enterprises aren't governing it.

## Key Claims

- GPT-4-turbo in May 2024 and November 2024 share a name but not identical weights; the endpoint name stays the same while behavior drifts.
- Azure OpenAI formalizes retirement dates for GA models, and deployments set to "upgrade when expired" can be auto-upgraded to a replacement model you didn't explicitly choose.
- Over 70% of researchers report being unable to reproduce another group's findings — before provider weight changes are even factored in.
- The structural fix: pin at model-version level (not endpoint alias), log the resolved model version on every inference, and require a re-evaluation cycle before any version change reaches regulated production.
- No industry consensus exists on when fine-tuning, instruction tuning, or a new RLHF signal turns a base model into a genuinely different artifact.

## Relevance

Core material for [AI governance](/concepts/ai-governance.md) and [version pinning](/concepts/version-pinning.md): it ties [model drift detection](/concepts/model-drift-detection.md) directly to the [audit trail](/concepts/audit-trail.md) regulated systems need.

## Quality

Practitioner blog post by Devlin Liles. Strong framing and concrete platform detail (Azure OpenAI retirement and auto-upgrade). Caveats: the reproducibility figure is cited second-hand, and the fine-tuning threshold question is left openly unresolved.

## Entities Mentioned

- [OpenAI](/entities/openai.md) — named as a provider issuing silent updates
- [Anthropic](/entities/anthropic.md) — named as a provider issuing silent updates
- [Azure OpenAI](/entities/azure-openai.md) — platform that formalized retirement and auto-upgrade behavior
- [SOC 2 Type II](/entities/soc-2-type-ii.md) — auditor context for tracing a decision to a specific model state

## Concepts Covered

- [version pinning](/concepts/version-pinning.md) — pin the model version, not the endpoint alias
- [audit trail](/concepts/audit-trail.md) — record the resolved model version for every inference event
- [model drift detection](/concepts/model-drift-detection.md) — detecting behavior change under a stable name

## Related Sources

- [Coalition First, Regulator Second](/sources/coalition-first-regulator-second.md)
