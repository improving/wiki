---
title: "The Bottleneck Isn't the Fix, It's Finding What to Fix"
type: "Source Summary"
description: "Coding agents' bottleneck is repository exploration, not reasoning; splitting exploration from solving cuts tokens up to 60%."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-bottleneck-isnt-the-fix-its-finding-what-to-fix/the-bottleneck-isnt-the-fix-its-finding-what-to-fix.md"
---

# The Bottleneck Isn't the Fix, It's Finding What to Fix — Summary

**Original source**: `references/devlinliles.com/the-bottleneck-isnt-the-fix-its-finding-what-to-fix/the-bottleneck-isnt-the-fix-its-finding-what-to-fix.md`

## Summary

Liles argues that the reflex to blame the model when a coding-agent pilot burns budget is aimed at the wrong layer. Two June research papers point to repository exploration as the real bottleneck. SWE-Explore shows file-level localization is largely solved and that line-level coverage and ranking efficiency separate good agents from great ones. FastContext turns that into an architecture decision: a cheap exploration subagent (4B–30B parameters) returns a short cited list of paths and line ranges, so the frontier solver never sees exploratory dead ends.

## Key Claims

- SWE-Explore derived line-level ground truth from the trajectories of agents that had already solved 848 real issues across 10 languages and 203 repositories.
- FastContext cut token consumption by up to 60% while improving end-to-end resolution by up to 5.5%, across SWE-bench Multilingual, SWE-bench Pro, and SWE-QA.
- The primary win is cost, not intelligence; a vendor pitching this as a capability leap is the tell to push back on.
- The FastContext paper was withdrawn on arXiv by the lead author (unresolved product IP) as of the post's writing, though its code and evaluation data remain public on GitHub.

## Relevance

Reframes where model-upgrade budget goes, bearing on [token cost](/concepts/token-cost.md), [model routing](/concepts/model-routing.md), and [context management](/concepts/context-management.md) in agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Strength: reads two papers side by side and flags the withdrawal and the SWE-bench-style scope limit; caveat: relies on a paper whose listing was withdrawn at time of writing.

## Entities Mentioned

- None.

## Concepts Covered

- [token cost](/concepts/token-cost.md) — the 60% reduction that dominates the result.
- [model routing](/concepts/model-routing.md) — cheap explorer versus frontier solver split.
- [Context Management](/concepts/context-management.md) — keeping dead-end searches out of the solver's context.

## Related Sources

- [Built for Demand That Hasn't Arrived](/sources/built-for-demand-that-hasnt-arrived.md)
- [Checking the Math on the $500 Million AI Spend Story](/sources/checking-the-math-on-the-500-million-ai-spend-story.md)
