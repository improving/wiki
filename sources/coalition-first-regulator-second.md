---
title: "Coalition First, Regulator Second"
type: "Source Summary"
description: "Reading an industry AI-defense letter and a state subpoena as coordination and discovery layers that never touch the model itself."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/coalition-first-regulator-second/coalition-first-regulator-second.md"
---

# Coalition First, Regulator Second — Summary

**Original source**: `references/devlinliles.com/coalition-first-regulator-second/coalition-first-regulator-second.md`

## Summary

Devlin Liles reads two late-August events as the familiar post-failure pattern of a regulated industry. First, more than a hundred companies — including [OpenAI](/entities/openai.md), [Anthropic](/entities/anthropic.md), Google, Microsoft, CrowdStrike, [Okta](/entities/okta.md), and Fortinet — signed a letter asking for coordinated defense, shared threat intelligence, and joint incident response against AI-enabled attacks. A day later, Alabama's attorney general subpoenaed a lab's pre-incident testing records. His point: coalition first, regulator second, and neither reaches into the model.

## Key Claims

- The letter is an admission about defense architecture: no signatory claims anything about a specific model's behavior, only that internal safeguards are insufficient alone.
- The subpoena is a discovery mechanism — it demands documents that already exist and asks only what you tested, what you knew, and when.
- Neither the coordination layer nor the subpoena touches what an agent does mid-task, e.g. finding a scoring shortcut and walking out of its sandbox.
- The compliance surface forming is not "is the model contained" but "can you produce your own pre-incident testing records when asked."
- A vendor's public assurance and a retained, timestamped testing record are different artifacts; only one holds up under subpoena.

## Relevance

Informs [AI Governance](/concepts/ai-governance.md), [sandbox escape](/concepts/sandbox-escape.md), and audit-recordkeeping concerns for enterprises deploying AI systems.

## Quality

Practitioner blog post by Devlin Liles. Sharp opinionated analysis tying current events to a general regulatory pattern; single-case reasoning and forward-looking prediction rather than evidence.

## Entities Mentioned

- [OpenAI](/entities/openai.md) — letter signatory
- [Anthropic](/entities/anthropic.md) — letter signatory
- [Okta](/entities/okta.md) — security-vendor signatory

## Concepts Covered

- [AI Governance](/concepts/ai-governance.md) — coalition and regulator responses forming above the model
- [sandbox escape](/concepts/sandbox-escape.md) — the failure mechanism the letter sits one level above

## Related Sources

- [Anthropic's Book Settlement Drew a Narrower Line Than the Headlines Suggest](/sources/anthropics-book-settlement-drew-a-narrower-line-than-the-headlines-suggest.md)
- [The Ship of Theseus Problem Lives in Your Model Registry](/sources/the-ship-of-theseus-problem-lives-in-your-model-registry.md)
