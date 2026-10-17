---
title: "The Review Bottleneck in AI-Assisted Delivery"
type: "Source Summary"
description: "AI sped up code generation but not review, making review the delivery constraint; the fix is pipeline review at a higher altitude."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/the-review-bottleneck-nobody-talks-about/the-review-bottleneck-nobody-talks-about.md"
---

# The Review Bottleneck in AI-Assisted Delivery — Summary

**Original source**: `references/devlinliles.com/the-review-bottleneck-nobody-talks-about/the-review-bottleneck-nobody-talks-about.md`

## Summary

AI coding tools made generation fast while review stayed slow, and that asymmetry now gates delivery velocity in most teams that adopted AI without redesigning evaluation. Using Theory of Constraints logic, Devlin Liles argues generation was never the bottleneck; verification was, and AI made that visible by making generation nearly free. The proposed fix is to move review from a human activity to a system activity: review becomes a pipeline stage staffed by specialized evaluation agents, with humans reviewing the system's output at a higher altitude.

## Key Claims

- An agent generates a feature in fifteen minutes while a human reviewer needs about two hours to evaluate it properly, so throughput is gated by review capacity.
- By the 90-day mark, teams report approval times longer than before AI adoption: generation got faster, delivery got slower.
- "Permission mode" (agent proposes, human approves) makes the human a throughput constraint that scales linearly while agents scale with compute; one developer overseeing ten agents approves things they have not evaluated.
- Review as a pipeline stage runs parallel specialist agents (security scanner, QA validator, architecture checker, performance profiler) with defined criteria and thresholds.
- MIT Sloan research is cited: human-AI collaboration achieves 94 percent success with governance infrastructure versus 73 percent for full autonomy.
- Objections addressed: correlated failure (answer with deterministic tools and diverse evaluators), history (older tools only checked syntax), and accountability (governance mode keeps a named human approving every release).

## Relevance

Central to the [Review Bottleneck](/concepts/review-bottleneck.md), and it engages [human-in-the-loop](/concepts/human-in-the-loop.md) oversight and the [Review Gate](/concepts/review-gate.md) as a pipeline stage.

## Quality

Practitioner blog post by Devlin Liles. Strong structure and it explicitly answers counterarguments; the 15-minute/2-hour and 1.5x figures are illustrative, and the MIT Sloan statistic is cited secondhand.

## Entities Mentioned

- [Devlin Liles](/entities/devlin-liles.md) — author
- [Herbert Simon](/entities/herbert-simon.md) — cited for "a wealth of information creates a poverty of attention"

## Concepts Covered

- [Review Bottleneck](/concepts/review-bottleneck.md) — the central thesis
- [human-in-the-loop](/concepts/human-in-the-loop.md) — permission mode and its limits
- [Review Gate](/concepts/review-gate.md) — review as an automated pipeline stage
