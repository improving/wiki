---
title: "Approved, Except Nobody Could Say Which Gate Approved It"
type: "Source Summary"
description: "Collapsing multi-gate results into one status hides which gate failed; persisting per-gate traces made bad loans attributable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/approved-except-nobody-could-say-which-gate-approved-it/approved-except-nobody-could-say-which-gate-approved-it.md"
---

# Approved, Except Nobody Could Say Which Gate Approved It — Summary

**Original source**: `references/devlinliles.com/approved-except-nobody-could-say-which-gate-approved-it/approved-except-nobody-could-say-which-gate-approved-it.md`

## Summary

A loan-application orchestration chained three quality gates — income verification, credit check, fraud check — but its dashboard showed only a single collapsed approved/declined status. When thirty synthetic applications, six carrying injected fraud-check failures, all got funded, there was no stored record of which gate had passed or failed: gate attribution loss was 100% on the six bad loans. Persisting and surfacing each gate's pass-or-fail result with its evidence snippet dropped attribution loss to zero. The pattern, Gate-Trace Visibility, buys inspectability at decision time rather than forensic reconstruction afterward.

## Key Claims

- Three gates ran before funding, but only an aggregate status was ever stored or surfaced.
- All six of thirty applications with injected fraud-check failures were funded anyway; the responsible gate could not be identified in 100% of those cases.
- The gates themselves may not have been broken — a single wrongly passing gate is invisible inside an overall green result.
- Persisting per-gate results with evidence snippets reduced gate attribution loss from 100% to zero on the six bad loans.
- The pattern stops well short of full causal attribution; it is lighter than a replayable, suppression-tested trace.

## Relevance

Informs [quality gates](/concepts/quality-gates.md) and [audit trail](/concepts/audit-trail.md) design in multi-gate orchestration, where per-step attribution matters.

## Quality

Practitioner blog post by Devlin Liles. Concrete, self-reported experiment with named metrics and candid scope caveats; evidence is a single synthetic test harness rather than production data.

## Entities Mentioned

- None.

## Concepts Covered

- [Quality Gates](/concepts/quality-gates.md) — the three chained gates whose individual results were lost
- [Audit Trail](/concepts/audit-trail.md) — per-gate traces as the record needed at decision time

## Related Sources

- [Automation Is a Professional Obligation, Not an Optimization](/sources/automation-is-a-professional-obligation-not-an-optimization.md)
- [Governance Is Not Overhead. It Is the Engine of Trust.](/sources/governance-is-not-overhead-it-is-the-engine-of-trust.md)
