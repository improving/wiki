---
title: "If You Can't Reconstruct What the Agent Did, You Don't Have a System"
type: "Source Summary"
description: "Argues agent observability must reconstruct a session's reasoning chain, and that OpenTelemetry GenAI semconv is the standard to instrument against."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md"
---

# If You Can't Reconstruct What the Agent Did, You Don't Have a System — Summary

**Original source**: `references/devlinliles.com/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md`

## Summary

Liles argues agentic systems need an audit capability beyond traditional logs: what the agent saw, decided, why, and did—the chain of reasoning, not just the chain of effects. Most production teams have logging but cannot reconstruct a session's full decision trace, and he contends OpenTelemetry's GenAI semantic conventions are the emerging standard to bet on.

## Key Claims

- The agent observability market grows from $1.97B in 2025 to an estimated $2.69B in 2026 (~mid-30s% CAGR), a signal that deployments are outpacing the infrastructure to observe them.
- OTel GenAI semconv defines four span operation types—`create_agent`, `invoke_agent`, `invoke_workflow`, and `execute_tool`—enabling reconstruction of the full execution tree.
- Datadog adopted the conventions natively from v1.37 (December 2025); OTel-native traces avoid vendor lock-in across backends like Datadog, Langfuse, and Arize Phoenix.
- Good auditing captures session genealogy, context snapshots (which make replay possible), and raw tool-call records separate from what the agent claimed it did.
- Compliance requires append-only, tamper-evident logs; for code-writing agents, git-based worktrees give the most complete change record.

## Relevance

Establishes the observability precondition for every governance capability; informs [audit trails](/concepts/audit-trail.md) and the tooling landscape around [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md), [OpenTelemetry](/entities/opentelemetry.md), [Datadog](/entities/datadog.md), and [LangSmith](/entities/langsmith.md).

## Quality

Practitioner blog post by Devlin Liles. Concrete standards, versions, and market figures with cited sources; the vendor-selection guidance is opinionated, and the market-size numbers come from a third-party buyer's guide.

## Entities Mentioned

- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the emerging tracing standard the post recommends
- [OpenTelemetry](/entities/opentelemetry.md) — the interoperability layer that avoids vendor lock-in
- [Datadog](/entities/datadog.md) — adopted the conventions natively in v1.37
- [LangSmith](/entities/langsmith.md) — the obvious first move on LangChain or LangGraph stacks

## Concepts Covered

- [Audit Trail](/concepts/audit-trail.md) — extended from API calls and writes to the reasoning chain

## Related Sources

- [Closing the Loop: The Graduated Case for Self-Healing Systems](/sources/observability-arc-07-self-healing-remediation.md)
