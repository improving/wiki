---
title: "What You're Actually Buying When You Choose Managed Inference"
type: "Source Summary"
description: "Managed inference sells the serving-layer engineering — scheduling, caching, routing, power tuning — that self-hosting teams must otherwise build themselves."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, ai-economics, devlinliles.com]
sources:
  - "references/devlinliles.com/what-youre-actually-buying-when-you-choose-managed-inference/what-youre-actually-buying-when-you-choose-managed-inference.md"
---

# What You're Actually Buying When You Choose Managed Inference — Summary

**Original source**: `references/devlinliles.com/what-youre-actually-buying-when-you-choose-managed-inference/what-youre-actually-buying-when-you-choose-managed-inference.md`

## Summary

The author argues that when a self-hosted agent deployment costs far more than the model's pricing page implies, the money is usually lost in the serving layer underneath the model, not in model choice. Drawing on the "Taming the Titans" survey and three subsequent papers, he shows how scheduling, early exit, power tuning, and queue-aware routing translate directly into cost and latency. Managed services like Azure OpenAI and Bedrock are largely selling this engineering already built and amortized, so due diligence should probe the serving layer rather than the model name.

## Key Claims

- NEAT uses neuron activation to exit reasoning early, cutting token generation 22–28 percent across four benchmarks and six models with accuracy held constant.
- KAIROS treats context growth as the power control signal, cutting average power draw 27 percent per instance, up to 39.8 percent at peak, and 46.3 percent across a coordinated fleet on H100s running vLLM.
- INFRAMIND feeds queue depth, KV-cache pressure, and real latency into [model routing](/concepts/model-routing.md), holding 99.9 percent SLO compliance at high load where load-blind baselines fall below 50 percent, with up to 7x lower latency.
- Self-hosting an open-weight model means inheriting the serving-layer problem unless the platform team builds comparable engineering.

## Relevance

Frames managed-versus-self-hosted inference as a build-versus-buy decision over serving infrastructure, informing cost and platform strategy.

## Quality

Practitioner blog post by Devlin Liles. Well structured around three cited papers with concrete figures; the cost conclusions are the author's inference from those results.

## Entities Mentioned

- [Azure OpenAI](/entities/azure-openai.md) — managed service that bundles serving engineering
- [Amazon Bedrock](/entities/amazon-bedrock.md) — managed service that bundles serving engineering
- [vLLM](/entities/vllm.md) — serving stack used in the KAIROS experiments

## Concepts Covered

- [Model routing](/concepts/model-routing.md) — INFRAMIND's queue-aware routing is the central example
