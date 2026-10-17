---
title: "Cognition"
type: "Entity"
description: "Maker of the Devin coding agent, cited as a case study in benchmark-versus-production gaps and model-tiering economics."
created: '2026-10-17'
updated: '2026-10-17'
tags: [organization, vendor, coding-agent, benchmarks]
sources:
  - "/sources/read-the-accuracy-number-next-to-the-cost-number.md"
  - "/sources/the-gap-between-coding-benchmarks-and-client-ready-software.md"
  - "/sources/tiering-isnt-one-decision-its-five.md"
  - "/sources/the-ai-value-question-has-an-answer-now.md"
---

# Cognition

Cognition is the company behind the [Devin](/entities/devin.md) coding agent. Across this corpus it appears as a reference point for the gap between coding-agent demos and client-ready software, for the model-tiering and routing decisions that determine real cost, and — uniquely — as a vendor willing to put money behind its claims.

## Overview

- FrontierCode graded merge-readiness with maintainers; Claude Opus 4.8 scored 13.4% on the hardest tasks.
- SaaSBench found over 95% of agent failures happen before the agent reaches business logic.
- RoadmapBench tasks touch a median of 3,700 lines across 51 files, so demos measure a different job than production modernization.
- Splitting plan and execution across models cut cost 35–41% at equal performance.
- Routing accuracy is a property of a router paired with a specific workload; aggregate accuracy can hide worse failure rates on the hardest requests.
- Cognition's $10M AI Productivity Guarantee makes Devin's value financially accountable: if it does not deliver the estimated engineering benefit, Cognition funds usage up to $10M ([the AI value question has an answer now](/sources/the-ai-value-question-has-an-answer-now.md)).
- The guarantee requires estimating human-equivalent engineering hours per session, which is what turns ROI talk into receipts.
- It stands against the Uber case, where an entire 2026 AI budget was spent in four months with no comparable measure of value returned.

## Related

- [Devin](/entities/devin.md) — its coding agent
- [Benchmark Validity](/concepts/benchmark-validity.md) — why demos overstate delivered capability
- [model routing](/concepts/model-routing.md) — the cost lever across five layers of the stack
- [SWE-bench](/entities/swe-bench.md) — the benchmark whose limits these findings challenge
- [AI ROI measurement](/concepts/ai-roi-measurement.md) — the guarantee turns value claims into measurable receipts
- [The Gap Between Coding Benchmarks and Client-Ready Software](/sources/the-gap-between-coding-benchmarks-and-client-ready-software.md) — primary source
