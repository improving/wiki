---
title: "Eval-Driven Development: The Discipline Agent Teams Are Missing"
type: "Source Summary"
description: "Eval-driven development applies TDD discipline to AI agents by writing evals first, across deterministic, model-graded, and human review tiers."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-evals, devlinliles.com]
sources:
  - "references/devlinliles.com/eval-driven-development-the-discipline-agent-teams-are-missing/eval-driven-development-the-discipline-agent-teams-are-missing.md"
---

# Eval-Driven Development: The Discipline Agent Teams Are Missing — Summary

**Original source**: `references/devlinliles.com/eval-driven-development-the-discipline-agent-teams-are-missing/eval-driven-development-the-discipline-agent-teams-are-missing.md`

## Summary

With 57% of organizations running AI agents in production, quality is the top barrier to deploying more. The failure is not the model; teams never defined what "correct" meant before building. Eval-driven development imports test-driven development's discipline — write the eval before the agent — using datasets of inputs and expected outputs or properties run against every build. It spans three tiers run in sequence: deterministic checks, model-graded judgment, and selective human review.

## Key Claims

- 57% of organizations have AI agents in production (McKinsey QuantumBlack), and quality is the number-one barrier to deploying more.
- Agent outputs vary across runs, model versions, prompts, and tool states, so TDD's deterministic contract does not transfer directly.
- Agentic evals assess trajectories, not responses: whether each tool call was necessary, whether parameters were correct, and whether errors were handled.
- AgentBench (ICLR 2024) evaluated LLMs as agents across eight environments, exposing a commercial/open-source gap invisible in single-turn benchmarks.
- A 10-step chain at 95% per step succeeds about 60% of the time; at 20 steps, under 36%.
- Run tiers in order — string comparisons are free, so do not pay for LLM judgment on failures a regex catches.
- Anthropic's Claude Code team started from 20-50 real production failures, not synthetic examples, then expanded as new failure modes emerged.

## Relevance

Informs [test-driven development](/concepts/test-driven-development.md), [evals-as-code](/concepts/evals-as-code.md), [golden dataset](/concepts/golden-dataset.md), [model-as-judge](/concepts/model-as-judge.md), and [evaluation harness](/concepts/evaluation-harness.md) practice.

## Quality

Practitioner blog post by Devlin Liles. Practical and well-cited (McKinsey, AgentBench, Anthropic); the 57% figure and tool recommendations are time-sensitive.

## Entities Mentioned

- [AgentBench](/entities/agentbench.md) — first systematic agent benchmark across eight environments
- [Braintrust](/entities/braintrust.md) — recommended eval tooling across providers
- [LangSmith](/entities/langsmith.md) — recommended tooling inside LangChain/LangGraph
- [Claude Code](/entities/claude-code.md) — team whose eval suite the post cites as a model

## Concepts Covered

- [test-driven development](/concepts/test-driven-development.md) — the discipline evals import and adapt
- [evals-as-code](/concepts/evals-as-code.md) — evals as a versioned suite run on every build
- [golden dataset](/concepts/golden-dataset.md) — datasets of inputs and expected outputs/properties
- [model-as-judge](/concepts/model-as-judge.md) — the model-graded tier for subjective qualities
