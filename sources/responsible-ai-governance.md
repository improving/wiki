---
title: "Responsible AI: Building Ethics and Governance into your Strategy from Day One"
type: "Source Summary"
description: "Most responsible AI programs audit once; import software's ratchet pattern so ethics metrics gate every deployment."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, governance, improving.com]
sources:
  - "references/improving.com/responsible-ai-governance/responsible-ai-governance.md"
---

# Responsible AI: Building Ethics and Governance into your Strategy from Day One — Summary

**Original source**: `references/improving.com/responsible-ai-governance/responsible-ai-governance.md`

## Summary

Devlin Liles argues that most responsible AI programs run a one-time audit, produce a document, and call it governance — which cannot catch drift between audits. He imports software's ratchet pattern: record each ethics metric as a checked-in floor that can only move up and that gates every deployment, so governance becomes continuous enforcement rather than a snapshot.

## Key Claims

- A quarterly audit is a photograph while a production system is a video; point-in-time compliance cannot demonstrate ongoing compliance under GDPR Article 22, the EU AI Act, or state high-risk rules.
- The ratchet stores each metric's current floor in a checked-in file, updates it only when a change improves on the floor, and blocks any merge that would drop a metric below it.
- A regional health plan enforced column-level access control and automated lineage on every dataset feeding a production agent, produced HIPAA audit entries as a byproduct of access, and required six approvals before any agent reached production.
- For hiring, record disparate impact as a floor and gate every retraining; for finance, gate explainability coverage against GDPR Article 22.
- Set the starting floor at current measured performance, not an aspirational target — a floor the system doesn't meet is a promise with no enforcement behind it.
- The ratchet only governs what is measured: Goodhart's law applies harder here, and human review still owns judgment calls a metric cannot resolve.

## Relevance

Reframes [responsible AI](/concepts/responsible-ai.md) and [AI governance](/concepts/ai-governance.md) as runtime enforcement rather than documents, turning [policy as code](/concepts/policy-as-code.md) into deployment gates. It depends on [quality gates](/concepts/quality-gates.md) and connects to [AI bias](/concepts/ai-bias.md) and [embedded governance](/concepts/embedded-governance.md).

## Quality

Practitioner essay by Improving's Devlin Liles; strong mechanism analogy with honest caveats, though the recruitment example is explicitly described as illustrative rather than observed.

## Entities Mentioned

- [NIST AI RMF](/entities/nist-ai-rmf.md) — framework describing what governance should cover
- [ISO/IEC 42001](/entities/iso-42001.md) — the AI management-system standard
- [GDPR](/entities/gdpr.md) — Article 22 automated-decision obligations
- [EU AI Act](/entities/eu-ai-act.md) — phased high-risk obligations
- [HIPAA](/entities/hipaa.md) — health data trail requirements
- [Devlin Liles](/entities/devlin-liles.md) — author
- [Improving](/entities/improving.md) — publisher

## Concepts Covered

- [responsible AI](/concepts/responsible-ai.md) — the main topic
- [AI governance](/concepts/ai-governance.md) — the controls being enforced
- [policy as code](/concepts/policy-as-code.md) — floors enforced mechanically
- [runtime governance](/concepts/runtime-governance.md) — enforcement between audits
- [quality gates](/concepts/quality-gates.md) — the ratchet as a gate
- [AI bias](/concepts/ai-bias.md) — disparate impact as a floor
- [embedded governance](/concepts/embedded-governance.md) — controls in the platform
- [Goodhart's law](/concepts/goodharts-law.md) — the metric-capture risk
