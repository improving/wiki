---
title: "Speculative Decoding"
type: "Concept"
description: "Accelerating inference by having a cheap draft model propose tokens that a larger target model verifies in parallel."
created: '2026-10-17'
updated: '2026-10-17'
tags: [inference, llm, performance]
sources:
  - "/sources/parallel-decode-is-the-inference-bet-nobodys-marketing-yet.md"
  - "/sources/the-free-half-of-speculative-decoding.md"
---

# Speculative Decoding

Speculative decoding speeds up autoregressive generation by letting a small, cheap draft model propose several tokens at once while the larger target model verifies them in parallel. It is the standard escape from the sequential dependency chain of token-by-token decoding, and this corpus treats it as both a mature serving technique and one of the assumptions that newer parallel-decoding architectures are starting to challenge.

## Key Claims

- The draft model never gets the final word, so a worse drafter only costs rejected guesses, not output quality.
- Quantizing the target model to INT4 alone yielded a 2.16x speedup; adding a quantized draft model pushed that to 3.57x.
- Aggressive target quantization dropped IFEval below the quality gate, requiring quantization-aware distillation to recover.
- A competition entry from the Nota team posted 6.978x on a single NVIDIA A10G.
- Autoregressive decoding is bounded by the sequential dependency chain and KV cache, while diffusion-based approaches such as Google DeepMind's DiffusionGemma reach roughly 1,500 tokens per second on one H100.
- Existing serving frameworks assume KV cache and speculative decoding, so parallel-decode methods lack stack support.

## Related

- [latency budget](/concepts/latency-budget.md) — the constraint speculative decoding is used to meet
- [token cost](/concepts/token-cost.md) — the economic lever quantization and drafting reduce
- [edge inference](/concepts/edge-inference.md) — the setting where a small draft model matters most
- [targeted fine-tuning](/concepts/targeted-fine-tuning.md) — a complementary architecture-level efficiency bet
- [vLLM](/entities/vllm.md) — a serving stack that assumes the speculative-decoding pattern
- [Parallel Decode Is the Inference Bet Nobody's Marketing Yet](/sources/parallel-decode-is-the-inference-bet-nobodys-marketing-yet.md) — primary source
- [The Free Half of Speculative Decoding](/sources/the-free-half-of-speculative-decoding.md) — primary source
