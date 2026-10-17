---
title: "Spec-Driven Development for AI: What Works, What Doesn't, and What to Do About It"
type: "Source Summary"
description: "Spec-driven development separates spec, documentation, and test for agents, but has hard limits that enthusiasts understate."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md"
---

# Spec-Driven Development for AI: What Works, What Doesn't, and What to Do About It — Summary

**Original source**: `references/devlinliles.com/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it/spec-driven-development-for-ai-what-works-what-doesnt-and-what-to-do-about-it.md`

## Summary

The post argues that treating one prompt as spec, documentation, and test simultaneously does none of the three well, and that spec-driven development for agents separates them: define output schemas, [acceptance criteria](/concepts/acceptance-criteria.md), and tool contracts before the agent runs. It cites [AWS Kiro](/entities/aws-kiro.md)'s three-file pattern (requirements in EARS notation, design, tasks) and Anthropic's decomposition of its model specification into 205 atomic, testable tenets. But it insists the discipline solves only part of the reliability problem and catalogues where specs break.

## Key Claims

- Spec-driven development borrows directly from test-driven development: define "correct" before building.
- [Distribution shift](/concepts/distribution-shift.md) kills the spec — accuracy drops up to 54% under prompt perturbation with no change to model or spec.
- Error handling is where specs are most incomplete and LLMs least reliable; constraint accumulation also degrades performance (arXiv:2605.06445).
- Version drift is silent: a prompt correct yesterday may fail after a model update, and a spec alone will not reveal it.
- [Model Context Protocol](/entities/model-context-protocol.md) is the canonical under-specified tool contract — it describes what a tool does but not when it may be called; 99 MCP-related CVEs were published in 2025.
- The ABC framework's Drift Bounds Theorem: if recovery rate exceeds natural drift rate, behavioral drift converges to a predictable ceiling.

## Relevance

Informs [acceptance criteria](/concepts/acceptance-criteria.md), [distribution shift](/concepts/distribution-shift.md), and [tool calling](/concepts/tool-calling.md) contracts in agentic delivery.

## Quality

Practitioner blog post by Devlin Liles. Densely sourced with named papers and platforms, but several arXiv references are not independently verifiable here and the 54% figure is quoted without its experimental detail.

## Entities Mentioned

- [AWS Kiro](/entities/aws-kiro.md) — operationalizes the three-file spec pattern.
- [Model Context Protocol](/entities/model-context-protocol.md) — cited as the canonical under-specified tool contract.
- [OpenAI](/entities/openai.md) — its strict: true mode enforces output schemas as inter-agent contracts.

## Concepts Covered

- [acceptance criteria](/concepts/acceptance-criteria.md) — must be unambiguous and machine-testable, not prose.
- [Distribution shift](/concepts/distribution-shift.md) — the property that makes specs fail under drifted inputs.
- [test-driven development](/concepts/test-driven-development.md) — the discipline spec-driven development borrows from.
- [Tool Calling](/concepts/tool-calling.md) — tool contracts should specify when a tool may be invoked, not just what it does.

## Related Sources

- [Coherent But Wrong - The Case for a Second Planning Checkpoint](/sources/coherent-but-wrong-the-case-for-a-second-planning-checkpoint.md)
