---
title: "Read the Accuracy Number Next to the Cost Number"
type: "Source Summary"
description: "Routing savings percentages need a paired accuracy metric, measured on the client's workload and on the hardest requests."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/read-the-accuracy-number-next-to-the-cost-number/read-the-accuracy-number-next-to-the-cost-number.md"
---

# Read the Accuracy Number Next to the Cost Number — Summary

**Original source**: `references/devlinliles.com/read-the-accuracy-number-next-to-the-cost-number/read-the-accuracy-number-next-to-the-cost-number.md`

## Summary

The post argues that a model-routing savings percentage without an adjacent accuracy number is a marketing claim with a decimal point. A router is a classifier that bets on every request, and its error rate is a quality problem before it is a cost problem: a hard request sent to a cheap model produces a worse answer that ships anyway while the cost figure looks identical. The discipline is to require an accuracy metric measured on a workload close to the client's own and holding up on the hardest requests.

## Key Claims

- NVIDIA's NeMo Switchyard launched August 11 alongside Nemotron 3.5 Lightning, packaging routing as an out-of-the-box feature; partners LangChain, Cognition, Ramp, and Classmethod's DevelopersIO published savings.
- The accuracy metric must travel with the cost number — same slide, same paragraph, same sentence; footnotes and follow-up posts are too late.
- Routing accuracy is a property of a router paired with a specific workload; a partner's disclosed number describes their traffic, not a client's ticket queue.
- An aggregate accuracy figure can hide a much worse failure rate on the hardest, highest-cost requests (security-sensitive refactors, cross-service changes, load-dependent bugs).
- Producing the accuracy number requires holding out real requests, running both paths, and comparing answers — slower and less flattering than the cost number.

## Relevance

Informs [model routing](/concepts/model-routing.md) and the demand that claims be [benchmark-valid](/concepts/benchmark-validity.md) for the workload at hand.

## Quality

Practitioner blog post by Devlin Liles. A clear, opinionated argument citing vendor disclosures; it is commentary, not an independent measurement, and offers no new data of its own.

## Entities Mentioned

- [Nvidia](/entities/nvidia.md) — ships NeMo Switchyard
- [LangChain](/entities/langchain.md) — partner that published routing savings
- [Cognition](/entities/cognition.md) — partner whose benchmark reflects autonomous-agent traffic

## Concepts Covered

- [model routing](/concepts/model-routing.md) — main topic
- [Benchmark Validity](/concepts/benchmark-validity.md) — accuracy must be measured on a relevant workload

## Related Sources

- [Using Evaluation Data to Match Model Capability to Task Requirements](/sources/using-evaluation-data-to-match-model-capability-to-task-requirements.md)
