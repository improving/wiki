---
title: "SHAP"
type: "Entity"
description: "Shapley-value attribution method for explaining model outputs and allocating credit among jointly moving initiatives."
created: '2026-10-17'
updated: '2026-10-17'
tags: [explainability, attribution, statistics]
sources:
  - "/sources/black-box-ai-fails-webers-test.md"
  - "/sources/from-model-lift-to-the-p-l.md"
---

# SHAP

SHAP (SHapley Additive exPlanations) is a game-theoretic method that attributes a model's output to its input features using Shapley values. It is the best-known member of the post-hoc explainability toolkit, and in this corpus it appears both as an answer to explainability demands and as a fair way to split credit between initiatives.

## Overview

One post argues that black-box neural networks fail Weber's rational-legal test in regulated domains, because post-hoc XAI explanations can be plausible yet unfaithful to the model's actual process — the structural response being interpretable models or designed-in explanation layers. The other uses Shapley value decomposition to allocate credit fairly among jointly moving initiatives when turning model lift into a P&L number, warning that naive summing overstates portfolio impact by 30 percent or more.

## Key Claims

- Post-hoc XAI explanations can be plausible yet unfaithful to the model's process
- Explainability is an architecture requirement, not a compliance checkbox
- Shapley value decomposition fairly allocates credit among jointly moving initiatives
- Naive summing of initiative lifts can overstate portfolio impact by 30 percent or more
- Cannibalization, intermediate capture, and window misalignment eat the difference

## Related

- [Interpretability](/concepts/interpretability.md) — the broader requirement SHAP serves
- [Causal Lineage Map](/concepts/causal-lineage-map.md) — the alternative to feature attribution for value claims
- [Model-as-Judge](/concepts/model-as-judge.md) — another form of machine-generated evaluation
- [Black Box AI Fails Weber's Test](/sources/black-box-ai-fails-webers-test.md) — primary source
