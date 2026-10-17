---
title: "Complexity Never Goes Away, it Just Moves"
type: "Source Summary"
description: "AI shifts complexity rather than removing it, moving engineering attention from writing code to the systems around models."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai, engineering, improving.com]
sources:
  - "references/improving.com/complexity-never-goes-away-ai-systems-engineering/complexity-never-goes-away-ai-systems-engineering.md"
---

# Complexity Never Goes Away, it Just Moves — Summary

**Original source**: `references/improving.com/complexity-never-goes-away-ai-systems-engineering/complexity-never-goes-away-ai-systems-engineering.md`

## Summary

The narratives that AI removes the need for engineers and makes software cheap and abundant are proving false; complexity just relocates. As AI automates line-by-line programming, engineering effort shifts to the systems around models — harness engineering on the input side and LLMOps on the output side — forming a feedback loop that improves results while reducing token consumption.

## Key Claims

- Engineering talent is a scarce resource and frustratingly hard to manage because it is subjective, non-fungible, and a moving target.
- Two pervasive narratives are proving false: that we will no longer need engineers, and that software will become cheap and abundant.
- Constraints show up physically, recently as painful token costs, but engineering talent itself is a subtler and equally stubborn constraint.
- Complexity has moved across eras: front-end engineering didn't exist in the command-line era; the web and mobile created it, then NoSQL, cloud, and graph databases exploded back-end complexity in the early 2000s.
- Writing imperative code now needs little attention in almost all cases, but new checkpoints have emerged; the objective is systems that get better results from AI while reducing token consumption.
- Prompt engineering developed into context engineering, where up-front planning for refined instructions improved both accuracy and cost.
- A barbell pattern has emerged: the pre- and post-processing steps around the LLM matter most, because the LLM is an expensive digital gauntlet.
- Harness engineering manages historical context, caching, tool integrations, external data services, and retry logic; LLMOps measures accuracy, token burn, and security; outputs from LLMOps become inputs that update the harness.
- Expect an explosion of paradigms and roles that don't yet exist; demand for systems engineers will increase, deployed in new and unique ways.

## Relevance

Informs [context engineering](/concepts/context-engineering.md), [prompt engineering](/concepts/prompt-engineering.md), [AI monitoring](/concepts/ai-monitoring.md), and [token cost](/concepts/token-cost.md).

## Quality

Opinion and analysis by Josh Harrison; a clear thesis with useful history, but light on primary evidence and closes with a service pitch.

## Entities Mentioned

- [Josh Harrison](/entities/josh-harrison.md) — author
- [Improving](/entities/improving.md) — the consultancy offering the AI expertise

## Concepts Covered

- [context engineering](/concepts/context-engineering.md) — the evolution of prompt engineering
- [prompt engineering](/concepts/prompt-engineering.md) — the first step into systems-around-models
- [AI monitoring](/concepts/ai-monitoring.md) — the LLMOps half of the feedback loop
- [token cost](/concepts/token-cost.md) — the physical constraint driving the shift
