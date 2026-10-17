---
title: "runtime governance"
type: "Concept"
description: "Enforcing governance at the moment each agent action executes, because policy documents and post-hoc review cannot constrain millisecond chains."
created: '2026-10-17'
updated: '2026-10-17'
tags: [governance, agents, policy]
sources:
  - "/sources/the-scaffolding-just-got-a-learning-rate.md"
  - "/sources/your-ai-governance-policy-is-not-governance.md"
---

# runtime governance

Runtime governance is the position that AI governance must be enforced architecturally at the moment each action executes, not written down in a policy document. A policy assumes a moral agent who reads and chooses to comply; an autonomous chain does not have one, and it runs in milliseconds, so post-hoc review is too late. This corpus argues active governance needs four runtime layers — rules, gating, behavior, and evidence — and that instructions decay over long trajectories, so the enforcement point must be live.

## Key Claims

- Policy documents assume a moral agency that agents do not have.
- Agentic chains execute in milliseconds, so post-hoc governance is impossible.
- Active governance needs four runtime layers: rules, gating, behavior, evidence.
- The operative test: ask what would happen if an agent tried to access restricted data *right now*.
- Skill documents behave like trainable external state, with a validation gate, so the harness itself must be governed.
- Instructions decay over long trajectories, so adherence cannot be assumed from a prompt alone.

## Related

- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the enforcement mechanism this concept names
- [Policy as Code](/concepts/policy-as-code.md) — expressing rules as executable, not written, artifacts
- [Governance engine](/concepts/governance-engine.md) — the component that evaluates rules per action
- [Embedded Governance](/concepts/embedded-governance.md) — governance placed inside the runtime rather than beside it
- [Bolt-on Governance](/concepts/bolt-on-governance.md) — the documentation-first approach this rejects
- [Your AI Governance Policy Is Not Governance](/sources/your-ai-governance-policy-is-not-governance.md) — primary source
