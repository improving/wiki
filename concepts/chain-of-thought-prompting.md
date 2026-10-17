---
title: "chain-of-thought prompting"
type: "Concept"
description: "Eliciting intermediate reasoning steps to unlock dormant capability, and the reasoning chain adversarial tracks attack."
created: '2026-10-17'
updated: '2026-10-17'
tags: [prompting, reasoning, reliability]
sources:
  - "/sources/adversarial-reasoning-architecture-a-multi-track-approach-to-ai-agent-reliability.md"
  - "/sources/the-model-knows-more-than-its-telling-you.md"
---

# chain-of-thought prompting

Chain-of-thought prompting asks a model to produce intermediate reasoning steps before its answer, which activates capability that simple prompts leave dormant. The same reasoning chain is also the surface that adversarial tracks attack, so prompting and verification are two sides of one reliability problem.

## Key Claims

- Chain-of-thought lifted PaLM 540B on GSM8K from 18% to 57%.
- Few-shot examples activate capabilities zero-shot prompts leave dormant.
- Model capability measured by simple prompts is a function of how it was asked.
- Single reasoning tracks optimize for coherence, not correctness.
- Structurally separate challengers produce harder critiques than self-critique, though sync points add roughly 40% latency.
- Route queries by complexity; dual-track cost only pays for high-stakes work.
- Capability assessments have a shelf life as prompting skill improves.

## Related

- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — the technique that activates dormant capability
- [Prompt Engineering](/concepts/prompt-engineering.md) — the broader practice
- [adversarial validators](/concepts/adversarial-validators.md) — attack the reasoning track
- [GSM8K](/entities/gsm8k.md) — the benchmark that measured the lift
- [Adversarial Reasoning Architecture: A Multi-Track Approach to AI Agent Reliability](/sources/adversarial-reasoning-architecture-a-multi-track-approach-to-ai-agent-reliability.md) — primary source
- [The Model Knows More Than It's Telling You](/sources/the-model-knows-more-than-its-telling-you.md) — primary source
