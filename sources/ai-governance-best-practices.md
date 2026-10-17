---
title: "Five AI Governance Best Practices Every Enterprise Needs Before Production"
type: "Source Summary"
description: "Five controls to build before an agent reaches production: model cards, audit trails, drift monitoring, oversight, incidents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, governance, improving.com]
sources:
  - "references/improving.com/ai-governance-best-practices/ai-governance-best-practices.md"
---

# Five AI Governance Best Practices Every Enterprise Needs Before Production — Summary

**Original source**: `references/improving.com/ai-governance-best-practices/ai-governance-best-practices.md`

## Summary

Devlin Liles lists five controls every enterprise should have before an agent reaches production — model cards, automated audit trails, continuous bias and drift monitoring, engineered human-in-the-loop boundaries, and an AI incident response plan — and maps each back onto the four-layer governance architecture.

## Key Claims

- Maintain a model card (training data, evaluation, limitations, approver) built at deployment time, because the information is cheap to capture once and expensive to reconstruct.
- Automated audit trails should record inputs, outputs, model version, prompts, data sources, and initiator identity, so an investigation is a single query rather than a multi-week forensic exercise.
- Bias monitoring must be continuous and matched to how fast a deployment can shift; a check that runs only at launch is a launch gate wearing a monitoring label.
- Human oversight needs explicit thresholds, not sentiment: a building-products manufacturer auto-accepted predictions above 95% confidence, routed 70–95% to fast review, and sent below 70% to full manual review.
- AI incident response must assume the visible symptom is several steps downstream and provide a way to walk the chain backward; a ten-step pipeline at 95% per step is only about 60% reliable end to end.
- Most enterprises have a policy document and an ethics committee but no control that stops a bad agent action before it ships; incident response doubles as an audit of whether the other four were built.

## Relevance

Concrete controls inside [AI governance](/concepts/ai-governance.md) and [responsible AI](/concepts/responsible-ai.md), building [audit trails](/concepts/audit-trail.md), [model drift detection](/concepts/model-drift-detection.md), and [human-in-the-loop](/concepts/human-in-the-loop.md) [confidence thresholds](/concepts/confidence-thresholds.md). The backward-tracing requirement rests on [quality gates](/concepts/quality-gates.md).

## Quality

Practitioner checklist by Improving's Devlin Liles; specific and well-exampled, though it presumes the four-layer architecture laid out in his companion post.

## Entities Mentioned

- [Hugging Face](/entities/hugging-face.md) — source of the model-card format
- [Gemini](/entities/gemini.md) — the sample model card cited
- [Devlin Liles](/entities/devlin-liles.md) — author
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [AI governance](/concepts/ai-governance.md) — the main topic
- [responsible AI](/concepts/responsible-ai.md) — the practices realized
- [audit trail](/concepts/audit-trail.md) — automated evidence
- [model drift detection](/concepts/model-drift-detection.md) — continuous monitoring
- [human-in-the-loop](/concepts/human-in-the-loop.md) — engineered oversight
- [confidence thresholds](/concepts/confidence-thresholds.md) — routing by certainty
- [quality gates](/concepts/quality-gates.md) — catching errors near the source
- [AI bias](/concepts/ai-bias.md) — the drift being watched
