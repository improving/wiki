---
title: "AI Governance as Infrastructure: A Four-Layer Framework for Agentic AI"
type: "Source Summary"
description: "Agentic AI needs governance built as CI/CD-like infrastructure — rulebook, gating, runtime enforcement, and evidence."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, governance, improving.com]
sources:
  - "references/improving.com/ai-governance-agentic-ai-framework/ai-governance-agentic-ai-framework.md"
---

# AI Governance as Infrastructure: A Four-Layer Framework for Agentic AI — Summary

**Original source**: `references/improving.com/ai-governance-agentic-ai-framework/ai-governance-agentic-ai-framework.md`

## Summary

Devlin Liles argues that AI governance frameworks fail because they are written as policy for entities that read, judge, and choose compliance, while agents execute at machine speed with no such capacity. He maps governance onto the CI/CD scaffolding engineering teams already trust, giving four layers: a risk rulebook, gating of models and tools, runtime enforcement before each action, and automatically generated tamper-resistant evidence.

## Key Claims

- A 40-slide framework sat on a shared drive while a team in the same company routed vendor contracts through a personal AI account.
- An agent at 95% per step completes a twenty-step chain correctly only about 36% of the time, and dozens of actions can run before a human looks at the output.
- Governance scaffolding parallels delivery scaffolding: audit trail ↔ version control, quality gate ↔ automated test, boundary definition ↔ deployment pipeline, human approval ↔ pull request review.
- The four layers are risk tiers and approval thresholds; gating which models, tools, and data sources may participate; runtime enforcement before every action; and automatically generated evidence.
- Investment concentrates in layer one with almost nothing built for layers two through four — true of both a global industrial manufacturer and an energy technology company he advised.
- Objections answered: auditors want evidence, and a runtime system produces stronger evidence than a policy binder; the architecture becomes necessary exactly when autonomy enters, not before.

## Relevance

Turns [AI governance](/concepts/ai-governance.md) into [runtime governance](/concepts/runtime-governance.md) infrastructure, with a [governance engine](/concepts/governance-engine.md) enforcing [boundary enforcement](/concepts/boundary-enforcement.md) and [human approval points](/concepts/human-approval-points.md). It is a concrete [AI operating model](/concepts/ai-operating-model.md) built on [cognitive scaffolding](/concepts/cognitive-scaffolding.md).

## Quality

Practitioner essay by Improving's Devlin Liles; the CI/CD analogy is clarifying and the client anecdotes are specific, though it advocates for Improving's own framework.

## Entities Mentioned

- [NIST AI RMF](/entities/nist-ai-rmf.md) — framework pointing at the gap without closing it
- [ISO/IEC 42001](/entities/iso-42001.md) — standard describing good governance
- [Devlin Liles](/entities/devlin-liles.md) — author
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [AI governance](/concepts/ai-governance.md) — the main topic
- [runtime governance](/concepts/runtime-governance.md) — enforcement per action
- [governance engine](/concepts/governance-engine.md) — the runtime control layer
- [boundary enforcement](/concepts/boundary-enforcement.md) — what the agent may touch
- [human approval points](/concepts/human-approval-points.md) — the PR-review analogue
- [AI operating model](/concepts/ai-operating-model.md) — decision rights and enforcement
- [cognitive scaffolding](/concepts/cognitive-scaffolding.md) — infrastructure holding knowledge
- [audit trail](/concepts/audit-trail.md) — evidence as version control
- [agent identity](/concepts/agent-identity.md) — privilege at the runtime layer
