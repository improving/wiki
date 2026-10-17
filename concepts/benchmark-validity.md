---
title: "Benchmark Validity"
type: "Concept"
description: "Whether a benchmark score actually predicts real-world performance, or only measures a narrow, distorted slice of capability."
created: '2026-10-17'
updated: '2026-10-17'
tags: [evaluation, benchmarks, ai-reliability]
sources:
  - "/sources/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark.md"
  - "/sources/it-can-read-the-diagram-it-cant-reason-about-it.md"
  - "/sources/no-model-is-consistently-good-at-reading-minds.md"
  - "/sources/the-chinese-room-is-running-in-production.md"
  - "/sources/the-gap-between-coding-benchmarks-and-client-ready-software.md"
---

# Benchmark Validity

Benchmark validity is the question of whether a published score predicts behavior on real workloads. This corpus repeatedly finds the two diverging: models and systems that look strong on single-turn, textbook-shaped benchmarks fail on multi-turn traffic, relational reasoning, and merge-ready enterprise tasks.

## Key Claims

- Vendor cache-hit figures usually come from single-turn benchmarks; real agent sessions run in turns and reuse decays across turn boundaries, so infrastructure sized off those numbers understates serving cost.
- On FeynmanBench, GPT-5.5 identified diagram elements 84% of the time but derived the underlying physics only 16% of the time — a "CP3 cliff."
- Nine frontier vision-language models scored inconsistently across false-belief and animacy tasks, and no single model led both; one score describes a narrow slice, not general theory of mind.
- Coding agents resolved only 13–39% of real merge-ready enterprise tasks; Claude Opus 4.8 scored 13.4% on the hardest FrontierCode tasks, and RoadmapBench tasks touched a median of 3,700 lines across 51 files.
- Behavioral benchmark scores and causal reliability on novel inputs diverge; distribution-shifted evaluation exposes gaps that standard accuracy tests hide.

## Related

- [Distribution shift](/concepts/distribution-shift.md) — the failure mode benchmarks hide
- [Goodhart's law](/concepts/goodharts-law.md) — why optimizing the metric breaks it
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — the ceiling problem
- [End-to-End Success Rate](/concepts/end-to-end-success-rate.md) — a validity-respecting metric
- [GPT-5.5](/entities/gpt-5-5.md) — measured on FeynmanBench
- [The Chinese Room Is Running in Production](/sources/the-chinese-room-is-running-in-production.md) — primary source
