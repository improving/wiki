---
title: "Retrieval-Augmented Generation"
type: "Concept"
description: "Injecting external documents into a model's context so answers reflect current evidence instead of frozen training priors."
created: '2026-10-17'
updated: '2026-10-17'
tags: [rag, retrieval, context]
sources:
  - "/sources/the-catalog-already-learned-to-talk-to-machines.md"
  - "/sources/the-context-window-is-not-a-filing-cabinet.md"
  - "/sources/when-your-agent-books-paris-is-it-thinking-about-a-city.md"
  - "/sources/your-models-beliefs-are-frozen-rag-is-the-workaround.md"
---

# Retrieval-Augmented Generation

Retrieval-augmented generation (RAG) injects external documents into a model's context at inference time so answers reflect current evidence rather than frozen training priors. Across this corpus it is the practical workaround for models whose beliefs cannot update, and a context-management discipline — shifting failure from a full window to a window filled with the wrong things.

## Key Claims

- Model weights do not update at inference; priors stay frozen at the training cutoff, so RAG injects current documents and recovers much of the time-sensitive accuracy gap.
- Models sometimes ignore retrieved evidence that contradicts a strongly encoded prior; fine-tuning is real belief revision but slower and costlier than retrieval.
- Saturation, pollution, and retrieval latency are the three context window problems; context pollution misleads agents even when there is technically enough room.
- Being explicit about what each step needs makes retrieval bounded and reliable.
- Agents acting in real systems need grounded representations, not quasi-intentional statistical mimicry of aboutness; retrieval tolerates shallow intentionality while consequential actions do not.
- Grounding must be architectural — verify representations against current system state before acting, and treat facts as unverified unless their last verification time is known.
- Catalog retrieval is its own problem: static keyword catalogs fail, so active metadata and a metadata knowledge graph keep descriptions current and model prompt–model–data relationships.

## Related

- [Context Window](/concepts/context-window.md) — the resource RAG fills
- [Context Management](/concepts/context-management.md) — the discipline that keeps it bounded
- [Context Pollution](/concepts/context-pollution.md) — RAG's characteristic failure
- [fine-tuning](/concepts/fine-tuning.md) — the slower alternative for belief revision
- [Active Metadata](/concepts/active-metadata.md) — keeping retrieved catalog descriptions current
- [Your Model's Beliefs Are Frozen. RAG Is the Workaround.](/sources/your-models-beliefs-are-frozen-rag-is-the-workaround.md) — primary source
