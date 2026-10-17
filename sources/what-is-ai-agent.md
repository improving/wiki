---
title: "What Is an AI Agent? Real Examples and What Deployment Requires"
type: "Source Summary"
description: "Defines an AI agent as software that acts without step-by-step approval, and argues deployment needs boundaries, checkpoints, and an audit trail."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, governance, improving.com]
sources:
  - "references/improving.com/what-is-ai-agent/what-is-ai-agent.md"
---

# What Is an AI Agent? Real Examples and What Deployment Requires — Summary

**Original source**: `references/improving.com/what-is-ai-agent/what-is-ai-agent.md`

## Summary

An AI agent is software that pursues a goal by taking a sequence of actions without a human approving each step, which is categorically different from a tool whose output passes through a person before becoming action. The post maps that line across customer service, code review, sales, and finance, then argues that reliable deployment requires written boundaries, checkpoints, and an audit trail — and that a single agent hits a ceiling that multi-agent orchestration lifts.

## Key Claims

- A tool's output is reviewed before it acts; an agent is handed a task, executes, and is reviewed after the fact — the gap between a demo and a production system.
- Lakeshore Learning: agents crawl funding and bond sites, scrape data, and map it into the sales queue; within about 90 days reps worked three times as many qualified leads with the process 42% faster.
- Improving's internal finance agent "Penny" cut a monthly variance investigation from three to five days to about fifteen minutes, with a person still deciding what to do.
- A single generalist agent yields gains of roughly 15–50%, then plateaus; a bigger model doesn't move the ceiling because it is one perspective holding competing concerns.
- Multi-agent orchestration — a plan validator, an implementer, a test writer from the requirement, and a security reviewer — mirrors Fred Brooks' surgical team.
- Chain reliability multiplies: 0.95¹⁰ ≈ 0.60 and 0.95²⁰ ≈ 0.36, the Lusser math behind why chain length, not step accuracy alone, determines trustworthiness.
- Deployment requires three practices: draw boundaries (data, systems, decisions), add a checkpoint, keep an audit trail.

## Relevance

Defines [agentic AI](/concepts/agentic-ai.md), explains the [single-agent ceiling](/concepts/single-agent-ceiling.md) and [multi-agent coordination](/concepts/multi-agent-coordination.md), and grounds it in [Lusser's law](/concepts/lussers-law.md).

## Quality

Practitioner explainer by Devlin Liles; concrete case numbers, but the vendor examples come from Improving's own engagements.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author
- [Lakeshore Learning](/entities/lakeshore-learning.md) — sales-agent case study
- [Improving](/entities/improving.md) — author firm and builder of Penny
- [Fred Brooks](/entities/fred-brooks.md) — surgical-team analogy source

## Concepts Covered

- [agentic AI](/concepts/agentic-ai.md) — goal-directed multi-step action
- [single-agent ceiling](/concepts/single-agent-ceiling.md) — the plateau from one perspective
- [multi-agent coordination](/concepts/multi-agent-coordination.md) — distributing narrow jobs
- [Lusser's law](/concepts/lussers-law.md) — chained-step reliability
- [human-in-the-loop](/concepts/human-in-the-loop.md) — the decision kept with a person
- [audit trail](/concepts/audit-trail.md) — logging what the agent did
