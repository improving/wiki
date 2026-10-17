---
title: "Running the Experiment Was Never the Hard Part"
type: "Source Summary"
description: "AlphaGo's per-move MCTS grading versus sparse end-of-episode LLM rewards, and why agent judgment lags execution."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/running-the-experiment-was-never-the-hard-part/running-the-experiment-was-never-the-hard-part.md"
---

# Running the Experiment Was Never the Hard Part — Summary

**Original source**: `references/devlinliles.com/running-the-experiment-was-never-the-hard-part/running-the-experiment-was-never-the-hard-part.md`

## Summary

Drawing on Eric Jang's Dwarkesh Patel conversation about rebuilding AlphaGo, the post contrasts AlphaGo's dense, per-move MCTS training signal with the single end-of-episode reward LLM agents get. That gap is the credit assignment problem, and it explains why agents execute experiments competently but choose research directions poorly. ResearchGym quantifies the split, and process reward models are an early attempt to close it.

## Key Claims

- Monte Carlo Tree Search graded every AlphaGo move, giving roughly 150 clean lessons per game and sidestepping credit assignment.
- A policy-gradient trajectory for an LLM agent can exceed 100,000 tokens yet ends in a single reward: the code passed or it did not.
- ResearchGym strips five oral/spotlight ICML, ICLR, and ACL papers of their methods; a GPT-5 agent completed barely a quarter of sub-tasks on average and beat the human baseline in exactly one of fifteen runs, by 11.5%.
- Performance plateaued after roughly nine hours because the agent stopped finding better ideas, not because it ran out of budget; the same shape appeared with Claude Code on Opus 4.5 and Codex on GPT-5.2.
- AgentPRM reports over 8x better compute efficiency than prior step-scoring approaches by scoring each step on progress toward the goal.
- The Go analogy has a hard limit: a research hypothesis has no ground-truth simulator, so open-ended judgment lacks a training signal.

## Relevance

Informs [process reward models](/concepts/process-reward-models.md) and [evaluation harness](/concepts/evaluation-harness.md) design in agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Grounded in a cited podcast and arXiv papers, with the analogy's limits explicitly flagged; the ResearchGym figures come from the referenced paper.

## Entities Mentioned

- [AlphaGo](/entities/alphago.md) — the dense-reward comparison point
- [Dwarkesh Patel](/entities/dwarkesh-patel.md) — host of the conversation with Eric Jang
- [GPT-5](/entities/gpt-5.md) — model behind the ResearchGym agent

## Concepts Covered

- [Process Reward Models](/concepts/process-reward-models.md) — the proposed fix for step-level credit assignment
- [evaluation harness](/concepts/evaluation-harness.md) — as used in ResearchGym's automated grading
