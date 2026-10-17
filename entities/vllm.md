---
title: "vLLM"
type: "Entity"
description: "Open-source LLM serving engine known for high-throughput scheduling and KV-cache management, used here as the reference self-hosted inference stack."
created: '2026-10-17'
updated: '2026-10-17'
tags: [inference, serving, open-source]
sources:
  - "/sources/parallel-decode-is-the-inference-bet-nobodys-marketing-yet.md"
  - "/sources/what-youre-actually-buying-when-you-choose-managed-inference.md"
---

# vLLM

An open-source large-language-model serving engine, widely used for self-hosted inference because of its throughput-oriented scheduling and KV-cache management. In this corpus it represents the serving layer whose engineering — not the model weights — usually determines self-hosted inference cost, and the stack that new decoding schemes must fit into.

## Overview

The serving layer decides most self-hosted inference economics: scheduling, KV-cache, routing, and power tuning are the work that managed vendors bundle. A parallel-decode source notes that existing serving frameworks, including those in the vLLM lineage, assume KV cache and [speculative decoding](/concepts/speculative-decoding.md); Google DeepMind's DiffusionGemma instead generates tokens in parallel via diffusion at roughly 1,500 tokens per second on a single H100, but lacks serving-stack support. Managed vendors market the same layer with techniques like NEAT (22–28% fewer reasoning tokens) and KAIROS (up to 46% lower agentic serving power draw).

## Key Claims

- The serving layer, not the model, usually decides self-hosted inference costs
- Existing serving frameworks assume KV cache and speculative decoding
- DiffusionGemma produces roughly 1,500 tokens per second on a single H100
- INFRAMIND's queue-aware orchestration holds 99.9% SLO compliance under load

## Related

- [Speculative Decoding](/concepts/speculative-decoding.md) — an assumption baked into vLLM-lineage servers
- [Open-Weight Models](/concepts/open-weight-models.md) — the weights vLLM typically serves
- [Token Cost](/concepts/token-cost.md) — the economics the serving layer governs
- [What You're Actually Buying When You Choose Managed Inference](/sources/what-youre-actually-buying-when-you-choose-managed-inference.md) — primary source
