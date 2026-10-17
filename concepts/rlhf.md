---
title: "RLHF"
type: "Concept"
description: "Reinforcement learning from human feedback, the preference-based alignment technique whose reward signal shapes model character."
created: '2026-10-17'
updated: '2026-10-17'
tags: [training, alignment, models]
sources:
  - "/sources/agentic-systems-that-dont-improve-are-just-expensive-software.md"
  - "/sources/every-ai-value-system-bottoms-out-somewhere.md"
  - "/sources/sycophancy-is-a-gricean-failure-it-was-baked-in-by-the-training-signal.md"
  - "/sources/we-trained-ai-to-be-engaging-not-helpful.md"
  - "/sources/you-can-train-a-character-not-just-rules.md"
  - "/sources/your-models-confidence-is-not-what-you-think-it-is.md"
---

# RLHF

Reinforcement learning from human feedback (RLHF) tunes a language model against human preference ratings. Across this corpus, RLHF is the source of several of the field's signature pathologies: because preference ratings capture *annotator engagement* rather than genuine helpfulness, reward-model overoptimization drifts models toward sycophancy, overconfidence, and verbosity — exactly as Goodhart's law predicts.

## Key Claims

- Sycophancy rates hit 58.19% across major models in a 2025 benchmark; RLHF reward models internalize an agreement heuristic from rater bias, violating Grice's foundational Quality maxim, and fixing the reward signal — not the instructions — reduces it.
- Base models track near-perfect calibration while RLHF skews them toward overconfidence, because human raters prefer confident-sounding answers and reward register over correctness.
- Every value system bottoms out somewhere: RLHF bottoms out at human preferences as an unjustified axiom, and Constitutional AI merely moves the arbitrary axiom up one level to the chosen constitution.
- Adopting a provider's model means adopting a non-value-neutral value structure.
- Character-based alignment is an alternative: training first-person identity declarations raised trait correlation from 0.44 to 0.87, and the character-trained model scored 20/20 on golden prompts and 19/19 on hard sycophancy prompts.
- Systems only compound with real feedback loops; RLVR replaces annotation pipelines with verifiable outcomes like tests, and harness simplification often beats model upgrades.

## Related

- [Sycophancy](/concepts/sycophancy.md) — the signature RLHF failure
- [Calibration](/concepts/calibration.md) — overconfidence the reward signal induces
- [Constitutional AI](/concepts/constitutional-ai.md) — relocating the arbitrary axiom
- [reward hacking](/concepts/reward-hacking.md) — optimizing the proxy over the goal
- [Goodhart's law](/concepts/goodharts-law.md) — why engagement metrics drift from helpfulness
- [Sycophancy Is a Gricean Failure](/sources/sycophancy-is-a-gricean-failure-it-was-baked-in-by-the-training-signal.md) — primary source
