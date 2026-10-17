---
title: "Google DeepMind"
type: "Entity"
description: "Google's AI research lab, whose DiffusionGemma decode work and 2026 leadership split show research and operational authority diverging."
created: '2026-10-17'
updated: '2026-10-17'
tags: [ai-lab, google, research, governance]
sources:
  - "/sources/parallel-decode-is-the-inference-bet-nobodys-marketing-yet.md"
  - "/sources/two-open-weight-letters-zero-neutral-parties.md"
  - "/sources/who-owns-ai-when-the-chief-scientist-isnt-the-one-running-it.md"
---

# Google DeepMind

Google DeepMind is Google's frontier AI research organization. Across this corpus it appears both as a source of inference research and as a case study in how research prestige and operational authority diverge as a lab scales.

## Overview

DiffusionGemma, DeepMind's diffusion-based generation model, produces roughly 1,500 tokens per second on a single H100 by generating tokens in parallel rather than autoregressively — a bet that lacks serving-stack support, since existing frameworks assume KV cache and speculative decoding. On governance, Google sat out the pro-open-weight letter that Nvidia backed. And on August 5, 2026, Google split its top AI research job into two titles: Demis Hassabis kept prestige as Alphabet chief scientist while Koray Kavukcuoglu gained budget and roadmap authority.

## Key Claims

- DiffusionGemma reaches roughly 1,500 tokens per second on a single H100 via parallel diffusion decode
- Autoregressive decoding is limited by the sequential dependency chain and the KV cache
- Google did not sign the pro-open-weight letter that Nvidia backed
- The August 5, 2026 reshuffle split research prestige from budget and roadmap authority
- Jeff Dean and Sanjay Ghemawat left within days, suggesting talent follows authority

## Related

- [Google](/entities/google.md) — parent company
- [Demis Hassabis](/entities/demis-hassabis.md) — kept the chief scientist title in the split
- [Open-Weight Models](/concepts/open-weight-models.md) — the letter Google sat out
- [Speculative Decoding](/concepts/speculative-decoding.md) — serving technique DiffusionGemma sidesteps
- [Parallel Decode Is the Inference Bet Nobody's Marketing Yet](/sources/parallel-decode-is-the-inference-bet-nobodys-marketing-yet.md) — primary source
