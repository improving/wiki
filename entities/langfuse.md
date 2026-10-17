---
title: "Langfuse"
type: "Entity"
description: "LLM observability and evaluation platform used here for prompt management, tracing, and self-hosted eval."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, observability, evaluation]
sources:
  - "/sources/designing-ai-systems-for-change.md"
  - "/sources/if-you-cant-reconstruct-what-the-agent-did-you-dont-have-a-system.md"
  - "/sources/llm-evaluation-ai-native-applications.md"
---

# Langfuse

Langfuse is an LLM observability and evaluation platform that appears in this corpus as a place to manage prompts, as one of the OTel-native backends that avoid vendor lock-in, and as a self-hosted option in the AI evaluation tool landscape.

## Role in the Corpus

- The "designing AI systems for change" architecture playbook recommends keeping prompts in managed systems — Langfuse or PromptLayer — so they can be versioned and evaluated rather than hard-coded.
- Agent-observability writing lists Langfuse alongside [Datadog](/entities/datadog.md) and Arize Phoenix as a backend that OTel-native traces can target, so instrumentation is decoupled from the vendor.
- The LLM evaluation survey names Langfuse among the evaluation tools (with Ragas, lm-evaluation-harness, DeepEval, Promptfoo, Arize Phoenix, Evidently, Giskard, and [LangSmith](/entities/langsmith.md)); most production setups use at least three.
- Its self-hosted posture suits teams that want prompt management and tracing without sending data to a third-party SaaS.

## Related

- [LLM evaluation](/concepts/llm-evaluation.md) — the continuous quality measurement it supports
- [audit trail](/concepts/audit-trail.md) — the reconstructable decision trace it helps capture
- [OpenTelemetry GenAI semantic conventions](/entities/opentelemetry-genai-semantic-conventions.md) — the standard its traces follow
- [prompt evaluation](/concepts/prompt-evaluation.md) — testing prompts like code
