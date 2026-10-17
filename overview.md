---
type: Overview
title: "Wiki Overview"
description: "High-level synthesis of the knowledge base; grows as sources are ingested."
created: '2026-10-17'
updated: '2026-10-17'
tags: [overview]
---

# Wiki Overview

High-level synthesis of the knowledge base.

The bundle now holds **594 source summaries** and **460 cross-linked pages** (254 concepts, 206 entities), drawn from two blogs:

- [devlinliles.com](/references/devlinliles.com/index.md) — Devlin Liles's *Emptying the Cup* (354 posts): agentic software delivery, AI governance, enterprise retrieval, observability, real-time video, and the philosophy and economics underneath.
- [driventodevelop.com](/references/driventodevelop.com/index.md) — David O'Hara's *Driven To Develop* (240 posts): leadership, culture, personal development and health, the DFW/Texas AI economy, and the consulting business model.

Both authors are [Improving](/entities/improving.md) leaders ([Devlin Liles](/entities/devlin-liles.md), [David O'Hara](/entities/david-o-hara.md)), so the two corpora share a delivery-and-governance spine while diverging on emphasis. Start from the [root index](/index.md), [sources](/sources/index.md), [concepts](/concepts/index.md), or [entities](/entities/index.md).

## Current Focus

The overlap is **AI in the enterprise**: how organizations adopt agents without losing reliability, accountability, or trust. Liles supplies the engineering depth — gates, orchestration, evaluation, retrieval. O'Hara supplies the executive frame — governance economics, the manager layer, workforce restructuring, and the regional build-out that supplies the capacity.

## Key Themes

### Compounding reliability is the engineering spine

Per-step accuracy compounds multiplicatively, so long chains fail far more than any step suggests ([Stacking Errors](/concepts/stacking-errors.md)); the remedy is a [quality gate](/concepts/quality-gates.md) at every transition, [human-in-the-loop](/concepts/human-in-the-loop.md) approval at irreversible steps, and [Saga Pattern](/concepts/saga-pattern.md) compensation where rollback is impossible.

### Governance: uniform rules fail, reversibility governs

Both corpora argue [AI Governance](/concepts/ai-governance.md) is runtime infrastructure, not a policy binder, built on [Data Governance](/concepts/data-governance.md), [agent identity](/concepts/agent-identity.md), and an [AI inventory](/concepts/ai-inventory.md). O'Hara sharpens it: [uniform governance](/concepts/uniform-governance.md) is how agents die, and [reversibility](/concepts/reversibility.md) — not autonomy level or risk category — should be the governing criterion. Framed against [NIST AI RMF](/entities/nist-ai-rmf.md) and the [EU AI Act](/entities/eu-ai-act.md).

### Leadership, culture, and personal development

O'Hara's older writing is a large, self-contained cluster: [self-awareness](/concepts/self-awareness.md) as the root of growth, [deliberate practice](/concepts/deliberate-practice.md), [emotional regulation](/concepts/emotional-regulation.md), [resilience](/concepts/resilience.md), [gratitude](/concepts/gratitude.md), [leading by example](/concepts/leading-by-example.md), and [company culture](/concepts/company-culture.md) with [psychological safety](/concepts/psychological-safety.md) and [conscious capitalism](/concepts/conscious-capitalism.md).

### The DFW / Texas AI economy

A distinct thread tracks the region as a load-bearing AI hub — infrastructure, talent, capital, and regulated-industry demand converging ([Regional AI Economy](/concepts/regional-ai-economy.md); [Texas](/entities/texas.md), [Dallas](/entities/dallas.md), [Fort Worth](/entities/fort-worth.md), [Dallas-Fort Worth](/entities/dallas-fort-worth.md)) — alongside the [shadow IT](/concepts/shadow-it.md) / shadow-AI governance gap it creates.

### Consulting is restructuring

AI compresses production time, so O'Hara argues the delivery and pricing models must change: [forward deployed engineering](/concepts/forward-deployed-engineering.md) is now table stakes, and [outcome-based pricing](/concepts/outcome-based-pricing.md) forces firms to own results rather than hours — measured, if at all, by [AI ROI measurement](/concepts/ai-roi-measurement.md) rather than activity.

### Engineering arcs, economics, and philosophy (Liles)

Parallel arcs cover enterprise retrieval ([Active Metadata](/concepts/active-metadata.md), [Skill Registry](/concepts/skill-registry.md), [Retrieval-Augmented Generation](/concepts/retrieval-augmented-generation.md)), observability ([OpenTelemetry](/entities/opentelemetry.md), [DORA](/entities/dora.md)), real-time video ([Selective Forwarding Unit](/concepts/selective-forwarding-unit.md), [Simulcast](/concepts/simulcast.md), [LiveKit](/entities/livekit.md) vs [mediasoup](/entities/mediasoup.md)), and the [AI maturity model](/concepts/ai-maturity-model.md), [model routing](/concepts/model-routing.md), and [Labor Compression](/concepts/labor-compression.md) economics — grounded in [Interpretability](/concepts/interpretability.md), [Sycophancy](/concepts/sycophancy.md), and [Tacit Knowledge](/concepts/tacit-knowledge.md).

## Open Questions

- Where the maturity model's stages 7–8 actually exist in production.
- Whether "reversibility as the governing criterion" scales when agent actions are only partially reversible.
- Whether outcome-based consulting pricing becomes real, or stays a fixed fee with a KPI attached.
- Whether the DFW AI build-out's infrastructure lead survives the grid-cost and talent questions the corpus raises.
- Whether governance frameworks ([NIST AI RMF](/entities/nist-ai-rmf.md)) add explicit data-governance guidance.
