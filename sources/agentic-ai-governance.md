---
title: "Why Trust Is the Hardest Part of Agentic AI Governance"
type: "Source Summary"
description: "Argues agent governance must be engineered before autonomy because agent failures compound faster than human review can track."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, security, improving.com]
sources:
  - "references/improving.com/agentic-ai-governance/agentic-ai-governance.md"
---

# Why Trust Is the Hardest Part of Agentic AI Governance — Summary

**Original source**: `references/improving.com/agentic-ai-governance/agentic-ai-governance.md`

## Summary

Agentic AI governance is the engineering work of building the controls that let an organization extend autonomy to AI agents and prove afterward what they did. The post argues this is harder than DevOps because agent errors compound arithmetically across chained steps, faster than any human review cadence can track, so trust has to be built into the system rather than observed into existence.

## Key Claims

- Agentic AI governance covers audit trails, boundary enforcement, quality gates, human-in-the-loop approvals, and access control, each designed before deployment and enforced by the system, because a policy document cannot stop an agent.
- Step accuracies multiply: at 95% per step, a 10-step chain completes correctly about 60% of the time and a 20-step chain about 36%; at 99% per step those rise to roughly 90% and 82%.
- Reliability engineers have understood the compounding math since Robert Lusser's work in the 1940s.
- A major airline moved compliance into the pipeline with regulatory-review agents checking every change against its own standards, rather than slowing teams to the speed of review.
- Boundaries must be access policy, not a system-prompt instruction: "a boundary an agent can talk its way around isn't a boundary."
- Better models shrink but do not remove the need for governance: even a failure once in a thousand runs still requires an audit trail to answer "show me what happened and why."
- Vendors may ship audit trails and access control as commodity features, but the operating model — which agents get how much autonomy over which decisions — stays with the business.
- DevOps-mature teams misread agent failures as trust violations because they are used to human actors who hesitate; agents don't, unless a confidence threshold is built.

## Relevance

Defines [runtime governance](/concepts/runtime-governance.md) as the discipline of [AI governance](/concepts/ai-governance.md), with [audit trails](/concepts/audit-trail.md), [quality gates](/concepts/quality-gates.md), and [boundary enforcement](/concepts/boundary-enforcement.md) as the first controls to build.

## Quality

Practitioner essay by Devlin Liles; concrete arithmetic and a named airline engagement, but vendor-adjacent and light on failure detail.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author
- [NIST AI RMF](/entities/nist-ai-rmf.md) — framework cited for the accountability requirement
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [runtime governance](/concepts/runtime-governance.md) — enforcing controls at execution time
- [AI governance](/concepts/ai-governance.md) — the broader control discipline
- [audit trail](/concepts/audit-trail.md) — the per-action record
- [quality gates](/concepts/quality-gates.md) — pass criteria at handoffs
- [boundary enforcement](/concepts/boundary-enforcement.md) — access policy over prompt instructions
- [human-in-the-loop](/concepts/human-in-the-loop.md) — approval reserved for irreversible decisions
- [least privilege](/concepts/least-privilege.md) — scoping each agent to its job
- [Lusser's law](/concepts/lussers-law.md) — the compounding reliability math
