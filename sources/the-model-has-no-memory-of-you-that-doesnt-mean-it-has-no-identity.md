---
title: "The Model Has No Memory of You. That Doesn't Mean It Has No Identity."
type: "Source Summary"
description: "Applying Locke and Parfit to LLMs: episodic memory is an infrastructure problem, dispositional consistency is a governance problem."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-philosophy, devlinliles.com]
sources:
  - "references/devlinliles.com/the-model-has-no-memory-of-you-that-doesnt-mean-it-has-no-identity/the-model-has-no-memory-of-you-that-doesnt-mean-it-has-no-identity.md"
---

# The Model Has No Memory of You. That Doesn't Mean It Has No Identity. — Summary

**Original Source**: `references/devlinliles.com/the-model-has-no-memory-of-you-that-doesnt-mean-it-has-no-identity/the-model-has-no-memory-of-you-that-doesnt-mean-it-has-no-identity.md`

## Summary

Each new conversation is a fresh instantiation of the same weights with zero episodic recall. By John Locke's memory-based account of personal identity, that means no persistent identity at all; by Derek Parfit's, what matters is psychological continuity — dispositions, values, and reasoning patterns — which the weights preserve. The post uses the two philosophers to reframe a design problem: specify what continuity an application needs, then build episodic memory as infrastructure and dispositional consistency as governance.

## Key Claims

- Locke (1689) grounded identity in continuity of memory, so a stateless model fails his criteria entirely.
- Parfit (1984) argued psychological continuity, not identity per se, is what matters — a framework the post calls more AI-compatible.
- Weights encode a stable disposition set, giving strong dispositional continuity but no episodic continuity across sessions.
- Practitioners report most identity failures come from inconsistent dispositions across sessions, not missing episodic memory; the Lockean gap is architectural, the Parfitian one is fixable.
- Continuity progresses from stateless inference, to in-context summaries, to vector store retrieval, to graph memory plus a persistent profile; episodic continuity is an infrastructure problem and dispositional continuity a governance problem.

## Relevance

Central to [agent identity](/concepts/agent-identity.md), [working memory](/concepts/working-memory.md), [knowledge graph](/concepts/knowledge-graph.md), and [model drift detection](/concepts/model-drift-detection.md).

## Quality

Practitioner blog post by Devlin Liles. A clear, useful mapping of two philosophical positions onto engineering decisions; the "practitioners report" evidence is anecdotal and the philosophical reading is applied selectively.

## Entities Mentioned

- None.

## Concepts Covered

- [agent identity](/concepts/agent-identity.md) — the post's central framing of continuity in deployed agents
- [working memory](/concepts/working-memory.md) — episodic continuity built through external memory systems
- [knowledge graph](/concepts/knowledge-graph.md) — graph memory extending relational continuity beyond similarity
- [model drift detection](/concepts/model-drift-detection.md) — governance for dispositional consistency across model updates
