---
title: "What Is an Enterprise AI Operating Model and How Do You Build One"
type: "Source Summary"
description: "Argues an AI operating model assigns who decides at each of eight delivery-loop stages, and that decision rights must be instrumented, not documented."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, governance, improving.com]
sources:
  - "references/improving.com/enterprise-ai-operating-model/enterprise-ai-operating-model.md"
---

# What Is an Enterprise AI Operating Model and How Do You Build One — Summary

**Original source**: `references/improving.com/enterprise-ai-operating-model/enterprise-ai-operating-model.md`

## Summary

An AI operating model answers one question at every stage of the delivery loop: who has the authority to decide, and what happens when that decision turns out wrong. The post argues most organizations have answered it for exactly one stage — usually code review, where a vendor shipped a tool — and that decision rights mean nothing unless instrumented in the pipeline.

## Key Claims

- The delivery loop runs Plan, Code, Build, Test, Release, Deploy, Operate, Monitor, and back to Plan; every stage has its own AI leverage point and needs an owner.
- In the author's experience, eight of ten organizations describe their AI governance as a code review policy — one-eighth of the answer.
- Plan and Release carry organization-wide risk and suit centralized decision-making with a small accountable group; Code, Build, and Test are team-specific and suit federated governance within guardrails; Deploy, Operate, and Monitor need a hybrid of central policy and local execution.
- Each model needs a different mechanism: a centralized gate (recorded sign-off), a federated documented boundary, or a hybrid explicit handoff point.
- A mid-cap software company found AI-assisted coding produced a different shape of vulnerability than its human-tuned scanner caught; the fix was a persona-based compliance agent wired into CI/CD.
- The Monitor-to-Plan feedback loop is decorative unless someone owns the connective tissue and a channel exists to change how Plan works.
- The operating model complements frameworks like ISO 42001 and NIST AI RMF, which list controls; it assigns who invokes them at each stage.

## Relevance

Defines the [AI operating model](/concepts/ai-operating-model.md) as the decision-rights layer of [AI governance](/concepts/ai-governance.md), and shows why [runtime governance](/concepts/runtime-governance.md) and [policy as code](/concepts/policy-as-code.md) must enforce what the model assigns.

## Quality

Practitioner essay by Devlin Liles; clear stage-by-stage framing and a named case, but vendor-adjacent and conceptual.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author
- [ISO/IEC 42001](/entities/iso-42001.md) — AI management-system standard cited
- [NIST AI RMF](/entities/nist-ai-rmf.md) — risk framework cited
- [Improving](/entities/improving.md) — author firm

## Concepts Covered

- [AI operating model](/concepts/ai-operating-model.md) — decision rights per stage
- [AI governance](/concepts/ai-governance.md) — the broader control discipline
- [runtime governance](/concepts/runtime-governance.md) — enforcement at execution time
- [operating model](/concepts/operating-model.md) — the designed structure of roles and decisions
- [policy as code](/concepts/policy-as-code.md) — rules enforced by systems
- [runtime policy enforcement](/concepts/runtime-policy-enforcement.md) — intercepting disallowed actions
