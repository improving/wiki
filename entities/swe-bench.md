---
title: "SWE-bench"
type: "Entity"
description: "Software-engineering benchmark for coding agents whose contamination, broken tests, and harness sensitivity make scores unreliable."
created: '2026-10-17'
updated: '2026-10-17'
tags: [benchmark, evaluation, coding-agents]
sources:
  - "/sources/cost-adjusted-capacity-when-tokens-stop-converting-to-mergeable-prs.md"
  - "/sources/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation.md"
  - "/sources/not-every-ticket-needs-the-250000-engineer.md"
  - "/sources/the-open-weight-cost-curve-is-an-architecture-story.md"
  - "/sources/the-plan-was-right-when-you-made-it.md"
  - "/sources/you-cant-improve-what-you-cant-measure-agentic-evaluation-done-right.md"
---

# SWE-bench

SWE-bench is the benchmark most often cited for coding-agent capability. In this corpus it is both a useful reference point and a cautionary tale about benchmark validity: contamination, broken tests, and harness choices all move its scores.

## Overview

Writers warn that SWE-bench Verified problems were audited with 59.4 percent showing broken tests, that frontier models could reproduce gold patches from hints, and that harness choice moved scores more than model choice. It remains useful for relative comparisons, and open-weight results like a 32B model reaching 36.6 percent show targeted training can close gaps.

## Key Claims

- SWE-bench Verified problems were audited and 59.4 percent had broken tests.
- Frontier models could reproduce gold patches from hints, indicating contamination.
- Harness choice moved scores more than model choice and flipped rankings.
- Static benchmarks freeze environment state, assuming the world holds still.
- Targeted training scaled a 32B open model to 36.6 percent on SWE-bench Verified.

## Related

- [Benchmark Validity](/concepts/benchmark-validity.md) — the concern these results raise
- [Benchmark Saturation](/concepts/benchmark-saturation.md) — why static scores lose meaning
- [evaluation harness](/concepts/evaluation-harness.md) — the variable that shifts rankings
- [METR](/entities/metr.md) — parallel evidence on graded versus human mergeability
- [Five Questions Before a Vendor's Benchmark](/sources/five-questions-i-ask-before-a-vendors-benchmark-goes-in-a-client-recommendation.md) — primary source
