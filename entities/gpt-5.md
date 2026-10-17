---
title: "GPT-5"
type: "Entity"
description: "OpenAI's frontier model, marking the point where capability kept rising while per-token prices reversed upward."
created: '2026-10-17'
updated: '2026-10-17'
tags: [model, openai, frontier]
sources:
  - "/sources/running-the-experiment-was-never-the-hard-part.md"
  - "/sources/why-now-the-capability-cost-inflection-point-that-changes-everything.md"
---

# GPT-5

GPT-5 is OpenAI's frontier language model and the endpoint of the corpus's capability-versus-cost narrative. It is cited both as an agent backbone that struggles with credit assignment and as the moment per-token prices stopped falling.

## Overview

One post contrasts AlphaGo with LLM agents: MCTS gave AlphaGo a graded target on every move, sidestepping credit assignment, while LLM agents get one reward at the end of a hundred-thousand-token trajectory. ResearchGym agents beat the human baseline in one of fifteen runs. Process reward models approximate per-step targets, but open-ended judgment remains unsolved.

The other post frames an inflection point. GPQA Diamond frontier capability rose from about 36% in 2023 to the high 80s in 2026, and per-token prices fell two orders of magnitude from GPT-3 to GPT-5 — then reversed upward. Enterprise AI bills roughly tripled as token consumption rose about 13x since January 2025.

## Key Claims

- LLM agents get one reward at the end of a hundred-thousand-token trajectory, unlike AlphaGo's per-move feedback.
- ResearchGym agents beat the human baseline in one of fifteen runs.
- Per-token prices fell two orders of magnitude from GPT-3 to GPT-5, then reversed upward.
- Enterprise AI bills roughly tripled as token consumption rose about 13x since January 2025.
- Training on human text may approach a data ceiling around 2027–2028.

## Related

- [Process Reward Models](/concepts/process-reward-models.md) — the per-step approximation it motivates
- [AlphaGo](/entities/alphago.md) — the contrast case for credit assignment
- [token cost](/concepts/token-cost.md) — the pricing reversal it anchors
- [Capability Forecasting](/concepts/capability-forecasting.md) — the trend it illustrates
- [Why Now: The Capability-Cost Inflection Point](/sources/why-now-the-capability-cost-inflection-point-that-changes-everything.md) — primary source
