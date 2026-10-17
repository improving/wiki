---
title: "Are We in Normal Science or a Revolution?"
type: "Source Summary"
description: "AI's unresolved normal-science-versus-paradigm-shift debate should push organizations to hedge forecasts and build for uncertainty."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/are-we-in-normal-science-or-a-revolution/are-we-in-normal-science-or-a-revolution.md"
---

# Are We in Normal Science or a Revolution? — Summary

**Original source**: `references/devlinliles.com/are-we-in-normal-science-or-a-revolution/are-we-in-normal-science-or-a-revolution.md`

## Summary

The AI field is in an unresolved argument about whether it is in Kuhn's normal science or a paradigm shift, and the answer determines whether investment theses and safety architectures rest on solid ground. Scaling laws (Kaplan et al., 2020) looked like normal science, but Chinchilla shifted the constants and emergent capabilities documented jumps the curve did not predict. Anomalies — persistent hallucinations, brittleness, task-specific gains — are accumulating. The prescription is to build for both: hedge forecasts with conservative estimates, build evaluation infrastructure that detects unexpected capability changes, and update safety architecture each model generation.

## Key Claims

- Kaplan et al. (2020) showed model performance was predictable from three variables: compute, data, and parameters.
- Chinchilla (2022) showed prior models were significantly compute-suboptimal, shifting constants without breaking the framework.
- Emergent capabilities appeared to phase-transition rather than interpolate; Schaeffer et al. (2023) challenged this as a possible measurement artifact.
- Persistent anomalies include hallucinations despite scale and RLHF, brittleness to small perturbations, and task-specific capability gains.
- Under uncertainty, hedge extrapolation with conservative estimates and build infrastructure to detect unexpected capability changes.

## Relevance

Informs [emergent capabilities](/concepts/emergent-capabilities.md) and [capability forecasting](/concepts/capability-forecasting.md), arguing for [evaluation harnesses](/concepts/evaluation-harness.md) that detect surprise capability changes.

## Quality

Practitioner blog post by Devlin Liles. Strong synthesis of named papers and Kuhn's framework; it is an interpretive argument rather than new evidence, and the Kuhn analogy is applied loosely.

## Entities Mentioned

- [OpenAI](/entities/openai.md) — source of the 2020 Kaplan et al. scaling-laws paper

## Concepts Covered

- [Emergent Capabilities](/concepts/emergent-capabilities.md) — behaviors the scaling curve did not predict
- [Capability Forecasting](/concepts/capability-forecasting.md) — the extrapolation now made dangerous
- [evaluation harness](/concepts/evaluation-harness.md) — infrastructure to detect unexpected capability changes
