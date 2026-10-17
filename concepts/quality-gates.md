---
title: "Quality Gates"
type: "Concept"
description: "Validation checkpoints at pipeline transitions that stop a bad value before it becomes the next step's input."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, reliability, delivery]
sources:
  - "/sources/approved-except-nobody-could-say-which-gate-approved-it.md"
  - "/sources/automation-is-a-professional-obligation-not-an-optimization.md"
  - "/sources/from-ci-cd-to-the-intelligence-operating-system.md"
  - "/sources/governance-is-not-overhead-it-is-the-engine-of-trust.md"
  - "/sources/proving-competency-at-every-stage-the-eight-stages-of-ai-maturity.md"
  - "/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md"
  - "/sources/stacking-errors-the-hidden-math-that-makes-governance-non-optional.md"
  - "/sources/technical-debt-is-a-chronic-condition-not-a-single-decision.md"
  - "/sources/the-8-stage-ai-trust-evolution-a-map-for-the-journey.md"
  - "/sources/the-engineers-evolution-stage-4-designing-and-governing-the-workflow.md"
  - "/sources/the-intelligent-software-factory.md"
  - "/sources/the-machine-is-learning-to-build-itself-you-still-have-to-decide-what-to-build.md"
  - "/sources/the-standards-that-scale-from-code-quality-to-ai-governance.md"
  - "/sources/the-woodshop-to-factory-transition-why-stage-3-is-not-a-small-step.md"
  - "/sources/unidirectional-quality-gates-in-ai-assisted-development-the-ratchet-pattern.md"
  - "/sources/when-small-mistakes-compound-building-systems-that-survive-imperfect-ai.md"
  - "/sources/your-agent-is-probably-less-reliable-than-you-think.md"
  - "/sources/your-ci-cd-pipeline-is-already-cognitive-scaffolding.md"
---

# Quality Gates

A quality gate is a validation checkpoint placed at a pipeline transition: it asks whether a value is sane as the *next* step's input and forces a branch — pass and continue, or fail and hold for review. Across this corpus, gates are the recurring answer to compounding error, whether in CI/CD pipelines, ALM stations, or agent chains. Catching a defect early is cheap; catching it late compounds cost.

## Key Claims

- Individually accurate steps can still produce a confidently wrong output, so gates belong at every handoff.
- Reliability compounds multiplicatively: ten steps at 95% accuracy yield only ~60% end-to-end, and at 85% per step a 20-step pipeline drops below 5%.
- A single collapsed "approved" status hides which gate failed; persisting per-gate traces with evidence dropped attribution loss from 100% to zero on wrongly funded loans.
- A protection harness is only as good as its weakest gate, and each Stage 4 harness automates gates so humans stop inspecting every step.
- The ratchet pattern records each metric's floor in a checked-in file so quality can only improve, though it works only on measurable metrics and is subject to Goodhart's law.
- Governance infrastructure is the AI equivalent of automated tests; quality is the structure work happens within, not a phase.

## Related

- [Stacking Errors](/concepts/stacking-errors.md) — the compounding math gates defend against
- [Lusser's Law](/concepts/lussers-law.md) — why series reliability is a product
- [human approval points](/concepts/human-approval-points.md) — the human variant of a gate
- [Audit Trail](/concepts/audit-trail.md) — persisting per-gate evidence
- [protection harness](/concepts/protection-harness.md) — automating gates at Stage 4
- [Quality Gates at Every Transition](/sources/quality-gates-at-every-transition-stopping-a-bad-value-before-it-becomes-the-next-steps-input.md) — primary source
