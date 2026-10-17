---
title: "protection harness"
type: "Concept"
description: "A set of automated gates that check artifacts between workflow steps and refuse those that fail them."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, quality, workflows, automation]
sources:
  - "/sources/the-engineers-evolution-stage-4-designing-and-governing-the-workflow.md"
  - "/sources/the-product-teams-evolution-stage-4-designing-the-system-that-decides.md"
  - "/sources/the-project-managers-evolution-stage-4-governing-the-delivery-system.md"
---

# protection harness

A protection harness is a set of automated gates that check artifacts between workflow steps and refuse any that fail them, moving checking out of human heads and into the pipeline. Across this corpus it is the defining move of Stage 4, where a team stops inspecting every step by hand and lets its velocity compound.

## Key Claims

- A protection harness automates gates so humans stop inspecting every step; it is only as good as its weakest gate.
- A weak gate stamps a blind spot across every generated artifact, and can pass everything while hiding quietly slipping projects.
- Teams should automate the simplest workflows first, prove the gates hold, then earn their way up to harder ones.
- Status-integrity gates reconcile reported status against live delivery signals.
- A focused four-to-six person Stage 4 team can outpace an eight-to-ten person team.
- Non-technical practitioners cap at advising on team-built workflows rather than building the harness themselves.

## Related

- [Quality Gates](/concepts/quality-gates.md) — the individual checks a harness composes
- [Review Gate](/concepts/review-gate.md) — the hand review this replaces
- [Competency Floor](/concepts/competency-floor.md) — the floor the harness raises
- [The Engineer's Evolution, Stage 4](/sources/the-engineers-evolution-stage-4-designing-and-governing-the-workflow.md) — primary source
