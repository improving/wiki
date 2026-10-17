---
title: "GitHub Copilot"
type: "Entity"
description: "GitHub's AI coding assistant, cited for cache-hit benchmark illusions and the single-agent ceiling on delivery work."
created: '2026-10-17'
updated: '2026-10-17'
tags: [product, coding-assistant, ai, benchmarks]
sources:
  - "/sources/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark.md"
  - "/sources/rogers-curve-is-the-best-diagnostic-tool-youre-not-using.md"
  - "/sources/the-single-agent-ceiling-why-one-ai-cant-hold-your-whole-delivery-lifecycle.md"
---

# GitHub Copilot

GitHub Copilot is GitHub's AI coding assistant and one of this corpus's reference examples of single-agent developer tooling. It appears both as a diffusion-stage marker and as a case where vendor benchmarks overstate real-world efficiency.

## Overview

- Vendor cache-hit figures usually come from single-turn benchmarks; real multi-turn agent sessions decay context reuse across turn boundaries, so sizing infrastructure off those numbers understates serving cost.
- Single agents optimize one objective and collapse competing concerns, plateauing at a 15 to 50 percent gain that does not translate to delivered value.
- Orchestration architecture matters more than model quality.
- In 2025 AI workflows sit at Early Adopter and agents at Innovator on [Rogers' curve](/concepts/diffusion-of-innovations.md), so applying an Innovator strategy as a Late Majority organization is the common mistake.

## Related

- [GitHub](/entities/github.md) — its maker
- [Single-Agent Ceiling](/concepts/single-agent-ceiling.md) — why one assistant cannot hold a whole delivery lifecycle
- [Diffusion of Innovations](/concepts/diffusion-of-innovations.md) — where Copilot-style tooling sits in adoption
- [Everett Rogers](/entities/everett-rogers.md) — originator of the diffusion curve
- [token cost](/concepts/token-cost.md) — the infrastructure sizing question behind cache hits
- [95 Trillion Tokens of Real Agent Traffic Looked Nothing Like the Benchmark](/sources/95-trillion-tokens-of-real-agent-traffic-looked-nothing-like-the-benchmark.md) — primary source
