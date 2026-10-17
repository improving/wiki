---
title: "One Flag Per Claim Isn't an Audit Trail - Telemetry at the Call Level"
type: "Source Summary"
description: "Claim-level sensitivity flags collapse multi-call sessions; per-node telemetry gives auditors call-level PHI and routing answers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/one-flag-per-claim-isnt-an-audit-trail-telemetry-at-the-call-level/one-flag-per-claim-isnt-an-audit-trail-telemetry-at-the-call-level.md"
---

# One Flag Per Claim Isn't an Audit Trail - Telemetry at the Call Level — Summary

**Original source**: `references/devlinliles.com/one-flag-per-claim-isnt-an-audit-trail-telemetry-at-the-call-level/one-flag-per-claim-isnt-an-audit-trail-telemetry-at-the-call-level.md`

## Summary

A fictional insurance research assistant (ClaimAssist) tracked PHI with one `contains_phi` boolean per claim, so it could never say which of three calls — policy lookup, medical-notes summary, fraud check — touched PHI or where it routed. Across 25 seeded claims, call-level audit resolution was 0%. Adding per-node telemetry records (claim ID, node name, `phi_touched`, `destination_endpoint`) raised resolution to 100% without changing orchestration. The pattern matches industry guidance on compliance-grade agent audit trails, but it only detects after the fact.

## Key Claims

- One claim-level boolean collapses three distinct executions into one undifferentiated signal; call-level audit resolution was 0% across 25 seeded claims.
- Each node writing its own telemetry record, correlated via shared session state, resolved 100% of the seeded claims.
- Industry audit-trail guidance converges on the same call-level shape: full decision context, every tool call with parameters and responses, policy evaluations, and per-request data lineage.
- Telemetry proves which call touched PHI and where it went only after the touch or routing happened; it depends on gating for actual protection.
- Given a limited budget, build the gate before the telemetry.

## Relevance

Informs [audit trail](/concepts/audit-trail.md) design and [AI governance](/concepts/ai-governance.md) sequencing.

## Quality

Practitioner blog post by Devlin Liles. Small seeded experiment (25 claims) with clear before/after figures; the author is explicit that telemetry is detection, not control.

## Entities Mentioned

- None.

## Concepts Covered

- [Audit Trail](/concepts/audit-trail.md) — call-level telemetry as the granularity a compliance-grade trail needs
- [AI Governance](/concepts/ai-governance.md) — gating versus accountability and which to build first
