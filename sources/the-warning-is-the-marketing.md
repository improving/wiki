---
title: "The Warning Is the Marketing"
type: "Source Summary"
description: "A lab's safety disclosure doubles as a capability boast, so govern models at runtime, not by vendor risk labels."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-warning-is-the-marketing/the-warning-is-the-marketing.md"
---

# The Warning Is the Marketing — Summary

**Original source**: `references/devlinliles.com/the-warning-is-the-marketing/the-warning-is-the-marketing.md`

## Summary

Devlin Liles argues that when OpenAI disclosed its unreleased model Astra might cross a "Critical" cybersecurity threshold, the warning did two jobs at once: honoring a responsible-scaling commitment and advertising how extraordinarily capable the model is. He draws a parallel to industrial near-miss reporting, where the regulator reads risk and the market reads capacity from the same document. Because a self-reported danger label is a vendor claim, he argues organizations should govern models with runtime enforcement rather than the vendor's self-assigned risk tier.

## Key Claims

- The same disclosure that names a safety threshold also signals frontier capability; a lab announcing its model is dangerous and one announcing it is powerful are the same announcement.
- Anthropic's same-week Claude Security expansion on Mythos 5 sends the opposite message — "our current model is capable enough that we're selling access" — yet both confirm frontier cyber capability has crossed a line worth discussing publicly.
- A vendor-reported benchmark score is a claim, not a fact, until a second party replicates it; a self-reported capability threshold deserves the same skepticism.
- Gating model permissions by the vendor's self-reported tier is "governing by label," the same failure mode that sank a decade of policy-document data governance.
- The fix is a runtime layer that catches a model doing something it shouldn't, independent of the tier assigned going in.

## Relevance

Core to [safety disclosure as marketing](/concepts/safety-disclosure-as-marketing.md), and it argues for [runtime governance](/concepts/runtime-governance.md) over label-based control.

## Quality

Practitioner blog post by Devlin Liles. A sharp, well-structured argument; it is opinion and analogy-driven with no original data, and the Astra threshold is taken as reported.

## Entities Mentioned

- [OpenAI](/entities/openai.md) — disclosed the Astra capability threshold
- [Anthropic](/entities/anthropic.md) — expanded Claude Security access the same week
- [Astra](/entities/astra.md) — the unreleased model at issue
- [Claude Security](/entities/claude-security.md) — vulnerability-scanning capability sold as standard usage
- [Mythos 5](/entities/mythos-5.md) — the model Claude Security scans

## Concepts Covered

- [Safety Disclosure as Marketing](/concepts/safety-disclosure-as-marketing.md) — central thesis
- [runtime governance](/concepts/runtime-governance.md) — proposed alternative to governing by vendor label
- [Runtime Policy Enforcement](/concepts/runtime-policy-enforcement.md) — the control that holds regardless of tier
