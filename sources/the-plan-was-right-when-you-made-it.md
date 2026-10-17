---
title: "The Plan Was Right When You Made It"
type: "Source Summary"
description: "Static benchmarks freeze the world while agents reason; a Stanford-led paper shows planning agents collapse when environments move on a fixed clock."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/the-plan-was-right-when-you-made-it/the-plan-was-right-when-you-made-it.md"
---

# The Plan Was Right When You Made It — Summary

**Original source**: `references/devlinliles.com/the-plan-was-right-when-you-made-it/the-plan-was-right-when-you-made-it.md`

## Summary

Uses a paper on real-time reasoning in evolving environments to argue that production agents fail because the world moves while they think. Benchmarks freeze a repo snapshot for reproducibility — right for benchmarks, wrong for production, where the ticket queue and codebase keep moving. The paper's Real-Time Reasoning Gym steps the environment forward on a fixed clock regardless of whether the agent has finished thinking, and both reactive and planning agents collapse under pressure. The authors' AgileThinker runs a reactive thread and a planning thread concurrently, letting the fast thread read the slow thread's unfinished reasoning, and it holds up far better.

## Key Claims

- Reactive agents (fixed token budget) fall from 89 to 15 as task difficulty rises; planning agents fall from 92 to 5 as the clock tightens.
- The Real-Time Reasoning Gym uses Freeway, Snake, and single-agent Overcooked, firing a default action if the agent has not acted when the clock ticks.
- AgileThinker held at 58 under the same time pressure that collapsed the planning agent from 92 to 5, and at 89 in real-time Overcooked where the planner scored zero.
- The authors validated against real API latency on DeepSeek's endpoint, finding a near-perfect linear relationship between token count and wall-clock time (R² of 0.9986).
- Every experiment ran on DeepSeek V3 and R1, because closed frontier models do not expose the raw reasoning stream the reactive thread depends on.

## Relevance

Informs [Benchmark Validity](/concepts/benchmark-validity.md), [checkpointing](/concepts/checkpointing.md), and the agentic-delivery theme of planning against a world that keeps moving.

## Quality

Practitioner blog post by Devlin Liles. Grounded in a specific paper with named figures and an honest limitations section; single-paper evidence, with transfer to closed frontier models left untested.

## Entities Mentioned

- [SWE-bench](/entities/swe-bench.md) — cited example of a frozen-snapshot benchmark
- [DeepSeek](/entities/deepseek.md) — the model family the experiments ran on

## Concepts Covered

- [Benchmark Validity](/concepts/benchmark-validity.md) — static benchmarks cannot see this failure mode
- [checkpointing](/concepts/checkpointing.md) — the coarser checkpoint-and-replan patch it contrasts with AgileThinker

## Related Sources

- [Cost-Adjusted Capacity: When Tokens Stop Converting to Mergeable PRs](/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md)
- [Five Questions I Ask Before a Vendor's Benchmark Goes in a Client Recommendation](/sources/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation.md)
