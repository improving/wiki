---
title: "Black Box AI Fails Weber's Test"
type: "Source Summary"
description: "Regulated AI needs Weber's rational-legal legitimacy, which black-box neural networks and post-hoc XAI can't supply; design interpretability in."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/black-box-ai-fails-webers-test/black-box-ai-fails-webers-test.md"
---

# Black Box AI Fails Weber's Test — Summary

**Original source**: `references/devlinliles.com/black-box-ai-fails-webers-test/black-box-ai-fails-webers-test.md`

## Summary

Max Weber's rational-legal authority derives legitimacy from articulable rules applied transparently, and modern institutional governance is almost entirely built on it. AI systems making consequential decisions in regulated domains are asking for that same authority but mostly cannot supply it: neural networks are not inherently interpretable, and post-hoc XAI methods produce plausible explanations that may not reflect the actual decision process. Devlin calls this the XAI legitimacy trap and argues explainability must be an architecture requirement, designed in from model selection.

## Key Claims

- The EU AI Act entered into force in August 2024, with prohibited-system obligations from February 2025 and high-risk requirements binding August 2026; HR, credit, healthcare triage, and law enforcement are classified high-risk.
- Neural network decisions emerge from billions of parameters with no path mapping to a human-readable rule; only the full weights truly describe the mechanism.
- Post-hoc explanations (SHAP values, attention visualizations, saliency maps) are approximations and can be plausible without being faithful.
- Some regulated use cases should use genuinely interpretable models (gradient-boosted trees, logistic regression, rules) instead of black boxes.
- Where frontier capability is required, design the XAI layer alongside the model, test explanations for fidelity, and audit them as the model updates.

## Relevance

Central to [interpretability](/concepts/interpretability.md) as a governance requirement, and to [AI governance](/concepts/ai-governance.md) and [model selection](/concepts/model-selection.md) in regulated contexts.

## Quality

Practitioner blog post by Devlin Liles. Strong framing and concrete regulatory dates; the XAI-fidelity claim is asserted with reference to research rather than a specific citation.

## Entities Mentioned

- [EU AI Act](/entities/eu-ai-act.md) — the regulation imposing explainability and oversight
- [SHAP](/entities/shap.md) — an example post-hoc explanation method

## Concepts Covered

- [Interpretability](/concepts/interpretability.md) — the post's central demand
- [AI Governance](/concepts/ai-governance.md) — legitimacy and oversight obligations in regulated use
- [Model selection](/concepts/model-selection.md) — choosing interpretable models where appropriate
