---
title: "The Capabilities Nobody Predicted"
type: "Source Summary"
description: "Emergent capabilities appear non-linearly at scale, so small-model pilots cannot forecast production behavior; plan with epistemic humility."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/the-capabilities-nobody-predicted/the-capabilities-nobody-predicted.md"
---

# The Capabilities Nobody Predicted — Summary

**Original source**: `references/devlinliles.com/the-capabilities-nobody-predicted/the-capabilities-nobody-predicted.md`

## Summary

Liles frames emergence as a structural problem for AI investment planning: models available for evaluation today may not predict the behavior of models deployed in eighteen months, because the capabilities that matter most appear suddenly and non-linearly at scales that cannot practically be tested ahead of time. He traces the debate from Wei et al.'s 2022 documentation of over 100 emergent tasks, through Schaeffer et al.'s argument that apparent cliffs are artifacts of discontinuous metrics, to a 2025 non-ergodic framework. The practical discipline: evaluate at scale when scale matters, use continuous metrics, and treat re-evaluation as a formal step in every model upgrade.

## Key Claims

- Tasks performed at near-random chance by 10B-parameter models jumped to high performance in 100B-parameter models, with in-context learning appearing as a phase transition.
- Schaeffer et al. argue emergence is often an artifact of exact-match scoring; switch to a continuous metric and the cliff flattens into a curve.
- If emergence is genuine, extrapolation from smaller models is unreliable — a small-model pilot is a lower bound, not a forecast.
- The safety implication is that dangerous capabilities could appear without appearing in any smaller evaluated model, the argument behind Anthropic's Responsible Scaling Policy.

## Relevance

Informs [emergent capabilities](/concepts/emergent-capabilities.md), [capability forecasting](/concepts/capability-forecasting.md), and [epistemic humility](/concepts/epistemic-humility.md) in AI planning and safety architecture.

## Quality

Practitioner blog post by Devlin Liles. Strength: even-handed treatment of both sides of the emergence debate with named papers; caveat: a synthesis piece with no original measurement.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — its Responsible Scaling Policy is cited as the safety argument for genuine emergence.

## Concepts Covered

- [Emergent Capabilities](/concepts/emergent-capabilities.md) — abilities appearing non-linearly at scale thresholds.
- [Capability Forecasting](/concepts/capability-forecasting.md) — why small-model pilots cannot predict production behavior.
- [Epistemic Humility](/concepts/epistemic-humility.md) — treating the current capability map as incomplete.
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — one of the abilities that appeared as a phase transition.
