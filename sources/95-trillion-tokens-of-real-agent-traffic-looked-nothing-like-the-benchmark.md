---
title: "95 Trillion Tokens of Real Agent Traffic Looked Nothing Like the Benchmark"
type: "Source Summary"
description: "Single-turn cache benchmarks mislead capacity planning because real agent sessions are multi-turn and reuse falls off after the first exchange."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark.md"
---

# 95 Trillion Tokens of Real Agent Traffic Looked Nothing Like the Benchmark — Summary

**Original source**: `references/devlinliles.com/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark.md`

## Summary

The post argues that quoted cache-hit-rate numbers come from single-turn benchmarks, the workload serving stacks were originally built for, and therefore describe a shape that production agent traffic never actually has. A paper analyzing 95 trillion tokens of real [GitHub Copilot](/entities/github-copilot.md) agent traffic found sessions run long and in turns, so the cache-hit-rate curve bends at each turn boundary and reuse that looked strong early stops describing later turns. Sizing infrastructure off that benchmark average effectively assumes every session ends after its first exchange.

## Key Claims

- Most vendor throughput figures derive from single-turn benchmarks where the cache stays warm because there is only one turn.
- A study of 95 trillion tokens of production GitHub Copilot agent traffic found real sessions run long and in turns, so cache hit rate curves across a session.
- Turn boundary is where the reuse curve bends: early turns reuse almost everything, deeper turns interleave tool output with reasoning and age context out.
- A single-turn benchmark measures the point of highest reuse and reports it as the throughput figure, making longer sessions look cheaper to serve than they are.
- The actionable question for any vendor claim is "which turn was the number measured on?"

## Relevance

Informs [benchmark validity](/concepts/benchmark-validity.md) and capacity-planning discussions, and connects to [context management](/concepts/context-management.md) in long-running agent loops.

## Quality

Practitioner blog post by Devlin Liles. Strengths: a single, well-framed vendor-skeptical question grounded in a large production dataset. Caveats: the post summarizes the paper's findings without naming it or giving reproducible methodology, and the cache-curve shape is described qualitatively.

## Entities Mentioned

- [GitHub Copilot](/entities/github-copilot.md) — the source of the 95 trillion tokens of agent traffic analyzed

## Concepts Covered

- [benchmark-validity](/concepts/benchmark-validity.md) — single-turn benchmarks fail to represent multi-turn agent workloads

## Related Sources

- [No Model Is Consistently Good at Reading Minds](/sources/no-model-is-consistently-good-at-reading-minds.md)
