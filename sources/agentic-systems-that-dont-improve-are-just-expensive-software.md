---
title: "Agentic Systems That Don't Improve Are Just Expensive Software"
type: "Source Summary"
description: "Without a feedback loop, agentic systems stay static; reflection, PRMs, RLVR, and trajectory memory close the loop."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/agentic-systems-that-dont-improve-are-just-expensive-software/agentic-systems-that-dont-improve-are-just-expensive-software.md"
---

# Agentic Systems That Don't Improve Are Just Expensive Software — Summary

**Original source**: `references/devlinliles.com/agentic-systems-that-dont-improve-are-just-expensive-software/agentic-systems-that-dont-improve-are-just-expensive-software.md`

## Summary

Devlin Liles argues the compounding return promised by agentic AI is real only for systems with a feedback loop; without one you have expensive software plus the overhead of managing agents. He surveys mechanisms that close the loop — reflection, Reflexion, process reward models, RLVR, and trajectory-informed memory — and concludes that unglamorous harness simplification often outperforms the exotic options.

## Key Claims

- Reflection (write, critique, rewrite) adds quality at predictable cost but only improves a single output within a session and cannot catch its own blind spots.
- Reflexion stores verbal memories of past mistakes in prompts — a bridge toward, but not a structured architecture for, cross-session learning.
- Process Reward Models score intermediate steps, catching errors before they compound, but require costly step-level training data.
- DeepSeek R1 demonstrated RLVR: for objectively verifiable tasks, the environment is the reward signal, avoiding human annotation and reward-model training.
- Trajectory-informed memory compounds positive performance by reusing successful action sequences, not just cataloging failures.
- Harness simplification — removing dead instructions and gamed constraints — consistently yields more gains than model upgrades.

## Relevance

Informs [Process Reward Models](/concepts/process-reward-models.md) and [RLHF](/concepts/rlhf.md) as feedback-loop choices for agentic systems.

## Quality

Practitioner blog post by Devlin Liles. Strength: concrete, actionable patterns with a stated practical preference. Caveat: comparative claims (e.g. simplification beating model upgrades) are asserted from experience, not benchmarked.

## Entities Mentioned

- [DeepSeek R1](/entities/deepseek-r1.md) — demonstrated RLVR at scale in January 2025

## Concepts Covered

- [Process Reward Models](/concepts/process-reward-models.md) — scoring intermediate reasoning steps
- [RLHF](/concepts/rlhf.md) — the dominant but annotation-heavy alternative to RLVR

## Related Sources

- [The Twelve Problems of Agentic Software Delivery](/sources/the-twelve-problems-of-agentic-software-delivery.md)
- [What a 10 Percent Chip-Stock Selloff Over One Model Release Actually Tells You](/sources/what-a-10-percent-chip-stock-selloff-over-one-model-release-actually-tells-you.md)
- [Your Model's Confidence Is Not What You Think It Is](/sources/your-models-confidence-is-not-what-you-think-it-is.md)
