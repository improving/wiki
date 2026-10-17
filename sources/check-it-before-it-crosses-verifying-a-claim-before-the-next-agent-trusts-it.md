---
title: "Check It Before It Crosses - Verifying a Claim Before the Next Agent Trusts It"
type: "Source Summary"
description: "A groundedness gate before each agent handoff stops planted errors and unsupported claims from propagating."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it.md"
---

# Check It Before It Crosses - Verifying a Claim Before the Next Agent Trusts It — Summary

**Original source**: `references/devlinliles.com/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it/check-it-before-it-crosses-verifying-a-claim-before-the-next-agent-trusts-it.md`

## Summary

Liles built a three-agent news pipeline—Source, Synthesis, Distribution—with no claim checks at either handoff. Planted factual errors survived into the final briefing, and downstream agents added untraceable embellishment, because every agent trusted the previous one by default. His fix inserts a verify-claim node before each handoff that matches candidate claims against annotated source spans and blocks anything ungrounded from propagating.

## Key Claims

- Each agent did its own job correctly; corruption happened at the seams, where catching errors was never anyone's job.
- Both claim-survival error rate and unsupported-claim rate dropped sharply with the gate; surviving claims carried near-complete verified coverage.
- The same "check it before it moves" shape appears independently in tabular fact-checking, claim decomposition, and provenance research tested against 20,000 real claims.
- The gate assumes good-faith content and does not catch prompt-injection style goal-hijacking, which needs no false factual claim.
- It checks groundedness at write time, not staleness by read time, and its value depends on having a trustworthy source to verify against.

## Relevance

Addresses [multi-agent coordination](/concepts/multi-agent-coordination.md) seams, [error propagation](/concepts/error-propagation.md), and [independent verification](/concepts/independent-verification.md), with a noted [prompt injection](/concepts/prompt-injection.md) limitation.

## Quality

Practitioner blog post by Devlin Liles. Clear measured scenario with explicitly named limitations; results come from a seeded synthetic corpus rather than production traffic.

## Entities Mentioned

- None.

## Concepts Covered

- [Multi-Agent Coordination](/concepts/multi-agent-coordination.md) — handoff seams where trust is misplaced
- [Error Propagation](/concepts/error-propagation.md) — planted errors flowing to the final briefing
- [Independent Verification](/concepts/independent-verification.md) — the groundedness gate before each handoff
- [Prompt injection](/concepts/prompt-injection.md) — the threat model the gate does not cover

## Related Sources

- [Ten Nodes, Forty-Five Connections, and a Throughput Drop Nobody Modeled](/sources/ten-nodes-forty-five-connections-and-a-throughput-drop-nobody-modeled.md)
