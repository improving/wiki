---
title: "Structured Recovery Orchestration for AI Agents: Beyond Retry"
type: "Source Summary"
description: "A seven-phase recovery pipeline that classifies agent failures and routes them beyond blind retry, warranted at ten-plus parallel agents."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/structured-recovery-orchestration-for-ai-agents-beyond-retry/structured-recovery-orchestration-for-ai-agents-beyond-retry.md"
---

# Structured Recovery Orchestration for AI Agents: Beyond Retry — Summary

**Original source**: `references/devlinliles.com/structured-recovery-orchestration-for-ai-agents-beyond-retry/structured-recovery-orchestration-for-ai-agents-beyond-retry.md`

## Summary

Distinguishes transient agent failures (network errors, rate limits — retry works) from structural failures (ambiguous specs, stale context, missing dependencies — retry reproduces the error). Drawing on Jim Gray's Heisenbug/Bohrbugs split, it presents a seven-phase recovery pipeline that classifies failures programmatically and routes each type to the right response.

## Key Claims

- Retry is a Heisenbug tool; most agent failures that matter are Bohrbugs that survive retry.
- Seven phases: evidence collection, root-cause classification, confidence-gated routing, human collaboration, guidance synthesis, instrumented re-entry, and prevention learning.
- Classification runs an LLM-based diagnostic over an evidence bundle, producing a failure type from a taxonomy plus a confidence score.
- A confidence threshold (about 80% to start) decides automatic recovery versus human review; a task failing twice escalates regardless.
- Prevention learning writes labeled failure/resolution examples to a shared store so common failure modes become constraints.
- The pipeline pays for itself around 10 or more parallel agents; below that scale it is over-engineering.

## Relevance

Extends agent reliability and [runtime governance](/concepts/runtime-governance.md), connecting [confidence thresholds](/concepts/confidence-thresholds.md) and [human-in-the-loop](/concepts/human-in-the-loop.md) review to structured agent recovery.

## Quality

Practitioner blog post by Devlin Liles. Describes a system refined over months of operating agents at scale; concrete and candid about its limits, though it reports no quantitative results.

## Entities Mentioned

- [Jim Gray](/entities/jim-gray.md) — source of the Heisenbug/Bohrbugs distinction

## Concepts Covered

- [Confidence Thresholds](/concepts/confidence-thresholds.md) — confidence-gated routing
- [human-in-the-loop](/concepts/human-in-the-loop.md) — structured human review handoff
- [runtime governance](/concepts/runtime-governance.md) — classification and routing as governance

## Related Sources

- [Engineering Reliability into Autonomous AI Agents](/sources/engineering-reliability-into-autonomous-ai-agents.md)
