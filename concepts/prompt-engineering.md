---
title: "Prompt Engineering"
type: "Concept"
description: "Shaping model output by establishing a language game in the prompt rather than issuing literal instructions."
created: '2026-10-17'
updated: '2026-10-17'
tags: [llm, prompting, evals]
sources:
  - "/sources/ai-evals-have-a-replication-problem.md"
  - "/sources/prompt-engineering-is-just-wittgenstein-with-a-gpu.md"
  - "/sources/ship-faster-with-ai-series.md"
---

# Prompt Engineering

Prompt engineering is the practice of framing a model's task through a system prompt and worked examples. One post argues it works less by instruction than by establishing a Wittgensteinian language game whose implicit norms bias a probability distribution; another shows that because prompts are rarely documented, published results built on them are hard to reproduce. In practice it is also the day-to-day interface to a prompt-driven development environment: [ship faster with AI series](/sources/ship-faster-with-ai-series.md) treats prompting as the working layer of a live build rather than a one-off trick.

## Key Claims

- System prompts establish language games, not instructions the model explicitly follows.
- A prompt biases a probability distribution rather than guaranteeing outputs.
- Game-based framing generalizes to edge cases better than enumerated rules; game contamination occurs when user register overrides the intended framing.
- Published benchmark scores hide the exact prompts, parameters, and test selection that produced them.
- The same model and prompt reproduce, but any variation drops consistency sharply.
- Build persistent eval suites against pinned model versions instead of ad hoc runs.
- Prompt-driven environments make prompting a standing part of the workflow: Improving's *Ship Faster with AI* series builds a real feature in its Engage platform live on camera, with prompting as the interface to the tooling rather than a demo prop ([ship faster with AI series](/sources/ship-faster-with-ai-series.md)).

## Related

- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — examples that seed the game
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — a reasoning-oriented framing
- [Replication Crisis](/concepts/replication-crisis.md) — why undocumented prompts undermine claims
- [Version Pinning](/concepts/version-pinning.md) — keeps prompts tied to a fixed model
- [AI Evals Have a Replication Problem](/sources/ai-evals-have-a-replication-problem.md) — primary source
- [Ship Faster with AI Series](/sources/ship-faster-with-ai-series.md) — prompting in a live build
