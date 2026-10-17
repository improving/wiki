---
title: "AlphaGo"
type: "Entity"
description: "DeepMind's Go-playing system, cited as the reference case for per-move feedback and hybrid neural-symbolic search."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, reinforcement-learning, search]
sources:
  - "/sources/hybrid-intelligence-neural-symbolic-governance.md"
  - "/sources/running-the-experiment-was-never-the-hard-part.md"
---

# AlphaGo

[Google DeepMind](/entities/google-deepmind.md)'s Go-playing system, used throughout this corpus as the counterexample that clarifies what current LLM agents still lack.

## Overview

AlphaGo combined a neural network with Monte Carlo Tree Search — neural capability plus a symbolic search structure — and it received a graded signal on every move. Both properties are invoked as contrasts to modern agent architectures.

## Key Claims

- MCTS gave AlphaGo a graded target on every move, sidestepping the credit assignment problem that plagues long-horizon learning.
- LLM agents, by contrast, get a single reward at the end of a hundred-thousand-token trajectory; in the cited ResearchGym experiments, agents beat the human baseline in only one of fifteen runs.
- [Process reward models](/concepts/process-reward-models.md) approximate AlphaGo's per-step targets, but open-ended judgment remains unsolved.
- As a hybrid of neural and search components, AlphaGo supports the corpus's [hybrid intelligence](/concepts/hybrid-intelligence.md) argument that neural capability without symbolic constraints produces unpredictable output, while symbolic constraints without neural capability produce brittle compliance.

## Related

- [Hybrid intelligence](/concepts/hybrid-intelligence.md) — the neural-plus-symbolic architecture it exemplifies
- [Process Reward Models](/concepts/process-reward-models.md) — the modern attempt to recover per-step feedback
- [Google DeepMind](/entities/google-deepmind.md) — its creator
- [Running the Experiment Was Never the Hard Part](/sources/running-the-experiment-was-never-the-hard-part.md) — primary source
