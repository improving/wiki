---
title: "A Bigger Context Window Is Not Working Memory"
type: "Source Summary"
description: "A large context window is attention, not memory; retention needs a separate mechanism deciding what to keep, fold, and compact."
created: '2026-10-17'
updated: '2026-10-17'
tags: [article, agentic-delivery, devlinliles.com]
sources:
  - "references/devlinliles.com/a-bigger-context-window-is-not-working-memory/a-bigger-context-window-is-not-working-memory.md"
---

# A Bigger Context Window Is Not Working Memory — Summary

**Original source**: `references/devlinliles.com/a-bigger-context-window-is-not-working-memory/a-bigger-context-window-is-not-working-memory.md`

## Summary

Teams answer "what's your context window?" in seconds and go quiet when asked about memory architecture, because they bought a bigger window and assumed it was the same thing. The post argues a [context window](/concepts/context-window.md) is what a model can attend to right now, while memory is what survives past now: what gets kept, compressed, carried across sessions, and discarded on purpose. It surveys five 2026 research efforts on training objectives, latency, reasoning transfer, and enterprise infrastructure that independently converged on retention needing its own mechanism.

## Key Claims

- Attention alone does not solve retention; information in the middle of a long context gets lost and models struggle to adapt to something new appearing late.
- A gated differentiable working-memory paper (ACL 2026, arXiv 2601.12906) uses a write controller scoring "Contextual Utility" and matches or beats standard fine-tuning on ZeroSCROLLS and LongBench v2 using a quarter of the gradient steps.
- Self-timed compaction (arXiv 2606.23525) runs 30–70 percent cheaper per question than fixed-schedule summarization and scores up to 18.1 points higher on math.
- [Anthropic](/entities/anthropic.md) shipped a production "Dreaming" process in Claude Managed Agents that writes curated memory updates between sessions, leaving session history untouched.
- Context Kubernetes (arXiv 2604.11623) frames enterprise-scale memory as an orchestration layer with a registry, router, permission layer, and freshness manager.

## Relevance

Central to [working-memory](/concepts/working-memory.md) and [context management](/concepts/context-management.md), and relevant to [context drift](/concepts/context-drift.md).

## Quality

Practitioner blog post by Devlin Liles. Strengths: synthesizes five independent 2026 papers plus one production feature into one structural claim, with named arXiv IDs and figures. Caveats: relies on very recent, un-hardened research and flags its own judgment-call dependence.

## Entities Mentioned

- [Anthropic](/entities/anthropic.md) — shipped the "Dreaming" memory process in Claude Managed Agents

## Concepts Covered

- [context-window](/concepts/context-window.md) — capacity to attend now, distinct from retention
- [working-memory](/concepts/working-memory.md) — what survives across turns and sessions

## Related Sources

- [The Model Can Only Know What's in the Window](/sources/the-model-can-only-know-whats-in-the-window.md)
