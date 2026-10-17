---
title: "Ollama"
type: "Entity"
description: "Tool for running local LLMs, used here for sovereign, offline-capable work such as CVE triage and data-transfer demos."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai, security, local-inference]
sources:
  - "/sources/human-cost-security-ai-era.md"
  - "/sources/your-prompt-is-a-cross-border-data-transfer.md"
---

# Ollama

Ollama is a tool for running large language models locally. It appears in this corpus as the practical way to keep inference on-premise for workloads where data sovereignty, offline resilience, and predictable economics matter more than raw capability.

## Role in the Corpus

- A CVE-triage demo (Python 3.8+, Ollama, qwen3.5) reads a CVE record, dependency manifests, and source code, using a structured six-step reasoning scaffold that can return "NOT AFFECTED" even when a scanner already filed a report.
- Local models suit CVE triage for [data sovereignty](/concepts/data-sovereignty.md), offline resilience during incident response, no cross-customer exposure, fewer credentials to defend, and predictable economics.
- In an AI-sovereignty demo, an LLM router toggles between local Ollama and cloud [Gemini](/entities/gemini.md), with an [OpenTelemetry](/entities/opentelemetry.md) collector tracing where each request went.

## Related

- [data sovereignty](/concepts/data-sovereignty.md) — the reason to run models locally
- [AI sovereignty](/concepts/ai-sovereignty.md) — the broader architecture argument
- [software supply chain security](/concepts/software-supply-chain-security.md) — the triage workload Ollama serves
- [vLLM](/entities/vllm.md) — the high-throughput self-hosted inference alternative
