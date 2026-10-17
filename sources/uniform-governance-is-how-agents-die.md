---
title: "Uniform Governance Is How Agents Die"
type: "Source Summary"
description: "Agents fail because governance treats every action as maximally risky; oversight should scale with reversibility instead."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, driventodevelop.com]
sources:
  - "references/driventodevelop.com/uniform-governance-is-how-agents-die/uniform-governance-is-how-agents-die.md"
---

# Uniform Governance Is How Agents Die — Summary

**Original source**: `references/driventodevelop.com/uniform-governance-is-how-agents-die/uniform-governance-is-how-agents-die.md`

## Summary

O'Hara argues that the failure mode killing enterprise AI agents is not missing governance but uniform governance: applying the same scrutiny to every action regardless of what it costs if it goes wrong. He opens on Gartner's projection that 40% of enterprises will demote or decommission autonomous agents by 2027 — not because the agents could not do the work, but because governance made it impossible. He describes the pattern from experience: an accurate, fast agent gets wrapped in an approval process where reading a file needs a ticket, generating a summary needs a review, and sending an internal message needs sign-off, until it is slower than the human it replaced and the team stops using it. The project dies "with a shrug." His proposed principle, carried over from Akamai's report, is reversibility: the governance burden should scale with how reversible the failure is, not with the agent's category or department. Only 14.4% of organizations deploy agents to production with full security approval.

## Key Claims

- Gartner projects 40% of enterprises will demote or decommission autonomous agents by 2027, for governance rather than capability reasons.
- Uniform governance treats every action as the most dangerous thing it could do: read a file, needs a ticket; summarize, needs review; send a message, needs sign-off.
- Over-governed agents become slower than the humans they replaced, and projects die without a formal failure.
- The governance burden should scale with reversibility — per Akamai's report — rather than with agent category or department.
- Only 14.4% of organizations send agents to production with full security approval; governance should be calibrated to the highest-consequence action an agent can take.

## Relevance

Directly concerns [AI Governance](/concepts/ai-governance.md), the critique of [uniform governance](/concepts/uniform-governance.md), and [reversibility](/concepts/reversibility.md) as the criterion for scaling oversight.

## Quality

Practitioner blog post by David O'Hara. Argues from a cited Gartner projection plus firsthand observation; the 40% figure is a forecast and the field evidence is anecdotal.

## Entities Mentioned

- [Gartner](/entities/gartner.md) — source of the 40%-by-2027 decommissioning projection
- [Akamai](/entities/akamai.md) — its report surfaced reversibility as the governing criterion
- [David O'Hara](/entities/david-o-hara.md) — author

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — governance design as the cause of agent failure
- [uniform governance](/concepts/uniform-governance.md) — the named failure mode of undifferentiated scrutiny
- [reversibility](/concepts/reversibility.md) — the criterion by which oversight burden should scale
- [human approval points](/concepts/human-approval-points.md) — approval gates applied indiscriminately to low-consequence actions
