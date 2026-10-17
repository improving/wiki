---
title: "94 Percent Confidence, Exact Match, Auto-Resolved"
type: "Source Summary"
description: "Disclosing confidence scores and evidence on every autonomous decision turns faith in a label into inspectable evidence."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/94-percent-confidence-exact-match-auto-resolved/94-percent-confidence-exact-match-auto-resolved.md"
---

# 94 Percent Confidence, Exact Match, Auto-Resolved — Summary

**Original source**: `references/devlinliles.com/94-percent-confidence-exact-match-auto-resolved/94-percent-confidence-exact-match-auto-resolved.md`

## Summary

The author built an IT service-desk agent that auto-remediates common endpoint issues and escalates to a technician when evidence is thin. The first version showed users only "resolved automatically" or "escalated for review," hiding the confidence number the agent already computed internally. On a forty-ticket test, ten near-threshold cases were auto-resolved with the same flat label as clear-cut ones, and the borderline-error rate came in above 40 percent. The fix discloses the score and the specific evidence behind every decision, at write time, so close calls look like close calls.

## Key Claims

- A forty-ticket test produced a borderline-error rate above 40 percent when near-threshold decisions were indistinguishable from clear-cut ones.
- The agent computed a confidence number on every ticket; disclosure costs almost nothing because the number already existed.
- The autonomy threshold (80 percent in the example) is a policy choice the mechanism reports but does not derive.
- Disclosure and [confidence calibration](/concepts/confidence-calibration.md) are separate claims; a mis-calibrated model can report 94 percent on a wrong answer, risking transparency theater.
- [McKinsey & Company](/entities/mckinsey-company.md)'s 2026 AI Trust Maturity Survey scores "agentic AI governance and controls" lowest of five dimensions, with only ~30 percent of organizations at maturity level 3+.

## Relevance

Informs [human-in-the-loop](/concepts/human-in-the-loop.md) design and [confidence calibration](/concepts/confidence-calibration.md), and speaks to the broader [AI Governance](/concepts/ai-governance.md) gap around autonomous action.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a concrete, quantified single-case experiment and a clear-eyed separation of disclosure from calibration. Caveats: the 40 percent figure comes from ten synthetic tickets, and the McKinsey figures are cited second-hand.

## Entities Mentioned

- [McKinsey & Company](/entities/mckinsey-company.md) — source of the 2026 AI Trust Maturity Survey figures

## Concepts Covered

- [human-in-the-loop](/concepts/human-in-the-loop.md) — the autonomy-versus-escalation split the agent automates
- [confidence-calibration](/concepts/confidence-calibration.md) — distinguishes showing a number from trusting it

## Related Sources

- [Getting the Right Answer for the Wrong Reason](/sources/getting-the-right-answer-for-the-wrong-reason.md)
