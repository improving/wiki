---
title: "The Model Stays Home. The Patch Ships."
type: "Source Summary"
description: "Anthropic's Claude Security scans code on Mythos 5 server-side, returning governed findings; Liles argues customers still owe their own second gate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-stays-home-the-patch-ships/the-model-stays-home-the-patch-ships.md"
---

# The Model Stays Home. The Patch Ships. — Summary

**Original source**: `references/devlinliles.com/the-model-stays-home-the-patch-ships/the-model-stays-home-the-patch-ships.md`

## Summary

Devlin Liles reads Anthropic's Claude Security launch as an "access-by-output" model: customers never touch the raw frontier model, only the governed product surface built on top of it. He compares it to export-controlled wind tunnels, where the lab runs your design and returns the data but keeps the machine. The architecture is right for a lab's own dual-use risk, he argues, but it solves only half the problem — the finding still needs a customer-side gate before it can be trusted.

## Key Claims

- Claude Security, in public beta for Enterprise, runs codebase vulnerability scans on Mythos 5 itself, billed as ordinary token usage with no add-on or special tier.
- Each scan returns a CWE-categorized finding, a confidence and severity rating, and a suggested patch, meant for human review before it ships through Claude Code.
- Anthropic paired the release with the Defender Advantage Fund — $35M in Claude credits for patching open-source vulnerabilities — and is widening the Cyber Verification Program's reduced-safeguard access toward Mythos-class models.
- A vendor finding is still a claim about the codebase; feeding it into an automated patch pipeline without an evaluation baseline repeats a long-standing governance failure.

## Relevance

Illustrates [runtime governance](/concepts/runtime-governance.md), a [control plane](/concepts/control-plane.md), [boundary enforcement](/concepts/boundary-enforcement.md), and [human approval points](/concepts/human-approval-points.md) applied to a vendor product surface.

## Quality

Practitioner blog post by Devlin Liles. Clear argument by analogy; the access-by-output framing is interpretation, and the product details are single-source reporting.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — vendor behind Claude Security
- [Claude Security](/entities/claude-security.md) — the scanning product in public beta
- [Claude Code](/entities/claude-code.md) — the surface a patch ships through after review
- [Mythos 5](/entities/mythos-5.md) — the frontier model running the scans server-side

## Concepts Covered

- [runtime governance](/concepts/runtime-governance.md) — four-layer model applied here
- [Control plane](/concepts/control-plane.md) — the customer-side check the post says is missing
- [Boundary enforcement](/concepts/boundary-enforcement.md) — enforced policy vs. a prompt suggestion
- [human approval points](/concepts/human-approval-points.md) — review before a patch reaches production
