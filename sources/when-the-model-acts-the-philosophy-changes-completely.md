---
title: "When the Model Acts, the Philosophy Changes Completely"
type: "Source Summary"
description: "Once a model acts in the world, its outputs are performatives, so governance must match the agent's performative depth."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-governance, devlinliles.com]
sources:
  - "references/devlinliles.com/when-the-model-acts-the-philosophy-changes-completely/when-the-model-acts-the-philosophy-changes-completely.md"
---

# When the Model Acts, the Philosophy Changes Completely — Summary

**Original source**: `references/devlinliles.com/when-the-model-acts-the-philosophy-changes-completely/when-the-model-acts-the-philosophy-changes-completely.md`

## Summary

The author uses J.L. Austin's 1955 performative-utterance lectures and [John Searle's](/entities/john-searle.md) speech act theory to argue that agentic AI changes the governance problem. A model that answers is locutionary and recoverable; a model with [tool calling](/concepts/tool-calling.md) that sends email, commits code, or writes to a database is performing an action that cannot be un-read. The governance architecture, he argues, must match the agent's performative depth — and most teams build evaluation for the read-only case and then promote the system to acting use without revisiting it.

## Key Claims

- Austin distinguished locutionary (what was said), illocutionary (what was done in saying it), and perlocutionary (the effect) acts; the practical split is read-only versus world-changing.
- An agent that chains writes across systems is "chaining performatives," each changing state later actions must work around.
- Read-only agents need evaluation and output monitoring; chaining write agents need intent validation, tool permission scoping, [approval gates](/concepts/human-approval-points.md), audit logging with rollback, and escalation paths.
- [Anthropic's](/entities/anthropic.md) [Constitutional AI](/concepts/constitutional-ai.md) is best read as making certain performatives less probable at training time, which is more robust than runtime-only filtering.
- The first question of every engagement: what is the worst wrong action this system could take, and how much would it cost to reverse?

## Relevance

Frames agentic [AI governance](/concepts/ai-governance.md) around action consequences rather than output accuracy, informing tool-permission and approval design.

## Quality

Practitioner blog post by Devlin Liles. Strong philosophical grounding with production anecdotes; the anecdotes are described generically rather than as cited cases.

## Entities Mentioned

- [John Searle](/entities/john-searle.md) — developed the speech act framework the post builds on
- [Anthropic](/entities/anthropic.md) — its Constitutional AI approach is analyzed through the framework

## Concepts Covered

- [Tool Calling](/concepts/tool-calling.md) — the mechanism that turns outputs into performatives
- [Constitutional AI](/concepts/constitutional-ai.md) — training-time shaping of agent dispositions
- [human approval points](/concepts/human-approval-points.md) — confirmation gates on high-consequence actions

## Related Sources

- [Every AI Value System Bottoms Out Somewhere](/sources/every-ai-value-system-bottoms-out-somewhere.md)
- [You Can Train a Character, Not Just Rules](/sources/you-can-train-a-character-not-just-rules.md)
