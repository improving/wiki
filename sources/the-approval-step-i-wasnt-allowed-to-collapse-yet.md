---
title: "The Approval Step I Wasn't Allowed to Collapse Yet"
type: "Source Summary"
description: "Collapsing a manager and compliance sign-off into one approval violated policy on over 70% of compliance-only cases; a fidelity checker blocked it."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-approval-step-i-wasnt-allowed-to-collapse-yet/the-approval-step-i-wasnt-allowed-to-collapse-yet.md"
---

# The Approval Step I Wasn't Allowed to Collapse Yet — Summary

**Original source**: `references/devlinliles.com/the-approval-step-i-wasnt-allowed-to-collapse-yet/the-approval-step-i-wasnt-allowed-to-collapse-yet.md`

## Summary

On an onboarding access-provisioning redesign, Liles tested collapsing a manager sign-off and an independent compliance sign-off into one combined approval. Ten of thirty-five synthetic cases had a compliance-only exception that a manager's context cannot encode, and the collapsed step violated policy on more than seventy percent of them. The fix is a fidelity checker that compares a proposed redesign against a documented map of what each human checkpoint actually verifies, blocking collapse until logged evidence shows the combined step matches human accuracy.

## Key Claims

- The collapsed approval violated policy on over 70% of the ten compliance-only exception cases.
- A manager's sign-off context does not encode contractor restrictions or restricted-system flags.
- A fidelity checker compares proposed redesigns against a process map that records what each checkpoint checks, not merely that one exists.
- Gating the collapse dropped the violation rate on the flagged cases to near zero; the two sign-offs stayed separate until evidence justified merging.
- The checker is only as good as the map of the current process; fidelity should be a ceiling that lifts with evidence, not a permanent wall.

## Relevance

Informs [human approval points](/concepts/human-approval-points.md), [quality gates](/concepts/quality-gates.md), and [human-in-the-loop](/concepts/human-in-the-loop.md) design.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete, testable failure rate and an honest account of the velocity cost. Caveats: a thirty-five-case synthetic test set.

## Entities Mentioned

- None.

## Concepts Covered

- [human approval points](/concepts/human-approval-points.md) — keeping independent sign-offs distinct until evidence supports merging
- [Quality Gates](/concepts/quality-gates.md) — the fidelity checker as a gate on proposed redesigns
- [human-in-the-loop](/concepts/human-in-the-loop.md) — the human checkpoints whose protective value must be preserved
