---
title: "Your AI Governance Policy Is Not Governance"
type: "Source Summary"
description: "A written AI policy is aspiration; real governance enforces rules at runtime through a four-layer control plane."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/your-ai-governance-policy-is-not-governance/your-ai-governance-policy-is-not-governance.md"
---

# Your AI Governance Policy Is Not Governance — Summary

**Original source**: `references/devlinliles.com/your-ai-governance-policy-is-not-governance/your-ai-governance-policy-is-not-governance.md`

## Summary

The post argues that a written AI policy is aspiration, not governance, because policy models assume a governed entity with moral agency that reads and chooses to comply. Agents execute at machine speed and scale, completing dozens of actions before a human sees output, so post-hoc review cannot work. Real governance must run in real time at the moment each action is proposed, implemented as a four-layer runtime control plane.

## Key Claims

- A single enterprise agentic workflow might complete ~40 discrete actions before a human sees any output, making post-hoc audit structurally too slow.
- An agent correct 95% of the time has only a 36% chance of completing a 20-step chain without error.
- The four-layer runtime control plane is: rules (risk appetite, tiers, approvals), gating (eligible models/tools/data/identities with least-privilege boundaries), behavior (an Agent Runtime Controller between proposed action and execution), and evidence (structured traces and tamper-resistant records).
- Most organizations invest heavily in layer one (the policy document and its review council) and almost nothing in layers two through four.
- A 2026 KPMG survey found 75% of large-enterprise leaders cite security, compliance, and auditability as top agentic AI requirements; EU AI Act Annex III enforcement takes effect August 2, 2026.

## Relevance

Informs [runtime governance](/concepts/runtime-governance.md), [Policy as Code](/concepts/policy-as-code.md), [Least privilege](/concepts/least-privilege.md), [Audit Trail](/concepts/audit-trail.md), and the [Control plane](/concepts/control-plane.md) architecture for agentic systems.

## Quality

Practitioner blog post by Devlin Liles, opening with an illustrative CTO anecdote. The 20-step probability is illustrative; the KPMG figure and EU dates are cited secondhand.

## Entities Mentioned

- [EU AI Act](/entities/eu-ai-act.md) — Annex III enforcement deadline cited
- [NIST AI RMF](/entities/nist-ai-rmf.md) — referenced as an input to the governance baseline

## Concepts Covered

- [runtime governance](/concepts/runtime-governance.md) — the post's central proposal
- [Policy as Code](/concepts/policy-as-code.md) — policy enforced by systems rather than memorized by people
- [Least privilege](/concepts/least-privilege.md) — gating layer's eligibility boundaries
- [Audit Trail](/concepts/audit-trail.md) — the evidence layer, generated automatically at action level
- [Control plane](/concepts/control-plane.md) — the four-layer runtime architecture
