---
title: "Daniel Kahneman"
type: "Entity"
description: "Psychologist whose work on fast versus slow thinking is invoked to argue that more reasoning tokens do not mean better answers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [psychology, reasoning, decision-making]
sources:
  - "/sources/adversarial-reasoning-architecture-a-multi-track-approach-to-ai-agent-reliability.md"
  - "/sources/your-model-is-overthinking-it-and-getting-it-wrong.md"
---

# Daniel Kahneman

Daniel Kahneman is a psychologist whose two-system account of fast, intuitive thinking versus slow, deliberate reasoning is invoked across this corpus to explain why AI agents fail and how to structure their reasoning.

## Overview

One post proposes an adversarial reasoning architecture in which a structurally separate challenger track attacks the primary chain. Because a single track optimizes for coherence rather than correctness, an independent challenger produces harder critiques than self-critique; sync points improve integration but add roughly 40 percent latency, so dual-track cost only pays for high-stakes work.

A companion post argues that more reasoning tokens do not mean more correct answers. Wrong answers in extended thinking accumulate more tokens than correct ones, accuracy peaks and then declines past an optimal thinking length, and enabling extended thinking everywhere degrades simple tasks and doubles cost. Both posts conclude that tasks should be routed by complexity.

## Key Claims

- Single reasoning tracks optimize for coherence, not correctness
- Structurally separate challengers produce harder critiques than self-critique
- Sync points improve integration but add roughly 40% latency
- Wrong answers in extended thinking accumulate more reasoning tokens than correct ones
- Accuracy peaks then declines past an optimal thinking length
- Enabling extended thinking everywhere degrades simple tasks and doubles cost

## Related

- [adversarial validators](/concepts/adversarial-validators.md) — the challenger-track idea
- [Confidence-Correctness Gap](/concepts/confidence-correctness-gap.md) — confident but wrong answers
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — the reasoning-token tradeoff
- [model routing](/concepts/model-routing.md) — routing hard tasks to more compute
- [Herbert Simon](/entities/herbert-simon.md) — adjacent theorist of bounded rationality
- [Your Model Is Overthinking It — And Getting It Wrong](/sources/your-model-is-overthinking-it-and-getting-it-wrong.md) — primary source
