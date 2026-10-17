---
title: "The Cost of Knowing: Observability in the Age of AI Agents"
type: "Source Summary"
description: "AI workloads multiply telemetry volume, turning observability into a FinOps problem and production signals into a delivery feedback loop."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, observability, devlinliles.com]
sources:
  - "references/devlinliles.com/observability-arc-08-finops-agentic/observability-arc-08-finops-agentic.md"
---

# The Cost of Knowing: Observability in the Age of AI Agents — Summary

**Original source**: `references/devlinliles.com/observability-arc-08-finops-agentic/observability-arc-08-finops-agentic.md`

## Summary

The arc's closing post argues two forces converged: observability became a FinOps problem, and AI became both the largest new source of telemetry and its newest consumer. AI/ML workloads generate 10–100× more telemetry than traditional apps, a structural mismatch rather than a tuning problem, while enterprise observability spend grows 28% year-over-year with "no natural ceiling." Meanwhile the stack converged on [OpenTelemetry](/entities/opentelemetry.md), [Honeycomb](/entities/honeycomb.md) shipped an MCP integration letting agents query production telemetry, and observability's real value becomes the feedback loop between what ships and what production does.

## Key Claims

- Apica/Omdia (2026) put AI telemetry at 10–100× traditional volume; the Gartner data-observability market hit $346.4M in 2024 on 20.8% growth.
- Some vendors bill LLM observability on token ingestion at ~$0.10 per 1,000 tokens, so tracing full prompts and completions means paying to store tokens twice.
- OTel GenAI semantic conventions (`gen_ai.*`) exit experimental status in early 2026; AWS CloudWatch added native OTel metrics with PromQL in April 2026.
- Datadog's April 2026 trace data: 69% of input tokens were system prompts, only 28% of calls used prompt caching, and ~5% of AI requests failed — ~60% from capacity limits, not model quality.
- SLOs on AI inference endpoints with the same rigor as core APIs would catch capacity failures before users do.

## Relevance

Informs [token cost](/concepts/token-cost.md) and [model context protocol](/entities/model-context-protocol.md), and closes the observability arc on feedback loops and AI unit economics.

## Quality

Practitioner blog post by Devlin Liles. Rich with dated 2026 vendor and research figures; the fintech feedback-loop example is single-case and the volume multiplier is a planning assumption, not a measured constant.

## Entities Mentioned

- [OpenTelemetry](/entities/opentelemetry.md) — the converged instrumentation layer
- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the `gen_ai.*` schema for AI telemetry
- [Honeycomb](/entities/honeycomb.md) — shipped an MCP integration for agent telemetry queries
- [Datadog](/entities/datadog.md) — Bits AI SRE and the State of AI Engineering trace data
- [Model Context Protocol](/entities/model-context-protocol.md) — lets agents query production telemetry

## Concepts Covered

- [token cost](/concepts/token-cost.md) — token ingestion as a new observability billing unit

## Related Sources

- [Metrics, Logs, Traces — and the War That Standardization Won](/sources/observability-arc-02-opentelemetry-standardization.md)
- [Wide Events, eBPF, and Why the Three Pillars Are a Tax You're Still Paying](/sources/observability-arc-04-wide-events-ebpf.md)
