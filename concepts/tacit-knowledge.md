---
title: "Tacit Knowledge"
type: "Concept"
description: "Unwritten organizational and model knowledge that agents and benchmarks routinely miss, requiring deliberate capture."
created: '2026-10-17'
updated: '2026-10-17'
tags: [knowledge-management, judgment, ai]
sources:
  - "/sources/judgment-was-built-by-proxy.md"
  - "/sources/the-model-knows-more-than-its-telling-you.md"
  - "/sources/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew.md"
---

# Tacit Knowledge

Tacit knowledge is the unwritten understanding — organizational memory and dormant model capability — that never appears in the codebase or a simple prompt. Across this corpus it is treated as a resource that must be deliberately captured and elicited, because agents and benchmarks systematically miss what nobody wrote down.

## Key Claims

- A coding agent can pass every automated check yet ship a change that breaks production, because critical reasoning lives in unwritten conversations rather than the codebase.
- Clean agent PRs do not trigger the memory that makes a reviewer pause; a memory layer only surfaces knowledge someone first wrote down.
- Model capability measured by simple prompts is a function of how it was asked: [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) lifted PaLM 540B on [GSM8K](/entities/gsm8k.md) from 18% to 57%.
- [Few-Shot Prompting](/concepts/few-shot-prompting.md) activates capabilities zero-shot prompts leave dormant, so capability assessments have a shelf life.
- AI removes the routine work that was apprenticeship, widening the experience gap; curated failure libraries, intent-specification drills, and evaluation exercises teach judgment directly.

## Related

- [Capability vs Activity](/concepts/capability-vs-activity.md) — the reps that once converted activity into judgment
- [chain-of-thought prompting](/concepts/chain-of-thought-prompting.md) — eliciting dormant capability
- [Few-Shot Prompting](/concepts/few-shot-prompting.md) — activating knowledge a prompt hides
- [Your Coding Agent Doesn't Know What Your Last Three Engineers Knew](/sources/your-coding-agent-doesnt-know-what-your-last-three-engineers-knew.md) — primary source
